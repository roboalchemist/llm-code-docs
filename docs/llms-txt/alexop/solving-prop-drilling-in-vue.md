# Source: https://alexop.dev/posts/solving-prop-drilling-in-vue

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/solving-prop-drilling-in-vue/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Solving Prop Drilling in Vue: Modern State Management Strategies | alexop.dev</title><meta name="title" content="Solving Prop Drilling in Vue: Modern State Management Strategies | alexop.dev"><meta name="description" content="Eliminate prop drilling in Vue apps using Composition API, Provide/Inject, and Pinia. Learn when to use each approach with practical examples."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Solving Prop Drilling in Vue: Modern State Management Strategies | alexop.dev"><meta property="og:description" content="Eliminate prop drilling in Vue apps using Composition API, Provide/Inject, and Pinia. Learn when to use each approach with practical examples."><meta property="og:url" content="https://alexop.dev/posts/solving-prop-drilling-in-vue/"><meta property="og:image" content="https://alexop.dev/posts/solving-prop-drilling-in-vue-modern-state-management-strategies/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-01-25T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/solving-prop-drilling-in-vue/"><meta property="twitter:title" content="Solving Prop Drilling in Vue: Modern State Management Strategies | alexop.dev"><meta property="twitter:description" content="Eliminate prop drilling in Vue apps using Composition API, Provide/Inject, and Pinia. Learn when to use each approach with practical examples."><meta property="twitter:image" content="https://alexop.dev/posts/solving-prop-drilling-in-vue-modern-state-management-strategies/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Solving Prop Drilling in Vue: Modern State Management Strategies | alexop.dev","description":"Eliminate prop drilling in Vue apps using Composition API, Provide/Inject, and Pinia. Learn when to use each approach with practical examples.","image":"https://alexop.dev/posts/solving-prop-drilling-in-vue-modern-state-management-strategies/index.png","datePublished":"2025-01-25T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: solving-prop-drilling-in-vue-modern-state-management-strategies; }@layer astro { ::view-transition-old(solving-prop-drilling-in-vue-modern-state-management-strategies) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(solving-prop-drilling-in-vue-modern-state-management-strategies) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(solving-prop-drilling-in-vue-modern-state-management-strategies) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(solving-prop-drilling-in-vue-modern-state-management-strategies) { 
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
	animation-name: astroFadeIn; }</style><style>.composable-demo:where(.astro-iyhjxl7g){margin:2rem 0;font-family:system-ui,-apple-system,sans-serif;position:relative}.controls:where(.astro-iyhjxl7g){margin-bottom:2rem;display:flex;gap:1rem;align-items:center}.component-tree:where(.astro-iyhjxl7g){position:relative;min-height:400px;background:#212737;border-radius:.5rem;padding:2rem;display:grid;grid-template-columns:250px 1fr;gap:2rem}@media(max-width:768px){.component-tree:where(.astro-iyhjxl7g){grid-template-columns:1fr;padding:.75rem;min-height:300px;gap:1rem}.composable-container:where(.astro-iyhjxl7g){margin-bottom:1rem}.component:where(.astro-iyhjxl7g){width:100%;max-width:100%;padding:1rem}.components-container:where(.astro-iyhjxl7g){gap:1rem}.code-snippet:where(.astro-iyhjxl7g){font-size:.8em;padding:.25rem}.composable:where(.astro-iyhjxl7g){padding:1rem}.composable-header:where(.astro-iyhjxl7g){margin-bottom:.5rem;font-size:1em}}.composable-container:where(.astro-iyhjxl7g){display:flex;flex-direction:column;justify-content:center}.composable:where(.astro-iyhjxl7g){position:relative;border:3px solid rgb(255,107,237);border-radius:.5rem;padding:1.5rem;background:#8a337b;color:#eaedf3;height:-moz-fit-content;height:fit-content}.composable-header:where(.astro-iyhjxl7g){font-weight:700;margin-bottom:1rem;font-size:1.1em}.code-snippet:where(.astro-iyhjxl7g){font-family:monospace;font-size:.9em;padding:.5rem;background:#0000004d;border-radius:.25rem;line-height:1.4}.components-container:where(.astro-iyhjxl7g){display:flex;flex-direction:column;gap:2rem}.component-row:where(.astro-iyhjxl7g){position:relative}.component:where(.astro-iyhjxl7g){position:relative;border:2px solid rgb(171,75,153);border-radius:.5rem;padding:1.5rem;width:250px;margin:0 auto;background:#343f60;cursor:pointer;transition:all .3s ease;z-index:2;color:#eaedf3}.component:where(.astro-iyhjxl7g):hover{transform:translate(10px);box-shadow:0 4px 15px #ff6bed33}.component:where(.astro-iyhjxl7g).highlight{border-color:#ff6bed;background:#8a337b;box-shadow:0 0 15px #ff6bed4d}.composable-access:where(.astro-iyhjxl7g){font-family:monospace;font-size:.9em;color:#ff6bed;margin-bottom:.5rem;opacity:0;transform:translate(-10px);transition:all .3s ease}.component:where(.astro-iyhjxl7g).highlight .composable-access:where(.astro-iyhjxl7g){opacity:1;transform:translate(0)}.user-button:where(.astro-iyhjxl7g){padding:.75rem 1.5rem;background:linear-gradient(135deg,#ff6bed,#ab4b99);color:#eaedf3;border:none;border-radius:.5rem;cursor:pointer;font-weight:500;transition:transform .2s ease}.user-button:where(.astro-iyhjxl7g):hover{transform:scale(1.05)}.user-indicator:where(.astro-iyhjxl7g){font-size:1rem;color:#eaedf3;padding:.5rem 1rem;border-radius:.5rem;background:#343f60}@keyframes composableUpdate{0%{transform:scale(1)}50%{transform:scale(1.05)}to{transform:scale(1)}}.composable:where(.astro-iyhjxl7g).updating{animation:composableUpdate .5s ease-in-out}
</style><style>.event-bus-demo:where(.astro-gcb4dmcu){margin:2rem 0;font-family:system-ui,-apple-system,sans-serif;position:relative}.controls:where(.astro-gcb4dmcu){margin-bottom:2rem;display:flex;gap:1rem;align-items:center}.demo-container:where(.astro-gcb4dmcu){position:relative;min-height:auto;background:#212737;border-radius:.5rem;padding:1rem;display:flex;flex-direction:column;gap:1.5rem;overflow-x:hidden}.event-bus:where(.astro-gcb4dmcu){position:relative;border:2px solid rgb(255,107,237);border-radius:.5rem;padding:1rem;background:#8a337b;color:#eaedf3;margin:0 auto;width:95%;max-width:600px}.event-bus-header:where(.astro-gcb4dmcu){font-weight:700;margin-bottom:1rem;font-size:1.1em;text-align:center}.code-snippet:where(.astro-gcb4dmcu){font-family:monospace;font-size:.8em;padding:.25rem;background:#0000004d;border-radius:.25rem;line-height:1.3}.components-grid:where(.astro-gcb4dmcu){display:grid;grid-template-columns:repeat(2,1fr);gap:2rem;padding:0 1rem}.component:where(.astro-gcb4dmcu){position:relative;border:2px solid rgb(171,75,153);border-radius:.5rem;padding:1.5rem;background:#343f60;cursor:pointer;transition:all .3s ease;z-index:2;color:#eaedf3}.component:where(.astro-gcb4dmcu):hover{transform:translateY(-5px);box-shadow:0 4px 15px #ff6bed33}.component:where(.astro-gcb4dmcu).highlight{border-color:#ff6bed;background:#8a337b;box-shadow:0 0 15px #ff6bed4d}.emit-code:where(.astro-gcb4dmcu),.listen-code:where(.astro-gcb4dmcu){font-family:monospace;font-size:.9em;color:#ff6bed;margin-bottom:.5rem;opacity:0;transform:translateY(5px);transition:all .3s ease}.component:where(.astro-gcb4dmcu).highlight .emit-code:where(.astro-gcb4dmcu),.component:where(.astro-gcb4dmcu).highlight .listen-code:where(.astro-gcb4dmcu){opacity:1;transform:translateY(0)}.event-dot:where(.astro-gcb4dmcu){position:absolute;width:8px;height:8px;border-radius:50%;top:-4px;left:50%;transform:translate(-50%)}.event-dot:where(.astro-gcb4dmcu).emitter{background:#ff6bed;box-shadow:0 0 8px #ff6bed}.event-dot:where(.astro-gcb4dmcu).listener{background:#4caf50;box-shadow:0 0 8px #4caf50}.event-paths:where(.astro-gcb4dmcu){position:absolute;inset:0;pointer-events:none}.event-particle:where(.astro-gcb4dmcu){position:absolute;width:6px;height:6px;border-radius:50%;background:#ff6bed;pointer-events:none;opacity:0}.user-button:where(.astro-gcb4dmcu){padding:.75rem 1.5rem;background:linear-gradient(135deg,#ff6bed,#ab4b99);color:#eaedf3;border:none;border-radius:.5rem;cursor:pointer;font-weight:500;transition:transform .2s ease}.user-button:where(.astro-gcb4dmcu):hover{transform:scale(1.05)}.user-indicator:where(.astro-gcb4dmcu){font-size:1rem;color:#eaedf3;padding:.5rem 1rem;border-radius:.5rem;background:#343f60}@keyframes eventBusUpdate{0%{transform:scale(1)}50%{transform:scale(1.05)}to{transform:scale(1)}}.event-bus:where(.astro-gcb4dmcu).updating{animation:eventBusUpdate .5s ease-in-out}@keyframes particleMove{0%{transform:translate(0);opacity:1}to{opacity:0}}@media(max-width:768px){.event-bus-demo:where(.astro-gcb4dmcu){margin:1rem 0}.controls:where(.astro-gcb4dmcu){margin-bottom:1rem}.demo-container:where(.astro-gcb4dmcu){padding:.75rem;gap:1rem}.event-bus:where(.astro-gcb4dmcu){padding:.75rem}.event-bus-header:where(.astro-gcb4dmcu){font-size:1em;margin-bottom:.5rem}.components-grid:where(.astro-gcb4dmcu){grid-template-columns:repeat(2,1fr);gap:.75rem;padding:0}.component:where(.astro-gcb4dmcu){padding:.75rem;font-size:.9em}.component-header:where(.astro-gcb4dmcu){font-size:.9em;margin-bottom:.25rem}.emit-code:where(.astro-gcb4dmcu),.listen-code:where(.astro-gcb4dmcu){font-size:.75em;margin-bottom:.25rem}.user-button:where(.astro-gcb4dmcu){padding:.5rem 1rem;font-size:.9em}.user-indicator:where(.astro-gcb4dmcu){font-size:.9em;padding:.4rem .8rem}.component:where(.astro-gcb4dmcu):hover{transform:none}}
</style><style>.pinia-demo:where(.astro-kemvofvq){margin:2rem 0;font-family:system-ui,-apple-system,sans-serif;position:relative}.controls:where(.astro-kemvofvq){margin-bottom:2rem;display:flex;gap:1rem;align-items:center}.component-tree:where(.astro-kemvofvq){position:relative;min-height:400px;background:#212737;border-radius:.5rem;padding:2rem;display:grid;grid-template-columns:250px 1fr;gap:2rem}@media(max-width:768px){.component-tree:where(.astro-kemvofvq){grid-template-columns:1fr;padding:1.5rem;gap:1.5rem}.store:where(.astro-kemvofvq){max-width:250px;margin:0 auto}.components-container:where(.astro-kemvofvq){margin-top:1rem}}.store-container:where(.astro-kemvofvq){display:flex;flex-direction:column;justify-content:center}.store:where(.astro-kemvofvq){position:relative;border:3px solid rgb(255,107,237);border-radius:.5rem;padding:1.5rem;background:#8a337b;color:#eaedf3;height:-moz-fit-content;height:fit-content}.store-header:where(.astro-kemvofvq){font-weight:700;margin-bottom:1rem;font-size:1.1em}.components-container:where(.astro-kemvofvq){display:flex;flex-direction:column;gap:2rem}.component-row:where(.astro-kemvofvq){position:relative}.component:where(.astro-kemvofvq){position:relative;border:2px solid rgb(171,75,153);border-radius:.5rem;padding:1.5rem;width:250px;margin:0 auto;background:#343f60;cursor:pointer;transition:all .3s ease;z-index:2;color:#eaedf3}.component:where(.astro-kemvofvq):hover{transform:translate(10px);box-shadow:0 4px 15px #ff6bed33}.component:where(.astro-kemvofvq).highlight{border-color:#ff6bed;background:#8a337b;box-shadow:0 0 15px #ff6bed4d}.store-access:where(.astro-kemvofvq){font-family:monospace;font-size:.9em;color:#ff6bed;margin-bottom:.5rem;opacity:0;transform:translate(-10px);transition:all .3s ease}.component:where(.astro-kemvofvq).highlight .store-access:where(.astro-kemvofvq){opacity:1;transform:translate(0)}.user-button:where(.astro-kemvofvq){padding:.75rem 1.5rem;background:linear-gradient(135deg,#ff6bed,#ab4b99);color:#eaedf3;border:none;border-radius:.5rem;cursor:pointer;font-weight:500;transition:transform .2s ease}.user-button:where(.astro-kemvofvq):hover{transform:scale(1.05)}.user-indicator:where(.astro-kemvofvq){font-size:1rem;color:#eaedf3;padding:.5rem 1rem;border-radius:.5rem;background:#343f60}@keyframes storeUpdate{0%{transform:scale(1)}50%{transform:scale(1.05)}to{transform:scale(1)}}.store:where(.astro-kemvofvq).updating{animation:storeUpdate .5s ease-in-out}
</style><style>.prop-drilling-demo:where(.astro-lltxioqt){margin:2rem 0;font-family:system-ui,-apple-system,sans-serif;position:relative}.controls:where(.astro-lltxioqt){margin-bottom:2rem;display:flex;gap:1rem;align-items:center}.component-tree:where(.astro-lltxioqt){position:relative;min-height:300px;background:#212737;border-radius:.5rem;padding:2rem}.component-row:where(.astro-lltxioqt){margin:2rem 0;position:relative}.component:where(.astro-lltxioqt){position:relative;border:2px solid rgb(171,75,153);border-radius:.5rem;padding:1.5rem;width:200px;margin:0 auto;background:#343f60;cursor:pointer;transition:all .3s ease,background-color .5s ease;z-index:2;color:#eaedf3}.component:where(.astro-lltxioqt):hover{transform:translateY(-2px);box-shadow:0 4px 15px #ff6bed33}.component:where(.astro-lltxioqt).highlight{border-color:#ff6bed;background:#8a337b;box-shadow:0 0 15px #ff6bed4d;transform:translateY(-2px) scale(1.05)}.prop-arrow:where(.astro-lltxioqt){position:absolute;bottom:-35px;left:50%;width:2px;height:30px;background:linear-gradient(to bottom,#ff6bed33,#ff6bed99);transform:translate(-50%);overflow:hidden}.prop-arrow:where(.astro-lltxioqt):after{content:"";position:absolute;bottom:-6px;left:-4px;border:5px solid transparent;border-top-color:#ff6bed}.prop-dot:where(.astro-lltxioqt){position:absolute;width:6px;height:6px;background:#ff6bed;border-radius:50%;left:50%;transform:translate(-50%) translateY(-100%);opacity:0}.prop-arrow:where(.astro-lltxioqt).animate .prop-dot:where(.astro-lltxioqt){animation:moveDot .6s cubic-bezier(.4,0,.2,1) forwards}@keyframes moveDot{0%{transform:translate(-50%) translateY(-100%);opacity:1}to{transform:translate(-50%) translateY(100%);opacity:0}}.user-button:where(.astro-lltxioqt){padding:.75rem 1.5rem;background:linear-gradient(135deg,#ff6bed,#ab4b99);color:#eaedf3;border:none;border-radius:.5rem;cursor:pointer;font-weight:500;transition:transform .2s ease}.user-button:where(.astro-lltxioqt):hover{transform:scale(1.05)}.user-indicator:where(.astro-lltxioqt){font-size:1rem;color:#eaedf3;padding:.5rem 1rem;border-radius:.5rem;background:#343f60;transition:background .3s ease}.component-tooltip:where(.astro-lltxioqt){position:absolute;top:-30px;left:50%;transform:translate(-50%);background:#000c;color:#fff;padding:4px 8px;border-radius:4px;font-size:.8rem;white-space:nowrap;opacity:0;transition:opacity .2s ease;pointer-events:none}.component:where(.astro-lltxioqt):hover .component-tooltip:where(.astro-lltxioqt){opacity:1}.user-text:where(.astro-lltxioqt){transition:all .3s ease}
</style><style>.provide-inject-demo:where(.astro-fqo3k26n){margin:2rem 0;font-family:system-ui,-apple-system,sans-serif;position:relative}.controls:where(.astro-fqo3k26n){margin-bottom:2rem;display:flex;gap:1rem;align-items:center}.component-tree:where(.astro-fqo3k26n){position:relative;min-height:400px;background:#212737;border-radius:.5rem;padding:2rem;display:grid;grid-template-columns:250px 1fr;gap:2rem}.provider-container:where(.astro-fqo3k26n){display:flex;flex-direction:column;gap:1rem}.provider:where(.astro-fqo3k26n),.symbol-key:where(.astro-fqo3k26n){position:relative;border:3px solid rgb(255,107,237);border-radius:.5rem;padding:1.5rem;background:#8a337b;color:#eaedf3}.provider-header:where(.astro-fqo3k26n),.symbol-header:where(.astro-fqo3k26n){font-weight:700;margin-bottom:1rem;font-size:1.1em}.code-snippet:where(.astro-fqo3k26n){font-family:monospace;font-size:.9em;padding:.5rem;background:#0000004d;border-radius:.25rem;line-height:1.4}.components-container:where(.astro-fqo3k26n){display:flex;flex-direction:column;gap:2rem}.component-row:where(.astro-fqo3k26n){position:relative}.component:where(.astro-fqo3k26n){position:relative;border:2px solid rgb(171,75,153);border-radius:.5rem;padding:1.5rem;width:250px;margin:0 auto;background:#343f60;cursor:pointer;transition:all .3s ease;z-index:2;color:#eaedf3}.component:where(.astro-fqo3k26n):hover{transform:translate(10px);box-shadow:0 4px 15px #ff6bed33}.component:where(.astro-fqo3k26n).highlight{border-color:#ff6bed;background:#8a337b;box-shadow:0 0 15px #ff6bed4d}.provide-code:where(.astro-fqo3k26n),.inject-code:where(.astro-fqo3k26n){font-family:monospace;font-size:.9em;color:#ff6bed;margin-bottom:.5rem;opacity:0;transform:translate(-10px);transition:all .3s ease}.pass-through:where(.astro-fqo3k26n){font-style:italic;color:#ab4b99;font-size:.9em;text-align:center}.component:where(.astro-fqo3k26n).highlight .provide-code:where(.astro-fqo3k26n),.component:where(.astro-fqo3k26n).highlight .inject-code:where(.astro-fqo3k26n){opacity:1;transform:translate(0)}.provide-arrow:where(.astro-fqo3k26n){position:absolute;bottom:-35px;left:50%;width:2px;height:30px;background:linear-gradient(to bottom,#ff6bed33,#ff6bed99);transform:translate(-50%);overflow:hidden}.provide-arrow:where(.astro-fqo3k26n):after{content:"";position:absolute;bottom:-6px;left:-4px;border:5px solid transparent;border-top-color:#ff6bed}.provide-dot:where(.astro-fqo3k26n){position:absolute;width:6px;height:6px;background:#ff6bed;border-radius:50%;left:50%;transform:translate(-50%) translateY(-100%);opacity:0}.provide-arrow:where(.astro-fqo3k26n).animate .provide-dot:where(.astro-fqo3k26n){animation:moveDot .8s cubic-bezier(.4,0,.2,1) forwards}@keyframes moveDot{0%{transform:translate(-50%) translateY(-100%);opacity:1}to{transform:translate(-50%) translateY(100%);opacity:0}}.user-button:where(.astro-fqo3k26n){padding:.75rem 1.5rem;background:linear-gradient(135deg,#ff6bed,#ab4b99);color:#eaedf3;border:none;border-radius:.5rem;cursor:pointer;font-weight:500;transition:transform .2s ease}.user-button:where(.astro-fqo3k26n):hover{transform:scale(1.05)}.user-indicator:where(.astro-fqo3k26n){font-size:1rem;color:#eaedf3;padding:.5rem 1rem;border-radius:.5rem;background:#343f60}@keyframes providerUpdate{0%{transform:scale(1)}50%{transform:scale(1.05)}to{transform:scale(1)}}.provider:where(.astro-fqo3k26n).updating{animation:providerUpdate .5s ease-in-out}@media(max-width:768px){.component-tree:where(.astro-fqo3k26n){grid-template-columns:1fr;padding:1rem;gap:1.5rem}.provider-container:where(.astro-fqo3k26n){max-width:100%}.provider:where(.astro-fqo3k26n),.symbol-key:where(.astro-fqo3k26n){padding:1rem}.component:where(.astro-fqo3k26n){width:100%;max-width:300px;padding:1rem}.code-snippet:where(.astro-fqo3k26n){font-size:.8em;padding:.5rem;overflow-x:auto}.controls:where(.astro-fqo3k26n){flex-direction:column;align-items:stretch}.user-button:where(.astro-fqo3k26n){width:100%}.user-indicator:where(.astro-fqo3k26n){text-align:center}}
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Solving Prop Drilling in Vue: Modern State Management Strategies</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-01-25T00:00:00.000Z">Jan 25, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Za9ilF" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Solving Prop Drilling in Vue: Modern State Management Strategies&quot;],&quot;content&quot;:[0,&quot;import PropDrillingDemo from \&quot;../../features/vue-demos/components/PropDrillingDemo.astro\&quot;;\nimport PiniaDemo from \&quot;../../features/vue-demos/components/PiniaDemo.astro\&quot;;\nimport ComposableDemo from \&quot;../../features/vue-demos/components/ComposableDemo.astro\&quot;;\nimport ProvideInjectDemo from \&quot;../../features/vue-demos/components/ProvideInjectDemo.astro\&quot;;\nimport EventBusDemo from \&quot;../../features/vue-demos/components/EventBusDemo.astro\&quot;;\n\n## TL;DR: Prop Drilling Solutions at a Glance\n\n- **Global state**: Pinia (Vue&#39;s official state management)\n- **Reusable logic**: Composables\n- **Component subtree sharing**: Provide/Inject\n- **Avoid**: Event buses for state management\n\n&gt; Click the toggle button to see interactive diagram animations that demonstrate each concept.\n\n---\n\n## The Hidden Cost of Prop Drilling: A Real-World Scenario\n\nImagine building a Vue dashboard where the user&#39;s name needs to be displayed in seven nested components. Every intermediate component becomes a middleman for data it doesn&#39;t need. Imagine changing the prop name from `userName` to `displayName`. You&#39;d have to update six components to pass along something they don&#39;t use!\n\n&lt;PropDrillingDemo /&gt;\n\n**This is prop drilling** – and it creates:\n\n- 🚨 **Brittle code** that breaks during refactors\n- 🕵️ **Debugging nightmares** from unclear data flow\n- 🐌 **Performance issues** from unnecessary re-renders\n\n---\n\n## Solution 1: Pinia for Global State Management\n\n### When to Use: App-wide state (user data, auth state, cart items)\n\n&lt;PiniaDemo /&gt;\n\n**Implementation**:\n\n```javascript\n// stores/user.js\nimport { defineStore } from &#39;pinia&#39;;\n\nexport const useUserStore = defineStore(&#39;user&#39;, {\nconst username = ref(localStorage.getItem(&#39;username&#39;) || &#39;Guest&#39;);\nconst isLoggedIn = computed(() =&gt; username.value !== &#39;Guest&#39;);\n\nfunction setUsername(newUsername) {\n    username.value = newUsername;\n    localStorage.setItem(&#39;username&#39;, newUsername);\n}\n\nreturn {\n    username,\n    isLoggedIn,\n    setUsername\n};\n});\n```\n\n**Component Usage**:\n\n```vue\n&lt;!-- DeeplyNestedComponent.vue --&gt;\n&lt;script setup&gt;\nimport { useUserStore } from \&quot;@/stores/user\&quot;;\nconst user = useUserStore();\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;div class=\&quot;user-info\&quot;&gt;\n    Welcome, {{ user.username }}!\n    &lt;button v-if=\&quot;!user.isLoggedIn\&quot; @click=\&quot;user.setUsername(&#39;John&#39;)\&quot;&gt;\n      Log In\n    &lt;/button&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n```\n\n✅ **Pros**\n\n- Centralized state with DevTools support\n- TypeScript-friendly\n- Built-in SSR support\n\n⚠️ **Cons**\n\n- Overkill for small component trees\n- Requires understanding of Flux architecture\n\n---\n\n## Solution 2: Composables for Reusable Logic\n\n### When to Use: Shared component logic (user preferences, form state)\n\n&lt;ComposableDemo /&gt;\n\n**Implementation with TypeScript**:\n\n```typescript\n// composables/useUser.ts\nimport { ref } from \&quot;vue\&quot;;\nconst username = ref(localStorage.getItem(\&quot;username\&quot;) || \&quot;Guest\&quot;);\n\nexport function useUser() {\n  const setUsername = (newUsername: string) =&gt; {\n    username.value = newUsername;\n    localStorage.setItem(\&quot;username\&quot;, newUsername);\n  };\n\n  return {\n    username,\n    setUsername,\n  };\n}\n```\n\n**Component Usage**:\n\n```vue\n&lt;!-- UserProfile.vue --&gt;\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nconst { username, setUsername } = useUser();\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;div class=\&quot;user-profile\&quot;&gt;\n    &lt;h2&gt;Welcome, {{ username }}!&lt;/h2&gt;\n    &lt;button @click=\&quot;setUsername(&#39;John&#39;)\&quot;&gt;Update Username&lt;/button&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n```\n\n✅ **Pros**\n\n- Zero-dependency solution\n- Perfect for logic reuse across components\n- Full TypeScript support\n\n⚠️ **Cons**\n\n- Shared state requires singleton pattern\n- No built-in DevTools integration\n- **SSR Memory Leaks**: State declared outside component scope persists between requests\n- **Not SSR-Safe**: Using this pattern in SSR can lead to state pollution across requests\n\n## Solution 3: Provide/Inject for Component Tree Scoping\n\n### When to Use: Library components or feature-specific user data\n\n&lt;ProvideInjectDemo /&gt;\n\n**Type-Safe Implementation**:\n\n```typescript\n\n\n// utilities/user.ts\nimport type { InjectionKey } from &#39;vue&#39;;\n\ninterface UserContext {\n  username: Ref&lt;string&gt;;\n  updateUsername: (name: string) =&gt; void;\n}\n\nexport const UserKey = Symbol(&#39;user&#39;) as InjectionKey&lt;UserContext&gt;;\n\n// ParentComponent.vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { UserKey } from &#39;@/utilities/user&#39;;\n\nconst username = ref&lt;string&gt;(&#39;Guest&#39;);\nconst updateUsername = (name: string) =&gt; {\n  username.value = name;\n};\n\nprovide(UserKey, { username, updateUsername });\n&lt;/script&gt;\n\n// DeepChildComponent.vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { UserKey } from &#39;@/utilities/user&#39;;\n\nconst { username, updateUsername } = inject(UserKey, {\n  username: ref(&#39;Guest&#39;),\n  updateUsername: () =&gt; console.warn(&#39;No user provider!&#39;),\n});\n&lt;/script&gt;\n```\n\n✅ **Pros**\n\n- Explicit component relationships\n- Perfect for component libraries\n- Type-safe with TypeScript\n\n⚠️ **Cons**\n\n- Can create implicit dependencies\n- Debugging requires tracing providers\n\n---\n\n## Why Event Buses Fail for State Management\n\n&lt;EventBusDemo /&gt;\n\nEvent buses create more problems than they solve for state management:\n\n1. **Spaghetti Data Flow**  \n   Components become invisibly coupled through arbitrary events. When `ComponentA` emits `update-theme`, who&#39;s listening? Why? DevTools can&#39;t help you track the chaos.\n\n2. **State Inconsistencies**  \n   Multiple components listening to the same event often maintain duplicate state:\n\n   ```javascript\n   // Two components, two sources of truth\n   eventBus.on(\&quot;login\&quot;, () =&gt; (this.isLoggedIn = true));\n   eventBus.on(\&quot;login\&quot;, () =&gt; (this.userStatus = \&quot;active\&quot;));\n   ```\n\n3. **Memory Leaks**  \n   Forgotten event listeners in unmounted components keep reacting to events, causing bugs and performance issues.\n\n**Where Event Buses Actually Work**\n\n- ✅ Global notifications (toasts, alerts)\n- ✅ Analytics tracking\n- ✅ Decoupled plugin events\n\n**Instead of Event Buses**: Use Pinia for state, composables for logic, and provide/inject for component trees.\n\n```mermaid\n---\ntitle: \&quot;Decision Guide: Choosing Your Weapon\&quot;\n---\ngraph TD\n    A[Need Shared State?] --&gt;|No| B[Props/Events]\n    A --&gt;|Yes| C{Scope?}\n    C --&gt;|App-wide| D[Pinia]\n    C --&gt;|Component Tree| E[Provide/Inject]\n    C --&gt;|Reusable Logic| F[Composables]\n```\n\n## Pro Tips for State Management Success\n\n1. **Start Simple**: Begin with props, graduate to composables\n2. **Type Everything**: Use TypeScript for stores/injections\n3. **Name Wisely**: Prefix stores (`useUserStore`) and injection keys (`UserKey`)\n4. **Monitor Performance**: Use Vue DevTools to track reactivity\n5. **Test State**: Write unit tests for Pinia stores/composables\n\nBy mastering these patterns, you&#39;ll write Vue apps that scale gracefully while keeping component relationships clear and maintainable.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <h2 id="tldr-prop-drilling-solutions-at-a-glance">TL;DR: Prop Drilling Solutions at a Glance<a class="heading-link" aria-label="Link to section" href="#tldr-prop-drilling-solutions-at-a-glance"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li><strong>Global state</strong>: Pinia (Vue’s official state management)</li>
<li><strong>Reusable logic</strong>: Composables</li>
<li><strong>Component subtree sharing</strong>: Provide/Inject</li>
<li><strong>Avoid</strong>: Event buses for state management</li>
</ul>
<blockquote>
<p>Click the toggle button to see interactive diagram animations that demonstrate each concept.</p>
</blockquote>
<hr/>
<h2 id="the-hidden-cost-of-prop-drilling-a-real-world-scenario">The Hidden Cost of Prop Drilling: A Real-World Scenario<a class="heading-link" aria-label="Link to section" href="#the-hidden-cost-of-prop-drilling-a-real-world-scenario"><span class="heading-link-icon">#</span></a></h2>
<p>Imagine building a Vue dashboard where the user’s name needs to be displayed in seven nested components. Every intermediate component becomes a middleman for data it doesn’t need. Imagine changing the prop name from <code>userName</code> to <code>displayName</code>. You’d have to update six components to pass along something they don’t use!</p>
<div class="prop-drilling-demo astro-lltxioqt"> <div class="controls astro-lltxioqt"> <button id="prop-drilling-userButton" class="user-button astro-lltxioqt">Change Username</button> <div class="user-indicator astro-lltxioqt">
Current User: <span id="prop-drilling-userValue" class="astro-lltxioqt">Guest</span> </div> </div> <div class="component-tree astro-lltxioqt"> <div class="component-row astro-lltxioqt"> <div class="component parent astro-lltxioqt" data-component="Parent"> <div class="component-header astro-lltxioqt">Parent</div> <div class="component-tooltip astro-lltxioqt">Provides username to Child</div> <div class="component-content astro-lltxioqt">
username: <span class="user-text astro-lltxioqt">Guest</span> </div> <div class="prop-arrow astro-lltxioqt"> <div class="prop-dot astro-lltxioqt"></div> </div> </div> </div> <div class="component-row astro-lltxioqt"> <div class="component child astro-lltxioqt" data-component="Child"> <div class="component-header astro-lltxioqt">Child</div> <div class="component-tooltip astro-lltxioqt">Passes username to Grandchild</div> <div class="component-content astro-lltxioqt">
username: <span class="user-text astro-lltxioqt">Guest</span> </div> <div class="prop-arrow astro-lltxioqt"> <div class="prop-dot astro-lltxioqt"></div> </div> </div> </div> <div class="component-row astro-lltxioqt"> <div class="component grandchild astro-lltxioqt" data-component="Grandchild"> <div class="component-header astro-lltxioqt">Grandchild</div> <div class="component-tooltip astro-lltxioqt">Uses username prop</div> <div class="component-content astro-lltxioqt">
username: <span class="user-text astro-lltxioqt">Guest</span> </div> </div> </div> </div> </div>  <script type="module">function r(){const l=document.getElementById("prop-drilling-userButton"),a=document.getElementById("prop-drilling-userValue"),c=document.querySelectorAll(".prop-drilling-demo .user-text"),s=document.querySelectorAll(".prop-drilling-demo .component"),o=["Guest","John","Alice","Bob"];let t=0;function d(){s.forEach((e,m)=>{setTimeout(()=>{e.classList.add("highlight");const n=e.querySelector(".prop-arrow");n&&n.classList.add("animate"),c.forEach(i=>{i.style.transition="none",i.textContent=o[t],setTimeout(()=>{i.style.transition="all 0.3s ease"},10)}),setTimeout(()=>{e.classList.remove("highlight"),n&&n.classList.remove("animate")},800)},m*400)})}function u(){t=(t+1)%o.length,a.textContent=o[t],d()}s.forEach(e=>{e.addEventListener("click",function(){this.classList.add("highlight"),setTimeout(()=>this.classList.remove("highlight"),300)})}),l.addEventListener("click",u)}document.readyState==="loading"?document.addEventListener("DOMContentLoaded",r):r();</script>
<p><strong>This is prop drilling</strong> – and it creates:</p>
<ul>
<li>🚨 <strong>Brittle code</strong> that breaks during refactors</li>
<li>🕵️ <strong>Debugging nightmares</strong> from unclear data flow</li>
<li>🐌 <strong>Performance issues</strong> from unnecessary re-renders</li>
</ul>
<hr/>
<h2 id="solution-1-pinia-for-global-state-management">Solution 1: Pinia for Global State Management<a class="heading-link" aria-label="Link to section" href="#solution-1-pinia-for-global-state-management"><span class="heading-link-icon">#</span></a></h2>
<h3 id="when-to-use-app-wide-state-user-data-auth-state-cart-items">When to Use: App-wide state (user data, auth state, cart items)<a class="heading-link" aria-label="Link to section" href="#when-to-use-app-wide-state-user-data-auth-state-cart-items"><span class="heading-link-icon">#</span></a></h3>
<!-- PiniaDemo.astro --><div class="pinia-demo astro-kemvofvq"> <div class="controls astro-kemvofvq"> <button id="pinia-userButton" class="user-button astro-kemvofvq">Change Username</button> <div class="user-indicator astro-kemvofvq">
Current User: <span id="pinia-userValue" class="astro-kemvofvq">Guest</span> </div> </div> <div class="component-tree astro-kemvofvq"> <!-- Store visualization --> <div class="store-container astro-kemvofvq"> <div class="store astro-kemvofvq"> <div class="store-header astro-kemvofvq">User Store</div> <div class="store-content astro-kemvofvq"> <div class="code-snippet astro-kemvofvq"> // stores/user.js<br class="astro-kemvofvq"> export const useUserStore = defineStore(&#39;user&#39;, {<br class="astro-kemvofvq">   username: ref(&#39;Guest&#39;),<br class="astro-kemvofvq">   setUsername: (name) =&gt; username.value = name<br class="astro-kemvofvq"> }); </div> </div> </div> </div> <!-- Components with store usage --> <div class="components-container astro-kemvofvq"> <div class="component-row astro-kemvofvq"> <div class="component parent astro-kemvofvq" data-component="Parent"> <div class="component-header astro-kemvofvq">Parent</div> <div class="component-content astro-kemvofvq"> <div class="store-access astro-kemvofvq">useUserStore()</div>
username: <span class="user-text astro-kemvofvq">Guest</span> </div> </div> </div> <div class="component-row astro-kemvofvq"> <div class="component child astro-kemvofvq" data-component="Child"> <div class="component-header astro-kemvofvq">Child</div> <div class="component-content astro-kemvofvq"> <div class="store-access astro-kemvofvq">useUserStore()</div>
username: <span class="user-text astro-kemvofvq">Guest</span> </div> </div> </div> <div class="component-row astro-kemvofvq"> <div class="component grandchild astro-kemvofvq" data-component="Grandchild"> <div class="component-header astro-kemvofvq">Grandchild</div> <div class="component-content astro-kemvofvq"> <div class="store-access astro-kemvofvq">useUserStore()</div>
username: <span class="user-text astro-kemvofvq">Guest</span> </div> </div> </div> </div> </div> </div>  <script type="module">function a(){const s=document.getElementById("pinia-userButton"),o=document.getElementById("pinia-userValue"),u=document.querySelectorAll(".pinia-demo .user-text"),c=document.querySelectorAll(".pinia-demo .component"),t=document.querySelector(".pinia-demo .store"),n=["Guest","John","Alice","Bob"];let i=0;function d(){t&&(t.classList.add("updating"),setTimeout(()=>t.classList.remove("updating"),500))}function l(){t.classList.add("highlight"),setTimeout(()=>t.classList.remove("highlight"),800),c.forEach((e,m)=>{setTimeout(()=>{e.classList.add("highlight"),setTimeout(()=>e.classList.remove("highlight"),800)},m*300+300)})}function r(){i=(i+1)%n.length,o&&(o.textContent=n[i]),d(),u.forEach(e=>{e.textContent=n[i]}),l()}c.forEach(e=>{e.addEventListener("click",function(){this.classList.add("highlight"),setTimeout(()=>this.classList.remove("highlight"),800)})}),s&&s.addEventListener("click",r)}document.readyState==="loading"?document.addEventListener("DOMContentLoaded",a):a();</script>
<p><strong>Implementation</strong>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="javascript"><code><span class="line"><span style="color:#51597D;font-style:italic">// stores/user.js</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">defineStore</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">pinia</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> useUserStore</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> defineStore</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">user</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#A9B1D6">const </span><span style="color:#C0CAF5">username</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">localStorage</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getItem</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">username</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> ||</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Guest</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#A9B1D6">;</span></span>
<span class="line"><span style="color:#A9B1D6">const </span><span style="color:#C0CAF5">isLoggedIn</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> computed</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> username</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#BB9AF7"> !==</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Guest</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#A9B1D6">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A9B1D6">function </span><span style="color:#7AA2F7">setUsername</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">newUsername</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    username</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> newUsername</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    localStorage</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">setItem</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">username</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> newUsername</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A9B1D6">return </span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#C0CAF5">    username</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    isLoggedIn</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    setUsername</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#A9B1D6">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// stores/user.js
import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
const username = ref(localStorage.getItem('username') || 'Guest');
const isLoggedIn = computed(() => username.value !== 'Guest');

function setUsername(newUsername) {
    username.value = newUsername;
    localStorage.setItem('username', newUsername);
}

return {
    username,
    isLoggedIn,
    setUsername
};
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Component Usage</strong>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#51597D;font-style:italic">&lt;!-- DeeplyNestedComponent.vue --&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useUserStore</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@/stores/user</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> user</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useUserStore</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">user-info</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#9AA5CE">    Welcome, {{ user.username }}!</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">button</span><span style="color:#BB9AF7"> v-if</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">!user.isLoggedIn</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> @click</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">user.setUsername(&#39;John&#39;)</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#9AA5CE">      Log In</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<!-- DeeplyNestedComponent.vue -->
<script setup>
import { useUserStore } from &#34;@/stores/user&#34;;
const user = useUserStore();
</script>

<template>
  <div class=&#34;user-info&#34;>
    Welcome, {{ user.username }}!
    <button v-if=&#34;!user.isLoggedIn&#34; @click=&#34;user.setUsername('John')&#34;>
      Log In
    </button>
  </div>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>✅ <strong>Pros</strong></p>
<ul>
<li>Centralized state with DevTools support</li>
<li>TypeScript-friendly</li>
<li>Built-in SSR support</li>
</ul>
<p>⚠️ <strong>Cons</strong></p>
<ul>
<li>Overkill for small component trees</li>
<li>Requires understanding of Flux architecture</li>
</ul>
<hr/>
<h2 id="solution-2-composables-for-reusable-logic">Solution 2: Composables for Reusable Logic<a class="heading-link" aria-label="Link to section" href="#solution-2-composables-for-reusable-logic"><span class="heading-link-icon">#</span></a></h2>
<h3 id="when-to-use-shared-component-logic-user-preferences-form-state">When to Use: Shared component logic (user preferences, form state)<a class="heading-link" aria-label="Link to section" href="#when-to-use-shared-component-logic-user-preferences-form-state"><span class="heading-link-icon">#</span></a></h3>
<!-- ComposableDemo.astro --><div class="composable-demo astro-iyhjxl7g"> <div class="controls astro-iyhjxl7g"> <button id="composable-userButton" class="user-button astro-iyhjxl7g">Change Username</button> <div class="user-indicator astro-iyhjxl7g">
Current User: <span id="composable-userValue" class="astro-iyhjxl7g">Guest</span> </div> </div> <div class="component-tree astro-iyhjxl7g"> <!-- Composable visualization --> <div class="composable-container astro-iyhjxl7g"> <div class="composable astro-iyhjxl7g"> <div class="composable-header astro-iyhjxl7g">useUser Composable</div> <div class="composable-content astro-iyhjxl7g"> <div class="code-snippet astro-iyhjxl7g"> const username = ref(&#39;Guest&#39;);<br class="astro-iyhjxl7g"> return { username, setUsername }; </div> </div> </div> </div> <!-- Components with composable usage --> <div class="components-container astro-iyhjxl7g"> <div class="component-row astro-iyhjxl7g"> <div class="component parent astro-iyhjxl7g" data-component="Parent"> <div class="component-header astro-iyhjxl7g">Parent</div> <div class="component-content astro-iyhjxl7g"> <div class="composable-access astro-iyhjxl7g"> const { username } = useUser() </div>
username: <span class="user-text astro-iyhjxl7g">Guest</span> </div> </div> </div> <div class="component-row astro-iyhjxl7g"> <div class="component child astro-iyhjxl7g" data-component="Child"> <div class="component-header astro-iyhjxl7g">Child</div> <div class="component-content astro-iyhjxl7g"> <div class="composable-access astro-iyhjxl7g"> const { username } = useUser() </div>
username: <span class="user-text astro-iyhjxl7g">Guest</span> </div> </div> </div> <div class="component-row astro-iyhjxl7g"> <div class="component grandchild astro-iyhjxl7g" data-component="Grandchild"> <div class="component-header astro-iyhjxl7g">Grandchild</div> <div class="component-content astro-iyhjxl7g"> <div class="composable-access astro-iyhjxl7g"> const { username } = useUser() </div>
username: <span class="user-text astro-iyhjxl7g">Guest</span> </div> </div> </div> </div> </div> </div>  <script type="module">function a(){const n=document.getElementById("composable-userButton"),c=document.getElementById("composable-userValue"),l=document.querySelectorAll(".composable-demo .user-text"),i=document.querySelectorAll(".composable-demo .component"),o=document.querySelector(".composable-demo .composable"),s=["Guest","John","Alice","Bob"];let t=0;function u(){o&&(o.classList.add("updating"),setTimeout(()=>o.classList.remove("updating"),500))}function m(){i.forEach((e,r)=>{setTimeout(()=>{e.classList.add("highlight"),setTimeout(()=>{e.classList.remove("highlight")},800)},r*300)})}function d(){t=(t+1)%s.length,c&&(c.textContent=s[t]),u(),l.forEach(e=>{e.textContent=s[t]}),m()}i.forEach(e=>{e.addEventListener("click",function(){this.classList.add("highlight"),setTimeout(()=>this.classList.remove("highlight"),800)})}),n&&n.addEventListener("click",d)}document.readyState==="loading"?document.addEventListener("DOMContentLoaded",a):a();</script>
<p><strong>Implementation with TypeScript</strong>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// composables/useUser.ts</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> username</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">localStorage</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getItem</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">username</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> ||</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Guest</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useUser</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> setUsername</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">newUsername</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    username</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> newUsername</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    localStorage</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">setItem</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">username</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> newUsername</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    username</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    setUsername</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// composables/useUser.ts
import { ref } from &#34;vue&#34;;
const username = ref(localStorage.getItem(&#34;username&#34;) || &#34;Guest&#34;);

export function useUser() {
  const setUsername = (newUsername: string) => {
    username.value = newUsername;
    localStorage.setItem(&#34;username&#34;, newUsername);
  };

  return {
    username,
    setUsername,
  };
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Component Usage</strong>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#51597D;font-style:italic">&lt;!-- UserProfile.vue --&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> username</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> setUsername</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useUser</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">user-profile</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">h2</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Welcome, {{ username }}!</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">h2</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">button</span><span style="color:#BB9AF7"> @click</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">setUsername(&#39;John&#39;)</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Update Username</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<!-- UserProfile.vue -->
<script setup lang=&#34;ts&#34;>
const { username, setUsername } = useUser();
</script>

<template>
  <div class=&#34;user-profile&#34;>
    <h2>Welcome, {{ username }}!</h2>
    <button @click=&#34;setUsername('John')&#34;>Update Username</button>
  </div>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>✅ <strong>Pros</strong></p>
<ul>
<li>Zero-dependency solution</li>
<li>Perfect for logic reuse across components</li>
<li>Full TypeScript support</li>
</ul>
<p>⚠️ <strong>Cons</strong></p>
<ul>
<li>Shared state requires singleton pattern</li>
<li>No built-in DevTools integration</li>
<li><strong>SSR Memory Leaks</strong>: State declared outside component scope persists between requests</li>
<li><strong>Not SSR-Safe</strong>: Using this pattern in SSR can lead to state pollution across requests</li>
</ul>
<h2 id="solution-3-provideinject-for-component-tree-scoping">Solution 3: Provide/Inject for Component Tree Scoping<a class="heading-link" aria-label="Link to section" href="#solution-3-provideinject-for-component-tree-scoping"><span class="heading-link-icon">#</span></a></h2>
<h3 id="when-to-use-library-components-or-feature-specific-user-data">When to Use: Library components or feature-specific user data<a class="heading-link" aria-label="Link to section" href="#when-to-use-library-components-or-feature-specific-user-data"><span class="heading-link-icon">#</span></a></h3>
<!-- ProvideInjectDemo.astro --><div class="provide-inject-demo astro-fqo3k26n"> <div class="controls astro-fqo3k26n"> <button id="provide-inject-userButton" class="user-button astro-fqo3k26n">Change Username</button> <div class="user-indicator astro-fqo3k26n">
Current User: <span id="provide-inject-userValue" class="astro-fqo3k26n">Guest</span> </div> </div> <div class="component-tree astro-fqo3k26n"> <!-- Provider visualization --> <div class="provider-container astro-fqo3k26n"> <div class="provider astro-fqo3k26n"> <div class="provider-header astro-fqo3k26n">Parent Provider</div> <div class="provider-content astro-fqo3k26n"> <div class="code-snippet astro-fqo3k26n"> import { provide, ref } from &#39;vue&#39;;<br class="astro-fqo3k26n"> const username = ref(&#39;Guest&#39;);<br class="astro-fqo3k26n"> provide(USER_KEY, username); </div> </div> </div> <div class="symbol-key astro-fqo3k26n"> <div class="symbol-header astro-fqo3k26n">Symbol Key</div> <div class="code-snippet astro-fqo3k26n"> const USER_KEY = Symbol(&#39;user&#39;); </div> </div> </div> <!-- Components with injection --> <div class="components-container astro-fqo3k26n"> <div class="component-row astro-fqo3k26n"> <div class="component parent astro-fqo3k26n" data-component="Parent"> <div class="component-header astro-fqo3k26n">Parent (Provider)</div> <div class="component-content astro-fqo3k26n"> <div class="provide-code astro-fqo3k26n">provide(USER_KEY, username)</div>
username: <span class="user-text astro-fqo3k26n">Guest</span> </div> <div class="provide-arrow astro-fqo3k26n"> <div class="provide-dot astro-fqo3k26n"></div> </div> </div> </div> <div class="component-row astro-fqo3k26n"> <div class="component child astro-fqo3k26n" data-component="Child"> <div class="component-header astro-fqo3k26n">Child (No Injection)</div> <div class="component-content astro-fqo3k26n"> <div class="pass-through astro-fqo3k26n">Passes username implicitly</div> </div> <div class="provide-arrow astro-fqo3k26n"> <div class="provide-dot astro-fqo3k26n"></div> </div> </div> </div> <div class="component-row astro-fqo3k26n"> <div class="component grandchild astro-fqo3k26n" data-component="Grandchild"> <div class="component-header astro-fqo3k26n">Grandchild (Injector)</div> <div class="component-content astro-fqo3k26n"> <div class="inject-code astro-fqo3k26n">const username = inject(USER_KEY)</div>
username: <span class="user-text astro-fqo3k26n">Guest</span> </div> </div> </div> </div> </div> </div>  <script type="module">function d(){const s=document.getElementById("provide-inject-userButton"),c=document.getElementById("provide-inject-userValue"),r=document.querySelectorAll(".provide-inject-demo .user-text"),t=document.querySelectorAll(".provide-inject-demo .component"),o=document.querySelector(".provide-inject-demo .provider"),u=document.querySelectorAll(".provide-inject-demo .provide-arrow"),n=["Guest","John","Alice","Bob"];let i=0;function a(){o&&(o.classList.add("updating"),setTimeout(()=>o.classList.remove("updating"),500))}function l(){t[0].classList.add("highlight"),setTimeout(()=>t[0].classList.remove("highlight"),800),u.forEach((e,h)=>{setTimeout(()=>{e.classList.add("animate"),setTimeout(()=>e.classList.remove("animate"),800)},h*400+400)}),setTimeout(()=>{t[2].classList.add("highlight"),setTimeout(()=>t[2].classList.remove("highlight"),800)},1600)}function m(){i=(i+1)%n.length,c&&(c.textContent=n[i]),a(),r.forEach(e=>{e.textContent=n[i]}),l()}t.forEach(e=>{e.addEventListener("click",function(){this.classList.add("highlight"),setTimeout(()=>this.classList.remove("highlight"),800)})}),s&&s.addEventListener("click",m)}document.readyState==="loading"?document.addEventListener("DOMContentLoaded",d):d();</script>
<p><strong>Type-Safe Implementation</strong>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// utilities/user.ts</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#BB9AF7"> type</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">InjectionKey</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> UserContext</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  username</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"><span style="color:#7AA2F7">  updateUsername</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">name</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> UserKey</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> Symbol</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">user</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF"> as</span><span style="color:#C0CAF5"> InjectionKey</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">UserContext</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ParentComponent.vue</span></span>
<span class="line"><span style="color:#BB9AF7">&lt;</span><span style="color:#C0CAF5">script</span><span style="color:#C0CAF5"> setup</span><span style="color:#C0CAF5"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">UserKey</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@/utilities/user</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> username</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Guest</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#7AA2F7"> updateUsername</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">name</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  username</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> name</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">provide</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">UserKey</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#C0CAF5"> username</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> updateUsername</span><span style="color:#9ABDF5"> })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">&lt;</span><span style="color:#89DDFF">/</span><span style="color:#C0CAF5">script</span><span style="color:#BB9AF7">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// DeepChildComponent.vue</span></span>
<span class="line"><span style="color:#BB9AF7">&lt;</span><span style="color:#C0CAF5">script</span><span style="color:#C0CAF5"> setup</span><span style="color:#C0CAF5"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">UserKey</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@/utilities/user</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> username</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> updateUsername</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> inject</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">UserKey</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  username</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Guest</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">  updateUsername</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">warn</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">No user provider!</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">&lt;</span><span style="color:#89DDFF">/</span><span style="color:#C0CAF5">script</span><span style="color:#BB9AF7">&gt;</span></span></code><button type="button" class="copy" data-code="

// utilities/user.ts
import type { InjectionKey } from 'vue';

interface UserContext {
  username: Ref<string>;
  updateUsername: (name: string) => void;
}

export const UserKey = Symbol('user') as InjectionKey<UserContext>;

// ParentComponent.vue
<script setup lang=&#34;ts&#34;>
import { UserKey } from '@/utilities/user';

const username = ref<string>('Guest');
const updateUsername = (name: string) => {
  username.value = name;
};

provide(UserKey, { username, updateUsername });
</script>

// DeepChildComponent.vue
<script setup lang=&#34;ts&#34;>
import { UserKey } from '@/utilities/user';

const { username, updateUsername } = inject(UserKey, {
  username: ref('Guest'),
  updateUsername: () => console.warn('No user provider!'),
});
</script>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>✅ <strong>Pros</strong></p>
<ul>
<li>Explicit component relationships</li>
<li>Perfect for component libraries</li>
<li>Type-safe with TypeScript</li>
</ul>
<p>⚠️ <strong>Cons</strong></p>
<ul>
<li>Can create implicit dependencies</li>
<li>Debugging requires tracing providers</li>
</ul>
<hr/>
<h2 id="why-event-buses-fail-for-state-management">Why Event Buses Fail for State Management<a class="heading-link" aria-label="Link to section" href="#why-event-buses-fail-for-state-management"><span class="heading-link-icon">#</span></a></h2>
<!-- EventBusDemo.astro --><div class="event-bus-demo astro-gcb4dmcu"> <div class="controls astro-gcb4dmcu"> <button id="event-bus-userButton" class="user-button astro-gcb4dmcu">Change Username</button> <div class="user-indicator astro-gcb4dmcu">
Current User: <span id="event-bus-userValue" class="astro-gcb4dmcu">Guest</span> </div> </div> <div class="demo-container astro-gcb4dmcu"> <!-- Event Bus visualization --> <div class="event-bus astro-gcb4dmcu"> <div class="event-bus-header astro-gcb4dmcu">Event Bus (mitt)</div> <div class="event-bus-content astro-gcb4dmcu"> <div class="code-snippet astro-gcb4dmcu"> const emitter = mitt();<br class="astro-gcb4dmcu"> // Events flying everywhere!<br class="astro-gcb4dmcu"> emitter.emit(&#39;userChange&#39;, username);<br class="astro-gcb4dmcu"> emitter.on(&#39;userChange&#39;, (name) =&gt; {...}); </div> </div> <div class="event-paths astro-gcb4dmcu"></div> </div> <!-- Components with event bus usage --> <div class="components-grid astro-gcb4dmcu"> <div class="component header astro-gcb4dmcu" data-component="Header"> <div class="component-header astro-gcb4dmcu">Header</div> <div class="component-content astro-gcb4dmcu"> <div class="emit-code astro-gcb4dmcu">emitter.emit(&#39;userChange&#39;, &#39;John&#39;)</div>
username: <span class="user-text astro-gcb4dmcu">Guest</span> </div> <div class="event-dot emitter astro-gcb4dmcu"></div> </div> <div class="component sidebar astro-gcb4dmcu" data-component="Sidebar"> <div class="component-header astro-gcb4dmcu">Sidebar</div> <div class="component-content astro-gcb4dmcu"> <div class="listen-code astro-gcb4dmcu"> emitter.on(&#39;userChange&#39;, setUsername) </div>
username: <span class="user-text astro-gcb4dmcu">Guest</span> </div> <div class="event-dot listener astro-gcb4dmcu"></div> </div> <div class="component footer astro-gcb4dmcu" data-component="Footer"> <div class="component-header astro-gcb4dmcu">Footer</div> <div class="component-content astro-gcb4dmcu"> <div class="emit-code astro-gcb4dmcu">emitter.emit(&#39;userChange&#39;, &#39;Alice&#39;)</div>
username: <span class="user-text astro-gcb4dmcu">Guest</span> </div> <div class="event-dot emitter astro-gcb4dmcu"></div> </div> <div class="component settings astro-gcb4dmcu" data-component="Settings"> <div class="component-header astro-gcb4dmcu">Settings</div> <div class="component-content astro-gcb4dmcu"> <div class="listen-code astro-gcb4dmcu">emitter.on(&#39;userChange&#39;, updateUI)</div>
username: <span class="user-text astro-gcb4dmcu">Guest</span> </div> <div class="event-dot listener astro-gcb4dmcu"></div> </div> </div> </div> </div>  <script type="module">function y(){const d=document.getElementById("event-bus-userButton"),m=document.getElementById("event-bus-userValue"),E=document.querySelectorAll(".event-bus-demo .user-text"),B=document.querySelectorAll(".event-bus-demo .component"),s=document.querySelector(".event-bus-demo .event-bus"),h=document.querySelector(".event-bus-demo .event-paths"),u=["Guest","John","Alice","Bob"];let i=0;function f(o,c,t,e){if(!h)return;const n=document.createElement("div");n.className="event-particle",n.style.left=`${o}px`,n.style.top=`${c}px`,h.appendChild(n);const l=n.animate([{transform:"translate(0, 0)",opacity:1},{transform:`translate(${t-o}px, ${e-c}px)`,opacity:0}],{duration:600,easing:"ease-out"});l.onfinish=()=>n.remove()}function L(){if(!s)return;const o=document.querySelectorAll(".event-dot.emitter"),c=document.querySelectorAll(".event-dot.listener"),t=s.getBoundingClientRect(),e=document.querySelector(".event-bus-demo")?.getBoundingClientRect();e&&o.forEach((n,l)=>{setTimeout(()=>{const p=n.getBoundingClientRect(),r=n.closest(".component");r&&(r.classList.add("highlight"),f(p.left-e.left,p.top-e.top,t.left-e.left+t.width/2,t.top-e.top+t.height),setTimeout(()=>{r.classList.remove("highlight"),c.forEach(g=>{const v=g.getBoundingClientRect();f(t.left-e.left+t.width/2,t.top-e.top+t.height,v.left-e.left,v.top-e.top);const a=g.closest(".component");a&&setTimeout(()=>{a.classList.add("highlight"),setTimeout(()=>a.classList.remove("highlight"),600)},300)})},600))},l*1500)})}function b(){s&&(s.classList.add("updating"),setTimeout(()=>s.classList.remove("updating"),500))}function C(){i=(i+1)%u.length,m&&(m.textContent=u[i]),b(),E.forEach(o=>{o.textContent=u[i]}),L()}B.forEach(o=>{o.addEventListener("click",function(){this.classList.add("highlight"),setTimeout(()=>this.classList.remove("highlight"),800)})}),d&&d.addEventListener("click",C)}document.readyState==="loading"?document.addEventListener("DOMContentLoaded",y):y();</script>
<p>Event buses create more problems than they solve for state management:</p>
<ol>
<li>
<p><strong>Spaghetti Data Flow</strong><br/>
Components become invisibly coupled through arbitrary events. When <code>ComponentA</code> emits <code>update-theme</code>, who’s listening? Why? DevTools can’t help you track the chaos.</p>
</li>
<li>
<p><strong>State Inconsistencies</strong><br/>
Multiple components listening to the same event often maintain duplicate state:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="javascript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Two components, two sources of truth</span></span>
<span class="line"><span style="color:#C0CAF5">eventBus</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">on</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">login</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> (</span><span style="color:#F7768E">this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">isLoggedIn</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">eventBus</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">on</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">login</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> (</span><span style="color:#F7768E">this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">userStatus</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">active</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// Two components, two sources of truth
eventBus.on(&#34;login&#34;, () => (this.isLoggedIn = true));
eventBus.on(&#34;login&#34;, () => (this.userStatus = &#34;active&#34;));" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
</li>
<li>
<p><strong>Memory Leaks</strong><br/>
Forgotten event listeners in unmounted components keep reacting to events, causing bugs and performance issues.</p>
</li>
</ol>
<p><strong>Where Event Buses Actually Work</strong></p>
<ul>
<li>✅ Global notifications (toasts, alerts)</li>
<li>✅ Analytics tracking</li>
<li>✅ Decoupled plugin events</li>
</ul>
<p><strong>Instead of Event Buses</strong>: Use Pinia for state, composables for logic, and provide/inject for component trees.</p>
<p><svg id="mermaid-0" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:610.890625px" viewBox="0 -50 610.890625 433.796875" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-0 .cluster-label text{fill:#F9FFFE;}#mermaid-0 .cluster-label span{color:#F9FFFE;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#ccc;color:#ccc;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-0 .arrowheadPath{fill:lightgrey;}#mermaid-0 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-0 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-0 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-0 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-0 .cluster text{fill:#F9FFFE;}#mermaid-0 .cluster span{color:#F9FFFE;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-0 .icon-shape rect,#mermaid-0 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-0_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M151.787,62L142.455,68.167C133.124,74.333,114.46,86.667,105.129,103.15C95.797,119.633,95.797,140.266,95.797,150.582L95.797,160.898" id="L_A_B_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_B_0" data-points="W3sieCI6MTUxLjc4NjkyNjI2OTUzMTI1LCJ5Ijo2Mn0seyJ4Ijo5NS43OTY4NzUsInkiOjk5fSx7IngiOjk1Ljc5Njg3NSwieSI6MTY0Ljg5ODQzNzV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M233.502,62L242.834,68.167C252.165,74.333,270.829,86.667,280.161,98.333C289.492,110,289.492,121,289.492,126.5L289.492,132" id="L_A_C_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_C_0" data-points="W3sieCI6MjMzLjUwMjEzNjIzMDQ2ODc1LCJ5Ijo2Mn0seyJ4IjoyODkuNDkyMTg3NSwieSI6OTl9LHsieCI6Mjg5LjQ5MjE4NzUsInkiOjEzNn1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M251.232,209.536L224.023,222.08C196.813,234.623,142.395,259.71,115.186,277.753C87.977,295.797,87.977,306.797,87.977,312.297L87.977,317.797" id="L_C_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_D_0" data-points="W3sieCI6MjUxLjIzMTc1NzcwMzY2MTk0LCJ5IjoyMDkuNTM2NDQ1MjAzNjYxOTR9LHsieCI6ODcuOTc2NTYyNSwieSI6Mjg0Ljc5Njg3NX0seyJ4Ijo4Ny45NzY1NjI1LCJ5IjozMjEuNzk2ODc1fV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M289.492,247.797L289.492,253.964C289.492,260.13,289.492,272.464,289.492,284.13C289.492,295.797,289.492,306.797,289.492,312.297L289.492,317.797" id="L_C_E_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_E_0" data-points="W3sieCI6Mjg5LjQ5MjE4NzUsInkiOjI0Ny43OTY4NzV9LHsieCI6Mjg5LjQ5MjE4NzUsInkiOjI4NC43OTY4NzV9LHsieCI6Mjg5LjQ5MjE4NzUsInkiOjMyMS43OTY4NzV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M329.329,207.96L361.092,220.766C392.855,233.572,456.381,259.185,488.143,277.491C519.906,295.797,519.906,306.797,519.906,312.297L519.906,317.797" id="L_C_F_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_F_0" data-points="W3sieCI6MzI5LjMyOTE0NDIyNjkzNTUsInkiOjIwNy45NTk5MTgyNzMwNjQ0Nn0seyJ4Ijo1MTkuOTA2MjUsInkiOjI4NC43OTY4NzV9LHsieCI6NTE5LjkwNjI1LCJ5IjozMjEuNzk2ODc1fV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel" transform="translate(95.796875, 99)"><g class="label" data-id="L_A_B_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>No</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(289.4921875, 99)"><g class="label" data-id="L_A_C_0" transform="translate(-14.453125, -12)"><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Yes</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(87.9765625, 284.796875)"><g class="label" data-id="L_C_D_0" transform="translate(-38.53125, -12)"><foreignObject width="77.0625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>App-wide</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(289.4921875, 284.796875)"><g class="label" data-id="L_C_E_0" transform="translate(-67.4296875, -12)"><foreignObject width="134.859375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Component Tree</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(519.90625, 284.796875)"><g class="label" data-id="L_C_F_0" transform="translate(-67.4296875, -12)"><foreignObject width="134.859375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Reusable Logic</p></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-0" transform="translate(192.64453125, 35)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Need Shared State?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B-1" transform="translate(95.796875, 191.8984375)"><rect class="basic label-container" style="" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Props/Events</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C-3" transform="translate(289.4921875, 191.8984375)"><polygon points="55.8984375,0 111.796875,-55.8984375 55.8984375,-111.796875 0,-55.8984375" class="label-container" transform="translate(-55.3984375, 55.8984375)"></polygon><g class="label" style="" transform="translate(-28.8984375, -12)"><rect></rect><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Scope?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-D-5" transform="translate(87.9765625, 348.796875)"><rect class="basic label-container" style="" x="-54.0859375" y="-27" width="108.171875" height="54"></rect><g class="label" style="" transform="translate(-24.0859375, -12)"><rect></rect><foreignObject width="48.171875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Pinia</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-E-7" transform="translate(289.4921875, 348.796875)"><rect class="basic label-container" style="" x="-97.4296875" y="-27" width="194.859375" height="54"></rect><g class="label" style="" transform="translate(-67.4296875, -12)"><rect></rect><foreignObject width="134.859375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Provide/Inject</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-F-9" transform="translate(519.90625, 348.796875)"><rect class="basic label-container" style="" x="-82.984375" y="-27" width="165.96875" height="54"></rect><g class="label" style="" transform="translate(-52.984375, -12)"><rect></rect><foreignObject width="105.96875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Composables</p></span></div></foreignObject></g></g></g></g></g><text text-anchor="middle" x="305.4453125" y="-25" class="flowchartTitleText">Decision Guide: Choosing Your Weapon</text></svg></p>
<h2 id="pro-tips-for-state-management-success">Pro Tips for State Management Success<a class="heading-link" aria-label="Link to section" href="#pro-tips-for-state-management-success"><span class="heading-link-icon">#</span></a></h2>
<ol>
<li><strong>Start Simple</strong>: Begin with props, graduate to composables</li>
<li><strong>Type Everything</strong>: Use TypeScript for stores/injections</li>
<li><strong>Name Wisely</strong>: Prefix stores (<code>useUserStore</code>) and injection keys (<code>UserKey</code>)</li>
<li><strong>Monitor Performance</strong>: Use Vue DevTools to track reactivity</li>
<li><strong>Test State</strong>: Write unit tests for Pinia stores/composables</li>
</ol>
<p>By mastering these patterns, you’ll write Vue apps that scale gracefully while keeping component relationships clear and maintainable.</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_solving-prop-drilling-in-vue" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="solving-prop-drilling-in-vue" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vue</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/solving-prop-drilling-in-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/solving-prop-drilling-in-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/solving-prop-drilling-in-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/solving-prop-drilling-in-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/solving-prop-drilling-in-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/solving-prop-drilling-in-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/solving-prop-drilling-in-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/vue-typescript-variant-props-type-safe-props/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How to Use the Variant Props Pattern in Vue</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to create type-safe Vue components where prop types depend on other props using TypeScript discriminated unions. A practical guide with real-world examples. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2024-12-15T00:00:00.000Z">Dec 15, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/tea-architecture-pinia-private-store-pattern/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How to Write Better Pinia Stores with the Elm Pattern</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to combine The Elm Architecture (TEA) principles with Pinia&#39;s private store pattern for testable, framework-agnostic state management in Vue applications. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-10-03T00:00:00.000Z">Oct 3, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/inline-vue-composables-refactoring/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">The Inline Vue Composables Refactoring pattern</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to apply Martin Fowler&#39;s Extract Function pattern to Vue components using inline composables, making your code cleaner and more maintainable. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-04-01T00:00:00.000Z">Apr 1, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "solving-prop-drilling-in-vue";

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
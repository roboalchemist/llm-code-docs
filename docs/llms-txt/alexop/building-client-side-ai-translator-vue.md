# Source: https://alexop.dev/posts/building-client-side-ai-translator-vue

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/building-client-side-ai-translator-vue/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>The Browser That Speaks 200 Languages: Building an AI Translator Without APIs | alexop.dev</title><meta name="title" content="The Browser That Speaks 200 Languages: Building an AI Translator Without APIs | alexop.dev"><meta name="description" content="Learn how to build a browser-based translator that works offline and handles 200 languages using Vue and Transformers.js"><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="The Browser That Speaks 200 Languages: Building an AI Translator Without APIs | alexop.dev"><meta property="og:description" content="Learn how to build a browser-based translator that works offline and handles 200 languages using Vue and Transformers.js"><meta property="og:url" content="https://alexop.dev/posts/building-client-side-ai-translator-vue/"><meta property="og:image" content="https://alexop.dev/posts/the-browser-that-speaks-200-languages-building-an-ai-translator-without-ap-is/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-02-02T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/building-client-side-ai-translator-vue/"><meta property="twitter:title" content="The Browser That Speaks 200 Languages: Building an AI Translator Without APIs | alexop.dev"><meta property="twitter:description" content="Learn how to build a browser-based translator that works offline and handles 200 languages using Vue and Transformers.js"><meta property="twitter:image" content="https://alexop.dev/posts/the-browser-that-speaks-200-languages-building-an-ai-translator-without-ap-is/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"The Browser That Speaks 200 Languages: Building an AI Translator Without APIs | alexop.dev","description":"Learn how to build a browser-based translator that works offline and handles 200 languages using Vue and Transformers.js","image":"https://alexop.dev/posts/the-browser-that-speaks-200-languages-building-an-ai-translator-without-ap-is/index.png","datePublished":"2025-02-02T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: the-browser-that-speaks-200-languages-building-an-ai-translator-without-ap-is; }@layer astro { ::view-transition-old(the-browser-that-speaks-200-languages-building-an-ai-translator-without-ap-is) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(the-browser-that-speaks-200-languages-building-an-ai-translator-without-ap-is) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(the-browser-that-speaks-200-languages-building-an-ai-translator-without-ap-is) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(the-browser-that-speaks-200-languages-building-an-ai-translator-without-ap-is) { 
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
	animation-name: astroFadeIn; }</style><style>.stackblitz-container:where(.astro-rrlsyoos){width:100%;margin:2rem 0;border-radius:8px;overflow:hidden;border:1px solid rgb(var(--color-border));background-color:rgb(var(--color-card));position:relative}.loading-overlay:where(.astro-rrlsyoos){position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background-color:rgb(var(--color-card));color:rgb(var(--color-text-base));font-size:1.1rem;z-index:1}iframe:where(.astro-rrlsyoos){width:100%;height:var(--height);border:none;position:relative;z-index:2}@media(max-width:768px){.stackblitz-container:where(.astro-rrlsyoos){margin:1rem 0}iframe:where(.astro-rrlsyoos){height:calc(var(--height) * .8)}}
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">The Browser That Speaks 200 Languages: Building an AI Translator Without APIs</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-02-02T00:00:00.000Z">Feb 2, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="MTv70" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;The Browser That Speaks 200 Languages: Building an AI Translator Without APIs&quot;],&quot;content&quot;:[0,&quot;import StackBlitzEmbed from \&quot;@features/mdx-components/components/StackBlitzEmbed.astro\&quot;;\n\n## Introduction\n\nMost AI translation tools rely on external APIs.\nThis means sending data to servers and paying for each request. But what if you could run translations directly in your browser? This guide shows you how to build a free, offline translator that handles 200 languages using Vue and Transformers.js.\n\n## The Tools\n\n- Vue 3 for the interface\n- Transformers.js to run AI models locally\n- Web Workers to handle heavy processing\n- NLLB-200, Meta&#39;s translation model\n\n```mermaid\n---\ntitle: Architecture Overview\n---\n\ngraph LR\n    Frontend[Vue Frontend]\n    Worker[Web Worker]\n    TJS[Transformers.js]\n    Model[NLLB-200 Model]\n\n    Frontend --&gt;|\&quot;Text\&quot;| Worker\n    Worker --&gt;|\&quot;Initialize\&quot;| TJS\n    TJS --&gt;|\&quot;Load\&quot;| Model\n    Model --&gt;|\&quot;Results\&quot;| TJS\n    TJS --&gt;|\&quot;Stream\&quot;| Worker\n    Worker --&gt;|\&quot;Translation\&quot;| Frontend\n\n    classDef default fill:#344060,stroke:#AB4B99,color:#EAEDF3\n    classDef accent fill:#8A337B,stroke:#AB4B99,color:#EAEDF3\n\n    class TJS,Model accent\n```\n\n## Building the Translator\n\n![AI Translator](../../assets/images/vue-ai-translate.png)\n\n### 1. Set Up Your Project\n\nCreate a new Vue project with TypeScript:\n\n```bash\nnpm create vite@latest vue-translator -- --template vue-ts\ncd vue-translator\nnpm install\nnpm install @huggingface/transformers\n```\n\n### 2. Create the Translation Worker\n\nThe translation happens in a background process. Create `src/worker/translation.worker.ts`:\n\n```typescript\nimport {\n  pipeline,\n  TextStreamer,\n  TranslationPipeline,\n} from \&quot;@huggingface/transformers\&quot;;\nimport type { PipelineType, ProgressCallback } from \&quot;@huggingface/transformers\&quot;;\n\n// Singleton pattern for the translation pipeline\nclass MyTranslationPipeline {\n  static task: PipelineType = \&quot;translation\&quot;;\n  // We use the distilled model for faster loading and inference\n  static model = \&quot;Xenova/nllb-200-distilled-600M\&quot;;\n  static instance: TranslationPipeline | null = null;\n\n  static async getInstance(progress_callback?: ProgressCallback) {\n    if (!this.instance) {\n      this.instance = (await pipeline(this.task, this.model, {\n        progress_callback,\n      })) as TranslationPipeline;\n    }\n    return this.instance;\n  }\n}\n\n// Type definitions for worker messages\ninterface TranslationRequest {\n  text: string;\n  src_lang: string;\n  tgt_lang: string;\n}\n\n// Worker message handler\nself.addEventListener(\n  \&quot;message\&quot;,\n  async (event: MessageEvent&lt;TranslationRequest&gt;) =&gt; {\n    try {\n      // Initialize the translation pipeline with progress tracking\n      const translator = await MyTranslationPipeline.getInstance(x =&gt; {\n        self.postMessage(x);\n      });\n\n      // Configure streaming for real-time translation updates\n      const streamer = new TextStreamer(translator.tokenizer, {\n        skip_prompt: true,\n        skip_special_tokens: true,\n        callback_function: (text: string) =&gt; {\n          self.postMessage({\n            status: \&quot;update\&quot;,\n            output: text,\n          });\n        },\n      });\n\n      // Perform the translation\n      const output = await translator(event.data.text, {\n        // @ts-ignore - Type definitions are incomplete\n        tgt_lang: event.data.tgt_lang,\n        src_lang: event.data.src_lang,\n        streamer,\n      });\n\n      // Send the final result\n      self.postMessage({\n        status: \&quot;complete\&quot;,\n        output,\n      });\n    } catch (error) {\n      self.postMessage({\n        status: \&quot;error\&quot;,\n        error:\n          error instanceof Error ? error.message : \&quot;An unknown error occurred\&quot;,\n      });\n    }\n  }\n);\n```\n\n### 3. Build the Interface\n\nCreate a clean interface with two main components:\n\n#### Language Selector (`src/components/LanguageSelector.vue`)\n\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\n// Language codes follow the ISO 639-3 standard with script codes\nconst LANGUAGES: Record&lt;string, string&gt; = {\n  English: \&quot;eng_Latn\&quot;,\n  French: \&quot;fra_Latn\&quot;,\n  Spanish: \&quot;spa_Latn\&quot;,\n  German: \&quot;deu_Latn\&quot;,\n  Chinese: \&quot;zho_Hans\&quot;,\n  Japanese: \&quot;jpn_Jpan\&quot;,\n  // Add more languages as needed\n};\n// Strong typing for component props\ninterface Props {\n  type: string;\n  modelValue: string;\n}\n\ndefineProps&lt;Props&gt;();\nconst emit = defineEmits&lt;{\n  (e: \&quot;update:modelValue\&quot;, value: string): void;\n}&gt;();\n\nconst onChange = (event: Event) =&gt; {\n  const target = event.target as HTMLSelectElement;\n  emit(\&quot;update:modelValue\&quot;, target.value);\n};\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;div class=\&quot;language-selector\&quot;&gt;\n    &lt;label&gt;{{ type }}: &lt;/label&gt;\n    &lt;select :value=\&quot;modelValue\&quot; @change=\&quot;onChange\&quot;&gt;\n      &lt;option\n        v-for=\&quot;[key, value] in Object.entries(LANGUAGES)\&quot;\n        :key=\&quot;key\&quot;\n        :value=\&quot;value\&quot;\n      &gt;\n        {{ key }}\n      &lt;/option&gt;\n    &lt;/select&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n\n&lt;style scoped&gt;\n.language-selector {\n  display: flex;\n  align-items: center;\n  gap: 0.5rem;\n}\n\nselect {\n  padding: 0.5rem;\n  border-radius: 4px;\n  border: 1px solid rgb(var(--color-border));\n  background-color: rgb(var(--color-card));\n  color: rgb(var(--color-text-base));\n  min-width: 200px;\n}\n&lt;/style&gt;\n```\n\n#### Progress Bar (`src/components/ProgressBar.vue`)\n\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\ndefineProps&lt;{\n  text: string;\n  percentage: number;\n}&gt;();\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;div class=\&quot;progress-container\&quot;&gt;\n    &lt;div class=\&quot;progress-bar\&quot; :style=\&quot;{ width: `${percentage}%` }\&quot;&gt;\n      {{ text }} ({{ percentage.toFixed(2) }}%)\n    &lt;/div&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n\n&lt;style scoped&gt;\n.progress-container {\n  width: 100%;\n  height: 20px;\n  background-color: rgb(var(--color-card));\n  border-radius: 10px;\n  margin: 10px 0;\n  overflow: hidden;\n  border: 1px solid rgb(var(--color-border));\n}\n\n.progress-bar {\n  height: 100%;\n  background-color: rgb(var(--color-accent));\n  transition: width 0.3s ease;\n  display: flex;\n  align-items: center;\n  padding: 0 10px;\n  color: rgb(var(--color-text-base));\n  font-size: 0.9rem;\n  white-space: nowrap;\n}\n\n.progress-bar:hover {\n  background-color: rgb(var(--color-card-muted));\n}\n&lt;/style&gt;\n```\n\n### 4. Put It All Together\n\nIn your main app file:\n\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { ref, onMounted, onUnmounted, watch, computed } from \&quot;vue\&quot;;\nimport LanguageSelector from \&quot;./components/LanguageSelector.vue\&quot;;\nimport ProgressBar from \&quot;./components/ProgressBar.vue\&quot;;\n\ninterface ProgressItem {\n  file: string;\n  progress: number;\n}\n\n// State\nconst worker = ref&lt;Worker | null&gt;(null);\nconst ready = ref&lt;boolean | null&gt;(null);\nconst disabled = ref(false);\nconst progressItems = ref&lt;Map&lt;string, ProgressItem&gt;&gt;(new Map());\n\nconst input = ref(\&quot;I love walking my dog.\&quot;);\nconst sourceLanguage = ref(\&quot;eng_Latn\&quot;);\nconst targetLanguage = ref(\&quot;fra_Latn\&quot;);\nconst output = ref(\&quot;\&quot;);\n\n// Computed property for progress items array\nconst progressItemsArray = computed(() =&gt; {\n  return Array.from(progressItems.value.values());\n});\n\n// Watch progress items\nwatch(\n  progressItemsArray,\n  newItems =&gt; {\n    console.log(\&quot;Progress items updated:\&quot;, newItems);\n  },\n  { deep: true }\n);\n\n// Translation handler\nconst translate = () =&gt; {\n  if (!worker.value) return;\n\n  disabled.value = true;\n  output.value = \&quot;\&quot;;\n\n  worker.value.postMessage({\n    text: input.value,\n    src_lang: sourceLanguage.value,\n    tgt_lang: targetLanguage.value,\n  });\n};\n\n// Worker message handler\nconst onMessageReceived = (e: MessageEvent) =&gt; {\n  switch (e.data.status) {\n    case \&quot;initiate\&quot;:\n      ready.value = false;\n      progressItems.value.set(e.data.file, {\n        file: e.data.file,\n        progress: 0,\n      });\n      progressItems.value = new Map(progressItems.value);\n      break;\n\n    case \&quot;progress\&quot;:\n      if (progressItems.value.has(e.data.file)) {\n        progressItems.value.set(e.data.file, {\n          file: e.data.file,\n          progress: e.data.progress,\n        });\n        progressItems.value = new Map(progressItems.value);\n      }\n      break;\n\n    case \&quot;done\&quot;:\n      progressItems.value.delete(e.data.file);\n      progressItems.value = new Map(progressItems.value);\n      break;\n\n    case \&quot;ready\&quot;:\n      ready.value = true;\n      break;\n\n    case \&quot;update\&quot;:\n      output.value += e.data.output;\n      break;\n\n    case \&quot;complete\&quot;:\n      disabled.value = false;\n      break;\n\n    case \&quot;error\&quot;:\n      console.error(\&quot;Translation error:\&quot;, e.data.error);\n      disabled.value = false;\n      break;\n  }\n};\n\n// Lifecycle hooks\nonMounted(() =&gt; {\n  worker.value = new Worker(\n    new URL(\&quot;./workers/translation.worker.ts\&quot;, import.meta.url),\n    { type: \&quot;module\&quot; }\n  );\n  worker.value.addEventListener(\&quot;message\&quot;, onMessageReceived);\n});\n\nonUnmounted(() =&gt; {\n  worker.value?.removeEventListener(\&quot;message\&quot;, onMessageReceived);\n  worker.value?.terminate();\n});\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;div class=\&quot;app\&quot;&gt;\n    &lt;h1&gt;Transformers.js&lt;/h1&gt;\n    &lt;h2&gt;ML-powered multilingual translation in Vue!&lt;/h2&gt;\n\n    &lt;div class=\&quot;container\&quot;&gt;\n      &lt;div class=\&quot;language-container\&quot;&gt;\n        &lt;LanguageSelector type=\&quot;Source\&quot; v-model=\&quot;sourceLanguage\&quot; /&gt;\n        &lt;LanguageSelector type=\&quot;Target\&quot; v-model=\&quot;targetLanguage\&quot; /&gt;\n      &lt;/div&gt;\n\n      &lt;div class=\&quot;textbox-container\&quot;&gt;\n        &lt;textarea\n          v-model=\&quot;input\&quot;\n          rows=\&quot;3\&quot;\n          placeholder=\&quot;Enter text to translate...\&quot;\n        /&gt;\n        &lt;textarea\n          v-model=\&quot;output\&quot;\n          rows=\&quot;3\&quot;\n          readonly\n          placeholder=\&quot;Translation will appear here...\&quot;\n        /&gt;\n      &lt;/div&gt;\n    &lt;/div&gt;\n\n    &lt;button :disabled=\&quot;disabled || ready === false\&quot; @click=\&quot;translate\&quot;&gt;\n      {{ ready === false ? \&quot;Loading...\&quot; : \&quot;Translate\&quot; }}\n    &lt;/button&gt;\n\n    &lt;div class=\&quot;progress-bars-container\&quot;&gt;\n      &lt;label v-if=\&quot;ready === false\&quot;&gt; Loading models... (only run once) &lt;/label&gt;\n      &lt;div v-for=\&quot;item in progressItemsArray\&quot; :key=\&quot;item.file\&quot;&gt;\n        &lt;ProgressBar :text=\&quot;item.file\&quot; :percentage=\&quot;item.progress\&quot; /&gt;\n      &lt;/div&gt;\n    &lt;/div&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n\n&lt;style scoped&gt;\n.app {\n  max-width: 800px;\n  margin: 0 auto;\n  padding: 2rem;\n  text-align: center;\n}\n\n.container {\n  margin: 2rem 0;\n}\n\n.language-container {\n  display: flex;\n  justify-content: center;\n  gap: 2rem;\n  margin-bottom: 1rem;\n}\n\n.textbox-container {\n  display: flex;\n  gap: 1rem;\n}\n\ntextarea {\n  flex: 1;\n  padding: 0.5rem;\n  border-radius: 4px;\n  border: 1px solid rgb(var(--color-border));\n  background-color: rgb(var(--color-card));\n  color: rgb(var(--color-text-base));\n  font-size: 1rem;\n  min-height: 100px;\n  resize: vertical;\n}\n\nbutton {\n  padding: 0.5rem 2rem;\n  font-size: 1.1rem;\n  cursor: pointer;\n  background-color: rgb(var(--color-accent));\n  color: rgb(var(--color-text-base));\n  border: none;\n  border-radius: 4px;\n  transition: background-color 0.3s;\n}\n\nbutton:hover:not(:disabled) {\n  background-color: rgb(var(--color-card-muted));\n}\n\nbutton:disabled {\n  opacity: 0.6;\n  cursor: not-allowed;\n}\n\n.progress-bars-container {\n  margin-top: 2rem;\n}\n\nh1 {\n  color: rgb(var(--color-text-base));\n  margin-bottom: 0.5rem;\n}\n\nh2 {\n  color: rgb(var(--color-card-muted));\n  font-size: 1.2rem;\n  font-weight: normal;\n  margin-top: 0;\n}\n&lt;/style&gt;\n```\n\n## Step 5: Optimizing the Build\n\nConfigure Vite to handle our Web Workers and TypeScript efficiently:\n\n```typescript\nimport { defineConfig } from \&quot;vite\&quot;;\nimport vue from \&quot;@vitejs/plugin-vue\&quot;;\n\nexport default defineConfig({\n  plugins: [vue()],\n  worker: {\n    format: \&quot;es\&quot;, // Use ES modules format for workers\n    plugins: [], // No additional plugins needed for workers\n  },\n  optimizeDeps: {\n    exclude: [\&quot;@huggingface/transformers\&quot;], // Prevent Vite from trying to bundle Transformers.js\n  },\n});\n```\n\n## How It Works\n\n1. You type text and select languages\n2. The text goes to a Web Worker\n3. Transformers.js loads the AI model (once)\n4. The model translates your text\n5. You see the translation appear in real time\n\nThe translator works offline after the first run. No data leaves your browser. No API keys needed.\n\n## Try It Yourself\n\n&lt;StackBlitzEmbed repo=\&quot;alexanderop/vue-ai-translate-poc\&quot; /&gt;\n\nWant to explore the code further? Check out the complete source code on [GitHub](https://github.com/alexanderop/vue-ai-translate-poc).\n\nWant to learn more? Explore these resources:\n\n- [Transformers.js docs](https://huggingface.co/docs/transformers.js)\n- [NLLB-200 model details](https://huggingface.co/facebook/nllb-200-distilled-600M)\n- [Web Workers guide](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API)&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <h2 id="introduction">Introduction<a class="heading-link" aria-label="Link to section" href="#introduction"><span class="heading-link-icon">#</span></a></h2>
<p>Most AI translation tools rely on external APIs.
This means sending data to servers and paying for each request. But what if you could run translations directly in your browser? This guide shows you how to build a free, offline translator that handles 200 languages using Vue and Transformers.js.</p>
<h2 id="the-tools">The Tools<a class="heading-link" aria-label="Link to section" href="#the-tools"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li>Vue 3 for the interface</li>
<li>Transformers.js to run AI models locally</li>
<li>Web Workers to handle heavy processing</li>
<li>NLLB-200, Meta’s translation model</li>
</ul>
<p><svg id="mermaid-0" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:1167.015625px" viewBox="0 -50 1167.015625 134" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-0 .cluster-label text{fill:#F9FFFE;}#mermaid-0 .cluster-label span{color:#F9FFFE;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#ccc;color:#ccc;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-0 .arrowheadPath{fill:lightgrey;}#mermaid-0 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-0 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-0 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-0 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-0 .cluster text{fill:#F9FFFE;}#mermaid-0 .cluster span{color:#F9FFFE;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-0 .icon-shape rect,#mermaid-0 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}#mermaid-0 .default>*{fill:#344060!important;stroke:#AB4B99!important;color:#EAEDF3!important;}#mermaid-0 .default span{fill:#344060!important;stroke:#AB4B99!important;color:#EAEDF3!important;}#mermaid-0 .default tspan{fill:#EAEDF3!important;}#mermaid-0 .accent>*{fill:#8A337B!important;stroke:#AB4B99!important;color:#EAEDF3!important;}#mermaid-0 .accent span{fill:#8A337B!important;stroke:#AB4B99!important;color:#EAEDF3!important;}#mermaid-0 .accent tspan{fill:#EAEDF3!important;}</style><g><marker id="mermaid-0_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M183.594,30.349L196.591,28.624C209.589,26.899,235.583,23.45,260.918,23.463C286.253,23.476,310.927,26.953,323.264,28.691L335.602,30.429" id="L_Frontend_Worker_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Frontend_Worker_0" data-points="W3sieCI6MTgzLjU5Mzc1LCJ5IjozMC4zNDg5MTYxMTY4NzA4NzV9LHsieCI6MjYxLjU3ODEyNSwieSI6MjB9LHsieCI6MzM5LjU2MjUsInkiOjMwLjk4NzM0MTc3MjE1MTl9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M495.891,30.637L508.085,28.864C520.279,27.091,544.667,23.546,568.393,23.219C592.12,22.893,615.185,25.786,626.717,27.232L638.25,28.678" id="L_Worker_TJS_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Worker_TJS_0" data-points="W3sieCI6NDk1Ljg5MDYyNSwieSI6MzAuNjM2NTUxMzY4MDk0OTl9LHsieCI6NTY5LjA1NDY4NzUsInkiOjIwfSx7IngiOjY0Mi4yMTg3NSwieSI6MjkuMTc2MDU2NjUxNjcyMzgzfV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M846.719,28.025L856.505,26.688C866.292,25.35,885.865,22.675,904.777,22.623C923.69,22.572,941.943,25.143,951.069,26.429L960.195,27.715" id="L_TJS_Model_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_TJS_Model_0" data-points="W3sieCI6ODQ2LjcxODc1LCJ5IjoyOC4wMjUyMzc4MTc4OTk0Mzh9LHsieCI6OTA1LjQzNzUsInkiOjIwfSx7IngiOjk2NC4xNTYyNSwieSI6MjguMjcyOTc3NDM1MzMyOTd9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M964.156,55.727L954.37,57.106C944.583,58.485,925.01,61.242,906.098,61.374C887.186,61.505,868.934,59.011,859.808,57.764L850.682,56.516" id="L_Model_TJS_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Model_TJS_0" data-points="W3sieCI6OTY0LjE1NjI1LCJ5Ijo1NS43MjcwMjI1NjQ2NjcwM30seyJ4Ijo5MDUuNDM3NSwieSI6NjR9LHsieCI6ODQ2LjcxODc1LCJ5Ijo1NS45NzQ3NjIxODIxMDA1Nn1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M642.219,54.824L630.025,56.353C617.831,57.883,593.443,60.941,569.714,60.794C545.986,60.646,522.918,57.293,511.383,55.616L499.849,53.939" id="L_TJS_Worker_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_TJS_Worker_0" data-points="W3sieCI6NjQyLjIxODc1LCJ5Ijo1NC44MjM5NDMzNDgzMjc2Mn0seyJ4Ijo1NjkuMDU0Njg3NSwieSI6NjR9LHsieCI6NDk1Ljg5MDYyNSwieSI6NTMuMzYzNDQ4NjMxOTA1MDF9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M339.563,53.013L326.565,54.844C313.568,56.675,287.573,60.338,262.239,60.532C236.905,60.726,212.232,57.452,199.896,55.814L187.559,54.177" id="L_Worker_Frontend_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Worker_Frontend_0" data-points="W3sieCI6MzM5LjU2MjUsInkiOjUzLjAxMjY1ODIyNzg0ODF9LHsieCI6MjYxLjU3ODEyNSwieSI6NjR9LHsieCI6MTgzLjU5Mzc1LCJ5Ijo1My42NTEwODM4ODMxMjkxMjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel" transform="translate(261.62097, 20.00604)"><g class="label" data-id="L_Frontend_Worker_0" transform="translate(-19.265625, -12)"><foreignObject width="38.53125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Text</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(569.0546875, 20)"><g class="label" data-id="L_Worker_TJS_0" transform="translate(-48.1640625, -12)"><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Initialize</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(905.4375, 20)"><g class="label" data-id="L_TJS_Model_0" transform="translate(-19.265625, -12)"><foreignObject width="38.53125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Load</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(905.4375, 64)"><g class="label" data-id="L_Model_TJS_0" transform="translate(-33.71875, -12)"><foreignObject width="67.4375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Results</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(569.0546875, 64)"><g class="label" data-id="L_TJS_Worker_0" transform="translate(-28.8984375, -12)"><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Stream</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(261.578125, 64)"><g class="label" data-id="L_Worker_Frontend_0" transform="translate(-52.984375, -12)"><foreignObject width="105.96875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Translation</p></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-Frontend-0" transform="translate(95.796875, 42)"><rect class="basic label-container" style="fill:#344060 !important;stroke:#AB4B99 !important" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="color:#EAEDF3 !important" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div style="color:rgb(234, 237, 243) !important;display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center" xmlns="http://www.w3.org/1999/xhtml"><span style="color:#EAEDF3 !important" class="nodeLabel"><p>Vue Frontend</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Worker-1" transform="translate(417.7265625, 42)"><rect class="basic label-container" style="fill:#344060 !important;stroke:#AB4B99 !important" x="-78.1640625" y="-27" width="156.328125" height="54"></rect><g class="label" style="color:#EAEDF3 !important" transform="translate(-48.1640625, -12)"><rect></rect><foreignObject width="96.328125" height="24"><div style="color:rgb(234, 237, 243) !important;display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center" xmlns="http://www.w3.org/1999/xhtml"><span style="color:#EAEDF3 !important" class="nodeLabel"><p>Web Worker</p></span></div></foreignObject></g></g><g class="node default accent" id="flowchart-TJS-2" transform="translate(744.46875, 42)"><rect class="basic label-container" style="fill:#8A337B !important;stroke:#AB4B99 !important" x="-102.25" y="-27" width="204.5" height="54"></rect><g class="label" style="color:#EAEDF3 !important" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div style="color:rgb(234, 237, 243) !important;display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center" xmlns="http://www.w3.org/1999/xhtml"><span style="color:#EAEDF3 !important" class="nodeLabel"><p>Transformers.js</p></span></div></foreignObject></g></g><g class="node default accent" id="flowchart-Model-3" transform="translate(1061.5859375, 42)"><rect class="basic label-container" style="fill:#8A337B !important;stroke:#AB4B99 !important" x="-97.4296875" y="-27" width="194.859375" height="54"></rect><g class="label" style="color:#EAEDF3 !important" transform="translate(-67.4296875, -12)"><rect></rect><foreignObject width="134.859375" height="24"><div style="color:rgb(234, 237, 243) !important;display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center" xmlns="http://www.w3.org/1999/xhtml"><span style="color:#EAEDF3 !important" class="nodeLabel"><p>NLLB-200 Model</p></span></div></foreignObject></g></g></g></g></g><text text-anchor="middle" x="583.5078125" y="-25" class="flowchartTitleText">Architecture Overview</text></svg></p>
<h2 id="building-the-translator">Building the Translator<a class="heading-link" aria-label="Link to section" href="#building-the-translator"><span class="heading-link-icon">#</span></a></h2>
<p><img src="/_astro/vue-ai-translate.tNt-GoRh_1G45Ox.webp" alt="AI Translator" loading="lazy" decoding="async" fetchpriority="auto" width="1882" height="1000"></p>
<h3 id="1-set-up-your-project">1. Set Up Your Project<a class="heading-link" aria-label="Link to section" href="#1-set-up-your-project"><span class="heading-link-icon">#</span></a></h3>
<p>Create a new Vue project with TypeScript:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">npm</span><span style="color:#9ECE6A"> create</span><span style="color:#9ECE6A"> vite@latest</span><span style="color:#9ECE6A"> vue-translator</span><span style="color:#E0AF68"> --</span><span style="color:#E0AF68"> --template</span><span style="color:#9ECE6A"> vue-ts</span></span>
<span class="line"><span style="color:#0DB9D7">cd</span><span style="color:#9ECE6A"> vue-translator</span></span>
<span class="line"><span style="color:#C0CAF5">npm</span><span style="color:#9ECE6A"> install</span></span>
<span class="line"><span style="color:#C0CAF5">npm</span><span style="color:#9ECE6A"> install</span><span style="color:#9ECE6A"> @huggingface/transformers</span></span></code><button type="button" class="copy" data-code="npm create vite@latest vue-translator -- --template vue-ts
cd vue-translator
npm install
npm install @huggingface/transformers" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="2-create-the-translation-worker">2. Create the Translation Worker<a class="heading-link" aria-label="Link to section" href="#2-create-the-translation-worker"><span class="heading-link-icon">#</span></a></h3>
<p>The translation happens in a background process. Create <code>src/worker/translation.worker.ts</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#0DB9D7">  pipeline</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#0DB9D7">  TextStreamer</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#0DB9D7">  TranslationPipeline</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@huggingface/transformers</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#BB9AF7"> type</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">PipelineType</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> ProgressCallback</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@huggingface/transformers</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Singleton pattern for the translation pipeline</span></span>
<span class="line"><span style="color:#BB9AF7">class</span><span style="color:#C0CAF5"> MyTranslationPipeline</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  static</span><span style="color:#73DACA"> task</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> PipelineType</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">translation</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // We use the distilled model for faster loading and inference</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  static</span><span style="color:#73DACA"> model</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Xenova/nllb-200-distilled-600M</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  static</span><span style="color:#73DACA"> instance</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> TranslationPipeline</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  static</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#7AA2F7"> getInstance</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">progress_callback</span><span style="color:#89DDFF">?:</span><span style="color:#C0CAF5"> ProgressCallback</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#F7768E">this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">instance</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#F7768E">      this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">instance</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7;font-style:italic">await</span><span style="color:#7AA2F7"> pipeline</span><span style="color:#9ABDF5">(</span><span style="color:#F7768E">this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">task</span><span style="color:#89DDFF">,</span><span style="color:#F7768E"> this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">model</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">        progress_callback</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      })) </span><span style="color:#89DDFF">as</span><span style="color:#C0CAF5"> TranslationPipeline</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#F7768E"> this</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">instance</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Type definitions for worker messages</span></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> TranslationRequest</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  text</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  src_lang</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  tgt_lang</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Worker message handler</span></span>
<span class="line"><span style="color:#C0CAF5">self</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">addEventListener</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#9ECE6A">message</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">event</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> MessageEvent</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">TranslationRequest</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // Initialize the translation pipeline with progress tracking</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> translator</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> MyTranslationPipeline</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getInstance</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">x</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">        self</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">postMessage</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">x</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // Configure streaming for real-time translation updates</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> streamer</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> TextStreamer</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">translator</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">tokenizer</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">        skip_prompt</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        skip_special_tokens</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">        callback_function</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">text</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">          self</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">postMessage</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">            status</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">update</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">            output</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> text</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // Perform the translation</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> output</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> translator</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">event</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">text</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">        // @ts-ignore - Type definitions are incomplete</span></span>
<span class="line"><span style="color:#73DACA">        tgt_lang</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> event</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">tgt_lang</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        src_lang</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> event</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">src_lang</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">        streamer</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // Send the final result</span></span>
<span class="line"><span style="color:#C0CAF5">      self</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">postMessage</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">        status</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">complete</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">        output</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">error</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">      self</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">postMessage</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">        status</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        error</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#C0CAF5">          error</span><span style="color:#89DDFF"> instanceof</span><span style="color:#C0CAF5"> Error</span><span style="color:#BB9AF7"> ?</span><span style="color:#C0CAF5"> error</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">message</span><span style="color:#BB9AF7"> :</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">An unknown error occurred</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="import {
  pipeline,
  TextStreamer,
  TranslationPipeline,
} from &#34;@huggingface/transformers&#34;;
import type { PipelineType, ProgressCallback } from &#34;@huggingface/transformers&#34;;

// Singleton pattern for the translation pipeline
class MyTranslationPipeline {
  static task: PipelineType = &#34;translation&#34;;
  // We use the distilled model for faster loading and inference
  static model = &#34;Xenova/nllb-200-distilled-600M&#34;;
  static instance: TranslationPipeline | null = null;

  static async getInstance(progress_callback?: ProgressCallback) {
    if (!this.instance) {
      this.instance = (await pipeline(this.task, this.model, {
        progress_callback,
      })) as TranslationPipeline;
    }
    return this.instance;
  }
}

// Type definitions for worker messages
interface TranslationRequest {
  text: string;
  src_lang: string;
  tgt_lang: string;
}

// Worker message handler
self.addEventListener(
  &#34;message&#34;,
  async (event: MessageEvent<TranslationRequest>) => {
    try {
      // Initialize the translation pipeline with progress tracking
      const translator = await MyTranslationPipeline.getInstance(x => {
        self.postMessage(x);
      });

      // Configure streaming for real-time translation updates
      const streamer = new TextStreamer(translator.tokenizer, {
        skip_prompt: true,
        skip_special_tokens: true,
        callback_function: (text: string) => {
          self.postMessage({
            status: &#34;update&#34;,
            output: text,
          });
        },
      });

      // Perform the translation
      const output = await translator(event.data.text, {
        // @ts-ignore - Type definitions are incomplete
        tgt_lang: event.data.tgt_lang,
        src_lang: event.data.src_lang,
        streamer,
      });

      // Send the final result
      self.postMessage({
        status: &#34;complete&#34;,
        output,
      });
    } catch (error) {
      self.postMessage({
        status: &#34;error&#34;,
        error:
          error instanceof Error ? error.message : &#34;An unknown error occurred&#34;,
      });
    }
  }
);" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="3-build-the-interface">3. Build the Interface<a class="heading-link" aria-label="Link to section" href="#3-build-the-interface"><span class="heading-link-icon">#</span></a></h3>
<p>Create a clean interface with two main components:</p>
<h4 id="language-selector-srccomponentslanguageselectorvue">Language Selector (<code>src/components/LanguageSelector.vue</code>)<a class="heading-link" aria-label="Link to section" href="#language-selector-srccomponentslanguageselectorvue"><span class="heading-link-icon">#</span></a></h4>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Language codes follow the ISO 639-3 standard with script codes</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> LANGUAGES</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Record</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  English</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">eng_Latn</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  French</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">fra_Latn</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  Spanish</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">spa_Latn</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  German</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">deu_Latn</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  Chinese</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">zho_Hans</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  Japanese</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">jpn_Jpan</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Add more languages as needed</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Strong typing for component props</span></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> Props</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  type</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  modelValue</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">defineProps</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Props</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> emit</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> defineEmits</span><span style="color:#89DDFF">&lt;</span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#9ABDF5">  (</span><span style="color:#E0AF68">e</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">update:modelValue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> value</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> void</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#7AA2F7"> onChange</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">event</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Event</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> target</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> event</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">target</span><span style="color:#89DDFF"> as</span><span style="color:#C0CAF5"> HTMLSelectElement</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  emit</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">update:modelValue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> target</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">language-selector</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">label</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">{{ type }}: </span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">label</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">select</span><span style="color:#BB9AF7"> :value</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">modelValue</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> @change</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">onChange</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">option</span></span>
<span class="line"><span style="color:#BB9AF7">        v-for</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">[key, value] in Object.entries(LANGUAGES)</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">        :key</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">key</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">        :value</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">value</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BA3C97">      &gt;</span></span>
<span class="line"><span style="color:#9AA5CE">        {{ key }}</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;/</span><span style="color:#F7768E">option</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">select</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">style</span><span style="color:#BB9AF7"> scoped</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">language-selector</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  display</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> flex</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  align-items</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> center</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  gap</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0.5</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#0DB9D7">select</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  padding</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0.5</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  border-radius</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 4</span><span style="color:#F7768E">px</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  border</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 1</span><span style="color:#F7768E">px</span><span style="color:#FF9E64"> solid</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-border</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  background-color</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-card</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  color</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-text-base</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  min-width</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 200</span><span style="color:#F7768E">px</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">style</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
// Language codes follow the ISO 639-3 standard with script codes
const LANGUAGES: Record<string, string> = {
  English: &#34;eng_Latn&#34;,
  French: &#34;fra_Latn&#34;,
  Spanish: &#34;spa_Latn&#34;,
  German: &#34;deu_Latn&#34;,
  Chinese: &#34;zho_Hans&#34;,
  Japanese: &#34;jpn_Jpan&#34;,
  // Add more languages as needed
};
// Strong typing for component props
interface Props {
  type: string;
  modelValue: string;
}

defineProps<Props>();
const emit = defineEmits<{
  (e: &#34;update:modelValue&#34;, value: string): void;
}>();

const onChange = (event: Event) => {
  const target = event.target as HTMLSelectElement;
  emit(&#34;update:modelValue&#34;, target.value);
};
</script>

<template>
  <div class=&#34;language-selector&#34;>
    <label>{{ type }}: </label>
    <select :value=&#34;modelValue&#34; @change=&#34;onChange&#34;>
      <option
        v-for=&#34;[key, value] in Object.entries(LANGUAGES)&#34;
        :key=&#34;key&#34;
        :value=&#34;value&#34;
      >
        {{ key }}
      </option>
    </select>
  </div>
</template>

<style scoped>
.language-selector {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

select {
  padding: 0.5rem;
  border-radius: 4px;
  border: 1px solid rgb(var(--color-border));
  background-color: rgb(var(--color-card));
  color: rgb(var(--color-text-base));
  min-width: 200px;
}
</style>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h4 id="progress-bar-srccomponentsprogressbarvue">Progress Bar (<code>src/components/ProgressBar.vue</code>)<a class="heading-link" aria-label="Link to section" href="#progress-bar-srccomponentsprogressbarvue"><span class="heading-link-icon">#</span></a></h4>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7AA2F7">defineProps</span><span style="color:#89DDFF">&lt;</span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  text</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  percentage</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">progress-container</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">progress-bar</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> :style</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">{ width: `${percentage}%` }</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#9AA5CE">      {{ text }} ({{ percentage.toFixed(2) }}%)</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">style</span><span style="color:#BB9AF7"> scoped</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">progress-container</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  width</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 100</span><span style="color:#F7768E">%</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  height</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 20</span><span style="color:#F7768E">px</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  background-color</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-card</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  border-radius</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 10</span><span style="color:#F7768E">px</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  margin</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 10</span><span style="color:#F7768E">px</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  overflow</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> hidden</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  border</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 1</span><span style="color:#F7768E">px</span><span style="color:#FF9E64"> solid</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-border</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">progress-bar</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  height</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 100</span><span style="color:#F7768E">%</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  background-color</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-accent</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  transition</span><span style="color:#89DDFF">:</span><span style="color:#BB9AF7"> width </span><span style="color:#FF9E64">0.3</span><span style="color:#F7768E">s</span><span style="color:#FF9E64"> ease</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  display</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> flex</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  align-items</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> center</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  padding</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#FF9E64"> 10</span><span style="color:#F7768E">px</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  color</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-text-base</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  font-size</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0.9</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  white-space</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> nowrap</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">progress-bar</span><span style="color:#E0AF68">:</span><span style="color:#BB9AF7">hover</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  background-color</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-card-muted</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">style</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
defineProps<{
  text: string;
  percentage: number;
}>();
</script>

<template>
  <div class=&#34;progress-container&#34;>
    <div class=&#34;progress-bar&#34; :style=&#34;{ width: `${percentage}%` }&#34;>
      {{ text }} ({{ percentage.toFixed(2) }}%)
    </div>
  </div>
</template>

<style scoped>
.progress-container {
  width: 100%;
  height: 20px;
  background-color: rgb(var(--color-card));
  border-radius: 10px;
  margin: 10px 0;
  overflow: hidden;
  border: 1px solid rgb(var(--color-border));
}

.progress-bar {
  height: 100%;
  background-color: rgb(var(--color-accent));
  transition: width 0.3s ease;
  display: flex;
  align-items: center;
  padding: 0 10px;
  color: rgb(var(--color-text-base));
  font-size: 0.9rem;
  white-space: nowrap;
}

.progress-bar:hover {
  background-color: rgb(var(--color-card-muted));
}
</style>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="4-put-it-all-together">4. Put It All Together<a class="heading-link" aria-label="Link to section" href="#4-put-it-all-together"><span class="heading-link-icon">#</span></a></h3>
<p>In your main app file:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ref</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> onMounted</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> onUnmounted</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> watch</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> computed</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> LanguageSelector</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">./components/LanguageSelector.vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> ProgressBar</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">./components/ProgressBar.vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> ProgressItem</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  file</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  progress</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// State</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> worker</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Worker</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> ready</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">boolean</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> disabled</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">false</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> progressItems</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Map</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> ProgressItem</span><span style="color:#89DDFF">&gt;&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">new</span><span style="color:#7AA2F7"> Map</span><span style="color:#9ABDF5">())</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> input</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">I love walking my dog.</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> sourceLanguage</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">eng_Latn</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> targetLanguage</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">fra_Latn</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> output</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Computed property for progress items array</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> progressItemsArray</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> computed</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> Array</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">from</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">progressItems</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">values</span><span style="color:#9ABDF5">())</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Watch progress items</span></span>
<span class="line"><span style="color:#7AA2F7">watch</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#C0CAF5">  progressItemsArray</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  newItems</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Progress items updated:</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> newItems</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span><span style="color:#73DACA"> deep</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Translation handler</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#7AA2F7"> translate</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">worker</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">  disabled</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  output</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">  worker</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">postMessage</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">    text</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> input</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    src_lang</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> sourceLanguage</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    tgt_lang</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> targetLanguage</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Worker message handler</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#7AA2F7"> onMessageReceived</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">e</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> MessageEvent</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  switch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">e</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">status</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">initiate</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#C0CAF5">      ready</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      progressItems</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">set</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">e</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">file</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">        file</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> e</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">file</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        progress</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      progressItems</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Map</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">progressItems</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">progress</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">progressItems</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">has</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">e</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">file</span><span style="color:#9ABDF5">)) {</span></span>
<span class="line"><span style="color:#C0CAF5">        progressItems</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">set</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">e</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">file</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">          file</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> e</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">file</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">          progress</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> e</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">progress</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">        progressItems</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Map</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">progressItems</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">done</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#C0CAF5">      progressItems</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">delete</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">e</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">file</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      progressItems</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Map</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">progressItems</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">ready</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#C0CAF5">      ready</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">update</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#C0CAF5">      output</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> +=</span><span style="color:#C0CAF5"> e</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">output</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">complete</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#C0CAF5">      disabled</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#C0CAF5">      console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">error</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Translation error:</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> e</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">error</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      disabled</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Lifecycle hooks</span></span>
<span class="line"><span style="color:#7AA2F7">onMounted</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  worker</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Worker</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#89DDFF">    new</span><span style="color:#7AA2F7"> URL</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">./workers/translation.worker.ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#7DCFFF"> import</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">meta</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">url</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    { </span><span style="color:#73DACA">type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">module</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  worker</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">addEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">message</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> onMessageReceived</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">onUnmounted</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  worker</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">?.</span><span style="color:#7AA2F7">removeEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">message</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> onMessageReceived</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  worker</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">?.</span><span style="color:#7AA2F7">terminate</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">app</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">h1</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Transformers.js</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">h1</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">h2</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">ML-powered multilingual translation in Vue!</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">h2</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">container</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">language-container</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;</span><span style="color:#DE5971">LanguageSelector </span><span style="color:#BB9AF7">type</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Source</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> v-model</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">sourceLanguage</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;</span><span style="color:#DE5971">LanguageSelector </span><span style="color:#BB9AF7">type</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Target</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> v-model</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">targetLanguage</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">textbox-container</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;</span><span style="color:#F7768E">textarea</span></span>
<span class="line"><span style="color:#BB9AF7">          v-model</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">input</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">          rows</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">3</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">          placeholder</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Enter text to translate...</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#FF5370">        /</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;</span><span style="color:#F7768E">textarea</span></span>
<span class="line"><span style="color:#BB9AF7">          v-model</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">output</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">          rows</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">3</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">          readonly</span></span>
<span class="line"><span style="color:#BB9AF7">          placeholder</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Translation will appear here...</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#FF5370">        /</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">button</span><span style="color:#BB9AF7"> :disabled</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">disabled || ready === false</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> @click</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">translate</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#9AA5CE">      {{ ready === false ? &quot;Loading...&quot; : &quot;Translate&quot; }}</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">progress-bars-container</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">label</span><span style="color:#BB9AF7"> v-if</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ready === false</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE"> Loading models... (only run once) </span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">label</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> v-for</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">item in progressItemsArray</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> :key</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">item.file</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;</span><span style="color:#DE5971">ProgressBar </span><span style="color:#BB9AF7">:text</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">item.file</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> :percentage</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">item.progress</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">style</span><span style="color:#BB9AF7"> scoped</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">app</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  max-width</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 800</span><span style="color:#F7768E">px</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  margin</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#FF9E64"> auto</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  padding</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 2</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  text-align</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> center</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">container</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  margin</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 2</span><span style="color:#F7768E">rem</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">language-container</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  display</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> flex</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  justify-content</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> center</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  gap</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 2</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  margin-bottom</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 1</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">textbox-container</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  display</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> flex</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  gap</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 1</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#0DB9D7">textarea</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  flex</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 1</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  padding</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0.5</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  border-radius</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 4</span><span style="color:#F7768E">px</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  border</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 1</span><span style="color:#F7768E">px</span><span style="color:#FF9E64"> solid</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-border</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  background-color</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-card</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  color</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-text-base</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  font-size</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 1</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  min-height</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 100</span><span style="color:#F7768E">px</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  resize</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> vertical</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#0DB9D7">button</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  padding</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0.5</span><span style="color:#F7768E">rem</span><span style="color:#FF9E64"> 2</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  font-size</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 1.1</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  cursor</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> pointer</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  background-color</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-accent</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  color</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-text-base</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  border</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> none</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  border-radius</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 4</span><span style="color:#F7768E">px</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  transition</span><span style="color:#89DDFF">:</span><span style="color:#BB9AF7"> background-color </span><span style="color:#FF9E64">0.3</span><span style="color:#F7768E">s</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#0DB9D7">button</span><span style="color:#E0AF68">:</span><span style="color:#BB9AF7">hover</span><span style="color:#E0AF68">:</span><span style="color:#BB9AF7">not</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">:</span><span style="color:#BB9AF7">disabled</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  background-color</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-card-muted</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#0DB9D7">button</span><span style="color:#E0AF68">:</span><span style="color:#BB9AF7">disabled</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  opacity</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0.6</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  cursor</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> not-allowed</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">progress-bars-container</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  margin-top</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 2</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#0DB9D7">h1</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  color</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-text-base</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  margin-bottom</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0.5</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#0DB9D7">h2</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  color</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> rgb</span><span style="color:#9ABDF5">(</span><span style="color:#0DB9D7">var</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">--color-card-muted</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  font-size</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 1.2</span><span style="color:#F7768E">rem</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  font-weight</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> normal</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  margin-top</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">style</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
import { ref, onMounted, onUnmounted, watch, computed } from &#34;vue&#34;;
import LanguageSelector from &#34;./components/LanguageSelector.vue&#34;;
import ProgressBar from &#34;./components/ProgressBar.vue&#34;;

interface ProgressItem {
  file: string;
  progress: number;
}

// State
const worker = ref<Worker | null>(null);
const ready = ref<boolean | null>(null);
const disabled = ref(false);
const progressItems = ref<Map<string, ProgressItem>>(new Map());

const input = ref(&#34;I love walking my dog.&#34;);
const sourceLanguage = ref(&#34;eng_Latn&#34;);
const targetLanguage = ref(&#34;fra_Latn&#34;);
const output = ref(&#34;&#34;);

// Computed property for progress items array
const progressItemsArray = computed(() => {
  return Array.from(progressItems.value.values());
});

// Watch progress items
watch(
  progressItemsArray,
  newItems => {
    console.log(&#34;Progress items updated:&#34;, newItems);
  },
  { deep: true }
);

// Translation handler
const translate = () => {
  if (!worker.value) return;

  disabled.value = true;
  output.value = &#34;&#34;;

  worker.value.postMessage({
    text: input.value,
    src_lang: sourceLanguage.value,
    tgt_lang: targetLanguage.value,
  });
};

// Worker message handler
const onMessageReceived = (e: MessageEvent) => {
  switch (e.data.status) {
    case &#34;initiate&#34;:
      ready.value = false;
      progressItems.value.set(e.data.file, {
        file: e.data.file,
        progress: 0,
      });
      progressItems.value = new Map(progressItems.value);
      break;

    case &#34;progress&#34;:
      if (progressItems.value.has(e.data.file)) {
        progressItems.value.set(e.data.file, {
          file: e.data.file,
          progress: e.data.progress,
        });
        progressItems.value = new Map(progressItems.value);
      }
      break;

    case &#34;done&#34;:
      progressItems.value.delete(e.data.file);
      progressItems.value = new Map(progressItems.value);
      break;

    case &#34;ready&#34;:
      ready.value = true;
      break;

    case &#34;update&#34;:
      output.value += e.data.output;
      break;

    case &#34;complete&#34;:
      disabled.value = false;
      break;

    case &#34;error&#34;:
      console.error(&#34;Translation error:&#34;, e.data.error);
      disabled.value = false;
      break;
  }
};

// Lifecycle hooks
onMounted(() => {
  worker.value = new Worker(
    new URL(&#34;./workers/translation.worker.ts&#34;, import.meta.url),
    { type: &#34;module&#34; }
  );
  worker.value.addEventListener(&#34;message&#34;, onMessageReceived);
});

onUnmounted(() => {
  worker.value?.removeEventListener(&#34;message&#34;, onMessageReceived);
  worker.value?.terminate();
});
</script>

<template>
  <div class=&#34;app&#34;>
    <h1>Transformers.js</h1>
    <h2>ML-powered multilingual translation in Vue!</h2>

    <div class=&#34;container&#34;>
      <div class=&#34;language-container&#34;>
        <LanguageSelector type=&#34;Source&#34; v-model=&#34;sourceLanguage&#34; />
        <LanguageSelector type=&#34;Target&#34; v-model=&#34;targetLanguage&#34; />
      </div>

      <div class=&#34;textbox-container&#34;>
        <textarea
          v-model=&#34;input&#34;
          rows=&#34;3&#34;
          placeholder=&#34;Enter text to translate...&#34;
        />
        <textarea
          v-model=&#34;output&#34;
          rows=&#34;3&#34;
          readonly
          placeholder=&#34;Translation will appear here...&#34;
        />
      </div>
    </div>

    <button :disabled=&#34;disabled || ready === false&#34; @click=&#34;translate&#34;>
      {{ ready === false ? &#34;Loading...&#34; : &#34;Translate&#34; }}
    </button>

    <div class=&#34;progress-bars-container&#34;>
      <label v-if=&#34;ready === false&#34;> Loading models... (only run once) </label>
      <div v-for=&#34;item in progressItemsArray&#34; :key=&#34;item.file&#34;>
        <ProgressBar :text=&#34;item.file&#34; :percentage=&#34;item.progress&#34; />
      </div>
    </div>
  </div>
</template>

<style scoped>
.app {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

.container {
  margin: 2rem 0;
}

.language-container {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-bottom: 1rem;
}

.textbox-container {
  display: flex;
  gap: 1rem;
}

textarea {
  flex: 1;
  padding: 0.5rem;
  border-radius: 4px;
  border: 1px solid rgb(var(--color-border));
  background-color: rgb(var(--color-card));
  color: rgb(var(--color-text-base));
  font-size: 1rem;
  min-height: 100px;
  resize: vertical;
}

button {
  padding: 0.5rem 2rem;
  font-size: 1.1rem;
  cursor: pointer;
  background-color: rgb(var(--color-accent));
  color: rgb(var(--color-text-base));
  border: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

button:hover:not(:disabled) {
  background-color: rgb(var(--color-card-muted));
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.progress-bars-container {
  margin-top: 2rem;
}

h1 {
  color: rgb(var(--color-text-base));
  margin-bottom: 0.5rem;
}

h2 {
  color: rgb(var(--color-card-muted));
  font-size: 1.2rem;
  font-weight: normal;
  margin-top: 0;
}
</style>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="step-5-optimizing-the-build">Step 5: Optimizing the Build<a class="heading-link" aria-label="Link to section" href="#step-5-optimizing-the-build"><span class="heading-link-icon">#</span></a></h2>
<p>Configure Vite to handle our Web Workers and TypeScript efficiently:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">defineConfig</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vite</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> vue</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@vitejs/plugin-vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#7DCFFF"> default</span><span style="color:#7AA2F7"> defineConfig</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">  plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#7AA2F7">vue</span><span style="color:#9ABDF5">()]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  worker</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    format</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">es</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic"> // Use ES modules format for workers</span></span>
<span class="line"><span style="color:#73DACA">    plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> []</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic"> // No additional plugins needed for workers</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  optimizeDeps</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    exclude</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">@huggingface/transformers</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic"> // Prevent Vite from trying to bundle Transformers.js</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="import { defineConfig } from &#34;vite&#34;;
import vue from &#34;@vitejs/plugin-vue&#34;;

export default defineConfig({
  plugins: [vue()],
  worker: {
    format: &#34;es&#34;, // Use ES modules format for workers
    plugins: [], // No additional plugins needed for workers
  },
  optimizeDeps: {
    exclude: [&#34;@huggingface/transformers&#34;], // Prevent Vite from trying to bundle Transformers.js
  },
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="how-it-works">How It Works<a class="heading-link" aria-label="Link to section" href="#how-it-works"><span class="heading-link-icon">#</span></a></h2>
<ol>
<li>You type text and select languages</li>
<li>The text goes to a Web Worker</li>
<li>Transformers.js loads the AI model (once)</li>
<li>The model translates your text</li>
<li>You see the translation appear in real time</li>
</ol>
<p>The translator works offline after the first run. No data leaves your browser. No API keys needed.</p>
<h2 id="try-it-yourself">Try It Yourself<a class="heading-link" aria-label="Link to section" href="#try-it-yourself"><span class="heading-link-icon">#</span></a></h2>
<div class="stackblitz-container astro-rrlsyoos" style="--height: 600px;"> <div class="loading-overlay astro-rrlsyoos" style="--height: 600px;">Loading project...</div> <iframe title="StackBlitz Embed" src="https://stackblitz.com/github/alexanderop/vue-ai-translate-poc?embed=1&file=&hideExplorer=false&theme=dark&view=preview&showDevTools=false" loading="lazy" allow="accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking" sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts" onload="this.previousElementSibling.style.display='none'" class="astro-rrlsyoos" style="--height: 600px;">
  </iframe> </div>  <script type="module">document.addEventListener("DOMContentLoaded",()=>{document.querySelectorAll(".stackblitz-container iframe").forEach(e=>{e.addEventListener("error",()=>{const t=e.closest(".stackblitz-container");if(t){const n=t.querySelector(".loading-overlay");n&&(n.textContent="Failed to load project. Please try refreshing the page.")}})})});</script>
<p>Want to explore the code further? Check out the complete source code on <a href="https://github.com/alexanderop/vue-ai-translate-poc" rel="noopener noreferrer" target="_blank">GitHub</a>.</p>
<p>Want to learn more? Explore these resources:</p>
<ul>
<li><a href="https://huggingface.co/docs/transformers.js" rel="noopener noreferrer" target="_blank">Transformers.js docs</a></li>
<li><a href="https://huggingface.co/facebook/nllb-200-distilled-600M" rel="noopener noreferrer" target="_blank">NLLB-200 model details</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API" rel="noopener noreferrer" target="_blank">Web Workers guide</a></li>
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_building-client-side-ai-translator-vue" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="building-client-side-ai-translator-vue" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vue</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/building-client-side-ai-translator-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/building-client-side-ai-translator-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/building-client-side-ai-translator-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/building-client-side-ai-translator-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/building-client-side-ai-translator-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/building-client-side-ai-translator-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/building-client-side-ai-translator-vue/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/type-safe-graphql-queries-vue3-codegen/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Type-Safe GraphQL Queries in Vue 3 with GraphQL Code Generator</h3> <p class="related-post-description astro-vj4tpspi"> Part 2 of the Vue 3 + GraphQL series: generate fully-typed `useQuery` composables in Vue 3 with GraphQL Code Generator </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-05-04T00:00:00.000Z">May 4, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> graphql </span> </div> </div> </a><a href="/posts/vue-accessibility-blueprint-8-steps/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Vue Accessibility Blueprint: 8 Steps</h3> <p class="related-post-description astro-vj4tpspi"> Master Vue accessibility with our comprehensive guide. Learn 8 crucial steps to create inclusive, WCAG-compliant web applications that work for all users. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-sm">Updated:</span><span class="italic text-sm"><time dateTime="2024-09-29T15:22:00.000Z">Sep 29, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/create-pwa-vue3-vite-4-steps/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Create a Native-Like App in 4 Steps: PWA Magic with Vue 3 and Vite</h3> <p class="related-post-description astro-vj4tpspi"> Transform your Vue 3 project into a powerful Progressive Web App in just 4 steps. Learn how to create offline-capable, installable web apps using Vite and modern PWA techniques. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-sm">Updated:</span><span class="italic text-sm"><time dateTime="2024-12-30T22:00:00.000Z">Dec 30, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "building-client-side-ai-translator-vue";

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
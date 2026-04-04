# Source: https://alexop.dev/posts/handling-api-calls-pinia-elm-pattern

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/handling-api-calls-pinia-elm-pattern/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>How to Handle API Calls in Pinia with The Elm Pattern | alexop.dev</title><meta name="title" content="How to Handle API Calls in Pinia with The Elm Pattern | alexop.dev"><meta name="description" content="Learn how to handle API calls in Pinia using the Elm pattern for predictable, testable side effects. Includes complete examples with the Pokemon API."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="How to Handle API Calls in Pinia with The Elm Pattern | alexop.dev"><meta property="og:description" content="Learn how to handle API calls in Pinia using the Elm pattern for predictable, testable side effects. Includes complete examples with the Pokemon API."><meta property="og:url" content="https://alexop.dev/posts/handling-api-calls-pinia-elm-pattern/"><meta property="og:image" content="https://alexop.dev/posts/how-to-handle-api-calls-in-pinia-with-the-elm-pattern/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-10-17T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/handling-api-calls-pinia-elm-pattern/"><meta property="twitter:title" content="How to Handle API Calls in Pinia with The Elm Pattern | alexop.dev"><meta property="twitter:description" content="Learn how to handle API calls in Pinia using the Elm pattern for predictable, testable side effects. Includes complete examples with the Pokemon API."><meta property="twitter:image" content="https://alexop.dev/posts/how-to-handle-api-calls-in-pinia-with-the-elm-pattern/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"How to Handle API Calls in Pinia with The Elm Pattern | alexop.dev","description":"Learn how to handle API calls in Pinia using the Elm pattern for predictable, testable side effects. Includes complete examples with the Pokemon API.","image":"https://alexop.dev/posts/how-to-handle-api-calls-in-pinia-with-the-elm-pattern/index.png","datePublished":"2025-10-17T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: how-to-handle-api-calls-in-pinia-with-the-elm-pattern; }@layer astro { ::view-transition-old(how-to-handle-api-calls-in-pinia-with-the-elm-pattern) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(how-to-handle-api-calls-in-pinia-with-the-elm-pattern) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(how-to-handle-api-calls-in-pinia-with-the-elm-pattern) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(how-to-handle-api-calls-in-pinia-with-the-elm-pattern) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">How to Handle API Calls in Pinia with The Elm Pattern</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-10-17T00:00:00.000Z">Oct 17, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="1D8nG" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;How to Handle API Calls in Pinia with The Elm Pattern&quot;],&quot;content&quot;:[0,&quot;import Aside from \&quot;@features/mdx-components/components/Aside.astro\&quot;;\nimport InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\n\n&lt;Aside type=\&quot;info\&quot; title=\&quot;When to Use This Pattern\&quot;&gt;\nIf your goal is to cache backend results or manage server state, Pinia is not the right tool.\nLibraries such as [pinia-colada](https://pinia-colada.esm.dev/), [TanStack Vue Query](https://tanstack.com/query/vue), or [RStore](https://rstore.dev/) are designed for this purpose.\nThey provide built-in caching, background refetching, and synchronization features that make them a better fit for working with APIs.\n\nThe approach described in this post is useful when you want to stay within Pinia but still keep your logic functional, predictable, and easy to test.\nIt is best for local logic, explicit message-driven updates, or cases where you need fine control over how side effects are triggered and handled.\n\n&lt;/Aside&gt;\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;Related Reading\&quot;&gt;\n  This post builds on the concepts introduced in{\&quot; \&quot;}\n  &lt;InternalLink slug=\&quot;tea-architecture-pinia-private-store-pattern\&quot;&gt;\n    How to Write Better Pinia Stores with the Elm Pattern\n  &lt;/InternalLink&gt;\n  . If you&#39;re new to The Elm Architecture or want to understand the full pattern\n  for structuring Pinia stores, start there first. This post focuses\n  specifically on handling side effects like API calls.\n&lt;/Aside&gt;\n\n## Understanding Pure Functions and Side Effects\n\nBefore diving into the pattern, it&#39;s important to understand the foundational concepts of functional programming that make this approach powerful.\n\n### What Is a Pure Function?\n\nA pure function is a function that satisfies two key properties:\n\n1. **Deterministic**: Given the same inputs, it always returns the same output.\n2. **No side effects**: It does not interact with anything outside its scope.\n\nHere&#39;s a simple example:\n\n```ts\n// Pure function - always predictable\nfunction add(a: number, b: number): number {\n  return a + b;\n}\n\nadd(2, 3); // Always returns 5\nadd(2, 3); // Always returns 5\n```\n\nThis function is pure because:\n\n- It only depends on its inputs (`a` and `b`)\n- It always produces the same result for the same inputs\n- It doesn&#39;t modify any external state\n- It doesn&#39;t perform any I/O operations\n\n### What Is a Side Effect?\n\nA side effect is any operation that interacts with the outside world or modifies state beyond the function&#39;s return value.\n\nCommon side effects include:\n\n```ts\n// Side effect: Network request\nfunction fetchUser(id: number) {\n  return fetch(`/api/users/${id}`); // Network I/O\n}\n\n// Side effect: Modifying external state\nlet count = 0;\nfunction increment() {\n  count++; // Mutates external variable\n}\n\n// Side effect: Writing to storage\nfunction saveUser(user: User) {\n  localStorage.setItem(\&quot;user\&quot;, JSON.stringify(user)); // I/O operation\n}\n\n// Side effect: Logging\nfunction calculate(x: number) {\n  console.log(\&quot;Calculating...\&quot;); // I/O operation\n  return x * 2;\n}\n```\n\nNone of these are pure functions because they interact with something beyond their inputs and outputs.\n\n### Why Does This Matter?\n\nPure functions are easier to:\n\n- **Test**: No need to mock APIs, databases, or global state\n- **Reason about**: The function&#39;s behavior is completely determined by its inputs\n- **Debug**: No hidden dependencies or unexpected state changes\n- **Reuse**: Work anywhere without environmental setup\n\nHowever, real applications need side effects. You can&#39;t build useful software without API calls, database writes, or user interactions.\n\nThe key insight from functional programming is not to eliminate side effects, but to **separate** them from your business logic.\n\n## Why Side Effects Are a Problem\n\nA pure function only depends on its inputs and always returns the same output.\nIf you include an API call or any asynchronous operation inside it, the function becomes unpredictable and hard to test.\n\nExample:\n\n```ts\nexport function update(model, msg) {\n  if (msg.type === \&quot;FETCH_POKEMON\&quot;) {\n    fetch(\&quot;https://pokeapi.co/api/v2/pokemon/pikachu\&quot;);\n    return { ...model, isLoading: true };\n  }\n}\n```\n\nThis mixes logic with side effects.\nThe function now depends on the network and the API structure, making it complex to test and reason about.\n\n## The Solution: Separate Logic and Effects\n\nThe Elm Architecture provides a simple way to handle side effects correctly.\n\n1. Keep the update function pure.\n2. Move side effects into separate functions that receive a dispatch function.\n3. Use the store as the bridge between both layers.\n\nThis separation keeps your business logic independent of the framework and easier to verify.\n\n### File Organization\n\nBefore diving into the code, here&#39;s how we organize the files for a Pinia store using the Elm pattern:\n\n```\nsrc/\n└── stores/\n    └── pokemon/\n        ├── pokemonModel.ts    # Types and initial state\n        ├── pokemonUpdate.ts   # Pure update function\n        ├── pokemonEffects.ts  # Side effects (API calls)\n        └── pokemon.ts         # Pinia store (connects everything)\n```\n\nEach file has a clear, single responsibility:\n\n- **`pokemonModel.ts`**: Defines the state shape and message types\n- **`pokemonUpdate.ts`**: Contains pure logic for state transitions\n- **`pokemonEffects.ts`**: Handles side effects like API calls\n- **`pokemon.ts`**: The Pinia store that wires everything together\n\nThis structure makes it easy to:\n\n- Find and modify specific logic\n- Test each piece independently\n- Reuse the update logic in different contexts\n- Add new effects without touching business logic\n\n## Example: Fetching Data from the Pokémon API\n\nThis example demonstrates how to handle an API call using this pattern.\n\n### `pokemonModel.ts`\n\nThe model defines the structure of the state and the possible messages that can change it.\n\n```ts\nexport type PokemonModel = {\n  isLoading: boolean;\n  pokemon: string | null;\n  error: string | null;\n};\n\nexport const initialModel: PokemonModel = {\n  isLoading: false,\n  pokemon: null,\n  error: null,\n};\n\nexport type PokemonMsg =\n  | { type: \&quot;FETCH_REQUEST\&quot;; name: string }\n  | { type: \&quot;FETCH_SUCCESS\&quot;; pokemon: string }\n  | { type: \&quot;FETCH_FAILURE\&quot;; error: string };\n```\n\n### `pokemonUpdate.ts`\n\nThe update function handles all state transitions in a pure way.\n\n```ts\nimport type { PokemonModel, PokemonMsg } from \&quot;./pokemonModel\&quot;;\n\nexport function update(model: PokemonModel, msg: PokemonMsg): PokemonModel {\n  switch (msg.type) {\n    case \&quot;FETCH_REQUEST\&quot;:\n      return { ...model, isLoading: true, error: null };\n\n    case \&quot;FETCH_SUCCESS\&quot;:\n      return { ...model, isLoading: false, pokemon: msg.pokemon };\n\n    case \&quot;FETCH_FAILURE\&quot;:\n      return { ...model, isLoading: false, error: msg.error };\n\n    default:\n      return model;\n  }\n}\n```\n\nThis function has no side effects.\nIt only describes how the state changes in response to a message.\n\n### `pokemonEffects.ts`\n\nThis file performs the network request and communicates back through the dispatch function.\n\n```ts\nimport type { PokemonMsg } from \&quot;./pokemonModel\&quot;;\n\nexport async function fetchPokemon(\n  name: string,\n  dispatch: (m: PokemonMsg) =&gt; void\n) {\n  dispatch({ type: \&quot;FETCH_REQUEST\&quot;, name });\n\n  try {\n    const res = await fetch(`https://pokeapi.co/api/v2/pokemon/${name}`);\n    if (!res.ok) throw new Error(\&quot;Not found\&quot;);\n    const data = await res.json();\n\n    dispatch({ type: \&quot;FETCH_SUCCESS\&quot;, pokemon: data.name });\n  } catch (e: any) {\n    dispatch({ type: \&quot;FETCH_FAILURE\&quot;, error: e.message });\n  }\n}\n```\n\nThis function does not depend on Pinia or Vue.\nIt simply performs the side effect and dispatches messages based on the result.\n\n### `pokemon.ts`\n\nThe Pinia store connects the pure logic and the side effect layer.\n\n```ts\nimport { defineStore } from \&quot;pinia\&quot;;\nimport { ref, readonly } from \&quot;vue\&quot;;\nimport {\n  initialModel,\n  type PokemonModel,\n  type PokemonMsg,\n} from \&quot;./pokemonModel\&quot;;\nimport { update } from \&quot;./pokemonUpdate\&quot;;\nimport { fetchPokemon } from \&quot;./pokemonEffects\&quot;;\n\nexport const usePokemonStore = defineStore(\&quot;pokemon\&quot;, () =&gt; {\n  const model = ref&lt;PokemonModel&gt;(initialModel);\n\n  function dispatch(msg: PokemonMsg) {\n    model.value = update(model.value, msg);\n  }\n\n  async function load(name: string) {\n    await fetchPokemon(name, dispatch);\n  }\n\n  return {\n    state: readonly(model),\n    load,\n  };\n});\n```\n\nThe store contains no direct logic for handling API responses.\nIt only coordinates updates and side effects.\n\n### Usage in a Component\n\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { ref } from \&quot;vue\&quot;;\nimport { usePokemonStore } from \&quot;@/stores/pokemon\&quot;;\n\nconst store = usePokemonStore();\nconst name = ref(\&quot;pikachu\&quot;);\n\nfunction fetchIt() {\n  store.load(name.value);\n}\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;div&gt;\n    &lt;input v-model=\&quot;name\&quot; placeholder=\&quot;Enter Pokémon name\&quot; /&gt;\n    &lt;button @click=\&quot;fetchIt\&quot;&gt;Search&lt;/button&gt;\n\n    &lt;p v-if=\&quot;store.state.isLoading\&quot;&gt;Loading...&lt;/p&gt;\n    &lt;p v-else-if=\&quot;store.state.error\&quot;&gt;Error: {{ store.state.error }}&lt;/p&gt;\n    &lt;p v-else-if=\&quot;store.state.pokemon\&quot;&gt;Found: {{ store.state.pokemon }}&lt;/p&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n```\n\nThe component only interacts with the public API of the store.\nIt does not mutate the state directly.\n\n## Why This Approach Works\n\nSeparating logic and effects provides several benefits.\n\n- The update function is pure and easy to test.\n- The side effect functions are independent and reusable.\n- The store focuses only on coordination.\n- The overall data flow remains predictable and maintainable.\n\nThis method is especially effective in projects where you want full control over how and when side effects are executed.\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;Testing Made Simple\&quot;&gt;\nBecause the `update` function is pure and framework-agnostic, you can test it with simple assertions without any mocking:\n\n```ts\nimport { describe, it, expect } from \&quot;vitest\&quot;;\nimport { update } from \&quot;./pokemonUpdate\&quot;;\n\ndescribe(\&quot;pokemon update\&quot;, () =&gt; {\n  it(\&quot;sets loading state on fetch request\&quot;, () =&gt; {\n    const state = { isLoading: false, pokemon: null, error: null };\n    const result = update(state, { type: \&quot;FETCH_REQUEST\&quot;, name: \&quot;pikachu\&quot; });\n\n    expect(result.isLoading).toBe(true);\n    expect(result.error).toBeNull();\n  });\n});\n```\n\nNo Pinia setup, no component mounting, just pure function testing.\n\n&lt;/Aside&gt;\n\n&lt;Aside type=\&quot;caution\&quot; title=\&quot;When This Pattern May Be Overkill\&quot;&gt;\nThe Elm pattern adds structure and discipline, but it comes with trade-offs:\n\n**Not ideal for simple stores:**\nIf your store just fetches data and displays it with minimal logic, the traditional Pinia approach is perfectly fine. Creating four separate files for a simple CRUD operation adds unnecessary complexity.\n\n**Requires team buy-in:**\nThis pattern works best when your entire team embraces functional programming concepts. If your team isn&#39;t comfortable with ideas like pure functions, immutability, and message-driven updates, this pattern will feel foreign and may be resisted.\n\n**Where it shines:**\n\n- Complex business logic with multiple state transitions\n- Stores that need rock-solid testing\n- Applications with sophisticated side effect orchestration (retries, cancellation, queuing)\n- Projects where state predictability is critical\n\n**Bottom line:** Start simple. Adopt this pattern when complexity demands it and your team is ready for functional programming principles. Don&#39;t use it just because it&#39;s clever—use it when it solves real problems.\n\n&lt;/Aside&gt;\n\n## Other Side Effects You Can Handle with This Pattern\n\nThis pattern is not limited to API requests.\nYou can manage any kind of asynchronous or external operation the same way.\n\nExamples include:\n\n- Writing to or reading from `localStorage` or `IndexedDB`\n- Sending analytics or telemetry events\n- Performing authentication or token refresh logic\n- Communicating with WebSockets or event streams\n- Scheduling background tasks with `setTimeout` or `requestAnimationFrame`\n- Reading files or using browser APIs such as the Clipboard or File System\n\nBy using the same structure, you can keep these effects organized and testable.\nEach effect becomes an independent unit that transforms external data into messages for your update function.\n\n## Summary\n\nIf you only need caching or background synchronization, use a specialized library such as [pinia-colada](https://pinia-colada.esm.dev/), [TanStack Vue Query](https://tanstack.com/query/vue), or [RStore](https://rstore.dev/).\nIf you need to stay within Pinia and still maintain a functional structure, this approach is effective.\n\n1. Define your model and messages.\n2. Keep the update function pure.\n3. Implement effects as separate functions that take a dispatch function.\n4. Connect them inside the store.\n\nThis structure keeps your Pinia stores predictable, testable, and easy to extend to any type of side effect.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div> <nav class="mb-8 astro-sbmhws2g" aria-labelledby="series-heading"> <div class="mb-1 text-sm font-bold tracking-wide text-skin-accent astro-sbmhws2g"> Pinia + Elm Architecture Series </div> <h2 id="series-heading" class="mb-2 text-xs font-semibold uppercase tracking-widest text-skin-accent astro-sbmhws2g">
This post is part of a series
</h2> <ol class="space-y-2 astro-sbmhws2g">  <li class="relative flex flex-col rounded py-2 pl-4 transition-all   astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-base/60 astro-sbmhws2g"> 1.
</span> <a href="/posts/tea-architecture-pinia-private-store-pattern/" class="font-medium underline-offset-4 text-skin-accent/80 hover:underline astro-sbmhws2g"> How to Write Better Pinia Stores with the Elm Pattern </a>  </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Learn how to combine The Elm Architecture (TEA) principles with Pinia&#39;s private store pattern for testable, framework-agnostic state management in Vue applications. </div> </li><li class="relative flex flex-col rounded py-2 pl-4 transition-all border-l-4 border-skin-accent bg-skin-card/60  astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-accent astro-sbmhws2g"> 2.
</span> <a href="/posts/handling-api-calls-pinia-elm-pattern/" class="font-medium underline-offset-4 pointer-events-none text-skin-accent astro-sbmhws2g" aria-current="page"> How to Handle API Calls in Pinia with The Elm Pattern </a> <span class="ml-2 text-xs font-bold text-green-400 astro-sbmhws2g">
(current)
</span> </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Learn how to handle API calls in Pinia using the Elm pattern for predictable, testable side effects. Includes complete examples with the Pokemon API. </div> </li>  </ol> <div class="mt-4 border-b border-skin-line opacity-40 astro-sbmhws2g"></div> </nav>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <aside aria-label="When to Use This Pattern" class="aside aside-info astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">ℹ️</span> When to Use This Pattern </p> <section class="aside-body astro-37uy2q7c"> <p>If your goal is to cache backend results or manage server state, Pinia is not the right tool.
Libraries such as <a target="_blank" rel="noopener noreferrer" href="https://pinia-colada.esm.dev/" rel="noopener noreferrer" target="_blank">pinia-colada</a>, <a target="_blank" rel="noopener noreferrer" href="https://tanstack.com/query/vue" rel="noopener noreferrer" target="_blank">TanStack Vue Query</a>, or <a target="_blank" rel="noopener noreferrer" href="https://rstore.dev/" rel="noopener noreferrer" target="_blank">RStore</a> are designed for this purpose.
They provide built-in caching, background refetching, and synchronization features that make them a better fit for working with APIs.</p><p>The approach described in this post is useful when you want to stay within Pinia but still keep your logic functional, predictable, and easy to test.
It is best for local logic, explicit message-driven updates, or cases where you need fine control over how side effects are triggered and handled.</p> </section> </div> </aside> 
<aside aria-label="Related Reading" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> Related Reading </p> <section class="aside-body astro-37uy2q7c"> <p>This post builds on the concepts introduced in </p><span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/tea-architecture-pinia-private-store-pattern/" class="internal-link astro-3tyn5ojg"> <p>How to Write Better Pinia Stores with the Elm Pattern</p> </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Write Better Pinia Stores with the Elm Pattern</span> <span class="preview-description astro-3tyn5ojg">Learn how to combine The Elm Architecture (TEA) principles with Pinia&#39;s private store pattern for testable, framework-agnostic state management in Vue applications.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span>  </span> <time class="preview-date astro-3tyn5ojg">Oct 3, 2025</time> </span> </span> </span>  <script>
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
</script><p>. If you’re new to The Elm Architecture or want to understand the full pattern
for structuring Pinia stores, start there first. This post focuses
specifically on handling side effects like API calls.</p> </section> </div> </aside> 
<h2 id="understanding-pure-functions-and-side-effects">Understanding Pure Functions and Side Effects<a class="heading-link" aria-label="Link to section" href="#understanding-pure-functions-and-side-effects"><span class="heading-link-icon">#</span></a></h2>
<p>Before diving into the pattern, it’s important to understand the foundational concepts of functional programming that make this approach powerful.</p>
<h3 id="what-is-a-pure-function">What Is a Pure Function?<a class="heading-link" aria-label="Link to section" href="#what-is-a-pure-function"><span class="heading-link-icon">#</span></a></h3>
<p>A pure function is a function that satisfies two key properties:</p>
<ol>
<li><strong>Deterministic</strong>: Given the same inputs, it always returns the same output.</li>
<li><strong>No side effects</strong>: It does not interact with anything outside its scope.</li>
</ol>
<p>Here’s a simple example:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#51597D;font-style:italic">// Pure function - always predictable</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> add</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">a</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> b</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> a</span><span style="color:#89DDFF"> +</span><span style="color:#C0CAF5"> b</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">add</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">2</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 3</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Always returns 5</span></span>
<span class="line"><span style="color:#7AA2F7">add</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">2</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 3</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Always returns 5</span></span></code><button type="button" class="copy" data-code="// Pure function - always predictable
function add(a: number, b: number): number {
  return a + b;
}

add(2, 3); // Always returns 5
add(2, 3); // Always returns 5" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This function is pure because:</p>
<ul>
<li>It only depends on its inputs (<code>a</code> and <code>b</code>)</li>
<li>It always produces the same result for the same inputs</li>
<li>It doesn’t modify any external state</li>
<li>It doesn’t perform any I/O operations</li>
</ul>
<h3 id="what-is-a-side-effect">What Is a Side Effect?<a class="heading-link" aria-label="Link to section" href="#what-is-a-side-effect"><span class="heading-link-icon">#</span></a></h3>
<p>A side effect is any operation that interacts with the outside world or modifies state beyond the function’s return value.</p>
<p>Common side effects include:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#51597D;font-style:italic">// Side effect: Network request</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> fetchUser</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">id</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#7AA2F7"> fetch</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">/api/users/</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">id</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Network I/O</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Side effect: Modifying external state</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">let</span><span style="color:#BB9AF7"> count</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> increment</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  count</span><span style="color:#89DDFF">++;</span><span style="color:#51597D;font-style:italic"> // Mutates external variable</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Side effect: Writing to storage</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> saveUser</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">user</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> User</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  localStorage</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">setItem</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">user</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> JSON</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">stringify</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">user</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // I/O operation</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Side effect: Logging</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> calculate</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">x</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Calculating...</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // I/O operation</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> x</span><span style="color:#89DDFF"> *</span><span style="color:#FF9E64"> 2</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// Side effect: Network request
function fetchUser(id: number) {
  return fetch(`/api/users/${id}`); // Network I/O
}

// Side effect: Modifying external state
let count = 0;
function increment() {
  count++; // Mutates external variable
}

// Side effect: Writing to storage
function saveUser(user: User) {
  localStorage.setItem(&#34;user&#34;, JSON.stringify(user)); // I/O operation
}

// Side effect: Logging
function calculate(x: number) {
  console.log(&#34;Calculating...&#34;); // I/O operation
  return x * 2;
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>None of these are pure functions because they interact with something beyond their inputs and outputs.</p>
<h3 id="why-does-this-matter">Why Does This Matter?<a class="heading-link" aria-label="Link to section" href="#why-does-this-matter"><span class="heading-link-icon">#</span></a></h3>
<p>Pure functions are easier to:</p>
<ul>
<li><strong>Test</strong>: No need to mock APIs, databases, or global state</li>
<li><strong>Reason about</strong>: The function’s behavior is completely determined by its inputs</li>
<li><strong>Debug</strong>: No hidden dependencies or unexpected state changes</li>
<li><strong>Reuse</strong>: Work anywhere without environmental setup</li>
</ul>
<p>However, real applications need side effects. You can’t build useful software without API calls, database writes, or user interactions.</p>
<p>The key insight from functional programming is not to eliminate side effects, but to <strong>separate</strong> them from your business logic.</p>
<h2 id="why-side-effects-are-a-problem">Why Side Effects Are a Problem<a class="heading-link" aria-label="Link to section" href="#why-side-effects-are-a-problem"><span class="heading-link-icon">#</span></a></h2>
<p>A pure function only depends on its inputs and always returns the same output.
If you include an API call or any asynchronous operation inside it, the function becomes unpredictable and hard to test.</p>
<p>Example:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> update</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">model</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> msg</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">msg</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">type</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">FETCH_POKEMON</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#7AA2F7">    fetch</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">https://pokeapi.co/api/v2/pokemon/pikachu</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#9ABDF5"> { </span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">model</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> isLoading</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="export function update(model, msg) {
  if (msg.type === &#34;FETCH_POKEMON&#34;) {
    fetch(&#34;https://pokeapi.co/api/v2/pokemon/pikachu&#34;);
    return { ...model, isLoading: true };
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This mixes logic with side effects.
The function now depends on the network and the API structure, making it complex to test and reason about.</p>
<h2 id="the-solution-separate-logic-and-effects">The Solution: Separate Logic and Effects<a class="heading-link" aria-label="Link to section" href="#the-solution-separate-logic-and-effects"><span class="heading-link-icon">#</span></a></h2>
<p>The Elm Architecture provides a simple way to handle side effects correctly.</p>
<ol>
<li>Keep the update function pure.</li>
<li>Move side effects into separate functions that receive a dispatch function.</li>
<li>Use the store as the bridge between both layers.</li>
</ol>
<p>This separation keeps your business logic independent of the framework and easier to verify.</p>
<h3 id="file-organization">File Organization<a class="heading-link" aria-label="Link to section" href="#file-organization"><span class="heading-link-icon">#</span></a></h3>
<p>Before diving into the code, here’s how we organize the files for a Pinia store using the Elm pattern:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>src/</span></span>
<span class="line"><span>└── stores/</span></span>
<span class="line"><span>    └── pokemon/</span></span>
<span class="line"><span>        ├── pokemonModel.ts    # Types and initial state</span></span>
<span class="line"><span>        ├── pokemonUpdate.ts   # Pure update function</span></span>
<span class="line"><span>        ├── pokemonEffects.ts  # Side effects (API calls)</span></span>
<span class="line"><span>        └── pokemon.ts         # Pinia store (connects everything)</span></span></code><button type="button" class="copy" data-code="src/
└── stores/
    └── pokemon/
        ├── pokemonModel.ts    # Types and initial state
        ├── pokemonUpdate.ts   # Pure update function
        ├── pokemonEffects.ts  # Side effects (API calls)
        └── pokemon.ts         # Pinia store (connects everything)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Each file has a clear, single responsibility:</p>
<ul>
<li><strong><code>pokemonModel.ts</code></strong>: Defines the state shape and message types</li>
<li><strong><code>pokemonUpdate.ts</code></strong>: Contains pure logic for state transitions</li>
<li><strong><code>pokemonEffects.ts</code></strong>: Handles side effects like API calls</li>
<li><strong><code>pokemon.ts</code></strong>: The Pinia store that wires everything together</li>
</ul>
<p>This structure makes it easy to:</p>
<ul>
<li>Find and modify specific logic</li>
<li>Test each piece independently</li>
<li>Reuse the update logic in different contexts</li>
<li>Add new effects without touching business logic</li>
</ul>
<h2 id="example-fetching-data-from-the-pokémon-api">Example: Fetching Data from the Pokémon API<a class="heading-link" aria-label="Link to section" href="#example-fetching-data-from-the-pokémon-api"><span class="heading-link-icon">#</span></a></h2>
<p>This example demonstrates how to handle an API call using this pattern.</p>
<h3 id="pokemonmodelts"><code>pokemonModel.ts</code><a class="heading-link" aria-label="Link to section" href="#pokemonmodelts"><span class="heading-link-icon">#</span></a></h3>
<p>The model defines the structure of the state and the possible messages that can change it.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> type</span><span style="color:#C0CAF5"> PokemonModel</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  isLoading</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  pokemon</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  error</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> initialModel</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> PokemonModel</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  isLoading</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  pokemon</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  error</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> type</span><span style="color:#C0CAF5"> PokemonMsg</span><span style="color:#89DDFF"> =</span></span>
<span class="line"><span style="color:#89DDFF">  |</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">FETCH_REQUEST</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span><span style="color:#73DACA"> name</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#89DDFF">  |</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">FETCH_SUCCESS</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span><span style="color:#73DACA"> pokemon</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#89DDFF">  |</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">FETCH_FAILURE</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span><span style="color:#73DACA"> error</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="export type PokemonModel = {
  isLoading: boolean;
  pokemon: string | null;
  error: string | null;
};

export const initialModel: PokemonModel = {
  isLoading: false,
  pokemon: null,
  error: null,
};

export type PokemonMsg =
  | { type: &#34;FETCH_REQUEST&#34;; name: string }
  | { type: &#34;FETCH_SUCCESS&#34;; pokemon: string }
  | { type: &#34;FETCH_FAILURE&#34;; error: string };" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="pokemonupdatets"><code>pokemonUpdate.ts</code><a class="heading-link" aria-label="Link to section" href="#pokemonupdatets"><span class="heading-link-icon">#</span></a></h3>
<p>The update function handles all state transitions in a pure way.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#BB9AF7"> type</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">PokemonModel</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> PokemonMsg</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">./pokemonModel</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> update</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">model</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> PokemonModel</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> msg</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> PokemonMsg</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> PokemonModel</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  switch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">msg</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">type</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">FETCH_REQUEST</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#9ABDF5"> { </span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">model</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> isLoading</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> error</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> null</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">FETCH_SUCCESS</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#9ABDF5"> { </span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">model</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> isLoading</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> pokemon</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> msg</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">pokemon</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">FETCH_FAILURE</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#9ABDF5"> { </span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">model</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> isLoading</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> error</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> msg</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">error</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    default</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#C0CAF5"> model</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import type { PokemonModel, PokemonMsg } from &#34;./pokemonModel&#34;;

export function update(model: PokemonModel, msg: PokemonMsg): PokemonModel {
  switch (msg.type) {
    case &#34;FETCH_REQUEST&#34;:
      return { ...model, isLoading: true, error: null };

    case &#34;FETCH_SUCCESS&#34;:
      return { ...model, isLoading: false, pokemon: msg.pokemon };

    case &#34;FETCH_FAILURE&#34;:
      return { ...model, isLoading: false, error: msg.error };

    default:
      return model;
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This function has no side effects.
It only describes how the state changes in response to a message.</p>
<h3 id="pokemoneffectsts"><code>pokemonEffects.ts</code><a class="heading-link" aria-label="Link to section" href="#pokemoneffectsts"><span class="heading-link-icon">#</span></a></h3>
<p>This file performs the network request and communicates back through the dispatch function.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#BB9AF7"> type</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">PokemonMsg</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">./pokemonModel</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> fetchPokemon</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">  name</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">  dispatch</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">m</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> PokemonMsg</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  dispatch</span><span style="color:#9ABDF5">({ </span><span style="color:#73DACA">type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">FETCH_REQUEST</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> name</span><span style="color:#9ABDF5"> })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> res</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> fetch</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">https://pokeapi.co/api/v2/pokemon/</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">name</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">res</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">ok</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">throw</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Error</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Not found</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> data</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> res</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">json</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">    dispatch</span><span style="color:#9ABDF5">({ </span><span style="color:#73DACA">type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">FETCH_SUCCESS</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> pokemon</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">name</span><span style="color:#9ABDF5"> })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">e</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> any</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#7AA2F7">    dispatch</span><span style="color:#9ABDF5">({ </span><span style="color:#73DACA">type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">FETCH_FAILURE</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> error</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> e</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">message</span><span style="color:#9ABDF5"> })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import type { PokemonMsg } from &#34;./pokemonModel&#34;;

export async function fetchPokemon(
  name: string,
  dispatch: (m: PokemonMsg) => void
) {
  dispatch({ type: &#34;FETCH_REQUEST&#34;, name });

  try {
    const res = await fetch(`https://pokeapi.co/api/v2/pokemon/${name}`);
    if (!res.ok) throw new Error(&#34;Not found&#34;);
    const data = await res.json();

    dispatch({ type: &#34;FETCH_SUCCESS&#34;, pokemon: data.name });
  } catch (e: any) {
    dispatch({ type: &#34;FETCH_FAILURE&#34;, error: e.message });
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This function does not depend on Pinia or Vue.
It simply performs the side effect and dispatches messages based on the result.</p>
<h3 id="pokemonts"><code>pokemon.ts</code><a class="heading-link" aria-label="Link to section" href="#pokemonts"><span class="heading-link-icon">#</span></a></h3>
<p>The Pinia store connects the pure logic and the side effect layer.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">defineStore</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">pinia</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ref</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> readonly</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#0DB9D7">  initialModel</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#BB9AF7">  type</span><span style="color:#0DB9D7"> PokemonModel</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#BB9AF7">  type</span><span style="color:#0DB9D7"> PokemonMsg</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">./pokemonModel</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">update</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">./pokemonUpdate</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">fetchPokemon</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">./pokemonEffects</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> usePokemonStore</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> defineStore</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">pokemon</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> model</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">PokemonModel</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initialModel</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> dispatch</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">msg</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> PokemonMsg</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    model</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> update</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">model</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> msg</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> load</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">name</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#7AA2F7"> fetchPokemon</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">name</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> dispatch</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    state</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> readonly</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">model</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    load</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="import { defineStore } from &#34;pinia&#34;;
import { ref, readonly } from &#34;vue&#34;;
import {
  initialModel,
  type PokemonModel,
  type PokemonMsg,
} from &#34;./pokemonModel&#34;;
import { update } from &#34;./pokemonUpdate&#34;;
import { fetchPokemon } from &#34;./pokemonEffects&#34;;

export const usePokemonStore = defineStore(&#34;pokemon&#34;, () => {
  const model = ref<PokemonModel>(initialModel);

  function dispatch(msg: PokemonMsg) {
    model.value = update(model.value, msg);
  }

  async function load(name: string) {
    await fetchPokemon(name, dispatch);
  }

  return {
    state: readonly(model),
    load,
  };
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The store contains no direct logic for handling API responses.
It only coordinates updates and side effects.</p>
<h3 id="usage-in-a-component">Usage in a Component<a class="heading-link" aria-label="Link to section" href="#usage-in-a-component"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">usePokemonStore</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@/stores/pokemon</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> store</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> usePokemonStore</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> name</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">pikachu</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> fetchIt</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  store</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">load</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">name</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">input</span><span style="color:#BB9AF7"> v-model</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">name</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> placeholder</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Enter Pokémon name</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">button</span><span style="color:#BB9AF7"> @click</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">fetchIt</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Search</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">p</span><span style="color:#BB9AF7"> v-if</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">store.state.isLoading</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Loading...</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">p</span><span style="color:#BB9AF7"> v-else-if</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">store.state.error</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Error: {{ store.state.error }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">p</span><span style="color:#BB9AF7"> v-else-if</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">store.state.pokemon</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Found: {{ store.state.pokemon }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
import { ref } from &#34;vue&#34;;
import { usePokemonStore } from &#34;@/stores/pokemon&#34;;

const store = usePokemonStore();
const name = ref(&#34;pikachu&#34;);

function fetchIt() {
  store.load(name.value);
}
</script>

<template>
  <div>
    <input v-model=&#34;name&#34; placeholder=&#34;Enter Pokémon name&#34; />
    <button @click=&#34;fetchIt&#34;>Search</button>

    <p v-if=&#34;store.state.isLoading&#34;>Loading...</p>
    <p v-else-if=&#34;store.state.error&#34;>Error: {{ store.state.error }}</p>
    <p v-else-if=&#34;store.state.pokemon&#34;>Found: {{ store.state.pokemon }}</p>
  </div>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The component only interacts with the public API of the store.
It does not mutate the state directly.</p>
<h2 id="why-this-approach-works">Why This Approach Works<a class="heading-link" aria-label="Link to section" href="#why-this-approach-works"><span class="heading-link-icon">#</span></a></h2>
<p>Separating logic and effects provides several benefits.</p>
<ul>
<li>The update function is pure and easy to test.</li>
<li>The side effect functions are independent and reusable.</li>
<li>The store focuses only on coordination.</li>
<li>The overall data flow remains predictable and maintainable.</li>
</ul>
<p>This method is especially effective in projects where you want full control over how and when side effects are executed.</p>
<aside aria-label="Testing Made Simple" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> Testing Made Simple </p> <section class="aside-body astro-37uy2q7c"> <p>Because the <code>update</code> function is pure and framework-agnostic, you can test it with simple assertions without any mocking:</p><pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">describe</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> it</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> expect</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vitest</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">update</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">./pokemonUpdate</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">pokemon update</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">sets loading state on fetch request</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> state</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">isLoading</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> false</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> pokemon</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> error</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> null</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> result</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> update</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">state</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">FETCH_REQUEST</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">pikachu</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5"> })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">result</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">isLoading</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">true</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">result</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">error</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBeNull</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="import { describe, it, expect } from &#34;vitest&#34;;
import { update } from &#34;./pokemonUpdate&#34;;

describe(&#34;pokemon update&#34;, () => {
  it(&#34;sets loading state on fetch request&#34;, () => {
    const state = { isLoading: false, pokemon: null, error: null };
    const result = update(state, { type: &#34;FETCH_REQUEST&#34;, name: &#34;pikachu&#34; });

    expect(result.isLoading).toBe(true);
    expect(result.error).toBeNull();
  });
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre><p>No Pinia setup, no component mounting, just pure function testing.</p> </section> </div> </aside> 
<aside aria-label="When This Pattern May Be Overkill" class="aside aside-caution astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">⚠️</span> When This Pattern May Be Overkill </p> <section class="aside-body astro-37uy2q7c"> <p>The Elm pattern adds structure and discipline, but it comes with trade-offs:</p><p><strong>Not ideal for simple stores:</strong>
If your store just fetches data and displays it with minimal logic, the traditional Pinia approach is perfectly fine. Creating four separate files for a simple CRUD operation adds unnecessary complexity.</p><p><strong>Requires team buy-in:</strong>
This pattern works best when your entire team embraces functional programming concepts. If your team isn’t comfortable with ideas like pure functions, immutability, and message-driven updates, this pattern will feel foreign and may be resisted.</p><p><strong>Where it shines:</strong></p><ul>
<li>Complex business logic with multiple state transitions</li>
<li>Stores that need rock-solid testing</li>
<li>Applications with sophisticated side effect orchestration (retries, cancellation, queuing)</li>
<li>Projects where state predictability is critical</li>
</ul><p><strong>Bottom line:</strong> Start simple. Adopt this pattern when complexity demands it and your team is ready for functional programming principles. Don’t use it just because it’s clever—use it when it solves real problems.</p> </section> </div> </aside> 
<h2 id="other-side-effects-you-can-handle-with-this-pattern">Other Side Effects You Can Handle with This Pattern<a class="heading-link" aria-label="Link to section" href="#other-side-effects-you-can-handle-with-this-pattern"><span class="heading-link-icon">#</span></a></h2>
<p>This pattern is not limited to API requests.
You can manage any kind of asynchronous or external operation the same way.</p>
<p>Examples include:</p>
<ul>
<li>Writing to or reading from <code>localStorage</code> or <code>IndexedDB</code></li>
<li>Sending analytics or telemetry events</li>
<li>Performing authentication or token refresh logic</li>
<li>Communicating with WebSockets or event streams</li>
<li>Scheduling background tasks with <code>setTimeout</code> or <code>requestAnimationFrame</code></li>
<li>Reading files or using browser APIs such as the Clipboard or File System</li>
</ul>
<p>By using the same structure, you can keep these effects organized and testable.
Each effect becomes an independent unit that transforms external data into messages for your update function.</p>
<h2 id="summary">Summary<a class="heading-link" aria-label="Link to section" href="#summary"><span class="heading-link-icon">#</span></a></h2>
<p>If you only need caching or background synchronization, use a specialized library such as <a href="https://pinia-colada.esm.dev/" rel="noopener noreferrer" target="_blank">pinia-colada</a>, <a href="https://tanstack.com/query/vue" rel="noopener noreferrer" target="_blank">TanStack Vue Query</a>, or <a href="https://rstore.dev/" rel="noopener noreferrer" target="_blank">RStore</a>.
If you need to stay within Pinia and still maintain a functional structure, this approach is effective.</p>
<ol>
<li>Define your model and messages.</li>
<li>Keep the update function pure.</li>
<li>Implement effects as separate functions that take a dispatch function.</li>
<li>Connect them inside the store.</li>
</ol>
<p>This structure keeps your Pinia stores predictable, testable, and easy to extend to any type of side effect.</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_handling-api-calls-pinia-elm-pattern" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="handling-api-calls-pinia-elm-pattern" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vue</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/handling-api-calls-pinia-elm-pattern/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/handling-api-calls-pinia-elm-pattern/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/handling-api-calls-pinia-elm-pattern/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/handling-api-calls-pinia-elm-pattern/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/handling-api-calls-pinia-elm-pattern/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/handling-api-calls-pinia-elm-pattern/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/handling-api-calls-pinia-elm-pattern/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/tea-architecture-pinia-private-store-pattern/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How to Write Better Pinia Stores with the Elm Pattern</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to combine The Elm Architecture (TEA) principles with Pinia&#39;s private store pattern for testable, framework-agnostic state management in Vue applications. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-10-03T00:00:00.000Z">Oct 3, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/how-to-write-clean-vue-components/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How to Write Clean Vue Components</h3> <p class="related-post-description astro-vj4tpspi"> There are many ways to write better Vue components. One of my favorite ways is to separate business logic into pure functions. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2024-01-28T15:22:00.000Z">Jan 28, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/robust-error-handling-in-typescript-a-journey-from-naive-to-rust-inspired-solutions/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Robust Error Handling in TypeScript: A Journey from Naive to Rust-Inspired Solutions</h3> <p class="related-post-description astro-vj4tpspi"> Learn to write robust, predictable TypeScript code using Rust&#39;s Result pattern. This post demonstrates practical examples and introduces the ts-results library, implementing Rust&#39;s powerful error management approach in TypeScript. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2023-11-18T15:22:00.000Z">Nov 18, 2023</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> typescript </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "handling-api-calls-pinia-elm-pattern";

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
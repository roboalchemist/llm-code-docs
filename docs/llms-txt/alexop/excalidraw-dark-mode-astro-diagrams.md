# Source: https://alexop.dev/posts/excalidraw-dark-mode-astro-diagrams

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/excalidraw-dark-mode-astro-diagrams/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Create Dark Mode-Compatible Technical Diagrams in Astro with Excalidraw: A Complete Guide | alexop.dev</title><meta name="title" content="Create Dark Mode-Compatible Technical Diagrams in Astro with Excalidraw: A Complete Guide | alexop.dev"><meta name="description" content="Learn how to create and integrate theme-aware Excalidraw diagrams into your Astro blog. This step-by-step guide shows you how to build custom components that automatically adapt to light and dark modes, perfect for technical documentation and blogs"><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Create Dark Mode-Compatible Technical Diagrams in Astro with Excalidraw: A Complete Guide | alexop.dev"><meta property="og:description" content="Learn how to create and integrate theme-aware Excalidraw diagrams into your Astro blog. This step-by-step guide shows you how to build custom components that automatically adapt to light and dark modes, perfect for technical documentation and blogs"><meta property="og:url" content="https://alexop.dev/posts/excalidraw-dark-mode-astro-diagrams/"><meta property="og:image" content="https://alexop.dev/posts/create-dark-mode-compatible-technical-diagrams-in-astro-with-excalidraw-a-complete-guide/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2024-10-27T07:00:00.000Z"><meta property="article:modified_time" content="2024-10-27T07:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/excalidraw-dark-mode-astro-diagrams/"><meta property="twitter:title" content="Create Dark Mode-Compatible Technical Diagrams in Astro with Excalidraw: A Complete Guide | alexop.dev"><meta property="twitter:description" content="Learn how to create and integrate theme-aware Excalidraw diagrams into your Astro blog. This step-by-step guide shows you how to build custom components that automatically adapt to light and dark modes, perfect for technical documentation and blogs"><meta property="twitter:image" content="https://alexop.dev/posts/create-dark-mode-compatible-technical-diagrams-in-astro-with-excalidraw-a-complete-guide/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Create Dark Mode-Compatible Technical Diagrams in Astro with Excalidraw: A Complete Guide | alexop.dev","description":"Learn how to create and integrate theme-aware Excalidraw diagrams into your Astro blog. This step-by-step guide shows you how to build custom components that automatically adapt to light and dark modes, perfect for technical documentation and blogs","image":"https://alexop.dev/posts/create-dark-mode-compatible-technical-diagrams-in-astro-with-excalidraw-a-complete-guide/index.png","datePublished":"2024-10-27T07:00:00.000Z","dateModified":"2024-10-27T07:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: create-dark-mode-compatible-technical-diagrams-in-astro-with-excalidraw-a-complete-guide; }@layer astro { ::view-transition-old(create-dark-mode-compatible-technical-diagrams-in-astro-with-excalidraw-a-complete-guide) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(create-dark-mode-compatible-technical-diagrams-in-astro-with-excalidraw-a-complete-guide) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(create-dark-mode-compatible-technical-diagrams-in-astro-with-excalidraw-a-complete-guide) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(create-dark-mode-compatible-technical-diagrams-in-astro-with-excalidraw-a-complete-guide) { 
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
</style><style>.excalidraw-figure:where(.astro-hxyrieg5){margin-top:2rem;margin-bottom:2rem;width:100%;max-width:100%}.excalidraw-svg:where(.astro-hxyrieg5){width:100%;--excalidraw-text: rgb(var(--color-text-base));--excalidraw-fill: rgb(var(--color-card));--excalidraw-accent: rgb(var(--color-accent))}.excalidraw-svg svg.excalidraw-rendered{display:block;height:auto;width:100%}figcaption:where(.astro-hxyrieg5){margin-top:1rem;text-align:center;font-size:.875rem;line-height:1.25rem;font-style:italic;--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1))}figcaption:where(.astro-hxyrieg5) a:where(.astro-hxyrieg5){--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));transition-property:opacity;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.2s}figcaption:where(.astro-hxyrieg5) a:where(.astro-hxyrieg5):hover{opacity:.8}figcaption:where(.astro-hxyrieg5) a:where(.astro-hxyrieg5){text-decoration:underline}
</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: astro; }@layer astro { ::view-transition-old(astro) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(astro) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(astro) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(astro) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: excalidraw; }@layer astro { ::view-transition-old(excalidraw) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(excalidraw) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(excalidraw) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(excalidraw) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Create Dark Mode-Compatible Technical Diagrams in Astro with Excalidraw: A Complete Guide</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2024-10-27T07:00:00.000Z">Oct 27, 2024</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Z1sJXlI" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Create Dark Mode-Compatible Technical Diagrams in Astro with Excalidraw: A Complete Guide&quot;],&quot;content&quot;:[0,&quot;import ExcalidrawSVG from \&quot;@features/mdx-components/components/ExcalidrawSVG.astro\&quot;;\nimport example from \&quot;../../assets/images/excalidraw-astro/example.svg?raw\&quot;;\nimport exampleImage from \&quot;../../assets/images/excalidraw-astro/example.svg\&quot;;\nimport Aside from \&quot;@features/mdx-components/components/Aside.astro\&quot;;\nimport { Image } from \&quot;astro:assets\&quot;;\n\n## Why You Need Theme-Aware Technical Diagrams in Your Astro Blog\n\nTechnical bloggers often face a common challenge: creating diagrams seamlessly integrating with their site’s design system. While tools like Excalidraw make it easy to create beautiful diagrams, maintaining their visual consistency across different theme modes can be frustrating. This is especially true when your Astro blog supports light and dark modes.\nThis tutorial will solve this problem by building a custom solution that automatically adapts your Excalidraw diagrams to match your site’s theme.\n\n## Common Challenges with Technical Diagrams in Web Development\n\nWhen working with Excalidraw, we face several issues:\n\n- Exported SVGs come with fixed colors\n- Diagrams don&#39;t automatically adapt to dark mode\n- Maintaining separate versions for different themes is time-consuming\n- Lack of interactive elements and smooth transitions\n\n## Before vs After: The Impact of Theme-Aware Diagrams\n\n&lt;div class=\&quot;grid grid-cols-2 gap-8 w-full\&quot;&gt;\n  &lt;div class=\&quot;w-full\&quot;&gt;\n    &lt;h4 class=\&quot;text-xl font-bold\&quot;&gt;Standard Export&lt;/h4&gt;\n    &lt;p&gt;Here&#39;s how a typical Excalidraw diagram looks without any customization:&lt;/p&gt;\n    &lt;Image\n      src={exampleImage}\n      alt=\&quot;How a excalidraw diagrams looks without our custom component\&quot;\n      width={400}\n      height={300}\n      class=\&quot;w-full h-auto object-cover\&quot;\n    /&gt;\n  &lt;/div&gt;\n\n  &lt;div class=\&quot;w-full\&quot;&gt;\n    &lt;h4 class=\&quot;text-xl font-bold\&quot;&gt;With Our Solution&lt;/h4&gt;\n    &lt;p&gt;And here&#39;s the same diagram using our custom component:&lt;/p&gt;\n    &lt;ExcalidrawSVG src={example} alt=\&quot;Example diagram\&quot;/&gt;\n  &lt;/div&gt;\n&lt;/div&gt;\n\n## Building a Theme-Aware Excalidraw Component for Astro\n\nWe&#39;ll create an Astro component that transforms static Excalidraw exports into dynamic, theme-aware diagrams. Our solution will:\n\n1. Automatically adapt to light and dark modes\n2. Support your custom design system colors\n3. Add interactive elements and smooth transitions\n4. Maintain accessibility standards\n\n💡 Quick Start: Need an Astro blog first? Use [AstroPaper](https://github.com/satnaing/astro-paper) as your starter or build from scratch. This tutorial focuses on the diagram component itself.\n\n## Step-by-Step Implementation Guide\n\n### 1. Implementing the Theme System\n\nFirst, let&#39;s define the color variables that will power our theme-aware diagrams:\n\n```css\nhtml[data-theme=\&quot;light\&quot;] {\n  --color-fill: 250, 252, 252;\n  --color-text-base: 34, 46, 54;\n  --color-accent: 211, 0, 106;\n  --color-card: 234, 206, 219;\n  --color-card-muted: 241, 186, 212;\n  --color-border: 227, 169, 198;\n}\n\nhtml[data-theme=\&quot;dark\&quot;] {\n  --color-fill: 33, 39, 55;\n  --color-text-base: 234, 237, 243;\n  --color-accent: 255, 107, 237;\n  --color-card: 52, 63, 96;\n  --color-card-muted: 138, 51, 123;\n  --color-border: 171, 75, 153;\n}\n```\n\n### 2. Creating Optimized Excalidraw Diagrams\n\nFollow these steps to prepare your diagrams:\n\n1. Create your diagram at [Excalidraw](https://excalidraw.com/)\n2. Export the diagram:\n   - Select your diagram\n   - Click the export button\n     ![How to export Excalidraw diagram as SVG](../../assets/images/excalidraw-astro/how-to-click-export-excalidraw.png)\n3. Configure export settings:\n   - Uncheck \&quot;Background\&quot;\n   - Choose SVG format\n   - Click \&quot;Save\&quot;\n     ![How to hide background and save as SVG](../../assets/images/excalidraw-astro/save-as-svg.png)\n\n### 3. Building the ExcalidrawSVG Component\n\nHere&#39;s our custom Astro component that handles the theme-aware transformation:\n\n```astro\n---\nimport type { ImageMetadata } from \&quot;astro\&quot;;\n\ninterface Props {\n  src: ImageMetadata | string;\n  alt: string;\n  caption?: string;\n}\n\nconst { src, alt, caption } = Astro.props;\n\nconst svgUrl = typeof src === \&quot;string\&quot; ? src : src.src;\n---\n\n&lt;figure class=\&quot;excalidraw-figure\&quot;&gt;\n  &lt;div class=\&quot;excalidraw-svg\&quot; data-svg-url={svgUrl} aria-label={alt}&gt;\n    &lt;img src={svgUrl} alt={alt} style=\&quot;display: none;\&quot; /&gt;\n  &lt;/div&gt;\n  {caption &amp;&amp; &lt;figcaption&gt;{caption}&lt;/figcaption&gt;}\n&lt;/figure&gt;\n\n&lt;script&gt;\n  function modifySvg(svgString: string): string {\n    const parser = new DOMParser();\n    const doc = parser.parseFromString(svgString, \&quot;image/svg+xml\&quot;);\n    const svg = doc.documentElement;\n\n    svg.setAttribute(\&quot;width\&quot;, \&quot;100%\&quot;);\n    svg.setAttribute(\&quot;height\&quot;, \&quot;100%\&quot;);\n    svg.classList.add(\&quot;w-full\&quot;, \&quot;h-auto\&quot;);\n\n    doc.querySelectorAll(\&quot;text\&quot;).forEach(text =&gt; {\n      text.removeAttribute(\&quot;fill\&quot;);\n      text.classList.add(\&quot;fill-skin-base\&quot;);\n    });\n\n    doc.querySelectorAll(\&quot;rect\&quot;).forEach(rect =&gt; {\n      rect.removeAttribute(\&quot;fill\&quot;);\n      rect.classList.add(\&quot;fill-skin-soft\&quot;);\n    });\n\n    doc.querySelectorAll(\&quot;path\&quot;).forEach(path =&gt; {\n      path.removeAttribute(\&quot;stroke\&quot;);\n      path.classList.add(\&quot;stroke-skin-accent\&quot;);\n    });\n\n    doc.querySelectorAll(\&quot;g\&quot;).forEach(g =&gt; {\n      g.classList.add(\&quot;excalidraw-element\&quot;);\n    });\n\n    return new XMLSerializer().serializeToString(doc);\n  }\n\n  function initExcalidrawSVG() {\n    const svgContainers =\n      document.querySelectorAll&lt;HTMLElement&gt;(\&quot;.excalidraw-svg\&quot;);\n    svgContainers.forEach(async container =&gt; {\n      const svgUrl = container.dataset.svgUrl;\n      if (svgUrl) {\n        try {\n          const response = await fetch(svgUrl);\n          if (!response.ok) {\n            throw new Error(`Failed to fetch SVG: ${response.statusText}`);\n          }\n          const svgData = await response.text();\n          const modifiedSvg = modifySvg(svgData);\n          container.innerHTML = modifiedSvg;\n        } catch (error) {\n          console.error(\&quot;Error in ExcalidrawSVG component:\&quot;, error);\n          container.innerHTML = `&lt;svg xmlns=\&quot;http://www.w3.org/2000/svg\&quot; viewBox=\&quot;0 0 100 100\&quot;&gt;\n            &lt;text x=\&quot;10\&quot; y=\&quot;50\&quot; fill=\&quot;red\&quot;&gt;Error loading SVG&lt;/text&gt;\n          &lt;/svg&gt;`;\n        }\n      }\n    });\n  }\n\n  // Run on initial page load\n  document.addEventListener(\&quot;DOMContentLoaded\&quot;, initExcalidrawSVG);\n\n  // Run on subsequent navigation\n  document.addEventListener(\&quot;astro:page-load\&quot;, initExcalidrawSVG);\n&lt;/script&gt;\n\n&lt;style&gt;\n  .excalidraw-figure {\n    @apply my-8 w-full max-w-full overflow-hidden;\n  }\n  .excalidraw-svg {\n    @apply w-full max-w-full overflow-hidden;\n  }\n  :global(.excalidraw-svg svg) {\n    @apply h-auto w-full;\n  }\n  :global(.excalidraw-svg .fill-skin-base) {\n    @apply fill-[rgb(34,46,54)] dark:fill-[rgb(234,237,243)];\n  }\n  :global(.excalidraw-svg .fill-skin-soft) {\n    @apply fill-[rgb(234,206,219)] dark:fill-[rgb(52,63,96)];\n  }\n  :global(.excalidraw-svg .stroke-skin-accent) {\n    @apply stroke-[rgb(211,0,106)] dark:stroke-[rgb(255,107,237)];\n  }\n  :global(.excalidraw-svg .excalidraw-element) {\n    @apply transition-all duration-300;\n  }\n  :global(.excalidraw-svg .excalidraw-element:hover) {\n    @apply opacity-80;\n  }\n  figcaption {\n    @apply mt-4 text-center text-sm italic text-skin-base;\n  }\n&lt;/style&gt;\n```\n\n### 4. Using the Component\n\nIntegrate the component into your MDX blog posts:\n\n💡 **Note:** We need to use MDX so that we can use the `ExcalidrawSVG` component in our blog posts. You can read more about MDX [here](https://mdxjs.com/).\n\n```mdx\n---\nimport ExcalidrawSVG from &#39;@features/mdx-components/components/ExcalidrawSVG.astro&#39;;\nimport myDiagram from &#39;../assets/my-diagram.svg&#39;;\n---\n\n# My Technical Blog Post\n\n&lt;ExcalidrawSVG\n  src={myDiagram}\n  alt=\&quot;Architecture diagram\&quot;\n  caption=\&quot;System architecture overview\&quot;\n/&gt;\n```\n\n### Best Practices and Tips for Theme-Aware Technical Diagrams\n\n1. **Simplicity and Focus**\n   - Keep diagrams simple and focused for better readability\n   - Avoid cluttering with unnecessary details\n\n2. **Consistent Styling**\n   - Use consistent styling across all diagrams\n   - Maintain a uniform look and feel throughout your documentation\n\n3. **Thorough Testing**\n   - Test thoroughly in both light and dark modes\n   - Ensure diagrams are clear and legible in all color schemes\n\n4. **Accessibility Considerations**\n   - Consider accessibility when choosing colors and contrast\n   - Ensure diagrams are understandable for users with color vision deficiencies\n\n5. **Smooth Transitions**\n   - Implement smooth transitions for theme changes\n   - Provide a seamless experience when switching between light and dark modes\n\n## Conclusion\n\nWith this custom component, you can now create technical diagrams that seamlessly integrate with your Astro blog&#39;s design system.\nThis solution eliminates the need for maintaining multiple versions of diagrams while providing a superior user experience through smooth transitions and interactive elements.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <h2 id="why-you-need-theme-aware-technical-diagrams-in-your-astro-blog">Why You Need Theme-Aware Technical Diagrams in Your Astro Blog<a class="heading-link" aria-label="Link to section" href="#why-you-need-theme-aware-technical-diagrams-in-your-astro-blog"><span class="heading-link-icon">#</span></a></h2>
<p>Technical bloggers often face a common challenge: creating diagrams seamlessly integrating with their site’s design system. While tools like Excalidraw make it easy to create beautiful diagrams, maintaining their visual consistency across different theme modes can be frustrating. This is especially true when your Astro blog supports light and dark modes.
This tutorial will solve this problem by building a custom solution that automatically adapts your Excalidraw diagrams to match your site’s theme.</p>
<h2 id="common-challenges-with-technical-diagrams-in-web-development">Common Challenges with Technical Diagrams in Web Development<a class="heading-link" aria-label="Link to section" href="#common-challenges-with-technical-diagrams-in-web-development"><span class="heading-link-icon">#</span></a></h2>
<p>When working with Excalidraw, we face several issues:</p>
<ul>
<li>Exported SVGs come with fixed colors</li>
<li>Diagrams don’t automatically adapt to dark mode</li>
<li>Maintaining separate versions for different themes is time-consuming</li>
<li>Lack of interactive elements and smooth transitions</li>
</ul>
<h2 id="before-vs-after-the-impact-of-theme-aware-diagrams">Before vs After: The Impact of Theme-Aware Diagrams<a class="heading-link" aria-label="Link to section" href="#before-vs-after-the-impact-of-theme-aware-diagrams"><span class="heading-link-icon">#</span></a></h2>
<div class="grid grid-cols-2 gap-8 w-full"><div class="w-full"><h4 class="text-xl font-bold">Standard Export</h4><p>Here’s how a typical Excalidraw diagram looks without any customization:</p><img src="/_astro/example.BQjXfBZh_ZQhCyI.svg" alt="How a excalidraw diagrams looks without our custom component" loading="lazy" decoding="async" fetchpriority="auto" width="400" height="300" class="w-full h-auto object-cover"></div><div class="w-full"><h4 class="text-xl font-bold">With Our Solution</h4><p>And here’s the same diagram using our custom component:</p><figure class="excalidraw-figure astro-hxyrieg5"> <div class="excalidraw-svg astro-hxyrieg5" role="img" aria-label="Example diagram"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 120" width="100%" class="excalidraw-rendered" preserveAspectRatio="xMidYMid meet">
  <!-- svg-source:excalidraw -->
  
  <defs>
    <style class="style-fonts">
      @font-face { font-family: Excalifont; src: url(data:font/woff2;base64,d09GMgABAAAAAArQAA4AAAAAEnAAAAp+AAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGhYbg3gcNAZgAHwRCAqXTJFCCyAAATYCJAM8BCAFgxgHIBtVDlGUkFYo2Y8E22bDOuLhuh5RW2LUEZIjXuro/+D5//3x7XMeP6mZRCBPKFCCV1dIku/P8zf/3OeosUFOGIBqXwDmv80SdqvQ+v+fyIhH1sRCWNNjxY7tIz1C618C0U0gPjMryciKKIFzL2f14S9V71/21rFEs8UjMuZLNo6FOcxua9cDKy2xYqm4Bu1FpxUuINalIFYT2BVxkWv1pg8CBBN0iiBUh8ivE0g5GohuU3YxuE3r2akNuM3q5GwNbvMburQDNwiA98bYPGendsAsBzqj0gqoivjwdQDzj4s0IiWwCQbzCKxs3nbomzbzmFQ6WgVpVFMz7sW5NXCiIQRG+1nYuHj4BBBIyDmGuMRrgFKwhotBnDjpcgnE0QVAykkRxGkB68mdXznJW6ITXxDuttPBaiVkOzqgyAIgdhSuuamS2EBeFOSue6o6UIvRBBx8HaXlAAzONiMTIZZfIFrYsXuYORcOUEQPq9s/DccZQ93UAHsnFXeup5p+PzEWEC0XJdMRzL5rLEJwXIrQYqQBBy1pQ3u60MMYGBI1aTvR/Ycz181Nc80UTcFkTdqYJmkoIjvEGLQadu2pKKn1QWWvrdpHVtUoU2QdXrQPlgy/mQcWLP8g0DHo71qw+tCuQ6e0oShFfKLYRQVNoxgDodaVYOVxqVVepHt8tyTqVS6mGtC+q9sEEgxAUtDu6Xybn5bVic80RGciWkSJABWQ5QxYgoYEfOUKwE+AxmdnKbe9WcwbvXgxmMihekjSq74YzifB2bzDEVG3CSGQYIAXR9u2OZIxkgCf1MfL8oOUJamfj/PYAQ0HYCKXEAZWlAYUhXlBnmb5bDebUG9JzKWPJXZ/XGQLFuzcqSGHLUSvATeGnQkAHH9ZFMueF+Ls1oKTPmMAjwn3nJjlgJwnmBv39LIulT3Rk4kBMGg6A/jOHYCbSLbcKKUmNRNSzru+jEnXRV0mNgHQhkQmbTgMIcbAWkid/RAy444T10OPV93uTuTOw2/0pDG9MqP6vtbUxpC7dkTJ3V513VtQnqxGDMOXBJpFURbRMdB8MV1NG9DYYrdDCqly6uKmrEUpMt0g73lyq+2XupVuVkzlpJTHp0JkEhq9MTWWdHycf44x3IYGwII2dC1+Y8DZfCeevirqkqfgkuCudw7h0iNUygZTlwcJI7goJCtIGuy3ojVEXReZwdQC4lczxlmoppMcxreWNURHsmaBL3rdBa8vJeoRlUCZcHnH4Yx2JuMnAMv3xi6NdCk0IV1WLot6e017thPDTeueonteNzVNWkOuoAEL4AqY8OFkhiPD0D50cdn1TfeXVDkVVASthIRmONwAuAHyfmLgJD6O/rVAPGu/bDAVYjYkhFNlhaWkuytIq2XfF/UQS6GSi9w4rZkou2yXp+i2fliPlwlrd3DTsgBOwsl2pM2psTvu0rETY1F6IRt0+1NdJrKA1kQX7NI0Jy0b3yTx9QVVP2nDwfL98oIFrY4KsJoO0OaDSzKnziB2iAES/5ypQUb8/jxoVJ5sxk1ZszSKanPNQiEQSJi8eyKaYFJ9EbOrkOOMTiKy+qhk5y+K/U06MfC+cNhP/KH6bS/I5rFVjNlStcOJOTE8ITyLOzIeGgnybBnbxrwgNWvoVoBn05ioEwIjpC0uFCXmhVidlUV9iJGzc6qBQWXAiWEok0FiE2gAdYBapTP0LwSqCVblCsAvgGVL3NJpl29cMN+3BB8WwpZqFnZcVPjIk3vHqt20SdXeoqr9AkpTMC6OufAxEQ8+RBSufMt5Zj4W8L9zyEHxzS3E3ZgdJFTxtr5ZvoV7MZk9bQSa0j1CPlPK4T52K3c5HMuFK/wk+ZdrlW/f7f+yp8So/wkOo0HSvsMG6W7w5gj8vCiEsEa3mXxMPPHwrhzEQSufl8fliKwkUyyZdfKw+9VdrNZ1vr5lenQklJX+7F13J7qiw1zoYsF70v+yu8Qd20JXMHqGriipi3tEthsCWdvCzRdlL1ec/fPW8Z2BBQGJ06YnnzltSccXVQRsbE+YFEv08i1/Z3jNHVwh4Xith0GwIXDDua7bZ2ctvFX4A3F9hZTnHlDot2PgZuLKlK80mHc+JXR0pchcvFhw5WVrr+UTfvnw4uSHFcUBnxXAIfdJhy9wbKsbebIsFIUad4Y7fCdaBHm0qOWs5DPVh8YpchW+Vcqx/DziN05R4wrTYf/4lXJtkL5jsa5GdB2td1rwHnS8jYibXL65A9HSDapDDiQWfDoVfvuX29tu/CBUF/RCc9/HdTEr4PgB6/K3hldTX+3+lD9/N6ZLW/K58u8dsmke2SmeVvaogWWfxJy8dfyXOySDZuUN7pXLfTgonInTeE+aipY7csXCWix9x4ehSdPjIT+H29rfO8df0xBV5uGusXm9TqClbd+p2rUTmK2Hj1cv6bDVR/FdKc6YKluImVnFzjgYf/Pxr5Qe9rKtJySi/MKpmhGxvfx6ohRRmWi48swSQlLc6Xy6nHbzfBl49HxM2/aXIxjfKIRFhbSCgZ8qjt+TDUoezeacSMQ454p7yj28sf4kbmbzIng7vakDCDeq1y9+v9dxuGsXttxn/f3GnFahLddpg2dk2UZkHY8zrc1q29fj65nF0Wp7cKncmmziaBc0I9/iyHDvo7siiicamKAwDmK3/XBhHozvn8w3SMmNmVxFnC8PLd4nLR1zaFCdlGS5jbVIuSv6+o5kSwJGwdJY3piGtKUPL7XwcSsuxwyg7ZFcDUiOfe25ZONqjsepyTXdIubl6ErctAmmxkvuVNvn1QNFJOaDf6y4aOhmkRUOJQs+NFf89pwdPz5cHPFxf52u9hEd0dGnXz+Q1l+sGry0LYfTO1BqKdUfuhGQsrHx9oOuJZJy7oH65h0t5Esig/AOroCYWxs7Li49wm058X1j+EZFjUmQzM5b7/bvTHX0591ntEOM3Vv2MRNdpesOXLo3ZHV976Sc/I7qfnAs1FJzLnf+1YIN/SIuDc1RKpAnCvMVlQ2gu4mKazz7msiphfoyu7aT61EgbtX72KkwsefRSOecmKJNKU/Q3hEfT7RPWLepY7zNV5dpOvcwprt7YWoLsLQszJvVmmhpH5Tn0iVPqfh4ZuSDySXy7qUM0XGycMTq5UUNGnzB8kJdin7qtO9lV4WiQrVRnIhwLNSw1FWVoTHK5JZkUU9145W4X9MDP2/s+XHKrwd0r4RsTH50VFeJ8nbUXxclr/i987lvnSD96ztB+AuAR2uiBgB4fODNuv+3/19nv7IbAPDRBen/spojJqT//i7/l/S1YVYjGDUQvHQJ6EUqVQOB8oN0rYEQvhDOQ6q1HKJlDhXqDcEaAki3UqJ5IFiTPYwbuKnt0dKlHQw8xoK7MpvVmc+lyiVEs8+lhHLSZVHIMJdNNo0uh1b84WpPDfTQgyYaaENLXLSnHV2IoBAnzXSlDQ10ohQnnehMS2pcTQyRRAeNNMw005MOtJDigyQOsRmCdRK7cRIha/ejZq9t2EARZnIlzkVsjZuEPmt0oCeBlqxiiy0hmIGQrBFLdIR4t9FIT5e1FA4200B3IjVoO6vboF5e7NyAMyNOdNPGHESCg1jmPw4=); }
    </style>
    
  <style>
  .ed-text { fill: var(--excalidraw-text, #222e36); }
  .ed-fill { fill: var(--excalidraw-fill, #eaced7); }
  .ed-accent-fill { fill: var(--excalidraw-accent, #d3006a); }
  .ed-accent-stroke { stroke: var(--excalidraw-accent, #d3006a); }
</style></defs>
  <g stroke-linecap="round" transform="translate(10 10) rotate(0 50 50)"><path d="M25 0 C35.79 -2.14, 54.05 1.63, 75 0 M25 0 C40.25 0.71, 51.22 0.12, 75 0 M75 0 C94.52 3.01, 100.93 6.35, 100 25 M75 0 C93.17 4.17, 104.08 7.77, 100 25 M100 25 C97.25 39.72, 103 46.16, 100 75 M100 25 C98.12 40.05, 98.89 53.8, 100 75 M100 75 C97.28 93.81, 92.55 100.25, 75 100 M100 75 C100.75 94.94, 92.41 101.28, 75 100 M75 100 C58.75 96.6, 37.98 96.31, 25 100 M75 100 C62.23 100.52, 50.92 101.89, 25 100 M25 100 C9.68 96.84, -1.55 95, 0 75 M25 100 C11.86 98.53, -0.26 93.57, 0 75 M0 75 C-2.94 55.41, -0.29 37.95, 0 25 M0 75 C2.17 63.9, -0.06 49.82, 0 25 M0 25 C-2.93 11.19, 8.44 -1.46, 25 0 M0 25 C-0.55 6.04, 8.78 -0.67, 25 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(32.16001892089844 47.5) rotate(0 27.839981079101562 12.5)"><text x="27.839981079101562" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Astro</text></g><g stroke-linecap="round" transform="translate(190 10) rotate(0 70 50)"><path d="M25 0 C59.35 -1.4, 89.18 -1.7, 115 0 M25 0 C46.42 -0.49, 69.3 0.88, 115 0 M115 0 C133.02 -3.16, 138.45 11.67, 140 25 M115 0 C135.19 -1.47, 139.74 10.24, 140 25 M140 25 C137.73 42.02, 140.37 61.17, 140 75 M140 25 C141.12 38.71, 138.89 49.45, 140 75 M140 75 C137.07 94.52, 131.78 98.54, 115 100 M140 75 C139.45 89.37, 132.12 99.33, 115 100 M115 100 C91.38 100.2, 75.77 99.65, 25 100 M115 100 C78.89 99.92, 43.67 102.85, 25 100 M25 100 C12.25 98.45, 1.85 95.29, 0 75 M25 100 C11.23 102.26, -0.58 95.29, 0 75 M0 75 C0.38 62.75, -2.9 43.91, 0 25 M0 75 C-1.69 62.74, 0.98 50.18, 0 25 M0 25 C-1.13 4.73, 5.49 -1.14, 25 0 M0 25 C-2.27 6.46, 7.85 0.14, 25 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(208.50003814697266 47.5) rotate(0 51.499961853027344 12.5)"><text x="51.499961853027344" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Excalidraw</text></g><g transform="translate(144.57014295069598 57.0083612114222) rotate(0 5.510000020265579 12.5)"><text x="0" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" text-anchor="start" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">+</text></g><g stroke-linecap="round" transform="translate(130 50) rotate(0 20 20)"><path d="M15.16 1.15 C19.14 0.09, 25.4 -0.02, 29.37 1.81 C33.34 3.63, 37.23 8.07, 38.97 12.09 C40.71 16.11, 41.11 21.91, 39.81 25.93 C38.5 29.95, 34.82 33.91, 31.15 36.22 C27.48 38.54, 22.28 40.2, 17.81 39.82 C13.34 39.43, 7.3 37.11, 4.33 33.91 C1.35 30.72, 0 25.01, -0.01 20.65 C-0.02 16.3, 1.43 11.29, 4.26 7.76 C7.08 4.23, 14.4 0.59, 16.94 -0.5 C19.48 -1.59, 19.32 0.75, 19.5 1.22 M14.12 -0.43 C17.84 -1.7, 22.79 -0.37, 26.53 1.41 C30.27 3.19, 34.2 6.5, 36.55 10.25 C38.91 14, 41.56 19.41, 40.65 23.89 C39.74 28.36, 34.47 34.64, 31.09 37.12 C27.71 39.6, 24.45 39.09, 20.36 38.76 C16.28 38.43, 9.87 37.6, 6.57 35.15 C3.27 32.7, 1.3 28.49, 0.57 24.05 C-0.16 19.62, -0.02 12.5, 2.21 8.55 C4.44 4.6, 12.17 1.49, 13.95 0.36 C15.73 -0.77, 12.59 1.36, 12.91 1.75" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></svg></div>  </figure> <script type="module">function n(i){const t=new DOMParser().parseFromString(i,"image/svg+xml"),o=t.documentElement;o.removeAttribute("filter"),t.querySelectorAll("[filter]").forEach(e=>e.removeAttribute("filter")),o.classList.add("excalidraw-rendered"),o.setAttribute("width","100%"),o.removeAttribute("height"),o.setAttribute("preserveAspectRatio","xMidYMid meet"),o.getAttribute("viewBox")||o.setAttribute("viewBox","0 0 800 600"),t.querySelectorAll("text").forEach(e=>{const r=e.getAttribute("y");if(!r||r==="NaN"||isNaN(parseFloat(r))){const c=parseFloat(e.getAttribute("font-size")||"16");e.setAttribute("y",String(Math.round(c*.85)))}});const a={"#222e36":"var(--excalidraw-text)","#eaced7":"var(--excalidraw-fill)","#d3006a":"var(--excalidraw-accent)"};return t.querySelectorAll("[fill]").forEach(e=>{const r=e.getAttribute("fill")?.toLowerCase();r&&a[r]&&e.setAttribute("fill",a[r])}),t.querySelectorAll("[stroke]").forEach(e=>{const r=e.getAttribute("stroke")?.toLowerCase();r&&a[r]&&e.setAttribute("stroke",a[r])}),new XMLSerializer().serializeToString(t)}function l(){document.querySelectorAll(".excalidraw-svg[data-svg-url]").forEach(async i=>{const s=i.dataset.svgUrl;if(s)try{const t=await fetch(s);if(!t.ok)throw new Error(`Failed to fetch SVG: ${t.statusText}`);i.innerHTML=n(await t.text())}catch(t){console.error("Error in ExcalidrawSVG component:",t)}})}document.addEventListener("DOMContentLoaded",l);document.addEventListener("astro:page-load",l);</script> </div></div>
<h2 id="building-a-theme-aware-excalidraw-component-for-astro">Building a Theme-Aware Excalidraw Component for Astro<a class="heading-link" aria-label="Link to section" href="#building-a-theme-aware-excalidraw-component-for-astro"><span class="heading-link-icon">#</span></a></h2>
<p>We’ll create an Astro component that transforms static Excalidraw exports into dynamic, theme-aware diagrams. Our solution will:</p>
<ol>
<li>Automatically adapt to light and dark modes</li>
<li>Support your custom design system colors</li>
<li>Add interactive elements and smooth transitions</li>
<li>Maintain accessibility standards</li>
</ol>
<p>💡 Quick Start: Need an Astro blog first? Use <a href="https://github.com/satnaing/astro-paper" rel="noopener noreferrer" target="_blank">AstroPaper</a> as your starter or build from scratch. This tutorial focuses on the diagram component itself.</p>
<h2 id="step-by-step-implementation-guide">Step-by-Step Implementation Guide<a class="heading-link" aria-label="Link to section" href="#step-by-step-implementation-guide"><span class="heading-link-icon">#</span></a></h2>
<h3 id="1-implementing-the-theme-system">1. Implementing the Theme System<a class="heading-link" aria-label="Link to section" href="#1-implementing-the-theme-system"><span class="heading-link-icon">#</span></a></h3>
<p>First, let’s define the color variables that will power our theme-aware diagrams:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="css"><code><span class="line"><span style="color:#0DB9D7">html</span><span style="color:#89DDFF">[</span><span style="color:#BB9AF7">data-theme</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">light</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">]</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  --color-fill</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 250</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 252</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 252</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  --color-text-base</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 34</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 46</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 54</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  --color-accent</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 211</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 106</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  --color-card</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 234</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 206</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 219</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  --color-card-muted</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 241</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 186</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 212</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  --color-border</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 227</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 169</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 198</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#0DB9D7">html</span><span style="color:#89DDFF">[</span><span style="color:#BB9AF7">data-theme</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">dark</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">]</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  --color-fill</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 33</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 39</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 55</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  --color-text-base</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 234</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 237</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 243</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  --color-accent</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 255</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 107</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 237</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  --color-card</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 52</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 63</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 96</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  --color-card-muted</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 138</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 51</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 123</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  --color-border</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 171</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 75</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 153</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="html[data-theme=&#34;light&#34;] {
  --color-fill: 250, 252, 252;
  --color-text-base: 34, 46, 54;
  --color-accent: 211, 0, 106;
  --color-card: 234, 206, 219;
  --color-card-muted: 241, 186, 212;
  --color-border: 227, 169, 198;
}

html[data-theme=&#34;dark&#34;] {
  --color-fill: 33, 39, 55;
  --color-text-base: 234, 237, 243;
  --color-accent: 255, 107, 237;
  --color-card: 52, 63, 96;
  --color-card-muted: 138, 51, 123;
  --color-border: 171, 75, 153;
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="2-creating-optimized-excalidraw-diagrams">2. Creating Optimized Excalidraw Diagrams<a class="heading-link" aria-label="Link to section" href="#2-creating-optimized-excalidraw-diagrams"><span class="heading-link-icon">#</span></a></h3>
<p>Follow these steps to prepare your diagrams:</p>
<ol>
<li>Create your diagram at <a href="https://excalidraw.com/" rel="noopener noreferrer" target="_blank">Excalidraw</a></li>
<li>Export the diagram:
<ul>
<li>Select your diagram</li>
<li>Click the export button
<img src="/_astro/how-to-click-export-excalidraw.yiPFHkbC_Z1iBfrn.webp" alt="How to export Excalidraw diagram as SVG" loading="lazy" decoding="async" fetchpriority="auto" width="1354" height="731"></li>
</ul>
</li>
<li>Configure export settings:
<ul>
<li>Uncheck “Background”</li>
<li>Choose SVG format</li>
<li>Click “Save”
<img src="/_astro/save-as-svg.B4-hkhby_FLm2S.webp" alt="How to hide background and save as SVG" loading="lazy" decoding="async" fetchpriority="auto" width="1170" height="674"></li>
</ul>
</li>
</ol>
<h3 id="3-building-the-excalidrawsvg-component">3. Building the ExcalidrawSVG Component<a class="heading-link" aria-label="Link to section" href="#3-building-the-excalidrawsvg-component"><span class="heading-link-icon">#</span></a></h3>
<p>Here’s our custom Astro component that handles the theme-aware transformation:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="astro"><code><span class="line"><span style="color:#51597D;font-style:italic">---</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#BB9AF7"> type</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ImageMetadata</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">astro</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> Props</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  src</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> ImageMetadata</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  alt</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  caption</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> src</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> alt</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> caption</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> Astro</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">props</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> svgUrl</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> typeof</span><span style="color:#C0CAF5"> src</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">string</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> ?</span><span style="color:#C0CAF5"> src</span><span style="color:#BB9AF7"> :</span><span style="color:#C0CAF5"> src</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">src</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">figure</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">excalidraw-figure</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">excalidraw-svg</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> data-svg-url</span><span style="color:#89DDFF">=</span><span style="color:#7DCFFF">{</span><span style="color:#C0CAF5">svgUrl</span><span style="color:#7DCFFF">}</span><span style="color:#BB9AF7"> aria-label</span><span style="color:#89DDFF">=</span><span style="color:#7DCFFF">{</span><span style="color:#C0CAF5">alt</span><span style="color:#7DCFFF">}</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">img</span><span style="color:#BB9AF7"> src</span><span style="color:#89DDFF">=</span><span style="color:#7DCFFF">{</span><span style="color:#C0CAF5">svgUrl</span><span style="color:#7DCFFF">}</span><span style="color:#BB9AF7"> alt</span><span style="color:#89DDFF">=</span><span style="color:#7DCFFF">{</span><span style="color:#C0CAF5">alt</span><span style="color:#7DCFFF">}</span><span style="color:#BB9AF7"> style</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">display: none;</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">  {</span><span style="color:#C0CAF5">caption</span><span style="color:#BB9AF7"> &amp;&amp;</span><span style="color:#BA3C97"> &lt;</span><span style="color:#F7768E">figcaption</span><span style="color:#BA3C97">&gt;</span><span style="color:#7DCFFF">{</span><span style="color:#C0CAF5">caption</span><span style="color:#7DCFFF">}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">figcaption</span><span style="color:#BA3C97">&gt;</span><span style="color:#7DCFFF">}</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">figure</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> modifySvg</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">svgString</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> parser</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> DOMParser</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> doc</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> parser</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">parseFromString</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">svgString</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">image/svg+xml</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> svg</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> doc</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">documentElement</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">    svg</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">setAttribute</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">width</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">100%</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    svg</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">setAttribute</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">height</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">100%</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    svg</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">classList</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">add</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">w-full</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">h-auto</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">    doc</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">querySelectorAll</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">text</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">forEach</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">text</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">      text</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">removeAttribute</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">fill</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      text</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">classList</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">add</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">fill-skin-base</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">    doc</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">querySelectorAll</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">rect</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">forEach</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">rect</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">      rect</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">removeAttribute</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">fill</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      rect</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">classList</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">add</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">fill-skin-soft</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">    doc</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">querySelectorAll</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">path</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">forEach</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">path</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">      path</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">removeAttribute</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">stroke</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      path</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">classList</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">add</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">stroke-skin-accent</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">    doc</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">querySelectorAll</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">g</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">forEach</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">g</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">      g</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">classList</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">add</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">excalidraw-element</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> XMLSerializer</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">serializeToString</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">doc</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> initExcalidrawSVG</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> svgContainers</span><span style="color:#89DDFF"> =</span></span>
<span class="line"><span style="color:#C0CAF5">      document</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">querySelectorAll</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">HTMLElement</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">.excalidraw-svg</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    svgContainers</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">forEach</span><span style="color:#9ABDF5">(</span><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#E0AF68"> container</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> svgUrl</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> container</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">dataset</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">svgUrl</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">svgUrl</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">        try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">          const</span><span style="color:#BB9AF7"> response</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> fetch</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">svgUrl</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">          if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">response</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">ok</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">            throw</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Error</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">Failed to fetch SVG: </span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">response</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">statusText</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">          const</span><span style="color:#BB9AF7"> svgData</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> response</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">text</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">          const</span><span style="color:#BB9AF7"> modifiedSvg</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> modifySvg</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">svgData</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">          container</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">innerHTML</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> modifiedSvg</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">        } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">error</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">          console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">error</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Error in ExcalidrawSVG component:</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> error</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">          container</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">innerHTML</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> `</span><span style="color:#9ECE6A">&lt;svg xmlns=&quot;http://www.w3.org/2000/svg&quot; viewBox=&quot;0 0 100 100&quot;&gt;</span></span>
<span class="line"><span style="color:#9ECE6A">            &lt;text x=&quot;10&quot; y=&quot;50&quot; fill=&quot;red&quot;&gt;Error loading SVG&lt;/text&gt;</span></span>
<span class="line"><span style="color:#9ECE6A">          &lt;/svg&gt;</span><span style="color:#89DDFF">`</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Run on initial page load</span></span>
<span class="line"><span style="color:#C0CAF5">  document</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">addEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">DOMContentLoaded</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> initExcalidrawSVG</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Run on subsequent navigation</span></span>
<span class="line"><span style="color:#C0CAF5">  document</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">addEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">astro:page-load</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> initExcalidrawSVG</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">style</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#E0AF68">  .</span><span style="color:#9ECE6A">excalidraw-figure</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9ABDF5">    @apply my-8 w-full max-w-full overflow-hidden</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#E0AF68">  .</span><span style="color:#9ECE6A">excalidraw-svg</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9ABDF5">    @apply w-full max-w-full overflow-hidden</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#C0CAF5">  :global(</span><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">excalidraw-svg</span><span style="color:#0DB9D7"> svg</span><span style="color:#C0CAF5">) </span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#9ABDF5">    @apply h-auto w-full</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#C0CAF5">  :global(</span><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">excalidraw-svg</span><span style="color:#E0AF68"> .</span><span style="color:#9ECE6A">fill-skin-base</span><span style="color:#C0CAF5">) </span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#9ABDF5">    @apply fill-[rgb(34,46,54)] dark</span><span style="color:#89DDFF">:</span><span style="color:#BB9AF7">fill-[</span><span style="color:#0DB9D7">rgb</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">234</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64">237</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64">243</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#C0CAF5">  :global(</span><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">excalidraw-svg</span><span style="color:#E0AF68"> .</span><span style="color:#9ECE6A">fill-skin-soft</span><span style="color:#C0CAF5">) </span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#9ABDF5">    @apply fill-[rgb(234,206,219)] dark</span><span style="color:#89DDFF">:</span><span style="color:#BB9AF7">fill-[</span><span style="color:#0DB9D7">rgb</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">52</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64">63</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64">96</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#C0CAF5">  :global(</span><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">excalidraw-svg</span><span style="color:#E0AF68"> .</span><span style="color:#9ECE6A">stroke-skin-accent</span><span style="color:#C0CAF5">) </span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#9ABDF5">    @apply stroke-[rgb(211,0,106)] dark</span><span style="color:#89DDFF">:</span><span style="color:#BB9AF7">stroke-[</span><span style="color:#0DB9D7">rgb</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">255</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64">107</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64">237</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#C0CAF5">  :global(</span><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">excalidraw-svg</span><span style="color:#E0AF68"> .</span><span style="color:#9ECE6A">excalidraw-element</span><span style="color:#C0CAF5">) </span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#9ABDF5">    @apply transition-all duration-300</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#C0CAF5">  :global(</span><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">excalidraw-svg</span><span style="color:#E0AF68"> .</span><span style="color:#9ECE6A">excalidraw-element</span><span style="color:#E0AF68">:</span><span style="color:#BB9AF7">hover</span><span style="color:#C0CAF5">) </span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#9ABDF5">    @apply opacity-80</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#0DB9D7">  figcaption</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9ABDF5">    @apply mt-4 text-center text-sm italic text-skin-base</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">style</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="---
import type { ImageMetadata } from &#34;astro&#34;;

interface Props {
  src: ImageMetadata | string;
  alt: string;
  caption?: string;
}

const { src, alt, caption } = Astro.props;

const svgUrl = typeof src === &#34;string&#34; ? src : src.src;
---

<figure class=&#34;excalidraw-figure&#34;>
  <div class=&#34;excalidraw-svg&#34; data-svg-url={svgUrl} aria-label={alt}>
    <img src={svgUrl} alt={alt} style=&#34;display: none;&#34; />
  </div>
  {caption &#38;&#38; <figcaption>{caption}</figcaption>}
</figure>

<script>
  function modifySvg(svgString: string): string {
    const parser = new DOMParser();
    const doc = parser.parseFromString(svgString, &#34;image/svg+xml&#34;);
    const svg = doc.documentElement;

    svg.setAttribute(&#34;width&#34;, &#34;100%&#34;);
    svg.setAttribute(&#34;height&#34;, &#34;100%&#34;);
    svg.classList.add(&#34;w-full&#34;, &#34;h-auto&#34;);

    doc.querySelectorAll(&#34;text&#34;).forEach(text => {
      text.removeAttribute(&#34;fill&#34;);
      text.classList.add(&#34;fill-skin-base&#34;);
    });

    doc.querySelectorAll(&#34;rect&#34;).forEach(rect => {
      rect.removeAttribute(&#34;fill&#34;);
      rect.classList.add(&#34;fill-skin-soft&#34;);
    });

    doc.querySelectorAll(&#34;path&#34;).forEach(path => {
      path.removeAttribute(&#34;stroke&#34;);
      path.classList.add(&#34;stroke-skin-accent&#34;);
    });

    doc.querySelectorAll(&#34;g&#34;).forEach(g => {
      g.classList.add(&#34;excalidraw-element&#34;);
    });

    return new XMLSerializer().serializeToString(doc);
  }

  function initExcalidrawSVG() {
    const svgContainers =
      document.querySelectorAll<HTMLElement>(&#34;.excalidraw-svg&#34;);
    svgContainers.forEach(async container => {
      const svgUrl = container.dataset.svgUrl;
      if (svgUrl) {
        try {
          const response = await fetch(svgUrl);
          if (!response.ok) {
            throw new Error(`Failed to fetch SVG: ${response.statusText}`);
          }
          const svgData = await response.text();
          const modifiedSvg = modifySvg(svgData);
          container.innerHTML = modifiedSvg;
        } catch (error) {
          console.error(&#34;Error in ExcalidrawSVG component:&#34;, error);
          container.innerHTML = `<svg xmlns=&#34;http://www.w3.org/2000/svg&#34; viewBox=&#34;0 0 100 100&#34;>
            <text x=&#34;10&#34; y=&#34;50&#34; fill=&#34;red&#34;>Error loading SVG</text>
          </svg>`;
        }
      }
    });
  }

  // Run on initial page load
  document.addEventListener(&#34;DOMContentLoaded&#34;, initExcalidrawSVG);

  // Run on subsequent navigation
  document.addEventListener(&#34;astro:page-load&#34;, initExcalidrawSVG);
</script>

<style>
  .excalidraw-figure {
    @apply my-8 w-full max-w-full overflow-hidden;
  }
  .excalidraw-svg {
    @apply w-full max-w-full overflow-hidden;
  }
  :global(.excalidraw-svg svg) {
    @apply h-auto w-full;
  }
  :global(.excalidraw-svg .fill-skin-base) {
    @apply fill-[rgb(34,46,54)] dark:fill-[rgb(234,237,243)];
  }
  :global(.excalidraw-svg .fill-skin-soft) {
    @apply fill-[rgb(234,206,219)] dark:fill-[rgb(52,63,96)];
  }
  :global(.excalidraw-svg .stroke-skin-accent) {
    @apply stroke-[rgb(211,0,106)] dark:stroke-[rgb(255,107,237)];
  }
  :global(.excalidraw-svg .excalidraw-element) {
    @apply transition-all duration-300;
  }
  :global(.excalidraw-svg .excalidraw-element:hover) {
    @apply opacity-80;
  }
  figcaption {
    @apply mt-4 text-center text-sm italic text-skin-base;
  }
</style>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="4-using-the-component">4. Using the Component<a class="heading-link" aria-label="Link to section" href="#4-using-the-component"><span class="heading-link-icon">#</span></a></h3>
<p>Integrate the component into your MDX blog posts:</p>
<p>💡 <strong>Note:</strong> We need to use MDX so that we can use the <code>ExcalidrawSVG</code> component in our blog posts. You can read more about MDX <a href="https://mdxjs.com/" rel="noopener noreferrer" target="_blank">here</a>.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="mdx"><code><span class="line"><span style="color:#9ECE6A">---</span></span>
<span class="line"><span style="color:#9ECE6A">import ExcalidrawSVG from &#39;@features/mdx-components/components/ExcalidrawSVG.astro&#39;;</span></span>
<span class="line"><span style="color:#9ECE6A">import myDiagram from &#39;../assets/my-diagram.svg&#39;;</span></span>
<span class="line"><span style="color:#9ECE6A">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">#</span><span style="color:#C0CAF5"> My Technical Blog Post</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#0DB9D7">ExcalidrawSVG</span></span>
<span class="line"><span style="color:#BB9AF7">  src</span><span style="color:#89DDFF">=</span><span style="color:#7DCFFF">{</span><span style="color:#C0CAF5">myDiagram</span><span style="color:#7DCFFF">}</span></span>
<span class="line"><span style="color:#BB9AF7">  alt</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Architecture diagram</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">  caption</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">System architecture overview</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BA3C97">/&gt;</span></span></code><button type="button" class="copy" data-code="---
import ExcalidrawSVG from '@features/mdx-components/components/ExcalidrawSVG.astro';
import myDiagram from '../assets/my-diagram.svg';
---

# My Technical Blog Post

<ExcalidrawSVG
  src={myDiagram}
  alt=&#34;Architecture diagram&#34;
  caption=&#34;System architecture overview&#34;
/>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="best-practices-and-tips-for-theme-aware-technical-diagrams">Best Practices and Tips for Theme-Aware Technical Diagrams<a class="heading-link" aria-label="Link to section" href="#best-practices-and-tips-for-theme-aware-technical-diagrams"><span class="heading-link-icon">#</span></a></h3>
<ol>
<li>
<p><strong>Simplicity and Focus</strong></p>
<ul>
<li>Keep diagrams simple and focused for better readability</li>
<li>Avoid cluttering with unnecessary details</li>
</ul>
</li>
<li>
<p><strong>Consistent Styling</strong></p>
<ul>
<li>Use consistent styling across all diagrams</li>
<li>Maintain a uniform look and feel throughout your documentation</li>
</ul>
</li>
<li>
<p><strong>Thorough Testing</strong></p>
<ul>
<li>Test thoroughly in both light and dark modes</li>
<li>Ensure diagrams are clear and legible in all color schemes</li>
</ul>
</li>
<li>
<p><strong>Accessibility Considerations</strong></p>
<ul>
<li>Consider accessibility when choosing colors and contrast</li>
<li>Ensure diagrams are understandable for users with color vision deficiencies</li>
</ul>
</li>
<li>
<p><strong>Smooth Transitions</strong></p>
<ul>
<li>Implement smooth transitions for theme changes</li>
<li>Provide a seamless experience when switching between light and dark modes</li>
</ul>
</li>
</ol>
<h2 id="conclusion">Conclusion<a class="heading-link" aria-label="Link to section" href="#conclusion"><span class="heading-link-icon">#</span></a></h2>
<p>With this custom component, you can now create technical diagrams that seamlessly integrate with your Astro blog’s design system.
This solution eliminates the need for maintaining multiple versions of diagrams while providing a superior user experience through smooth transitions and interactive elements.</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_excalidraw-dark-mode-astro-diagrams" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="excalidraw-dark-mode-astro-diagrams" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/astro/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">astro</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/excalidraw/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">excalidraw</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/excalidraw-dark-mode-astro-diagrams/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/excalidraw-dark-mode-astro-diagrams/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/excalidraw-dark-mode-astro-diagrams/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/excalidraw-dark-mode-astro-diagrams/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/excalidraw-dark-mode-astro-diagrams/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/excalidraw-dark-mode-astro-diagrams/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/excalidraw-dark-mode-astro-diagrams/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/typescript-snippets-astro-show-dont-tell/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">TypeScript Snippets in Astro: Show, Don&#39;t Tell</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to add interactive type information and syntax highlighting to TypeScript snippets in your Astro site, enhancing code readability and user experience. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-sm">Updated:</span><span class="italic text-sm"><time dateTime="2024-09-29T00:00:00.000Z">Sep 29, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> astro </span> </div> </div> </a><a href="/posts/presentation-mode-demo/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Presentation Mode: Turn Your Blog Posts into Slides</h3> <p class="related-post-description astro-vj4tpspi"> A complete demo of presentation mode with v-click animations and drawing annotations. Press P to see keyboard navigation, incremental reveals, and press D to draw on slides! </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-sm">Updated:</span><span class="italic text-sm"><time dateTime="2026-01-24T00:00:00.000Z">Jan 24, 2026</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> demo </span> </div> </div> </a><a href="/posts/how-to-use-ai-for-effective-diagram-creation-a-guide-to-chatgpt-and-mermaid/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How to Use AI for Effective Diagram Creation: A Guide to ChatGPT and Mermaid</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to leverage ChatGPT and Mermaid to create effective diagrams for technical documentation and communication. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-02-09T00:00:00.000Z">Feb 9, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> ai </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "excalidraw-dark-mode-astro-diagrams";

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
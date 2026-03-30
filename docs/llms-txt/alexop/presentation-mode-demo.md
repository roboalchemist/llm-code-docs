# Source: https://alexop.dev/posts/presentation-mode-demo

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/presentation-mode-demo/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Presentation Mode: Turn Your Blog Posts into Slides | alexop.dev</title><meta name="title" content="Presentation Mode: Turn Your Blog Posts into Slides | alexop.dev"><meta name="description" content="A complete demo of presentation mode with v-click animations and drawing annotations. Press P to see keyboard navigation, incremental reveals, and press D to draw on slides!"><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Presentation Mode: Turn Your Blog Posts into Slides | alexop.dev"><meta property="og:description" content="A complete demo of presentation mode with v-click animations and drawing annotations. Press P to see keyboard navigation, incremental reveals, and press D to draw on slides!"><meta property="og:url" content="https://alexop.dev/posts/presentation-mode-demo/"><meta property="og:image" content="https://alexop.dev/posts/presentation-mode-turn-your-blog-posts-into-slides/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2026-01-23T00:00:00.000Z"><meta property="article:modified_time" content="2026-01-24T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/presentation-mode-demo/"><meta property="twitter:title" content="Presentation Mode: Turn Your Blog Posts into Slides | alexop.dev"><meta property="twitter:description" content="A complete demo of presentation mode with v-click animations and drawing annotations. Press P to see keyboard navigation, incremental reveals, and press D to draw on slides!"><meta property="twitter:image" content="https://alexop.dev/posts/presentation-mode-turn-your-blog-posts-into-slides/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Presentation Mode: Turn Your Blog Posts into Slides | alexop.dev","description":"A complete demo of presentation mode with v-click animations and drawing annotations. Press P to see keyboard navigation, incremental reveals, and press D to draw on slides!","image":"https://alexop.dev/posts/presentation-mode-turn-your-blog-posts-into-slides/index.png","datePublished":"2026-01-23T00:00:00.000Z","dateModified":"2026-01-24T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: presentation-mode-turn-your-blog-posts-into-slides; }@layer astro { ::view-transition-old(presentation-mode-turn-your-blog-posts-into-slides) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(presentation-mode-turn-your-blog-posts-into-slides) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(presentation-mode-turn-your-blog-posts-into-slides) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(presentation-mode-turn-your-blog-posts-into-slides) { 
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
</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: demo; }@layer astro { ::view-transition-old(demo) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(demo) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(demo) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(demo) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: presentation; }@layer astro { ::view-transition-old(presentation) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(presentation) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(presentation) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(presentation) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: feature; }@layer astro { ::view-transition-old(feature) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(feature) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(feature) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(feature) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Presentation Mode: Turn Your Blog Posts into Slides</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-base">Updated:</span><span class="italic text-base"><time dateTime="2026-01-24T00:00:00.000Z">Jan 24, 2026</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Z1N70cE" prefix="r29" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Presentation Mode: Turn Your Blog Posts into Slides&quot;],&quot;content&quot;:[0,&quot;import Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\nimport Aside from \&quot;@features/mdx-components/components/Aside.astro\&quot;;\nimport ContextWindowVisualizer from \&quot;@features/llm-education/components/ContextWindowVisualizer.tsx\&quot;;\nimport { VClick, VClicks, Slide, MagicMove, SubagentDiagram, Note } from \&quot;@features/presentation\&quot;;\n\n&lt;Alert type=\&quot;info\&quot; title=\&quot;Try It Now!\&quot;&gt;\n  Press **P** on your keyboard or click the floating button in the bottom-right corner to enter presentation mode. Use arrow keys to navigate between slides, and press **D** to draw annotations directly on slides!\n&lt;/Alert&gt;\n\n# Presentation Mode\n\nTurn your blog posts into beautiful slides with incremental reveals\n\n---\n\n## Why Presentation Mode?\n\n**The Problem:** You write a great blog post, then need to present it at a meetup.\n\n**Old Solution:** Recreate everything in PowerPoint or Google Slides.\n\n**New Solution:** Just add `presentation: true` to your frontmatter!\n\n```yaml\n---\ntitle: \&quot;My Awesome Post\&quot;\npresentation: true\n---\n```\n\n---\n\n## Keyboard Shortcuts\n\n| Key | Action |\n|-----|--------|\n| **P** | Toggle presentation mode |\n| **→** or **Space** | Next click step, then next slide |\n| **←** | Previous click step, then previous slide |\n| **1-9** | Jump to slide N (resets clicks) |\n| **Home** | First slide |\n| **End** | Last slide |\n| **D** | Toggle drawing mode |\n| **G** | Toggle grid overview |\n| **Escape** | Exit drawing → grid → presentation |\n\n---\n\n# Drawing Annotations\n\nDraw directly on slides with Excalidraw!\n\n---\n\n## Try Drawing Mode\n\nPress **D** to toggle drawing mode. A toolbar will appear with these tools:\n\n&lt;VClicks&gt;\n\n- **↖ Selection** - Select and move drawings\n- **✏️ Freedraw** - Freehand drawing (press P)\n- **→ Arrow** - Draw arrows (press A)\n- **□ Rectangle** - Draw rectangles (press R)\n- **○ Ellipse** - Draw circles (press O)\n- **T Text** - Add text annotations (press T)\n- **🧹 Eraser** - Erase drawings (press E)\n\n&lt;/VClicks&gt;\n\n---\n\n## Drawing Features\n\n&lt;VClick /&gt;\n\n**Colors:** 6 preset colors - Red, Blue, Green, Yellow, White, Black\n\n&lt;VClick /&gt;\n\n**Stroke Widths:** 3 sizes - Thin (1px), Medium (2px), Thick (4px)\n\n&lt;VClick /&gt;\n\n**Persistence:** Drawings stay when you navigate between slides!\n\n&lt;VClick /&gt;\n\n**Shortcuts:**\n- `C` - Clear current slide\n- `Shift+C` - Clear all slides\n- `Escape` - Exit drawing mode\n\n---\n\n## Use Cases\n\nWhy draw on slides during presentations?\n\n&lt;VClicks&gt;\n\n- Circle important code sections\n- Draw arrows connecting concepts\n- Add quick annotations for Q&amp;A\n- Highlight key points in diagrams\n- Sketch ideas during discussions\n\n&lt;/VClicks&gt;\n\n---\n\n# V-Click Animations\n\nReveal content step-by-step with Slidev-style click animations\n\n---\n\n## Sequential Reveals\n\nPress **→** to reveal each point:\n\n&lt;VClick /&gt;\n\n**Step 1:** First, we define the problem clearly.\n\n&lt;VClick /&gt;\n\n**Step 2:** Then, we explore possible solutions.\n\n&lt;VClick /&gt;\n\n**Step 3:** Finally, we implement and test!\n\n---\n\n## Building a List\n\nBenefits of incremental reveals:\n\n&lt;VClicks&gt;\n\n- Keeps audience focused on the current point\n- Creates natural pacing for your talk\n- Prevents information overload\n- Makes complex topics digestible\n\n&lt;/VClicks&gt;\n\n---\n\n## V-Click Syntax\n\nIn MDX files, use components to control reveals:\n\n```mdx\n&lt;VClick /&gt;\nContent appears on click\n\n&lt;VClicks&gt;\n- Each list item\n- Gets its own click\n&lt;/VClicks&gt;\n\n&lt;VClick order={3} /&gt;\nExplicit order (appears third)\n\n&lt;VClick hide /&gt;\nThis disappears on click\n```\n\n---\n\n# Custom Components\n\nInteractive React components work in slides!\n\n---\n\n## Context Window Visualizer\n\nThis is a custom React component rendered inside a slide:\n\n&lt;ContextWindowVisualizer client:load /&gt;\n\nTry typing messages to see the context fill up!\n\n---\n\n## Code Blocks Work Perfectly\n\nHere&#39;s a Vue composable example with full syntax highlighting:\n\n```typescript\nimport { ref, computed } from &#39;vue&#39;\n\nexport function useCounter(initial = 0) {\n  const count = ref(initial)\n\n  const double = computed(() =&gt; count.value * 2)\n\n  function increment() {\n    count.value++\n  }\n\n  return { count, double, increment }\n}\n```\n\n---\n\n## Magic Move: Code Evolution\n\nWatch code transform with smooth animations (press **→** to advance):\n\n&lt;MagicMove\n  lang=\&quot;typescript\&quot;\n  steps={[\n    `const x = 1`,\n    `const x = 1\nconst y = 2`,\n    `const x = 1\nconst y = 2\n\nfunction add(a: number, b: number) {\n  return a + b\n}`,\n    `const x = 1\nconst y = 2\n\nfunction add(a: number, b: number) {\n  return a + b\n}\n\nconst sum = add(x, y)\nconsole.log(sum) // 3`\n  ]}\n/&gt;\n\nEach arrow press animates the code to its next state!\n\n---\n\n## Mermaid Diagrams\n\nFlowcharts render beautifully in slides:\n\n```mermaid\ngraph LR\n    A[Blog Post] --&gt; B{presentation: true?}\n    B --&gt;|Yes| C[Show Toggle Button]\n    B --&gt;|No| D[Normal Post]\n    C --&gt; E[Press P]\n    E --&gt; F[Fullscreen Slides!]\n```\n\n---\n\n## Animated Diagrams\n\nInteractive diagrams with self-contained animations:\n\n&lt;SubagentDiagram\n  task=\&quot;Find auth files\&quot;\n  files={[\&quot;Auth.tsx\&quot;, \&quot;auth.ts\&quot;, \&quot;authService.ts\&quot;]}\n/&gt;\n\nClick **Start** to see the Explore subagent flow animation!\n\n---\n\n# Slide Layouts\n\n---\n\n## Available Layouts\n\nThis feature supports 9 different layout types:\n\n| Layout | Description |\n|--------|-------------|\n| `default` | Standard centered prose |\n| `cover` | Large title, full-bleed |\n| `center` | Fully centered content |\n| `two-cols` | Two-column split |\n| `image-left` | Image 40%, content 60% |\n| `image-right` | Content 60%, image 40% |\n| `image` | Full-bleed background |\n| `quote` | Prominent blockquote |\n| `section` | Section divider |\n| `iframe` | Embedded website/demo |\n\n---\n\n## Iframe Layout\n\nEmbed live demos, CodePen, StackBlitz, or videos directly in slides:\n\n&lt;Slide layout=\&quot;iframe\&quot; src=\&quot;https://stackblitz.com/edit/vitejs-vite-wdjbsx?embed=1&amp;file=src%2FApp.vue&amp;hideExplorer=1\&quot; title=\&quot;Vue Counter Demo\&quot; /&gt;\n\nThis is a live StackBlitz embed - fully interactive!\n\n---\n\n## Layout Syntax\n\nIn **.md files**, use HTML comments. In **.mdx files**, use components:\n\n```mdx\n{/* MDX format */}\n&lt;Slide layout=\&quot;cover\&quot; /&gt;\n# My Title\n\n---\n\n{/* .md format */}\n&lt;!--slide:{\&quot;layout\&quot;:\&quot;cover\&quot;}--&gt;\n# My Title\n```\n\n&lt;Aside type=\&quot;note\&quot; title=\&quot;MDX vs MD\&quot;&gt;\nBoth file formats support layouts and v-clicks! For `.md` files use HTML comments, for `.mdx` files use the `Slide`, `VClick`, and `VClicks` components.\n&lt;/Aside&gt;\n\n---\n\n## Layout Properties\n\nAll layouts accept these properties:\n\n| Property | Description |\n|----------|-------------|\n| `layout` | Layout name (required) |\n| `image` | Path to image in /public |\n| `backgroundSize` | CSS value (default: cover) |\n| `class` | Custom CSS class |\n| `src` | URL for iframe layout |\n| `title` | Accessibility title for iframe |\n\n---\n\n## Layout Animations\n\nEach layout type has its own animation:\n\n| Layout | Animation |\n|--------|-----------|\n| `default` | Slide |\n| `center` | Slide |\n| `two-cols` | Slide |\n| `cover` | **Fade** |\n| `image` | **Zoom** |\n| `quote` | **Fade** |\n| `section` | **Fade** |\n| `iframe` | **Fade** |\n\n---\n\n# Technical Details\n\n---\n\n## Architecture Overview\n\n```mermaid\nflowchart TB\n    subgraph Frontend\n        A[PresentationToggle] --&gt; B[PresentationMode]\n        B --&gt; C[PresentationSlide]\n        B --&gt; D[PresentationControls]\n        B --&gt; E[PresentationProgress]\n    end\n\n    subgraph Layouts\n        C --&gt; F[SlideLayoutDefault]\n        C --&gt; G[SlideLayoutCover]\n        C --&gt; H[SlideLayoutTwoCols]\n        C --&gt; I[... more layouts]\n    end\n\n    subgraph Content\n        J[Blog Post] --&gt; K[Compiled HTML]\n        K --&gt; L[Parse slide comments]\n        L --&gt; M[SlideData Array]\n    end\n\n    M --&gt; C\n```\n\n---\n\n## Tips for Great Slides\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;Best Practices\&quot;&gt;\n\n1. **Keep slides focused** - One idea per slide\n2. **Use headings** - They become slide titles\n3. **Leverage layouts** - Pick the right layout for content\n4. **Use v-clicks** - Reveal complex info step-by-step\n5. **Test navigation** - Make sure flow makes sense\n\n&lt;/Aside&gt;\n\n### Content Length\n\n&lt;VClicks&gt;\n\n- Short slides work best\n- If content overflows, it scrolls within the slide\n- But try to keep each slide digestible\n- Use v-clicks to break up longer content\n\n&lt;/VClicks&gt;\n\n---\n\n## Accessibility Features\n\n&lt;VClicks&gt;\n\n- **Focus trap** - Tab stays within the modal\n- **ARIA live region** - Announces \&quot;Slide X of Y, Step N of M\&quot;\n- **Escape to exit** - Standard modal behavior\n- **Keyboard navigation** - No mouse required\n- **Theme aware** - Respects light/dark mode\n- **Reduced motion** - V-click respects `prefers-reduced-motion`\n\n&lt;/VClicks&gt;\n\n---\n\n## Speaker Notes &amp; Presenter View\n\nPress **N** to open the presenter view popup!\n\n&lt;VClick /&gt;\n\nThe presenter view shows:\n\n&lt;VClicks&gt;\n\n- Current and next slide previews\n- Speaker notes with click-step highlighting\n- A timer you can start/pause/reset\n- Navigation controls\n\n&lt;/VClicks&gt;\n\n&lt;Note&gt;{\&quot;This is a speaker note! It&#39;s only visible in the presenter view.\\n[click] Now explain that the presenter view opens in a popup window.\\n[click] Walk through each feature: previews, notes, timer, controls.\\n[click] Mention keyboard shortcuts: T for timer, R to reset.\&quot;}&lt;/Note&gt;\n\n---\n\n## Notes with Click Markers\n\nNotes can reveal progressively with your click steps:\n\n&lt;VClick /&gt;\n\n**Step 1:** Define the problem\n\n&lt;VClick /&gt;\n\n**Step 2:** Explore solutions\n\n&lt;VClick /&gt;\n\n**Step 3:** Implement and ship!\n\n&lt;Note&gt;{\&quot;Always visible intro text for this slide.\\n[click] Talk about why defining the problem clearly matters.\\n[click] Mention 2-3 solution approaches you considered.\\n[click] Emphasize shipping fast and iterating.\&quot;}&lt;/Note&gt;\n\n---\n\n# Thank You!\n\nPress **Escape** to exit or continue with arrow keys\n\n---\n\n## Quick Reference\n\n**File format trade-offs:**\n\n| Format | Custom Components | Layouts | V-Click | Syntax |\n|--------|-------------------|---------|---------|--------|\n| `.mdx` | Yes | Yes | Yes | Components |\n| `.md` | No | Yes | Yes | HTML comments |\n\n&lt;VClick /&gt;\n\nPress **Escape** to exit presentation mode!&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <div class="alert alert-info astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl"></span> Try It Now! </p> <div class="alert-content astro-7kdbuayl"> <p>Press <strong>P</strong> on your keyboard or click the floating button in the bottom-right corner to enter presentation mode. Use arrow keys to navigate between slides, and press <strong>D</strong> to draw annotations directly on slides!</p> </div> </div> 
<h1 id="presentation-mode">Presentation Mode</h1>
<p>Turn your blog posts into beautiful slides with incremental reveals</p>
<hr/>
<h2 id="why-presentation-mode">Why Presentation Mode?<a class="heading-link" aria-label="Link to section" href="#why-presentation-mode"><span class="heading-link-icon">#</span></a></h2>
<p><strong>The Problem:</strong> You write a great blog post, then need to present it at a meetup.</p>
<p><strong>Old Solution:</strong> Recreate everything in PowerPoint or Google Slides.</p>
<p><strong>New Solution:</strong> Just add <code>presentation: true</code> to your frontmatter!</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="yaml"><code><span class="line"><span style="color:#A9B1D6">---</span></span>
<span class="line"><span style="color:#F7768E">title</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">My Awesome Post</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#F7768E">presentation</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#A9B1D6">---</span></span></code><button type="button" class="copy" data-code="---
title: &#34;My Awesome Post&#34;
presentation: true
---" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="keyboard-shortcuts">Keyboard Shortcuts<a class="heading-link" aria-label="Link to section" href="#keyboard-shortcuts"><span class="heading-link-icon">#</span></a></h2>













































<table><thead><tr><th>Key</th><th>Action</th></tr></thead><tbody><tr><td data-label="Key"><strong>P</strong></td><td data-label="Action">Toggle presentation mode</td></tr><tr><td data-label="Key"><strong>→</strong> or <strong>Space</strong></td><td data-label="Action">Next click step, then next slide</td></tr><tr><td data-label="Key"><strong>←</strong></td><td data-label="Action">Previous click step, then previous slide</td></tr><tr><td data-label="Key"><strong>1-9</strong></td><td data-label="Action">Jump to slide N (resets clicks)</td></tr><tr><td data-label="Key"><strong>Home</strong></td><td data-label="Action">First slide</td></tr><tr><td data-label="Key"><strong>End</strong></td><td data-label="Action">Last slide</td></tr><tr><td data-label="Key"><strong>D</strong></td><td data-label="Action">Toggle drawing mode</td></tr><tr><td data-label="Key"><strong>G</strong></td><td data-label="Action">Toggle grid overview</td></tr><tr><td data-label="Key"><strong>Escape</strong></td><td data-label="Action">Exit drawing → grid → presentation</td></tr></tbody></table>
<hr/>
<h1 id="drawing-annotations">Drawing Annotations</h1>
<p>Draw directly on slides with Excalidraw!</p>
<hr/>
<h2 id="try-drawing-mode">Try Drawing Mode<a class="heading-link" aria-label="Link to section" href="#try-drawing-mode"><span class="heading-link-icon">#</span></a></h2>
<p>Press <strong>D</strong> to toggle drawing mode. A toolbar will appear with these tools:</p>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ul>
<li><strong>↖ Selection</strong> - Select and move drawings</li>
<li><strong>✏️ Freedraw</strong> - Freehand drawing (press P)</li>
<li><strong>→ Arrow</strong> - Draw arrows (press A)</li>
<li><strong>□ Rectangle</strong> - Draw rectangles (press R)</li>
<li><strong>○ Ellipse</strong> - Draw circles (press O)</li>
<li><strong>T Text</strong> - Add text annotations (press T)</li>
<li><strong>🧹 Eraser</strong> - Erase drawings (press E)</li>
</ul><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<hr/>
<h2 id="drawing-features">Drawing Features<a class="heading-link" aria-label="Link to section" href="#drawing-features"><span class="heading-link-icon">#</span></a></h2>
<script type="application/json" data-vclick-marker="v-click">{}</script>
<p><strong>Colors:</strong> 6 preset colors - Red, Blue, Green, Yellow, White, Black</p>
<script type="application/json" data-vclick-marker="v-click">{}</script>
<p><strong>Stroke Widths:</strong> 3 sizes - Thin (1px), Medium (2px), Thick (4px)</p>
<script type="application/json" data-vclick-marker="v-click">{}</script>
<p><strong>Persistence:</strong> Drawings stay when you navigate between slides!</p>
<script type="application/json" data-vclick-marker="v-click">{}</script>
<p><strong>Shortcuts:</strong></p>
<ul>
<li><code>C</code> - Clear current slide</li>
<li><code>Shift+C</code> - Clear all slides</li>
<li><code>Escape</code> - Exit drawing mode</li>
</ul>
<hr/>
<h2 id="use-cases">Use Cases<a class="heading-link" aria-label="Link to section" href="#use-cases"><span class="heading-link-icon">#</span></a></h2>
<p>Why draw on slides during presentations?</p>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ul>
<li>Circle important code sections</li>
<li>Draw arrows connecting concepts</li>
<li>Add quick annotations for Q&amp;A</li>
<li>Highlight key points in diagrams</li>
<li>Sketch ideas during discussions</li>
</ul><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<hr/>
<h1 id="v-click-animations">V-Click Animations</h1>
<p>Reveal content step-by-step with Slidev-style click animations</p>
<hr/>
<h2 id="sequential-reveals">Sequential Reveals<a class="heading-link" aria-label="Link to section" href="#sequential-reveals"><span class="heading-link-icon">#</span></a></h2>
<p>Press <strong>→</strong> to reveal each point:</p>
<script type="application/json" data-vclick-marker="v-click">{}</script>
<p><strong>Step 1:</strong> First, we define the problem clearly.</p>
<script type="application/json" data-vclick-marker="v-click">{}</script>
<p><strong>Step 2:</strong> Then, we explore possible solutions.</p>
<script type="application/json" data-vclick-marker="v-click">{}</script>
<p><strong>Step 3:</strong> Finally, we implement and test!</p>
<hr/>
<h2 id="building-a-list">Building a List<a class="heading-link" aria-label="Link to section" href="#building-a-list"><span class="heading-link-icon">#</span></a></h2>
<p>Benefits of incremental reveals:</p>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ul>
<li>Keeps audience focused on the current point</li>
<li>Creates natural pacing for your talk</li>
<li>Prevents information overload</li>
<li>Makes complex topics digestible</li>
</ul><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<hr/>
<h2 id="v-click-syntax">V-Click Syntax<a class="heading-link" aria-label="Link to section" href="#v-click-syntax"><span class="heading-link-icon">#</span></a></h2>
<p>In MDX files, use components to control reveals:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="mdx"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#0DB9D7">VClick</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#A9B1D6">Content appears on click</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#0DB9D7">VClicks</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#C0CAF5">-</span><span style="color:#A9B1D6"> Each list item</span></span>
<span class="line"><span style="color:#C0CAF5">-</span><span style="color:#A9B1D6"> Gets its own click</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#0DB9D7">VClicks</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#0DB9D7">VClick</span><span style="color:#BB9AF7"> order</span><span style="color:#89DDFF">=</span><span style="color:#7DCFFF">{</span><span style="color:#FF9E64">3</span><span style="color:#7DCFFF">}</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#A9B1D6">Explicit order (appears third)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#0DB9D7">VClick</span><span style="color:#BB9AF7"> hide</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#A9B1D6">This disappears on click</span></span></code><button type="button" class="copy" data-code="<VClick />
Content appears on click

<VClicks>
- Each list item
- Gets its own click
</VClicks>

<VClick order={3} />
Explicit order (appears third)

<VClick hide />
This disappears on click" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h1 id="custom-components">Custom Components</h1>
<p>Interactive React components work in slides!</p>
<hr/>
<h2 id="context-window-visualizer">Context Window Visualizer<a class="heading-link" aria-label="Link to section" href="#context-window-visualizer"><span class="heading-link-icon">#</span></a></h2>
<p>This is a custom React component rendered inside a slide:</p>
<astro-island uid="wMNSb" prefix="r42" component-url="/_astro/ContextWindowVisualizer.YlsTKjWa.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{}" ssr client="load" opts="{&quot;name&quot;:&quot;ContextWindowVisualizer&quot;,&quot;value&quot;:true}" await-children><div class="w-full max-w-3xl mx-auto my-8"><div class="rounded-lg overflow-hidden border border-[rgb(var(--color-border))] shadow-2xl"><div class="flex items-center gap-2 px-4 py-3 bg-[rgb(var(--color-card))] border-b border-[rgb(var(--color-border))]"><div class="flex gap-2"><div class="w-3 h-3 rounded-full bg-red-500/80"></div><div class="w-3 h-3 rounded-full bg-yellow-500/80"></div><div class="w-3 h-3 rounded-full bg-green-500/80"></div></div><div class="flex-1 text-center"><span class="text-sm text-[rgb(var(--color-text-base))] opacity-60 font-mono">context-window-demo</span></div><button class="text-xs px-2 py-1 rounded border border-[rgb(var(--color-border))]
                       text-[rgb(var(--color-text-base))] opacity-60 hover:opacity-100
                       hover:border-[rgb(var(--color-accent))] transition-all">Reset</button></div><div class="bg-[rgb(var(--color-fill))] font-mono text-sm"><div class="px-4 py-3 border-b border-[rgb(var(--color-border))]"><div class="flex items-center justify-between mb-2"><span class="text-[rgb(var(--color-accent))]">CONTEXT WINDOW</span><span class="text-[rgb(var(--color-text-base))] opacity-70">3.1k<!-- --> / <!-- -->200.0k<!-- --> tokens (<!-- -->1.6<!-- -->%)</span></div><div class="h-2 bg-[rgb(var(--color-card))] rounded-full overflow-hidden"><div class="h-full bg-[rgb(var(--color-accent))] transition-all duration-300" style="width:1.55%"></div></div><div class="flex justify-between mt-1 text-xs text-[rgb(var(--color-text-base))] opacity-50"><span>Used: <!-- -->1.6<!-- -->%</span><span>Remaining: <!-- -->98.5<!-- -->%</span></div></div><div class="p-4 max-h-80 overflow-y-auto"><div class="border border-[rgb(var(--color-border))] rounded"><div class="px-3 py-2 bg-[rgb(var(--color-card))] border-b border-[rgb(var(--color-border))] text-xs text-[rgb(var(--color-text-base))] opacity-70">messages: Message[] = [</div><div class="divide-y divide-[rgb(var(--color-border))]"><div class="px-3 py-2 flex items-start gap-3 hover:bg-[rgb(var(--color-card))] transition-colors"><span class="text-[rgb(var(--color-text-base))] opacity-50 w-16 flex-shrink-0">[<!-- -->0<!-- -->]</span><div class="flex-1 min-w-0"><span class="text-purple-400 font-medium">System<!-- -->:</span><span class="text-[rgb(var(--color-text-base))] ml-2 break-words">&quot;<!-- -->System prompt + CLAUDE.md<!-- -->&quot;</span></div><span class="text-[rgb(var(--color-text-base))] opacity-50 text-xs flex-shrink-0">3100<!-- --> tok</span></div><div class="px-3 py-2 flex items-center gap-3 text-[rgb(var(--color-accent))]"><span class="opacity-50 w-16 flex-shrink-0">[<!-- -->1<!-- -->]</span><span class="flex items-center"><span class="mr-2">← You are here</span><span class="inline-block w-2 h-4 bg-[rgb(var(--color-accent))] opacity-100 transition-opacity duration-100"></span></span></div></div><div class="px-3 py-2 bg-[rgb(var(--color-card))] border-t border-[rgb(var(--color-border))] text-xs text-[rgb(var(--color-text-base))] opacity-70">]</div></div><div class="mt-4 border border-dashed border-[rgb(var(--color-border))] rounded p-3 text-center"><div class="text-[rgb(var(--color-text-base))] opacity-50 text-xs mb-1">Yesterday&#x27;s session?</div><div class="text-[rgb(var(--color-text-base))] opacity-70">∅ Not in the array. Doesn&#x27;t exist.</div></div></div><form class="border-t border-[rgb(var(--color-border))]"><div class="flex items-center px-4 py-3"><span class="text-[rgb(var(--color-accent))] mr-2">❯</span><input type="text" placeholder="Type a message to see context fill up..." class="flex-1 bg-transparent text-[rgb(var(--color-text-base))] outline-none
                           placeholder:text-[rgb(var(--color-text-base))] placeholder:opacity-30" value=""/><button type="submit" class="ml-2 px-3 py-1 rounded border border-[rgb(var(--color-accent))]
                           text-[rgb(var(--color-accent))] text-sm hover:bg-[rgb(var(--color-accent))]
                           hover:text-[rgb(var(--color-fill))] transition-all">Send</button></div></form></div></div><p class="text-center mt-4 text-sm text-[rgb(var(--color-text-base))] opacity-50">Each message you send adds to the array. The context window is just a sliding array of messages.</p></div><!--astro:end--></astro-island>
<p>Try typing messages to see the context fill up!</p>
<hr/>
<h2 id="code-blocks-work-perfectly">Code Blocks Work Perfectly<a class="heading-link" aria-label="Link to section" href="#code-blocks-work-perfectly"><span class="heading-link-icon">#</span></a></h2>
<p>Here’s a Vue composable example with full syntax highlighting:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ref</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> computed</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useCounter</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">initial</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> count</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initial</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> double</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> computed</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> count</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> *</span><span style="color:#FF9E64"> 2</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> increment</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#C0CAF5">    count</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">++</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">count</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> double</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> increment</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import { ref, computed } from 'vue'

export function useCounter(initial = 0) {
  const count = ref(initial)

  const double = computed(() => count.value * 2)

  function increment() {
    count.value++
  }

  return { count, double, increment }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="magic-move-code-evolution">Magic Move: Code Evolution<a class="heading-link" aria-label="Link to section" href="#magic-move-code-evolution"><span class="heading-link-icon">#</span></a></h2>
<p>Watch code transform with smooth animations (press <strong>→</strong> to advance):</p>
<div class="magic-move-container" data-magic-move> <script type="application/json" data-magic-move-config>{"stepsLz":"NobwRAxg9gJgpmAXJKA7AzgFwAQA9sC82AjGADRgAWAhupUmACoDyAZgKoD6ArAGwAyAEU4ApdAFdKMAEIBZbgGZpxdq0EBBAJYBxALQAnAI4BpBfyicA5oeq8AngBZuUcmExQA1nAxJQKVJjemAzQGMEUUKys6HDBiAAMFNAANlD6DADEAJyCAOwAwoIAHK6saJgAyph2yQiIxBRedgwsHDwCwmKSMvJKKmpaekam5lY29k5QuvFgAL5k4KGBAQzYrpHRsUjcSVCp6cgZ6lnKgryl5VU1dYlgTS1sXHxCohJScorKqho6BiZmFmstkczl0pHmi3KQQYuHWURicV4u32mWk0iy6gAYrkLgErrUkLd7shWk8Oq9uh8+t9Bn8RoDxiCpgAmOYLfzLOJgNYReFbRC5ZFpTLHU7nChlPHVAkJRpwZokx7tF5dd69L4DX7DAFjYGTXQKNmQgLQ5AEOGbOJFIUHMAZIo5QSYzG4yrSm5yhVMJXPTpvHqffo/Ib/UZAiaghxGjmm7kWhFILI2kUnYhnV34j13eUPNq+ilqwM0rWhhl60HcaNLWOkXmWpDEW4pYWHZ1ZACivCjEsu7sJntzZJV/qpGuDdJ14aZunOEJjK2QAB1UPH+cQGtmvaTlX7Keqg7TtWHGfqcbMALoUZKaVBwABy4gAtgAjOD6dBIVjUZIxCjPyyZMQ1DEM+zLimArAAYc1BZM+xAwOBmCUHAj73tQqEMO4Hh2FMqCaJYlDBHO0DwCEaBYHghAkMuoQUXYVGshQNB0AwzCYgoj4AF6Yrw4gKPkqDSIIAAKAAOIjsHeACK8DsNoFSifExi8LwIj8MkjB2MQ4jxDAWScMQcAzBQWHeB+iB+NWC7+Fgq5xE2ewtnaOQFMUGZ9vUA6Knm5KqgG1KaiG9K6hGUwzMRULWTyYAbAmiA7CgKKHKKabgZKbrXP2m6DjuBb+WOh6liF07guyVlcrCdZxUiiVORkaIYti7mZbK2XeUOu6FgF45HmWoW6KyEUmlFdlIIKtW2kcqbpj2UotUSObtblfmjgeJbBVO+qGkNnIMOaVX8taE2ZA6ghOi6s0ZTKC1bj6vkjvuxZBZOJ6RlWkVctFsX8kmx3JdNaW9vNXnej5w57kWgUTse5ZTJWO01qN9QOUldptp23YQUD10g9u+YrY9UO9cV+qzmVH0MMuSPriDbEcdxvH8YJIniZJMlwHJClKSpakaVpOl6QZRm6Ge5PDVytHhDFfJxMQzLJocLmFCUl2Zg2tPsVxPF8QJQliRJ0myfJinKap6madpun6YZ8S6CUCMjQdsvjc2k0pTNWNzTjbVgHTWuM7rLMG+znMmzz5v81bQu21k73iwwzROw2R2u6i6JYjiqseTdrGawzOvM/rbNG1zpu8xbAvW8LjZx7tyBfTLDa/an/1is13vEr7efa0zeus4bHPG9zZt85bgs22CpXGnXYD7dL9aIMyKN1ad53t1mnd+/nvdB8Xg+l+Ho+V9HYKDWLM8NwvzIbi3dru4DXsb4tXf0z3gdFwPofD+Xkfj9X23n1jIxeecVmTyz+mjTEHYuzryypvbuAdC79xDkPMuEcx5V1tsQKMDsuRUyTovBQGtX6IL7sHEuYcR4VyjhPYg8NLxgGvLeB8L43zmS/D+OAf4oJ2iAiBMCpQeEZBgnBBCrgkIoTQhhZAWEcK6DwgRIi5NSLIElpRIgxAaLkRwPRIgzJlzLlYOIVAEBMCaDQNgagMAYAAApqCIGwKgJ8r59BkGwM+BxTjWH6AAJTYBAMufQsRxD6FQJY7AABqdxy5ZiuGYvQZAolMCCH0MYbguhxCCAAO4wAAG7oFYKYCoUlHzMAAErMgcHAQwAArbQnFdA1P4LgO83AynsFEtIAA6oYAAWs+YybhPBmV8NPWMkskbL0mkrNyWcWobk7nje6ENuqFQ2q9MKtdYyXziglW+U025zI7s/JZ4MuoFXWi9WGYItnWUqiA/kNV9kNQzrA1qiy7pnPymtZ6MN+pnzGY7B5cQXaOTdgDN5Oclr4wepDHqRVNqggAYCrkc9vpWgVnaVezpIW40+Z1b5T1oZ9WnDgwBQL0WJkxQc1KuKfanIJatIlxNEVw1uVyWswKGxTMyOjGBRyn63TBoywm8L1nXLJiiymK4CE0x9lvN+SDyH70oT/DBJ9RZStUdo6m4D9kzJVp7K6dQFnPwVaQ3en9UGH2oX/W29tyWfWpqC1GNKPbpTVu8s1CCC5kL3l/NBR8aHC1jrghO1MU5grTo1TORrPVQpfv7X1lqUEHyob/TBYJwqOtWNTZuUbW60oFXA71JDk0f1Taq9Bx9aFT3nKipGS9qXYounG7OxCk07wrRQ7+1bg1YIBfW3NBDr7UvvnS+BZau3IJ7YG21mbiDIqHcgYBlLF56oLZA6BmMPXtvlT66dyqA02ozSfbB7LpWNqIT7JJKS0kZOyXkgpRSSnlMqdUupDSmktLaR07pfSBlgnhjmpcMquWLwcCDW9qT0mZJyfkwpChimlIqVU2p9TGnNNae0zpPT+lYMlcuiCxjTHmLA2u5kezN31XTk1YtXqvTQfvXBp9iHkNvrQ5+zDP6cP/vw2CTVRGdn8gUNe/Z476MJqY7Bx9CGX0offehr9WHf24YA1gh1WqwBWJgEjBQkGIEZFyOodQzI6NtuBje5JMGH3wefUh19qGP0Ye/dhv9eHAPEFDSBsANi9MurqhiISmJKySag9Z5jsn7Psac0p7jbm1P8aXhe5A1A9ORtde2eIWJeCGt3ZZzu0nbOsfkxx5zymePufUwNOt5UGDIAIQofNrqW0TufkVljcmHMKc4y5lTvGPO2zASluMBCHA8sLe67GgqGAdai2xxzimuOudU3xwDzIl11eQF4lxSMHA32o/EQQ6I8htcYxFmTdmFs9fK/F1bg2Bpkq0xQMbAXJqtbC1Zu9l2SvdbK3FlbA3quUZG8JuIDgMt1QkxZ4553vvFa6zFpbfXKuJfW4RrbYBnx7ea3VLLOW8vTZLXDmznXouLd6xVhLa2huCcxw18D3AJtYsdDiz7hWLsI/JzdgH/WqtJc00JpG3ADuuuh/l2Hs3Odk+u/95bfO0dDe81pnbb5hcbtdUdk7saJczcSdL+bpXYvy9RzTg02atM+OF5D6Z6hguhZh3rsAc2rtG+R1T+71WFC1YpvXYXuPwWHMd8TqX8OZdu8p3doH/GFCDsx+AAhvBmfZDt06B3uuQ/67D4bv7xuUfU4e6Jkb+DwO8FNSTyLrvc/u6j/zwD+mRtBMwCE8jjdEC8A13VF55mM+eS+6TnPSPI+A7r7bBQwGtNg6QLl6lQW09ndDwPqvQ/bsj8VwaDHvvtNI14AHzI+R4j5CxOnonDHF+V9+yv3npvC90631PgUye58hYX1npfl+Ker4V2bhQgvMcRKRlyFFxXlZ1bV7ykwN2X0/2vwLy92VyFwIVyE71t3t1f2d0gI/x5xN1gP43GxG2x0QLE2owPyPxf3Z3awwMR2gOwM91wJ93jlA0AIMw52zygKwPz1oMAwcDjy31iUQKo1dWfxP0fkz3QNYMwLlw4Ojy4M2y3xLzXVyBqhYPfyoPYI92kNtgcBwQYSYXvGcTYU/G/F/CxyET4VAjSiEREXgkQmQlQjvHQjqCGWwlwnwkInehURshwHwA0S0TCGwF0WwH0VQEMRIzMQsR0zsU8X0NcXcSiO8T8QCVQCbxb3CSiWfBiQMRMW0WwAkEfCogiNwDcTsB8V8PQD2DgAADpUhLAbFci/EAB6eo7AQ0JiWgBJMAdgaQdgTiAACVyCgCknEE0HUi6REDvA8FwAcAAE0KhGA4AHBtAejLAslHwukej2xmRmBnwpj2Asl2ApIpJ1wpJxFhkfALItMJkCEn88hlY3ly8coYUVkLlfkSV9QLcEDGcx0IVyChUOo8omUiYEUNkbkw1kB7k10nlqNu8ddT8E0GV/jRU1krl/lQdACvig9wC8VhUES4UkS/lpxZCGDZ4kYbcTpQC0D4SCZcTLl8T9QnsPi1099JsH5jVRDKTYVVkaTXiKwRtOU11GxqU+Ud1YSsS/iqTOSXiSZQRN8iT5C285VJ1O134Z0VVe0g07URYRtLjwM5ZZ8bjZlg8+9FTt5lSj1rV011UJ4/979nV0Si1DSE1zVy0VTj0LSa0Q0RtE4dTSTDhoS0CnTD1/VzS1V3SsF3jMcH8vM7SpsRCz9kAAzTSgy00Qz+1J4Rs0U28m1DMPsHSO0TSlUkyq11SF0eCiSH9R1DNxcRT90p1EyrVky+0NTF0RtV1MzkDeUoEMZ/SD06zK01T50z16TMc5Sr5r1lCL9VDJD1DR8gNi9W8r5mCKDxDJy89pz19iAZSZ4jETEwj5zQEBCu9aMYTYyIDlzucpza91y78yy9MiCxdvjcz+8JzzzVzLyzdiBrSiSdM9MDN9ljNTMe9qzxyfsVya8193z4DMc/NGs3tMghC0CXcJDXzwKHtktQTt9GsfS7R8ceJCcTzwszzZdkLv9UL6CZ4Gc10mtm1ySfjz8QKXywKSLgdSyL49tk8qz8Knz6KiLGKb9gdCSZ5Vd0gxtgDJotcXIELKCGLh8mKkshyt8XtwMHBYLDgczMSuKuceKZK+KksJ8GS28IdoyWT40CKVDpKv8dL0d8CcdqUcLctJLCKI8LKcD1trzyLhdk81KgKlyzKtLnLOChtPzWKCERcjKHLfKnKYCAqBpIKt8hL1dqVxLTtaK39ny/KoqNDzcRsrcQqsKU9UCUqxCIrq9tKXKx8yLtl/cwrCrELQLSrorY8RsE9S8n9U8yDHzgLNLIqaDMqi90KRzqp7jUruLuqpCZyG90LkjQkd92zfSjy7jTK0rRq1yf89KIyd88r4KaqpL0qerxrNzYw0tE8mS7QSDj9wqlqSr/Leq3LKrEDWqCqOqfLLqr89r19f8RsADEDRKySzo2cnqK8RqrqMrxrYqbzEDZrnI2rhDWS4yiqXrqCxr188D0KCDwNcg7y6ozr2r1LOrw9ga3qzd9s5ymDFqgbXqkaiaWLYw+D0aDyUD59trHKCbKaHsHABLYwBr+RFCQZOjui+iBihiRixiJjpjZj5jFjljVj1jNjtjdj9jDjiApJdAtCSbEDxpO4+bej+jBjhjkhRjxjJiZi5iFiliVi1iNitidi9iDijiVa1qt9tSFDNr9S8LYahqOiujtbBa9aDbRbjaJazbpbLa5abbFblaHADqKU28ihMbA97Tcbn4taBbdbhbDaxaTbJbzaZarb5bbalaVbbrrJciSTfyoT5rCrk6dahb9aRajbxbTapaLbZbraFa7aIdUSCEigVK74HzE6vQq6fa07/aG6s7g6W687w6VawaZ4MyF4ig8qvLOLNavaU6a6/b67M6g7m7c6w67amdO7wMHRqqAaGBB7U7a706A7G7s6Q7W787laRcRtvyCEshk9/yzNjzYaE1z71666M7A6m6c7Q626C7uBqbrJoLwMsg464Loa0Df7fb/7r6x6d6QGH7dBFARtwS28sgy7XVsaYaTKfZEHh7N7AHb6J696wH5KiTFLGT6bfq15K7V7q6kGr7R7t7gH76p7uAHbwboHIT7yMTvKB7WGh7L6R6t6gG77J796o6uQvTGSe6MhCGEHxGL6N6AGb7x7d7QHH6i6uQcroHNr4GWH+a2GyHtHUHuG5GwGgrOa9yfpfoV6LGJGtGUGuHZHqHH6Z7xlyJyjqZ4hk81HzHvbNHkHOGZGqH9GZxwyt8KigmVGl7v7eaNG/6OHpHKG9GMGy8Rtqigm8qP7ALl6k70n2GpGKHdH0Gp6O8RsoH+S5V9UzHT7kBSHJHyGdG0GeG7beAObi6nxqZdTDNQnWnPa3GInMmqnum7HlaYF0LjHGnGHFYWn+6z7ymrHPHomcnan+HgqdSNyT61m2mNmOnrGvGYncmFGGBGjmihmVGRduAshchBAFqSHTmPGonsmanenDHL1ZUKzXHwmMnKmunbGfGZx7YdCbw9DvF2EjCuETDAJgJzDBFMgrCxETJbCpFHDZEXDFE5hzwgA===","stepCount":4,"lineNumbers":false,"duration":800,"stagger":1}</script> <!-- Static fallback: first step for non-presentation view --> <div class="magic-move-fallback"><pre class="shiki tokyo-night" style="background-color:#1a1b26;color:#a9b1d6" tabindex="0"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> x</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 1</span></span></code></pre></div> </div>
<p>Each arrow press animates the code to its next state!</p>
<hr/>
<h2 id="mermaid-diagrams">Mermaid Diagrams<a class="heading-link" aria-label="Link to section" href="#mermaid-diagrams"><span class="heading-link-icon">#</span></a></h2>
<p>Flowcharts render beautifully in slides:</p>
<p><svg id="mermaid-0" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:1222.859375px" viewBox="0 0 1222.859375 253.03125" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-0 .cluster-label text{fill:#F9FFFE;}#mermaid-0 .cluster-label span{color:#F9FFFE;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#ccc;color:#ccc;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-0 .arrowheadPath{fill:lightgrey;}#mermaid-0 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-0 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-0 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-0 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-0 .cluster text{fill:#F9FFFE;}#mermaid-0 .cluster span{color:#F9FFFE;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-0 .icon-shape rect,#mermaid-0 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-0_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M154.703,126.516L158.87,126.516C163.036,126.516,171.37,126.516,179.036,126.516C186.703,126.516,193.703,126.516,197.203,126.516L200.703,126.516" id="L_A_B_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_B_0" data-points="W3sieCI6MTU0LjcwMzEyNSwieSI6MTI2LjUxNTYyNX0seyJ4IjoxNzkuNzAzMTI1LCJ5IjoxMjYuNTE1NjI1fSx7IngiOjIwNC43MDMxMjUsInkiOjEyNi41MTU2MjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M412.383,97.165L423.851,93.39C435.318,89.615,458.253,82.065,475.629,78.29C493.005,74.516,504.823,74.516,510.732,74.516L516.641,74.516" id="L_B_C_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_C_0" data-points="W3sieCI6NDEyLjM4MzI4MTA4NzIxNTQsInkiOjk3LjE2NDUzMTA4NzIxNTM3fSx7IngiOjQ4MS4xODc1LCJ5Ijo3NC41MTU2MjV9LHsieCI6NTIwLjY0MDYyNSwieSI6NzQuNTE1NjI1fV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M412.383,155.867L423.851,159.642C435.318,163.416,458.253,170.966,481.247,174.741C504.242,178.516,527.297,178.516,538.824,178.516L550.352,178.516" id="L_B_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_D_0" data-points="W3sieCI6NDEyLjM4MzI4MTA4NzIxNTQsInkiOjE1NS44NjY3MTg5MTI3ODQ2NX0seyJ4Ijo0ODEuMTg3NSwieSI6MTc4LjUxNTYyNX0seyJ4Ijo1NTQuMzUxNTYyNSwieSI6MTc4LjUxNTYyNX1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M754.031,74.516L758.198,74.516C762.365,74.516,770.698,74.516,778.365,74.516C786.031,74.516,793.031,74.516,796.531,74.516L800.031,74.516" id="L_C_E_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_E_0" data-points="W3sieCI6NzU0LjAzMTI1LCJ5Ijo3NC41MTU2MjV9LHsieCI6Nzc5LjAzMTI1LCJ5Ijo3NC41MTU2MjV9LHsieCI6ODA0LjAzMTI1LCJ5Ijo3NC41MTU2MjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M931.469,74.516L935.635,74.516C939.802,74.516,948.135,74.516,955.802,74.516C963.469,74.516,970.469,74.516,973.969,74.516L977.469,74.516" id="L_E_F_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_E_F_0" data-points="W3sieCI6OTMxLjQ2ODc1LCJ5Ijo3NC41MTU2MjV9LHsieCI6OTU2LjQ2ODc1LCJ5Ijo3NC41MTU2MjV9LHsieCI6OTgxLjQ2ODc1LCJ5Ijo3NC41MTU2MjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_A_B_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(481.1875, 74.515625)"><g class="label" data-id="L_B_C_0" transform="translate(-14.453125, -12)"><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Yes</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(481.1875, 178.515625)"><g class="label" data-id="L_B_D_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>No</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C_E_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_E_F_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-0" transform="translate(81.3515625, 126.515625)"><rect class="basic label-container" style="" x="-73.3515625" y="-27" width="146.703125" height="54"></rect><g class="label" style="" transform="translate(-43.3515625, -12)"><rect></rect><foreignObject width="86.703125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Blog Post</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B-1" transform="translate(323.21875, 126.515625)"><polygon points="118.515625,0 237.03125,-118.515625 118.515625,-237.03125 0,-118.515625" class="label-container" transform="translate(-118.015625, 118.515625)"></polygon><g class="label" style="" transform="translate(-91.515625, -12)"><rect></rect><foreignObject width="183.03125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>presentation: true?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C-3" transform="translate(637.3359375, 74.515625)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Show Toggle Button</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-D-5" transform="translate(637.3359375, 178.515625)"><rect class="basic label-container" style="" x="-82.984375" y="-27" width="165.96875" height="54"></rect><g class="label" style="" transform="translate(-52.984375, -12)"><rect></rect><foreignObject width="105.96875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Normal Post</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-E-7" transform="translate(867.75, 74.515625)"><rect class="basic label-container" style="" x="-63.71875" y="-27" width="127.4375" height="54"></rect><g class="label" style="" transform="translate(-33.71875, -12)"><rect></rect><foreignObject width="67.4375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Press P</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-F-9" transform="translate(1098.1640625, 74.515625)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Fullscreen Slides!</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<hr/>
<h2 id="animated-diagrams">Animated Diagrams<a class="heading-link" aria-label="Link to section" href="#animated-diagrams"><span class="heading-link-icon">#</span></a></h2>
<p>Interactive diagrams with self-contained animations:</p>
<div class="subagent-diagram-container astro-tpygpejy" data-subagent-diagram> <!-- Animated React component (shown in presentation mode via CSS) --> <!-- Using client:load instead of client:visible because CSS hides this with display:none --> <!-- until presentation mode activates, which prevents IntersectionObserver from firing --> <astro-island uid="1P9sOl" prefix="r34" component-url="/_astro/SubagentDiagramRenderer.DLSSo-ru.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;config&quot;:[0,{&quot;task&quot;:[0,&quot;Find auth files&quot;],&quot;files&quot;:[1,[[0,&quot;Auth.tsx&quot;],[0,&quot;auth.ts&quot;],[0,&quot;authService.ts&quot;]]],&quot;autoStart&quot;:[0,false],&quot;speed&quot;:[0,0.6]}]}" ssr client="load" opts="{&quot;name&quot;:&quot;SubagentDiagramRenderer&quot;,&quot;value&quot;:true}" await-children><div class="subagent-diagram-animated"><svg viewBox="0 0 620 420" class="subagent-diagram-svg-animated"><defs><marker id="arrowhead-animated" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" class="arrowhead-fill"></polygon></marker></defs><g class="agent-node main-agent"><circle cx="100" cy="80" r="45" class="agent-circle main"></circle><text x="100" y="72" text-anchor="middle" class="agent-icon">🤖</text><text x="100" y="95" text-anchor="middle" class="agent-label">Main Agent</text></g><g class="file-tree" transform="translate(340, 50)"><text x="0" y="0" class="tree-header">File Tree</text><line x1="0" y1="10" x2="180" y2="10" class="tree-header-line"></line><g opacity="0.7"><text x="0" y="35" class="tree-node folder ">📁<!-- --> <!-- -->src/</text></g><g opacity="0.7"><text x="16" y="61" class="tree-node folder ">📁<!-- --> <!-- -->components/</text></g><g opacity="0.7"><text x="32" y="87" class="tree-node file ">📄<!-- --> <!-- -->Auth.tsx</text></g><g opacity="0.7"><text x="32" y="113" class="tree-node file ">📄<!-- --> <!-- -->Button.tsx</text></g><g opacity="0.7"><text x="16" y="139" class="tree-node folder ">📁<!-- --> <!-- -->utils/</text></g><g opacity="0.7"><text x="32" y="165" class="tree-node file ">📄<!-- --> <!-- -->auth.ts</text></g><g opacity="0.7"><text x="32" y="191" class="tree-node file ">📄<!-- --> <!-- -->helpers.ts</text></g><g opacity="0.7"><text x="16" y="217" class="tree-node folder ">📁<!-- --> <!-- -->services/</text></g><g opacity="0.7"><text x="32" y="243" class="tree-node file ">📄<!-- --> <!-- -->authService.ts</text></g></g></svg><button class="subagent-diagram-button" tabindex="0">▶ Start</button></div><!--astro:end--></astro-island> <!-- Static fallback for non-presentation view --> <div class="subagent-diagram-fallback astro-tpygpejy"> <svg viewBox="0 0 600 320" class="subagent-diagram-svg astro-tpygpejy"> <!-- Main Agent --> <g class="agent-group main-agent astro-tpygpejy"> <circle cx="100" cy="80" r="40" class="agent-circle astro-tpygpejy"></circle> <text x="100" y="75" text-anchor="middle" class="agent-icon astro-tpygpejy">🤖</text> <text x="100" y="95" text-anchor="middle" class="agent-label astro-tpygpejy">Main Agent</text> </g> <!-- Explore Subagent --> <g class="agent-group explore-agent astro-tpygpejy"> <circle cx="100" cy="220" r="35" class="subagent-circle astro-tpygpejy"></circle> <text x="100" y="215" text-anchor="middle" class="agent-icon astro-tpygpejy">🔍</text> <text x="100" y="235" text-anchor="middle" class="agent-label astro-tpygpejy">Explore</text> </g> <!-- Delegation Arrow --> <g class="arrow-group astro-tpygpejy"> <path d="M100,120 L100,180" class="arrow-path astro-tpygpejy" marker-end="url(#arrowhead)"></path> <text x="115" y="150" class="arrow-label astro-tpygpejy">delegate</text> </g> <!-- Report Arrow --> <g class="arrow-group astro-tpygpejy"> <path d="M135,200 Q200,150 135,100" class="arrow-path dashed astro-tpygpejy" marker-end="url(#arrowhead)"></path> <text x="180" y="145" class="arrow-label astro-tpygpejy">report</text> </g> <!-- File Tree --> <g class="file-tree astro-tpygpejy" transform="translate(300, 40)"> <text x="0" y="0" class="folder astro-tpygpejy">📁 src/</text> <text x="20" y="30" class="folder astro-tpygpejy">📁 components/</text> <text x="40" y="60" class="file highlight astro-tpygpejy">📄 Auth.tsx</text> <text x="40" y="90" class="file astro-tpygpejy">📄 Button.tsx</text> <text x="20" y="120" class="folder astro-tpygpejy">📁 utils/</text> <text x="40" y="150" class="file highlight astro-tpygpejy">📄 auth.ts</text> <text x="40" y="180" class="file astro-tpygpejy">📄 helpers.ts</text> <text x="20" y="210" class="folder astro-tpygpejy">📁 services/</text> <text x="40" y="240" class="file highlight astro-tpygpejy">📄 authService.ts</text> </g> <!-- Search Arrow --> <g class="arrow-group astro-tpygpejy"> <path d="M145,220 L280,150" class="arrow-path search-arrow astro-tpygpejy" marker-end="url(#arrowhead)"></path> <text x="200" y="200" class="arrow-label astro-tpygpejy">search</text> </g> <!-- Arrow marker definition --> <defs class="astro-tpygpejy"> <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto" class="astro-tpygpejy"> <polygon points="0 0, 10 3.5, 0 7" class="arrowhead-fill astro-tpygpejy"></polygon> </marker> </defs> </svg> <p class="subagent-diagram-caption astro-tpygpejy">
The Explore subagent searches files and reports discovered matches back to the main agent.
</p> </div> </div> 
<p>Click <strong>Start</strong> to see the Explore subagent flow animation!</p>
<hr/>
<h1 id="slide-layouts">Slide Layouts</h1>
<hr/>
<h2 id="available-layouts">Available Layouts<a class="heading-link" aria-label="Link to section" href="#available-layouts"><span class="heading-link-icon">#</span></a></h2>
<p>This feature supports 9 different layout types:</p>

















































<table><thead><tr><th>Layout</th><th>Description</th></tr></thead><tbody><tr><td data-label="Layout"><code>default</code></td><td data-label="Description">Standard centered prose</td></tr><tr><td data-label="Layout"><code>cover</code></td><td data-label="Description">Large title, full-bleed</td></tr><tr><td data-label="Layout"><code>center</code></td><td data-label="Description">Fully centered content</td></tr><tr><td data-label="Layout"><code>two-cols</code></td><td data-label="Description">Two-column split</td></tr><tr><td data-label="Layout"><code>image-left</code></td><td data-label="Description">Image 40%, content 60%</td></tr><tr><td data-label="Layout"><code>image-right</code></td><td data-label="Description">Content 60%, image 40%</td></tr><tr><td data-label="Layout"><code>image</code></td><td data-label="Description">Full-bleed background</td></tr><tr><td data-label="Layout"><code>quote</code></td><td data-label="Description">Prominent blockquote</td></tr><tr><td data-label="Layout"><code>section</code></td><td data-label="Description">Section divider</td></tr><tr><td data-label="Layout"><code>iframe</code></td><td data-label="Description">Embedded website/demo</td></tr></tbody></table>
<hr/>
<h2 id="iframe-layout">Iframe Layout<a class="heading-link" aria-label="Link to section" href="#iframe-layout"><span class="heading-link-icon">#</span></a></h2>
<p>Embed live demos, CodePen, StackBlitz, or videos directly in slides:</p>
<script type="application/json" data-slide-config>{"layout":"iframe","src":"https://stackblitz.com/edit/vitejs-vite-wdjbsx?embed=1&file=src%2FApp.vue&hideExplorer=1","title":"Vue Counter Demo"}</script> <div class="slide-iframe-fallback"><iframe src="https://stackblitz.com/edit/vitejs-vite-wdjbsx?embed=1&file=src%2FApp.vue&hideExplorer=1" title="Vue Counter Demo" class="slide-iframe-blog" loading="lazy" sandbox="allow-scripts allow-forms allow-same-origin allow-popups"></iframe></div>
<p>This is a live StackBlitz embed - fully interactive!</p>
<hr/>
<h2 id="layout-syntax">Layout Syntax<a class="heading-link" aria-label="Link to section" href="#layout-syntax"><span class="heading-link-icon">#</span></a></h2>
<p>In <strong>.md files</strong>, use HTML comments. In <strong>.mdx files</strong>, use components:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="mdx"><code><span class="line"><span style="color:#9ECE6A">{</span><span style="color:#51597D;font-style:italic">/* MDX format */</span><span style="color:#9ECE6A">}</span></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#0DB9D7">Slide</span><span style="color:#BB9AF7"> layout</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">cover</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#89DDFF">#</span><span style="color:#C0CAF5"> My Title</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-weight:bold">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ECE6A">{</span><span style="color:#51597D;font-style:italic">/* .md format */</span><span style="color:#9ECE6A">}</span></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#FF5370">!--slide:{&quot;layout&quot;:&quot;cover&quot;}--&gt;</span></span>
<span class="line"><span style="color:#FF5370">#</span><span style="color:#BB9AF7"> My</span><span style="color:#BB9AF7"> Title</span></span></code><button type="button" class="copy" data-code="{/* MDX format */}
<Slide layout=&#34;cover&#34; />
# My Title

---

{/* .md format */}
<!--slide:{&#34;layout&#34;:&#34;cover&#34;}-->
# My Title" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<aside aria-label="MDX vs MD" class="aside aside-note astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">📝</span> MDX vs MD </p> <section class="aside-body astro-37uy2q7c"> <p>Both file formats support layouts and v-clicks! For <code>.md</code> files use HTML comments, for <code>.mdx</code> files use the <code>Slide</code>, <code>VClick</code>, and <code>VClicks</code> components.</p> </section> </div> </aside> 
<hr/>
<h2 id="layout-properties">Layout Properties<a class="heading-link" aria-label="Link to section" href="#layout-properties"><span class="heading-link-icon">#</span></a></h2>
<p>All layouts accept these properties:</p>

































<table><thead><tr><th>Property</th><th>Description</th></tr></thead><tbody><tr><td data-label="Property"><code>layout</code></td><td data-label="Description">Layout name (required)</td></tr><tr><td data-label="Property"><code>image</code></td><td data-label="Description">Path to image in /public</td></tr><tr><td data-label="Property"><code>backgroundSize</code></td><td data-label="Description">CSS value (default: cover)</td></tr><tr><td data-label="Property"><code>class</code></td><td data-label="Description">Custom CSS class</td></tr><tr><td data-label="Property"><code>src</code></td><td data-label="Description">URL for iframe layout</td></tr><tr><td data-label="Property"><code>title</code></td><td data-label="Description">Accessibility title for iframe</td></tr></tbody></table>
<hr/>
<h2 id="layout-animations">Layout Animations<a class="heading-link" aria-label="Link to section" href="#layout-animations"><span class="heading-link-icon">#</span></a></h2>
<p>Each layout type has its own animation:</p>









































<table><thead><tr><th>Layout</th><th>Animation</th></tr></thead><tbody><tr><td data-label="Layout"><code>default</code></td><td data-label="Animation">Slide</td></tr><tr><td data-label="Layout"><code>center</code></td><td data-label="Animation">Slide</td></tr><tr><td data-label="Layout"><code>two-cols</code></td><td data-label="Animation">Slide</td></tr><tr><td data-label="Layout"><code>cover</code></td><td data-label="Animation"><strong>Fade</strong></td></tr><tr><td data-label="Layout"><code>image</code></td><td data-label="Animation"><strong>Zoom</strong></td></tr><tr><td data-label="Layout"><code>quote</code></td><td data-label="Animation"><strong>Fade</strong></td></tr><tr><td data-label="Layout"><code>section</code></td><td data-label="Animation"><strong>Fade</strong></td></tr><tr><td data-label="Layout"><code>iframe</code></td><td data-label="Animation"><strong>Fade</strong></td></tr></tbody></table>
<hr/>
<h1 id="technical-details">Technical Details</h1>
<hr/>
<h2 id="architecture-overview">Architecture Overview<a class="heading-link" aria-label="Link to section" href="#architecture-overview"><span class="heading-link-icon">#</span></a></h2>
<p><svg id="mermaid-1" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:1561.48828125px" viewBox="0 0 1561.48828125 740" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-1{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1 .error-icon{fill:#a44141;}#mermaid-1 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-1 .edge-thickness-normal{stroke-width:1px;}#mermaid-1 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-1 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-1 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-1 p{margin:0;}#mermaid-1 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-1 .cluster-label text{fill:#F9FFFE;}#mermaid-1 .cluster-label span{color:#F9FFFE;}#mermaid-1 .cluster-label span p{background-color:transparent;}#mermaid-1 .label text,#mermaid-1 span{fill:#ccc;color:#ccc;}#mermaid-1 .node rect,#mermaid-1 .node circle,#mermaid-1 .node ellipse,#mermaid-1 .node polygon,#mermaid-1 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-1 .rough-node .label text,#mermaid-1 .node .label text,#mermaid-1 .image-shape .label,#mermaid-1 .icon-shape .label{text-anchor:middle;}#mermaid-1 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-1 .rough-node .label,#mermaid-1 .node .label,#mermaid-1 .image-shape .label,#mermaid-1 .icon-shape .label{text-align:center;}#mermaid-1 .node.clickable{cursor:pointer;}#mermaid-1 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-1 .arrowheadPath{fill:lightgrey;}#mermaid-1 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-1 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-1 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-1 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-1 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-1 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-1 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-1 .cluster text{fill:#F9FFFE;}#mermaid-1 .cluster span{color:#F9FFFE;}#mermaid-1 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-1 rect.text{fill:none;stroke-width:0;}#mermaid-1 .icon-shape,#mermaid-1 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-1 .icon-shape p,#mermaid-1 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-1 .icon-shape rect,#mermaid-1 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-1 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-1 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-1 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-1_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-1_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-1_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"><g class="cluster" id="Content" data-look="classic"><rect style="" x="8" y="8" width="322.65625" height="441"></rect><g class="cluster-label" transform="translate(135.609375, 8)"><foreignObject width="67.4375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Content</p></span></div></foreignObject></g></g><g class="cluster" id="Layouts" data-look="classic"><rect style="" x="238.9609375" y="628" width="1115.03125" height="104"></rect><g class="cluster-label" transform="translate(762.7578125, 628)"><foreignObject width="67.4375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Layouts</p></span></div></foreignObject></g></g><g class="cluster" id="Frontend" data-look="classic"><rect style="" x="350.65625" y="241" width="1202.83203125" height="337"></rect><g class="cluster-label" transform="translate(913.541015625, 241)"><foreignObject width="77.0625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Frontend</p></span></div></foreignObject></g></g></g><g class="edgePaths"><path d="M1089.504,320L1089.504,324.167C1089.504,328.333,1089.504,336.667,1089.504,344.333C1089.504,352,1089.504,359,1089.504,362.5L1089.504,366" id="L_A_B_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_B_0" data-points="W3sieCI6MTA4OS41MDM5MDYyNSwieSI6MzIwfSx7IngiOjEwODkuNTAzOTA2MjUsInkiOjM0NX0seyJ4IjoxMDg5LjUwMzkwNjI1LCJ5IjozNzB9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M989.29,424L973.825,428.167C958.36,432.333,927.43,440.667,911.965,449C896.5,457.333,896.5,465.667,889.456,473.68C882.413,481.694,868.325,489.388,861.282,493.236L854.238,497.083" id="L_B_C_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_C_0" data-points="W3sieCI6OTg5LjI5MDMzOTU0MzI2OTMsInkiOjQyNH0seyJ4Ijo4OTYuNSwieSI6NDQ5fSx7IngiOjg5Ni41LCJ5Ijo0NzR9LHsieCI6ODUwLjcyNzM4ODgyMjExNTQsInkiOjQ5OX1d" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M1089.504,424L1089.504,428.167C1089.504,432.333,1089.504,440.667,1089.504,449C1089.504,457.333,1089.504,465.667,1089.504,473.333C1089.504,481,1089.504,488,1089.504,491.5L1089.504,495" id="L_B_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_D_0" data-points="W3sieCI6MTA4OS41MDM5MDYyNSwieSI6NDI0fSx7IngiOjEwODkuNTAzOTA2MjUsInkiOjQ0OX0seyJ4IjoxMDg5LjUwMzkwNjI1LCJ5Ijo0NzR9LHsieCI6MTA4OS41MDM5MDYyNSwieSI6NDk5fV0=" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M1196.566,415.395L1229.165,420.996C1261.764,426.596,1326.962,437.798,1359.561,447.566C1392.16,457.333,1392.16,465.667,1392.16,473.333C1392.16,481,1392.16,488,1392.16,491.5L1392.16,495" id="L_B_E_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_E_0" data-points="W3sieCI6MTE5Ni41NjY0MDYyNSwieSI6NDE1LjM5NDYzMDg3MjQ4MzJ9LHsieCI6MTM5Mi4xNjAxNTYyNSwieSI6NDQ5fSx7IngiOjEzOTIuMTYwMTU2MjUsInkiOjQ3NH0seyJ4IjoxMzkyLjE2MDE1NjI1LCJ5Ijo0OTl9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M689.41,540.168L639.618,546.473C589.826,552.779,490.241,565.389,440.449,575.861C390.656,586.333,390.656,594.667,390.656,603C390.656,611.333,390.656,619.667,390.656,627.333C390.656,635,390.656,642,390.656,645.5L390.656,649" id="L_C_F_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_F_0" data-points="W3sieCI6Njg5LjQxMDE1NjI1LCJ5Ijo1NDAuMTY4MDEyNzA4OTIxOX0seyJ4IjozOTAuNjU2MjUsInkiOjU3OH0seyJ4IjozOTAuNjU2MjUsInkiOjYwM30seyJ4IjozOTAuNjU2MjUsInkiOjYyOH0seyJ4IjozOTAuNjU2MjUsInkiOjY1M31d" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M730.221,553L719.253,557.167C708.286,561.333,686.35,569.667,675.382,578C664.414,586.333,664.414,594.667,664.414,603C664.414,611.333,664.414,619.667,664.414,627.333C664.414,635,664.414,642,664.414,645.5L664.414,649" id="L_C_G_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_G_0" data-points="W3sieCI6NzMwLjIyMTIyODk2NjM0NjIsInkiOjU1M30seyJ4Ijo2NjQuNDE0MDYyNSwieSI6NTc4fSx7IngiOjY2NC40MTQwNjI1LCJ5Ijo2MDN9LHsieCI6NjY0LjQxNDA2MjUsInkiOjYyOH0seyJ4Ijo2NjQuNDE0MDYyNSwieSI6NjUzfV0=" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M872.365,553L883.333,557.167C894.3,561.333,916.236,569.667,927.204,578C938.172,586.333,938.172,594.667,938.172,603C938.172,611.333,938.172,619.667,938.172,627.333C938.172,635,938.172,642,938.172,645.5L938.172,649" id="L_C_H_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_H_0" data-points="W3sieCI6ODcyLjM2NDcwODUzMzY1MzgsInkiOjU1M30seyJ4Ijo5MzguMTcxODc1LCJ5Ijo1Nzh9LHsieCI6OTM4LjE3MTg3NSwieSI6NjAzfSx7IngiOjkzOC4xNzE4NzUsInkiOjYyOH0seyJ4Ijo5MzguMTcxODc1LCJ5Ijo2NTN9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M913.176,540.168L962.968,546.473C1012.76,552.779,1112.345,565.389,1162.137,575.861C1211.93,586.333,1211.93,594.667,1211.93,603C1211.93,611.333,1211.93,619.667,1211.93,627.333C1211.93,635,1211.93,642,1211.93,645.5L1211.93,649" id="L_C_I_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_I_0" data-points="W3sieCI6OTEzLjE3NTc4MTI1LCJ5Ijo1NDAuMTY4MDEyNzA4OTIxOX0seyJ4IjoxMjExLjkyOTY4NzUsInkiOjU3OH0seyJ4IjoxMjExLjkyOTY4NzUsInkiOjYwM30seyJ4IjoxMjExLjkyOTY4NzUsInkiOjYyOH0seyJ4IjoxMjExLjkyOTY4NzUsInkiOjY1M31d" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M169.328,87L169.328,91.167C169.328,95.333,169.328,103.667,169.328,111.333C169.328,119,169.328,126,169.328,129.5L169.328,133" id="L_J_K_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_J_K_0" data-points="W3sieCI6MTY5LjMyODEyNSwieSI6ODd9LHsieCI6MTY5LjMyODEyNSwieSI6MTEyfSx7IngiOjE2OS4zMjgxMjUsInkiOjEzN31d" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M169.328,191L169.328,195.167C169.328,199.333,169.328,207.667,169.328,216C169.328,224.333,169.328,232.667,169.328,240.333C169.328,248,169.328,255,169.328,258.5L169.328,262" id="L_K_L_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_K_L_0" data-points="W3sieCI6MTY5LjMyODEyNSwieSI6MTkxfSx7IngiOjE2OS4zMjgxMjUsInkiOjIxNn0seyJ4IjoxNjkuMzI4MTI1LCJ5IjoyNDF9LHsieCI6MTY5LjMyODEyNSwieSI6MjY2fV0=" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M169.328,320L169.328,324.167C169.328,328.333,169.328,336.667,169.328,344.333C169.328,352,169.328,359,169.328,362.5L169.328,366" id="L_L_M_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_L_M_0" data-points="W3sieCI6MTY5LjMyODEyNSwieSI6MzIwfSx7IngiOjE2OS4zMjgxMjUsInkiOjM0NX0seyJ4IjoxNjkuMzI4MTI1LCJ5IjozNzB9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M169.328,424L169.328,428.167C169.328,432.333,169.328,440.667,213.456,449C257.585,457.333,345.841,465.667,431.861,475.766C517.882,485.865,601.666,497.73,643.558,503.662L685.45,509.595" id="L_M_C_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_M_C_0" data-points="W3sieCI6MTY5LjMyODEyNSwieSI6NDI0fSx7IngiOjE2OS4zMjgxMjUsInkiOjQ0OX0seyJ4Ijo0MzQuMDk3NjU2MjUsInkiOjQ3NH0seyJ4Ijo2ODkuNDEwMTU2MjUsInkiOjUxMC4xNTU4MjY0NzE3NzcyfV0=" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_A_B_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B_C_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B_D_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B_E_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C_F_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C_G_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C_H_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C_I_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_J_K_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_K_L_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_L_M_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_M_C_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-0" transform="translate(1089.50390625, 293)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>PresentationToggle</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B-1" transform="translate(1089.50390625, 397)"><rect class="basic label-container" style="" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>PresentationMode</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C-3" transform="translate(801.29296875, 526)"><rect class="basic label-container" style="" x="-111.8828125" y="-27" width="223.765625" height="54"></rect><g class="label" style="" transform="translate(-81.8828125, -12)"><rect></rect><foreignObject width="163.765625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>PresentationSlide</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-D-5" transform="translate(1089.50390625, 526)"><rect class="basic label-container" style="" x="-126.328125" y="-27" width="252.65625" height="54"></rect><g class="label" style="" transform="translate(-96.328125, -12)"><rect></rect><foreignObject width="192.65625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>PresentationControls</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-E-7" transform="translate(1392.16015625, 526)"><rect class="basic label-container" style="" x="-126.328125" y="-27" width="252.65625" height="54"></rect><g class="label" style="" transform="translate(-96.328125, -12)"><rect></rect><foreignObject width="192.65625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>PresentationProgress</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-F-9" transform="translate(390.65625, 680)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>SlideLayoutDefault</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-G-11" transform="translate(664.4140625, 680)"><rect class="basic label-container" style="" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>SlideLayoutCover</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-H-13" transform="translate(938.171875, 680)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>SlideLayoutTwoCols</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-I-15" transform="translate(1211.9296875, 680)"><rect class="basic label-container" style="" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>... more layouts</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-J-16" transform="translate(169.328125, 60)"><rect class="basic label-container" style="" x="-73.3515625" y="-27" width="146.703125" height="54"></rect><g class="label" style="" transform="translate(-43.3515625, -12)"><rect></rect><foreignObject width="86.703125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Blog Post</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-K-17" transform="translate(169.328125, 164)"><rect class="basic label-container" style="" x="-92.6171875" y="-27" width="185.234375" height="54"></rect><g class="label" style="" transform="translate(-62.6171875, -12)"><rect></rect><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Compiled HTML</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-L-19" transform="translate(169.328125, 293)"><rect class="basic label-container" style="" x="-126.328125" y="-27" width="252.65625" height="54"></rect><g class="label" style="" transform="translate(-96.328125, -12)"><rect></rect><foreignObject width="192.65625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Parse slide comments</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-M-21" transform="translate(169.328125, 397)"><rect class="basic label-container" style="" x="-102.25" y="-27" width="204.5" height="54"></rect><g class="label" style="" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>SlideData Array</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<hr/>
<h2 id="tips-for-great-slides">Tips for Great Slides<a class="heading-link" aria-label="Link to section" href="#tips-for-great-slides"><span class="heading-link-icon">#</span></a></h2>
<aside aria-label="Best Practices" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> Best Practices </p> <section class="aside-body astro-37uy2q7c"> <ol>
<li><strong>Keep slides focused</strong> - One idea per slide</li>
<li><strong>Use headings</strong> - They become slide titles</li>
<li><strong>Leverage layouts</strong> - Pick the right layout for content</li>
<li><strong>Use v-clicks</strong> - Reveal complex info step-by-step</li>
<li><strong>Test navigation</strong> - Make sure flow makes sense</li>
</ol> </section> </div> </aside> 
<h3 id="content-length">Content Length<a class="heading-link" aria-label="Link to section" href="#content-length"><span class="heading-link-icon">#</span></a></h3>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ul>
<li>Short slides work best</li>
<li>If content overflows, it scrolls within the slide</li>
<li>But try to keep each slide digestible</li>
<li>Use v-clicks to break up longer content</li>
</ul><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<hr/>
<h2 id="accessibility-features">Accessibility Features<a class="heading-link" aria-label="Link to section" href="#accessibility-features"><span class="heading-link-icon">#</span></a></h2>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ul>
<li><strong>Focus trap</strong> - Tab stays within the modal</li>
<li><strong>ARIA live region</strong> - Announces “Slide X of Y, Step N of M”</li>
<li><strong>Escape to exit</strong> - Standard modal behavior</li>
<li><strong>Keyboard navigation</strong> - No mouse required</li>
<li><strong>Theme aware</strong> - Respects light/dark mode</li>
<li><strong>Reduced motion</strong> - V-click respects <code>prefers-reduced-motion</code></li>
</ul><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<hr/>
<h2 id="speaker-notes--presenter-view">Speaker Notes &amp; Presenter View<a class="heading-link" aria-label="Link to section" href="#speaker-notes--presenter-view"><span class="heading-link-icon">#</span></a></h2>
<p>Press <strong>N</strong> to open the presenter view popup!</p>
<script type="application/json" data-vclick-marker="v-click">{}</script>
<p>The presenter view shows:</p>
<script type="application/json" data-vclick-marker="v-clicks-start">{}</script><ul>
<li>Current and next slide previews</li>
<li>Speaker notes with click-step highlighting</li>
<li>A timer you can start/pause/reset</li>
<li>Navigation controls</li>
</ul><script type="application/json" data-vclick-marker="v-clicks-end">{}</script>
<script type="application/json" data-slide-note="true">""</script>
<hr/>
<h2 id="notes-with-click-markers">Notes with Click Markers<a class="heading-link" aria-label="Link to section" href="#notes-with-click-markers"><span class="heading-link-icon">#</span></a></h2>
<p>Notes can reveal progressively with your click steps:</p>
<script type="application/json" data-vclick-marker="v-click">{}</script>
<p><strong>Step 1:</strong> Define the problem</p>
<script type="application/json" data-vclick-marker="v-click">{}</script>
<p><strong>Step 2:</strong> Explore solutions</p>
<script type="application/json" data-vclick-marker="v-click">{}</script>
<p><strong>Step 3:</strong> Implement and ship!</p>
<script type="application/json" data-slide-note="true">""</script>
<hr/>
<h1 id="thank-you">Thank You!</h1>
<p>Press <strong>Escape</strong> to exit or continue with arrow keys</p>
<hr/>
<h2 id="quick-reference">Quick Reference<a class="heading-link" aria-label="Link to section" href="#quick-reference"><span class="heading-link-icon">#</span></a></h2>
<p><strong>File format trade-offs:</strong></p>


























<table><thead><tr><th>Format</th><th>Custom Components</th><th>Layouts</th><th>V-Click</th><th>Syntax</th></tr></thead><tbody><tr><td data-label="Format"><code>.mdx</code></td><td data-label="Custom Components">Yes</td><td data-label="Layouts">Yes</td><td data-label="V-Click">Yes</td><td data-label="Syntax">Components</td></tr><tr><td data-label="Format"><code>.md</code></td><td data-label="Custom Components">No</td><td data-label="Layouts">Yes</td><td data-label="V-Click">Yes</td><td data-label="Syntax">HTML comments</td></tr></tbody></table>
<script type="application/json" data-vclick-marker="v-click">{}</script>
<p>Press <strong>Escape</strong> to exit presentation mode!</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 3 21 3 21 9"></polyline>
          <polyline points="9 21 3 21 3 15"></polyline>
          <line x1="21" y1="3" x2="14" y2="10"></line>
          <line x1="3" y1="21" x2="10" y2="14"></line>
        </svg>
        <span>Fullscreen</span>
      `,n.appendChild(o);const d=m=>{m.stopPropagation(),c.innerHTML="";const i=t.cloneNode(!0),s=t.id,w=`-modal-${Date.now()}`,u=`${s}${w}`;i.setAttribute("id",u);const E=new Map;i.querySelectorAll("[id]").forEach(l=>{if(l===i)return;const a=l.getAttribute("id"),h=a+w;E.set(a,h),l.setAttribute("id",h)});let r=i.innerHTML;E.forEach((l,a)=>{r=r.replace(new RegExp(`url\\(#${a}\\)`,"g"),`url(#${l})`),r=r.replace(new RegExp(`href="#${a}"`,"g"),`href="#${l}"`)}),r=r.replace(new RegExp(`#${s}([^_\\w-])`,"g"),`#${u}$1`),r=r.replace(new RegExp(`#${s}\\{`,"g"),`#${u}{`),i.innerHTML=r,i.removeAttribute("style");const y=i.getAttribute("viewBox");if(y){const[,,l,a]=y.split(" ").map(Number);i.setAttribute("width",String(l)),i.setAttribute("height",String(a))}c.appendChild(i),e.showModal(),f.focus()};n.addEventListener("click",d),n.addEventListener("keydown",m=>{(m.key==="Enter"||m.key===" ")&&(m.preventDefault(),d(m))})}),f?.addEventListener("click",v),e?.addEventListener("click",t=>{const o=e?.querySelector(".mermaid-modal-content")?.getBoundingClientRect(),d=t;o&&(d.clientX<o.left||d.clientX>o.right||d.clientY<o.top||d.clientY>o.bottom)&&v()}),e.addEventListener("close",b)}function v(){const e=document.getElementById("mermaid-modal");e&&e.open&&e.close()}function b(){const c=document.getElementById("mermaid-modal")?.querySelector(".mermaid-modal-diagram");c&&(c.innerHTML="")}document.readyState==="loading"?document.addEventListener("DOMContentLoaded",g):g();document.addEventListener("astro:page-load",()=>{p.clear(),g()});</script> <astro-island uid="Z1mkpaA" prefix="r30" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="PresentationMode" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;articleSelector&quot;:[0,&quot;#article&quot;],&quot;title&quot;:[0,&quot;Presentation Mode: Turn Your Blog Posts into Slides&quot;],&quot;slug&quot;:[0,&quot;presentation-mode-demo&quot;],&quot;conference&quot;:[0]}" ssr client="load" opts="{&quot;name&quot;:&quot;PresentationMode&quot;,&quot;value&quot;:true}" await-children><button type="button" aria-label="Enter presentation mode (P)" class="fixed bottom-20 right-4 flex items-center gap-2 rounded-full bg-skin-accent px-4 py-2 text-skin-inverted shadow-lg transition-all duration-300 hover:opacity-90 hover:scale-105 opacity-100"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-presentation h-5 w-5"><path d="M2 3h20"></path><path d="M21 3v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V3"></path><path d="m7 21 5-5 5 5"></path></svg><span class="text-sm font-medium">(P)</span></button><!--astro:end--></astro-island> <div id="cta-follow" class="notification-container fixed bottom-24 left-0 z-50 max-w-sm -translate-x-full opacity-0 transition-all duration-500 ease-out astro-vj4tpspi"> <div class="mx-4 transform rounded-lg border-l-4 border-skin-accent bg-skin-card p-6 shadow-xl transition-transform duration-200 hover:scale-[1.02] astro-vj4tpspi"> <div class="flex flex-col gap-4 astro-vj4tpspi"> <div class="flex items-center gap-3 astro-vj4tpspi"> <div class="rounded-full bg-skin-accent bg-opacity-10 p-2 astro-vj4tpspi"> <svg class="h-6 w-6 text-skin-accent astro-vj4tpspi" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg> </div> <h3 class="text-xl font-bold text-skin-accent astro-vj4tpspi">Stay Updated!</h3> </div> <div class="space-y-2 astro-vj4tpspi"> <p class="text-base leading-relaxed text-skin-base astro-vj4tpspi">
Subscribe to my newsletter for more TypeScript, Vue, and web dev
              insights directly in your inbox.
</p> <ul class="ml-1 list-inside list-disc space-y-1 text-sm text-skin-base astro-vj4tpspi"> <li class="astro-vj4tpspi">Background information about the articles</li> <li class="astro-vj4tpspi">
Weekly Summary of all the interesting blog posts that I read
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_presentation-mode-demo" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="presentation-mode-demo" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/demo/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">demo</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/presentation/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">presentation</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/feature/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">feature</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/presentation-mode-demo/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/presentation-mode-demo/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/presentation-mode-demo/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/presentation-mode-demo/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/presentation-mode-demo/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/presentation-mode-demo/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/presentation-mode-demo/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/create-ai-presentations-fast/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Bolt Your Presentations: AI-Powered Slides</h3> <p class="related-post-description astro-vj4tpspi"> Elevate your dev presentations with AI-powered tools. Learn to leverage Bolt, Slidev, and WebContainers for rapid, code-friendly slide creation. This guide walks developers through 7 steps to build impressive tech presentations using Markdown and browser-based Node.js. Master efficient presentation development with instant prototyping and one-click deployment to Netlify </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2024-10-05T00:00:00.000Z">Oct 5, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> productivity </span> </div> </div> </a><a href="/posts/excalidraw-dark-mode-astro-diagrams/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Create Dark Mode-Compatible Technical Diagrams in Astro with Excalidraw: A Complete Guide</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to create and integrate theme-aware Excalidraw diagrams into your Astro blog. This step-by-step guide shows you how to build custom components that automatically adapt to light and dark modes, perfect for technical documentation and blogs </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2024-10-27T07:00:00.000Z">Oct 27, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> astro </span> </div> </div> </a><a href="/posts/visual-regression-testing-with-vue-and-vitest-browser/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How to Do Visual Regression Testing in Vue with Vitest?</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to implement visual regression testing in Vue.js using Vitest&#39;s browser mode. This comprehensive guide covers setting up screenshot-based testing, creating component stories, and integrating with CI/CD pipelines for automated visual testing. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-02-22T00:00:00.000Z">Feb 22, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "presentation-mode-demo";

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
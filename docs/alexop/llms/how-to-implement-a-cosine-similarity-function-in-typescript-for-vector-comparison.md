# Source: https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>How to Implement a Cosine Similarity Function in TypeScript for Vector Comparison | alexop.dev</title><meta name="title" content="How to Implement a Cosine Similarity Function in TypeScript for Vector Comparison | alexop.dev"><meta name="description" content="Learn how to build an efficient cosine similarity function in TypeScript for comparing vector embeddings. This step-by-step guide includes code examples, performance optimizations, and practical applications for semantic search and AI recommendation systems"><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="How to Implement a Cosine Similarity Function in TypeScript for Vector Comparison | alexop.dev"><meta property="og:description" content="Learn how to build an efficient cosine similarity function in TypeScript for comparing vector embeddings. This step-by-step guide includes code examples, performance optimizations, and practical applications for semantic search and AI recommendation systems"><meta property="og:url" content="https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison/"><meta property="og:image" content="https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-type-script-for-vector-comparison/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-03-08T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison/"><meta property="twitter:title" content="How to Implement a Cosine Similarity Function in TypeScript for Vector Comparison | alexop.dev"><meta property="twitter:description" content="Learn how to build an efficient cosine similarity function in TypeScript for comparing vector embeddings. This step-by-step guide includes code examples, performance optimizations, and practical applications for semantic search and AI recommendation systems"><meta property="twitter:image" content="https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-type-script-for-vector-comparison/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"How to Implement a Cosine Similarity Function in TypeScript for Vector Comparison | alexop.dev","description":"Learn how to build an efficient cosine similarity function in TypeScript for comparing vector embeddings. This step-by-step guide includes code examples, performance optimizations, and practical applications for semantic search and AI recommendation systems","image":"https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-type-script-for-vector-comparison/index.png","datePublished":"2025-03-08T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: how-to-implement-a-cosine-similarity-function-in-type-script-for-vector-comparison; }@layer astro { ::view-transition-old(how-to-implement-a-cosine-similarity-function-in-type-script-for-vector-comparison) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(how-to-implement-a-cosine-similarity-function-in-type-script-for-vector-comparison) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(how-to-implement-a-cosine-similarity-function-in-type-script-for-vector-comparison) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(how-to-implement-a-cosine-similarity-function-in-type-script-for-vector-comparison) { 
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
</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: typescript; }@layer astro { ::view-transition-old(typescript) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: mathematics; }@layer astro { ::view-transition-old(mathematics) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(mathematics) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(mathematics) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(mathematics) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">How to Implement a Cosine Similarity Function in TypeScript for Vector Comparison</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-03-08T00:00:00.000Z">Mar 8, 2025</time><span class="sr-only"> at </span></span></div> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><astro-island uid="1yfbz8" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;How to Implement a Cosine Similarity Function in TypeScript for Vector Comparison&quot;],&quot;content&quot;:[0,&quot;import VectorExplainer from \&quot;@features/llm-education/components/VectorExplainer\&quot;;\nimport CosineSimilarityVisualizer from \&quot;@features/llm-education/components/CosineSimilarityVisualizer\&quot;;\nimport Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\n\nTo understand how an AI can understand that the word \&quot;cat\&quot; is similar to \&quot;kitten,\&quot; you must realize cosine similarity. In short, with the help of embeddings, we can represent words as vectors in a high-dimensional space. If the word \&quot;cat\&quot; is represented as a vector [1, 0, 0], the word \&quot;kitten\&quot; would be represented as [1, 0, 1]. Now, we can use cosine similarity to measure the similarity between the two vectors. In this blog post, we will break down the concept of cosine similarity and implement it in TypeScript.\n\n&lt;Alert type=\&quot;note\&quot;&gt;\n  I won&#39;t explain how embeddings work in this blog post, but only how to use\n  them.\n&lt;/Alert&gt;\n\n## What Is Cosine Similarity? A Simple Explanation\n\nThe cosine similarity formula measures how similar two vectors are by examining the angle between them, not their sizes. Here&#39;s how it works in plain English:\n\n1. **What it does**: It tells you if two vectors point in the same direction, opposite directions, or somewhere in between.\n\n2. **The calculation**:\n   - First, multiply the corresponding elements of both vectors and add these products together (the dot product)\n   - Then, calculate how long each vector is (its magnitude)\n   - Finally, divide the dot product by the product of the two magnitudes\n\n3. **The result**:\n   - If you get 1, the vectors point in exactly the same direction (perfectly similar)\n   - If you get 0, the vectors stand perpendicular to each other (completely unrelated)\n   - If you get -1, the vectors point in exactly opposite directions (perfectly dissimilar)\n   - Any value in between indicates the degree of similarity\n\n4. **Why it&#39;s useful**:\n   - It ignores vector size and focuses only on direction\n   - This means you can consider two things similar even if one is much \&quot;bigger\&quot; than the other\n   - For example, a short document about cats and a long document about cats would show similarity, despite their different lengths\n\n5. **In AI applications**:\n   - We convert words, documents, images, etc. into vectors with many dimensions\n   - Cosine similarity helps us find related items by measuring how closely their vectors align\n   - This powers features like semantic search, recommendations, and content matching\n\n## Why Cosine Similarity Matters for Modern Web Development\n\nWhen you build applications with any of these features, you directly work with vector mathematics:\n\n- **Semantic search**: Finding relevant content based on meaning, not just keywords\n- **AI-powered recommendations**: \&quot;Users who liked this also enjoyed...\&quot;\n- **Content matching**: Identifying similar articles, products, or user profiles\n- **Natural language processing**: Understanding and comparing text meaning\n\nAll of these require you to compare vectors, and cosine similarity offers one of the most effective methods to do so.\n\n## Visualizing Cosine Similarity\n\n&lt;CosineSimilarityVisualizer client:only=\&quot;react\&quot; /&gt;\n\n### Cosine Similarity Explained\n\nCosine similarity measures the cosine of the angle between two vectors, showing how similar they are regardless of their magnitude. The value ranges from:\n\n- **+1**: When vectors point in the same direction (perfectly similar)\n- **0**: When vectors stand perpendicular (no similarity)\n- **-1**: When vectors point in opposite directions (completely dissimilar)\n\nWith the interactive visualization above, you can:\n\n1. Move both vectors by dragging the colored circles at their endpoints\n2. Observe how the angle between them changes\n3. See how cosine similarity relates to this angle\n4. Note that cosine similarity depends only on the angle, not the vectors&#39; lengths\n\n## Step-by-Step Example Calculation\n\nLet me walk you through a manual calculation of cosine similarity between two simple vectors. This helps build intuition before we implement it in code.\n\nGiven two vectors: $\\vec{v_1} = [3, 4]$ and $\\vec{v_2} = [5, 2]$\n\nI&#39;ll calculate their cosine similarity step by step:\n\n**Step 1**: Calculate the dot product.\n\n$$\n\\vec{v_1} \\cdot \\vec{v_2} = 3 \\times 5 + 4 \\times 2 = 15 + 8 = 23\n$$\n\n**Step 2**: Calculate the magnitude of each vector.\n\n$$\n||\\vec{v_1}|| = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5\n$$\n\n$$\n||\\vec{v_2}|| = \\sqrt{5^2 + 2^2} = \\sqrt{25 + 4} = \\sqrt{29} \\approx 5.385\n$$\n\n**Step 3**: Calculate the cosine similarity by dividing the dot product by the product of magnitudes.\n\n$$\n\\cos(\\theta) = \\frac{\\vec{v_1} \\cdot \\vec{v_2}}{||\\vec{v_1}|| \\cdot ||\\vec{v_2}||}\n$$\n\n$$\n= \\frac{23}{5 \\times 5.385} = \\frac{23}{26.925} \\approx 0.854\n$$\n\nTherefore, the cosine similarity between vectors $\\vec{v_1}$ and $\\vec{v_2}$ is approximately 0.854, which shows that these vectors point in roughly the same direction.\n\n## Building a Cosine Similarity Function in TypeScript\n\nLet&#39;s implement an optimized cosine similarity function in TypeScript that combines the functional approach with the more efficient `Math.hypot()` method:\n\n```typescript\n/**\n * Calculates the cosine similarity between two vectors\n * @param vecA First vector\n * @param vecB Second vector\n * @returns A value between -1 and 1, where 1 means identical\n */\nfunction cosineSimilarity(vecA: number[], vecB: number[]): number {\n  if (vecA.length !== vecB.length) {\n    throw new Error(\&quot;Vectors must have the same dimensions\&quot;);\n  }\n\n  // Calculate dot product: A·B = Σ(A[i] * B[i])\n  const dotProduct = vecA.reduce((sum, a, i) =&gt; sum + a * vecB[i], 0);\n\n  // Calculate magnitudes using Math.hypot()\n  const magnitudeA = Math.hypot(...vecA);\n  const magnitudeB = Math.hypot(...vecB);\n\n  // Check for zero magnitude\n  if (magnitudeA === 0 || magnitudeB === 0) {\n    return 0;\n  }\n\n  // Calculate cosine similarity: (A·B) / (|A|*|B|)\n  return dotProduct / (magnitudeA * magnitudeB);\n}\n```\n\n## Testing Our Implementation\n\nLet&#39;s see how our function works with some example vectors:\n\n```typescript\n// Example 1: Similar vectors pointing in roughly the same direction\nconst vecA = [3, 4];\nconst vecB = [5, 2];\nconsole.log(`Similarity: ${cosineSimilarity(vecA, vecB).toFixed(3)}`);\n// Output: Similarity: 0.857\n\n// Example 2: Perpendicular vectors\nconst vecC = [1, 0];\nconst vecD = [0, 1];\nconsole.log(`Similarity: ${cosineSimilarity(vecC, vecD).toFixed(3)}`);\n// Output: Similarity: 0.000\n\n// Example 3: Opposite vectors\nconst vecE = [2, 3];\nconst vecF = [-2, -3];\nconsole.log(`Similarity: ${cosineSimilarity(vecE, vecF).toFixed(3)}`);\n// Output: Similarity: -1.000\n```\n\nMathematically, we can verify these results:\n\nFor Example 1:\n$$\\text{cosine similarity} = \\frac{3 \\times 5 + 4 \\times 2}{\\sqrt{3^2 + 4^2} \\times \\sqrt{5^2 + 2^2}} = \\frac{15 + 8}{\\sqrt{25} \\times \\sqrt{29}} = \\frac{23}{5 \\times \\sqrt{29}} \\approx 0.857$$\n\nFor Example 2:\n$$\\text{cosine similarity} = \\frac{1 \\times 0 + 0 \\times 1}{\\sqrt{1^2 + 0^2} \\times \\sqrt{0^2 + 1^2}} = \\frac{0}{1 \\times 1} = 0$$\n\nFor Example 3:\n$$\\text{cosine similarity} = \\frac{2 \\times (-2) + 3 \\times (-3)}{\\sqrt{2^2 + 3^2} \\times \\sqrt{(-2)^2 + (-3)^2}} = \\frac{-4 - 9}{\\sqrt{13} \\times \\sqrt{13}} = \\frac{-13}{13} = -1$$\n\n## Complete TypeScript Solution\n\nHere&#39;s a complete TypeScript solution that includes our cosine similarity function along with some utility methods:\n\n```typescript\nclass VectorUtils {\n  /**\n   * Calculates the cosine similarity between two vectors\n   */\n  static cosineSimilarity(vecA: number[], vecB: number[]): number {\n    if (vecA.length !== vecB.length) {\n      throw new Error(\n        `Vector dimensions don&#39;t match: ${vecA.length} vs ${vecB.length}`\n      );\n    }\n\n    const dotProduct = vecA.reduce((sum, a, i) =&gt; sum + a * vecB[i], 0);\n    const magnitudeA = Math.hypot(...vecA);\n    const magnitudeB = Math.hypot(...vecB);\n\n    if (magnitudeA === 0 || magnitudeB === 0) {\n      return 0;\n    }\n\n    return dotProduct / (magnitudeA * magnitudeB);\n  }\n\n  /**\n   * Calculates the dot product of two vectors\n   */\n  static dotProduct(vecA: number[], vecB: number[]): number {\n    if (vecA.length !== vecB.length) {\n      throw new Error(\n        `Vector dimensions don&#39;t match: ${vecA.length} vs ${vecB.length}`\n      );\n    }\n\n    return vecA.reduce((sum, a, i) =&gt; sum + a * vecB[i], 0);\n  }\n\n  /**\n   * Calculates the magnitude (length) of a vector\n   */\n  static magnitude(vec: number[]): number {\n    return Math.hypot(...vec);\n  }\n\n  /**\n   * Normalizes a vector (converts to unit vector)\n   */\n  static normalize(vec: number[]): number[] {\n    const mag = this.magnitude(vec);\n\n    if (mag === 0) {\n      return Array(vec.length).fill(0);\n    }\n\n    return vec.map(v =&gt; v / mag);\n  }\n\n  /**\n   * Converts cosine similarity to angular distance in degrees\n   */\n  static similarityToDegrees(similarity: number): number {\n    // Clamp similarity to [-1, 1] to handle floating point errors\n    const clampedSimilarity = Math.max(-1, Math.min(1, similarity));\n    return Math.acos(clampedSimilarity) * (180 / Math.PI);\n  }\n}\n```\n\n## Using Cosine Similarity in Real Web Applications\n\nWhen you work with AI in web applications, you&#39;ll often need to calculate similarity between vectors. Here&#39;s a practical example:\n\n```typescript\n// Example: Semantic search implementation\nfunction semanticSearch(\n  queryEmbedding: number[],\n  documentEmbeddings: DocumentWithEmbedding[]\n): SearchResult[] {\n  return documentEmbeddings\n    .map(doc =&gt; ({\n      document: doc,\n      relevance: VectorUtils.cosineSimilarity(queryEmbedding, doc.embedding),\n    }))\n    .filter(result =&gt; result.relevance &gt; 0.7) // Only consider relevant results\n    .sort((a, b) =&gt; b.relevance - a.relevance);\n}\n```\n\n## Using OpenAI Embedding Models with Cosine Similarity\n\nWhile the examples above used simple vectors for clarity, real-world AI applications typically use embedding models that transform text and other data into high-dimensional vector spaces.\n\nOpenAI provides powerful embedding models that you can easily incorporate into your applications. These models transform text into vectors with hundreds or thousands of dimensions that capture semantic meaning:\n\n```typescript\n// Example of using OpenAI embeddings with our cosine similarity function\nasync function compareTextSimilarity(\n  textA: string,\n  textB: string\n): Promise&lt;number&gt; {\n  // Get embeddings from OpenAI API\n  const responseA = await fetch(\&quot;https://api.openai.com/v1/embeddings\&quot;, {\n    method: \&quot;POST\&quot;,\n    headers: {\n      Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,\n      \&quot;Content-Type\&quot;: \&quot;application/json\&quot;,\n    },\n    body: JSON.stringify({\n      model: \&quot;text-embedding-3-large\&quot;,\n      input: textA,\n    }),\n  });\n\n  const responseB = await fetch(\&quot;https://api.openai.com/v1/embeddings\&quot;, {\n    method: \&quot;POST\&quot;,\n    headers: {\n      Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,\n      \&quot;Content-Type\&quot;: \&quot;application/json\&quot;,\n    },\n    body: JSON.stringify({\n      model: \&quot;text-embedding-3-large\&quot;,\n      input: textB,\n    }),\n  });\n\n  const embeddingA = (await responseA.json()).data[0].embedding;\n  const embeddingB = (await responseB.json()).data[0].embedding;\n\n  // Calculate similarity using our function\n  return VectorUtils.cosineSimilarity(embeddingA, embeddingB);\n}\n```\n\n&lt;Alert type=\&quot;warning\&quot;&gt;\n  In a production environment, you should pre-compute embeddings for your\n  content (like blog posts, products, or documents) and store them in a vector\n  database (like Pinecone, Qdrant, or Milvus). Re-computing embeddings for every\n  user request as shown in this example wastes resources and slows performance.\n  A better approach: embed your content once during indexing, store the vectors,\n  and only embed the user&#39;s query when performing a search.\n&lt;/Alert&gt;\n\nOpenAI&#39;s latest embedding models like `text-embedding-3-large` have up to 3,072 dimensions, capturing extremely nuanced semantic relationships between words and concepts. These high-dimensional embeddings enable much more accurate similarity measurements than simpler vector representations.\n\nFor more information on OpenAI&#39;s embedding models, including best practices and implementation details, check out their documentation at [https://platform.openai.com/docs/guides/embeddings](https://platform.openai.com/docs/guides/embeddings).\n\n## Conclusion\n\nUnderstanding vectors and cosine similarity provides practical tools that empower you to work effectively with modern AI features. By implementing these concepts in TypeScript, you gain a deeper understanding and precise control over calculating similarity in your applications.\nThe interactive visualizations we&#39;ve explored help you build intuition about these mathematical concepts, while the TypeScript implementation gives you the tools to apply them in real-world scenarios.\nWhether you build recommendation systems, semantic search, or content-matching features, the foundation you&#39;ve gained here will help you implement more intelligent, accurate, and effective AI-powered features in your web applications.\n\n## Join the Discussion\n\nThis article has sparked interesting discussions across different platforms. Join the conversation to share your thoughts, ask questions, or learn from others&#39; perspectives about implementing cosine similarity in AI applications.\n\n- [Join the discussion on Hacker News →](https://news.ycombinator.com/item?id=43307541)\n- [Discuss on Reddit r/typescript →](https://www.reddit.com/r/typescript/comments/1j73whg/how_to_implement_a_cosine_similarity_function_in/)\n\n---&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>To understand how an AI can understand that the word “cat” is similar to “kitten,” you must realize cosine similarity. In short, with the help of embeddings, we can represent words as vectors in a high-dimensional space. If the word “cat” is represented as a vector [1, 0, 0], the word “kitten” would be represented as [1, 0, 1]. Now, we can use cosine similarity to measure the similarity between the two vectors. In this blog post, we will break down the concept of cosine similarity and implement it in TypeScript.</p>
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> Note </p> <div class="alert-content astro-7kdbuayl"> <p>I won’t explain how embeddings work in this blog post, but only how to use
them.</p> </div> </div> 
<h2 id="what-is-cosine-similarity-a-simple-explanation">What Is Cosine Similarity? A Simple Explanation<a class="heading-link" aria-label="Link to section" href="#what-is-cosine-similarity-a-simple-explanation"><span class="heading-link-icon">#</span></a></h2>
<p>The cosine similarity formula measures how similar two vectors are by examining the angle between them, not their sizes. Here’s how it works in plain English:</p>
<ol>
<li>
<p><strong>What it does</strong>: It tells you if two vectors point in the same direction, opposite directions, or somewhere in between.</p>
</li>
<li>
<p><strong>The calculation</strong>:</p>
<ul>
<li>First, multiply the corresponding elements of both vectors and add these products together (the dot product)</li>
<li>Then, calculate how long each vector is (its magnitude)</li>
<li>Finally, divide the dot product by the product of the two magnitudes</li>
</ul>
</li>
<li>
<p><strong>The result</strong>:</p>
<ul>
<li>If you get 1, the vectors point in exactly the same direction (perfectly similar)</li>
<li>If you get 0, the vectors stand perpendicular to each other (completely unrelated)</li>
<li>If you get -1, the vectors point in exactly opposite directions (perfectly dissimilar)</li>
<li>Any value in between indicates the degree of similarity</li>
</ul>
</li>
<li>
<p><strong>Why it’s useful</strong>:</p>
<ul>
<li>It ignores vector size and focuses only on direction</li>
<li>This means you can consider two things similar even if one is much “bigger” than the other</li>
<li>For example, a short document about cats and a long document about cats would show similarity, despite their different lengths</li>
</ul>
</li>
<li>
<p><strong>In AI applications</strong>:</p>
<ul>
<li>We convert words, documents, images, etc. into vectors with many dimensions</li>
<li>Cosine similarity helps us find related items by measuring how closely their vectors align</li>
<li>This powers features like semantic search, recommendations, and content matching</li>
</ul>
</li>
</ol>
<h2 id="why-cosine-similarity-matters-for-modern-web-development">Why Cosine Similarity Matters for Modern Web Development<a class="heading-link" aria-label="Link to section" href="#why-cosine-similarity-matters-for-modern-web-development"><span class="heading-link-icon">#</span></a></h2>
<p>When you build applications with any of these features, you directly work with vector mathematics:</p>
<ul>
<li><strong>Semantic search</strong>: Finding relevant content based on meaning, not just keywords</li>
<li><strong>AI-powered recommendations</strong>: “Users who liked this also enjoyed…”</li>
<li><strong>Content matching</strong>: Identifying similar articles, products, or user profiles</li>
<li><strong>Natural language processing</strong>: Understanding and comparing text meaning</li>
</ul>
<p>All of these require you to compare vectors, and cosine similarity offers one of the most effective methods to do so.</p>
<h2 id="visualizing-cosine-similarity">Visualizing Cosine Similarity<a class="heading-link" aria-label="Link to section" href="#visualizing-cosine-similarity"><span class="heading-link-icon">#</span></a></h2>
<style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Z1i6jOa" component-url="/_astro/CosineSimilarityVisualizer.UosDoiPB.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{}" ssr client="only" opts="{&quot;name&quot;:&quot;CosineSimilarityVisualizer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island>
<h3 id="cosine-similarity-explained">Cosine Similarity Explained<a class="heading-link" aria-label="Link to section" href="#cosine-similarity-explained"><span class="heading-link-icon">#</span></a></h3>
<p>Cosine similarity measures the cosine of the angle between two vectors, showing how similar they are regardless of their magnitude. The value ranges from:</p>
<ul>
<li><strong>+1</strong>: When vectors point in the same direction (perfectly similar)</li>
<li><strong>0</strong>: When vectors stand perpendicular (no similarity)</li>
<li><strong>-1</strong>: When vectors point in opposite directions (completely dissimilar)</li>
</ul>
<p>With the interactive visualization above, you can:</p>
<ol>
<li>Move both vectors by dragging the colored circles at their endpoints</li>
<li>Observe how the angle between them changes</li>
<li>See how cosine similarity relates to this angle</li>
<li>Note that cosine similarity depends only on the angle, not the vectors’ lengths</li>
</ol>
<h2 id="step-by-step-example-calculation">Step-by-Step Example Calculation<a class="heading-link" aria-label="Link to section" href="#step-by-step-example-calculation"><span class="heading-link-icon">#</span></a></h2>
<p>Let me walk you through a manual calculation of cosine similarity between two simple vectors. This helps build intuition before we implement it in code.</p>
<p>Given two vectors: <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mover accent="true"><msub><mi>v</mi><mn>1</mn></msub><mo>⃗</mo></mover><mo>=</mo><mo stretchy="false">[</mo><mn>3</mn><mo separator="true">,</mo><mn>4</mn><mo stretchy="false">]</mo></mrow><annotation encoding="application/x-tex">\vec{v_1} = [3, 4]</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.864em;vertical-align:-0.15em"></span><span class="mord accent"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.714em"><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="accent-body" style="left:-0.2355em"><span class="overlay" style="height:0.714em;width:0.471em"><svg xmlns="http://www.w3.org/2000/svg" width="0.471em" height="0.714em" style="width:0.471em" viewBox="0 0 471 714" preserveAspectRatio="xMinYMin"><path d="M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z"></path></svg></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em"></span><span class="mopen">[</span><span class="mord">3</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em"></span><span class="mord">4</span><span class="mclose">]</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mover accent="true"><msub><mi>v</mi><mn>2</mn></msub><mo>⃗</mo></mover><mo>=</mo><mo stretchy="false">[</mo><mn>5</mn><mo separator="true">,</mo><mn>2</mn><mo stretchy="false">]</mo></mrow><annotation encoding="application/x-tex">\vec{v_2} = [5, 2]</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.864em;vertical-align:-0.15em"></span><span class="mord accent"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.714em"><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="accent-body" style="left:-0.2355em"><span class="overlay" style="height:0.714em;width:0.471em"><svg xmlns="http://www.w3.org/2000/svg" width="0.471em" height="0.714em" style="width:0.471em" viewBox="0 0 471 714" preserveAspectRatio="xMinYMin"><path d="M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z"></path></svg></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em"></span><span class="mopen">[</span><span class="mord">5</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em"></span><span class="mord">2</span><span class="mclose">]</span></span></span></span></p>
<p>I’ll calculate their cosine similarity step by step:</p>
<p><strong>Step 1</strong>: Calculate the dot product.</p>
<span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mover accent="true"><msub><mi>v</mi><mn>1</mn></msub><mo>⃗</mo></mover><mo>⋅</mo><mover accent="true"><msub><mi>v</mi><mn>2</mn></msub><mo>⃗</mo></mover><mo>=</mo><mn>3</mn><mo>×</mo><mn>5</mn><mo>+</mo><mn>4</mn><mo>×</mo><mn>2</mn><mo>=</mo><mn>15</mn><mo>+</mo><mn>8</mn><mo>=</mo><mn>23</mn></mrow><annotation encoding="application/x-tex">\vec{v_1} \cdot \vec{v_2} = 3 \times 5 + 4 \times 2 = 15 + 8 = 23</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.864em;vertical-align:-0.15em"></span><span class="mord accent"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.714em"><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="accent-body" style="left:-0.2355em"><span class="overlay" style="height:0.714em;width:0.471em"><svg xmlns="http://www.w3.org/2000/svg" width="0.471em" height="0.714em" style="width:0.471em" viewBox="0 0 471 714" preserveAspectRatio="xMinYMin"><path d="M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z"></path></svg></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222em"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right:0.2222em"></span></span><span class="base"><span class="strut" style="height:0.864em;vertical-align:-0.15em"></span><span class="mord accent"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.714em"><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="accent-body" style="left:-0.2355em"><span class="overlay" style="height:0.714em;width:0.471em"><svg xmlns="http://www.w3.org/2000/svg" width="0.471em" height="0.714em" style="width:0.471em" viewBox="0 0 471 714" preserveAspectRatio="xMinYMin"><path d="M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z"></path></svg></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:0.7278em;vertical-align:-0.0833em"></span><span class="mord">3</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mbin">×</span><span class="mspace" style="margin-right:0.2222em"></span></span><span class="base"><span class="strut" style="height:0.7278em;vertical-align:-0.0833em"></span><span class="mord">5</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em"></span></span><span class="base"><span class="strut" style="height:0.7278em;vertical-align:-0.0833em"></span><span class="mord">4</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mbin">×</span><span class="mspace" style="margin-right:0.2222em"></span></span><span class="base"><span class="strut" style="height:0.6444em"></span><span class="mord">2</span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:0.7278em;vertical-align:-0.0833em"></span><span class="mord">15</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em"></span></span><span class="base"><span class="strut" style="height:0.6444em"></span><span class="mord">8</span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:0.6444em"></span><span class="mord">23</span></span></span></span></span>
<p><strong>Step 2</strong>: Calculate the magnitude of each vector.</p>
<span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mi mathvariant="normal">∣</mi><mi mathvariant="normal">∣</mi><mover accent="true"><msub><mi>v</mi><mn>1</mn></msub><mo>⃗</mo></mover><mi mathvariant="normal">∣</mi><mi mathvariant="normal">∣</mi><mo>=</mo><msqrt><mrow><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup></mrow></msqrt><mo>=</mo><msqrt><mrow><mn>9</mn><mo>+</mo><mn>16</mn></mrow></msqrt><mo>=</mo><msqrt><mn>25</mn></msqrt><mo>=</mo><mn>5</mn></mrow><annotation encoding="application/x-tex">||\vec{v_1}|| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em"></span><span class="mord">∣∣</span><span class="mord accent"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.714em"><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="accent-body" style="left:-0.2355em"><span class="overlay" style="height:0.714em;width:0.471em"><svg xmlns="http://www.w3.org/2000/svg" width="0.471em" height="0.714em" style="width:0.471em" viewBox="0 0 471 714" preserveAspectRatio="xMinYMin"><path d="M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z"></path></svg></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span><span class="mord">∣∣</span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.24em;vertical-align:-0.1777em"></span><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.0623em"><span class="svg-align" style="top:-3.2em"><span class="pstrut" style="height:3.2em"></span><span class="mord" style="padding-left:1em"><span class="mord"><span class="mord">3</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7401em"><span style="top:-2.989em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222em"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mord"><span class="mord">4</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7401em"><span style="top:-2.989em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span><span style="top:-3.0223em"><span class="pstrut" style="height:3.2em"></span><span class="hide-tail" style="min-width:1.02em;height:1.28em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.28em" viewBox="0 0 400000 1296" preserveAspectRatio="xMinYMin slice"><path d="M263,681c0.7,0,18,39.7,52,119
c34,79.3,68.167,158.7,102.5,238c34.3,79.3,51.8,119.3,52.5,120
c340,-704.7,510.7,-1060.3,512,-1067
l0 -0
c4.7,-7.3,11,-11,19,-11
H40000v40H1012.3
s-271.3,567,-271.3,567c-38.7,80.7,-84,175,-136,283c-52,108,-89.167,185.3,-111.5,232
c-22.3,46.7,-33.8,70.3,-34.5,71c-4.7,4.7,-12.3,7,-23,7s-12,-1,-12,-1
s-109,-253,-109,-253c-72.7,-168,-109.3,-252,-110,-252c-10.7,8,-22,16.7,-34,26
c-22,17.3,-33.3,26,-34,26s-26,-26,-26,-26s76,-59,76,-59s76,-60,76,-60z
M1001 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1777em"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.04em;vertical-align:-0.1256em"></span><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9144em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord" style="padding-left:0.833em"><span class="mord">9</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mord">16</span></span></span><span style="top:-2.8744em"><span class="pstrut" style="height:3em"></span><span class="hide-tail" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1256em"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.04em;vertical-align:-0.0839em"></span><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9561em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord" style="padding-left:0.833em"><span class="mord">25</span></span></span><span style="top:-2.9161em"><span class="pstrut" style="height:3em"></span><span class="hide-tail" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.0839em"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:0.6444em"></span><span class="mord">5</span></span></span></span></span>
<span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mi mathvariant="normal">∣</mi><mi mathvariant="normal">∣</mi><mover accent="true"><msub><mi>v</mi><mn>2</mn></msub><mo>⃗</mo></mover><mi mathvariant="normal">∣</mi><mi mathvariant="normal">∣</mi><mo>=</mo><msqrt><mrow><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup></mrow></msqrt><mo>=</mo><msqrt><mrow><mn>25</mn><mo>+</mo><mn>4</mn></mrow></msqrt><mo>=</mo><msqrt><mn>29</mn></msqrt><mo>≈</mo><mn>5.385</mn></mrow><annotation encoding="application/x-tex">||\vec{v_2}|| = \sqrt{5^2 + 2^2} = \sqrt{25 + 4} = \sqrt{29} \approx 5.385</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em"></span><span class="mord">∣∣</span><span class="mord accent"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.714em"><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="accent-body" style="left:-0.2355em"><span class="overlay" style="height:0.714em;width:0.471em"><svg xmlns="http://www.w3.org/2000/svg" width="0.471em" height="0.714em" style="width:0.471em" viewBox="0 0 471 714" preserveAspectRatio="xMinYMin"><path d="M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z"></path></svg></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span><span class="mord">∣∣</span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.24em;vertical-align:-0.1777em"></span><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.0623em"><span class="svg-align" style="top:-3.2em"><span class="pstrut" style="height:3.2em"></span><span class="mord" style="padding-left:1em"><span class="mord"><span class="mord">5</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7401em"><span style="top:-2.989em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222em"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mord"><span class="mord">2</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7401em"><span style="top:-2.989em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span><span style="top:-3.0223em"><span class="pstrut" style="height:3.2em"></span><span class="hide-tail" style="min-width:1.02em;height:1.28em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.28em" viewBox="0 0 400000 1296" preserveAspectRatio="xMinYMin slice"><path d="M263,681c0.7,0,18,39.7,52,119
c34,79.3,68.167,158.7,102.5,238c34.3,79.3,51.8,119.3,52.5,120
c340,-704.7,510.7,-1060.3,512,-1067
l0 -0
c4.7,-7.3,11,-11,19,-11
H40000v40H1012.3
s-271.3,567,-271.3,567c-38.7,80.7,-84,175,-136,283c-52,108,-89.167,185.3,-111.5,232
c-22.3,46.7,-33.8,70.3,-34.5,71c-4.7,4.7,-12.3,7,-23,7s-12,-1,-12,-1
s-109,-253,-109,-253c-72.7,-168,-109.3,-252,-110,-252c-10.7,8,-22,16.7,-34,26
c-22,17.3,-33.3,26,-34,26s-26,-26,-26,-26s76,-59,76,-59s76,-60,76,-60z
M1001 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1777em"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.04em;vertical-align:-0.1256em"></span><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9144em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord" style="padding-left:0.833em"><span class="mord">25</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mord">4</span></span></span><span style="top:-2.8744em"><span class="pstrut" style="height:3em"></span><span class="hide-tail" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1256em"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.04em;vertical-align:-0.0839em"></span><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9561em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord" style="padding-left:0.833em"><span class="mord">29</span></span></span><span style="top:-2.9161em"><span class="pstrut" style="height:3em"></span><span class="hide-tail" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.0839em"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">≈</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:0.6444em"></span><span class="mord">5.385</span></span></span></span></span>
<p><strong>Step 3</strong>: Calculate the cosine similarity by dividing the dot product by the product of magnitudes.</p>
<span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mi>cos</mi><mo>⁡</mo><mo stretchy="false">(</mo><mi>θ</mi><mo stretchy="false">)</mo><mo>=</mo><mfrac><mrow><mover accent="true"><msub><mi>v</mi><mn>1</mn></msub><mo>⃗</mo></mover><mo>⋅</mo><mover accent="true"><msub><mi>v</mi><mn>2</mn></msub><mo>⃗</mo></mover></mrow><mrow><mi mathvariant="normal">∣</mi><mi mathvariant="normal">∣</mi><mover accent="true"><msub><mi>v</mi><mn>1</mn></msub><mo>⃗</mo></mover><mi mathvariant="normal">∣</mi><mi mathvariant="normal">∣</mi><mo>⋅</mo><mi mathvariant="normal">∣</mi><mi mathvariant="normal">∣</mi><mover accent="true"><msub><mi>v</mi><mn>2</mn></msub><mo>⃗</mo></mover><mi mathvariant="normal">∣</mi><mi mathvariant="normal">∣</mi></mrow></mfrac></mrow><annotation encoding="application/x-tex">\cos(\theta) = \frac{\vec{v_1} \cdot \vec{v_2}}{||\vec{v_1}|| \cdot ||\vec{v_2}||}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em"></span><span class="mop">cos</span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right:0.02778em">θ</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:2.327em;vertical-align:-0.936em"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.391em"><span style="top:-2.314em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord">∣∣</span><span class="mord accent"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.714em"><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="accent-body" style="left:-0.2355em"><span class="overlay" style="height:0.714em;width:0.471em"><svg xmlns="http://www.w3.org/2000/svg" width="0.471em" height="0.714em" style="width:0.471em" viewBox="0 0 471 714" preserveAspectRatio="xMinYMin"><path d="M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z"></path></svg></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span><span class="mord">∣∣</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mord">∣∣</span><span class="mord accent"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.714em"><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="accent-body" style="left:-0.2355em"><span class="overlay" style="height:0.714em;width:0.471em"><svg xmlns="http://www.w3.org/2000/svg" width="0.471em" height="0.714em" style="width:0.471em" viewBox="0 0 471 714" preserveAspectRatio="xMinYMin"><path d="M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z"></path></svg></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span><span class="mord">∣∣</span></span></span><span style="top:-3.23em"><span class="pstrut" style="height:3em"></span><span class="frac-line" style="border-bottom-width:0.04em"></span></span><span style="top:-3.677em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord accent"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.714em"><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="accent-body" style="left:-0.2355em"><span class="overlay" style="height:0.714em;width:0.471em"><svg xmlns="http://www.w3.org/2000/svg" width="0.471em" height="0.714em" style="width:0.471em" viewBox="0 0 471 714" preserveAspectRatio="xMinYMin"><path d="M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z"></path></svg></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222em"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mord accent"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.714em"><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="accent-body" style="left:-0.2355em"><span class="overlay" style="height:0.714em;width:0.471em"><svg xmlns="http://www.w3.org/2000/svg" width="0.471em" height="0.714em" style="width:0.471em" viewBox="0 0 471 714" preserveAspectRatio="xMinYMin"><path d="M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z"></path></svg></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.936em"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span>
<span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mo>=</mo><mfrac><mn>23</mn><mrow><mn>5</mn><mo>×</mo><mn>5.385</mn></mrow></mfrac><mo>=</mo><mfrac><mn>23</mn><mn>26.925</mn></mfrac><mo>≈</mo><mn>0.854</mn></mrow><annotation encoding="application/x-tex">= \frac{23}{5 \times 5.385} = \frac{23}{26.925} \approx 0.854</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.3669em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:2.0908em;vertical-align:-0.7693em"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.3214em"><span style="top:-2.314em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord">5</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mbin">×</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mord">5.385</span></span></span><span style="top:-3.23em"><span class="pstrut" style="height:3em"></span><span class="frac-line" style="border-bottom-width:0.04em"></span></span><span style="top:-3.677em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord">23</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.7693em"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:2.0074em;vertical-align:-0.686em"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.3214em"><span style="top:-2.314em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord">26.925</span></span></span><span style="top:-3.23em"><span class="pstrut" style="height:3em"></span><span class="frac-line" style="border-bottom-width:0.04em"></span></span><span style="top:-3.677em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord">23</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.686em"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">≈</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:0.6444em"></span><span class="mord">0.854</span></span></span></span></span>
<p>Therefore, the cosine similarity between vectors <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mover accent="true"><msub><mi>v</mi><mn>1</mn></msub><mo>⃗</mo></mover></mrow><annotation encoding="application/x-tex">\vec{v_1}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.864em;vertical-align:-0.15em"></span><span class="mord accent"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.714em"><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="accent-body" style="left:-0.2355em"><span class="overlay" style="height:0.714em;width:0.471em"><svg xmlns="http://www.w3.org/2000/svg" width="0.471em" height="0.714em" style="width:0.471em" viewBox="0 0 471 714" preserveAspectRatio="xMinYMin"><path d="M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z"></path></svg></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span></span> and <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mover accent="true"><msub><mi>v</mi><mn>2</mn></msub><mo>⃗</mo></mover></mrow><annotation encoding="application/x-tex">\vec{v_2}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.864em;vertical-align:-0.15em"></span><span class="mord accent"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.714em"><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em"><span class="pstrut" style="height:2.7em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span><span style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="accent-body" style="left:-0.2355em"><span class="overlay" style="height:0.714em;width:0.471em"><svg xmlns="http://www.w3.org/2000/svg" width="0.471em" height="0.714em" style="width:0.471em" viewBox="0 0 471 714" preserveAspectRatio="xMinYMin"><path d="M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z"></path></svg></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em"><span></span></span></span></span></span></span></span></span> is approximately 0.854, which shows that these vectors point in roughly the same direction.</p>
<h2 id="building-a-cosine-similarity-function-in-typescript">Building a Cosine Similarity Function in TypeScript<a class="heading-link" aria-label="Link to section" href="#building-a-cosine-similarity-function-in-typescript"><span class="heading-link-icon">#</span></a></h2>
<p>Let’s implement an optimized cosine similarity function in TypeScript that combines the functional approach with the more efficient <code>Math.hypot()</code> method:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Calculates the cosine similarity between two vectors</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * </span><span style="color:#646E9C;font-style:italic">@param</span><span style="color:#5A638C;font-style:italic"> vecA</span><span style="color:#51597D;font-style:italic"> First vector</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * </span><span style="color:#646E9C;font-style:italic">@param</span><span style="color:#5A638C;font-style:italic"> vecB</span><span style="color:#51597D;font-style:italic"> Second vector</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * </span><span style="color:#646E9C;font-style:italic">@returns</span><span style="color:#51597D;font-style:italic"> A value between -1 and 1, where 1 means identical</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> cosineSimilarity</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">vecA</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> vecB</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">[])</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">vecA</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#BB9AF7"> !==</span><span style="color:#C0CAF5"> vecB</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">    throw</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Error</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Vectors must have the same dimensions</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Calculate dot product: A·B = Σ(A[i] * B[i])</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> dotProduct</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> vecA</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">reduce</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">sum</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> a</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> i</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> sum</span><span style="color:#89DDFF"> +</span><span style="color:#C0CAF5"> a</span><span style="color:#89DDFF"> *</span><span style="color:#C0CAF5"> vecB</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">i</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Calculate magnitudes using Math.hypot()</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> magnitudeA</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">hypot</span><span style="color:#9ABDF5">(</span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">vecA</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> magnitudeB</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">hypot</span><span style="color:#9ABDF5">(</span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">vecB</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Check for zero magnitude</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">magnitudeA</span><span style="color:#BB9AF7"> ===</span><span style="color:#FF9E64"> 0</span><span style="color:#BB9AF7"> ||</span><span style="color:#C0CAF5"> magnitudeB</span><span style="color:#BB9AF7"> ===</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Calculate cosine similarity: (A·B) / (|A|*|B|)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> dotProduct</span><span style="color:#89DDFF"> /</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">magnitudeA</span><span style="color:#89DDFF"> *</span><span style="color:#C0CAF5"> magnitudeB</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="/**
 * Calculates the cosine similarity between two vectors
 * @param vecA First vector
 * @param vecB Second vector
 * @returns A value between -1 and 1, where 1 means identical
 */
function cosineSimilarity(vecA: number[], vecB: number[]): number {
  if (vecA.length !== vecB.length) {
    throw new Error(&#34;Vectors must have the same dimensions&#34;);
  }

  // Calculate dot product: A·B = Σ(A[i] * B[i])
  const dotProduct = vecA.reduce((sum, a, i) => sum + a * vecB[i], 0);

  // Calculate magnitudes using Math.hypot()
  const magnitudeA = Math.hypot(...vecA);
  const magnitudeB = Math.hypot(...vecB);

  // Check for zero magnitude
  if (magnitudeA === 0 || magnitudeB === 0) {
    return 0;
  }

  // Calculate cosine similarity: (A·B) / (|A|*|B|)
  return dotProduct / (magnitudeA * magnitudeB);
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="testing-our-implementation">Testing Our Implementation<a class="heading-link" aria-label="Link to section" href="#testing-our-implementation"><span class="heading-link-icon">#</span></a></h2>
<p>Let’s see how our function works with some example vectors:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Example 1: Similar vectors pointing in roughly the same direction</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> vecA</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> [</span><span style="color:#FF9E64">3</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 4</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> vecB</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> [</span><span style="color:#FF9E64">5</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 2</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">Similarity: </span><span style="color:#7DCFFF">${</span><span style="color:#7AA2F7">cosineSimilarity</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">vecA</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> vecB</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toFixed</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">3</span><span style="color:#9ABDF5">)</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Output: Similarity: 0.857</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Example 2: Perpendicular vectors</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> vecC</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> [</span><span style="color:#FF9E64">1</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> vecD</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> [</span><span style="color:#FF9E64">0</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 1</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">Similarity: </span><span style="color:#7DCFFF">${</span><span style="color:#7AA2F7">cosineSimilarity</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">vecC</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> vecD</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toFixed</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">3</span><span style="color:#9ABDF5">)</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Output: Similarity: 0.000</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Example 3: Opposite vectors</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> vecE</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> [</span><span style="color:#FF9E64">2</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 3</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> vecF</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">-</span><span style="color:#FF9E64">2</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> -</span><span style="color:#FF9E64">3</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">Similarity: </span><span style="color:#7DCFFF">${</span><span style="color:#7AA2F7">cosineSimilarity</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">vecE</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> vecF</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toFixed</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">3</span><span style="color:#9ABDF5">)</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Output: Similarity: -1.000</span></span></code><button type="button" class="copy" data-code="// Example 1: Similar vectors pointing in roughly the same direction
const vecA = [3, 4];
const vecB = [5, 2];
console.log(`Similarity: ${cosineSimilarity(vecA, vecB).toFixed(3)}`);
// Output: Similarity: 0.857

// Example 2: Perpendicular vectors
const vecC = [1, 0];
const vecD = [0, 1];
console.log(`Similarity: ${cosineSimilarity(vecC, vecD).toFixed(3)}`);
// Output: Similarity: 0.000

// Example 3: Opposite vectors
const vecE = [2, 3];
const vecF = [-2, -3];
console.log(`Similarity: ${cosineSimilarity(vecE, vecF).toFixed(3)}`);
// Output: Similarity: -1.000" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Mathematically, we can verify these results:</p>
<p>For Example 1:
<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mtext>cosine similarity</mtext><mo>=</mo><mfrac><mrow><mn>3</mn><mo>×</mo><mn>5</mn><mo>+</mo><mn>4</mn><mo>×</mo><mn>2</mn></mrow><mrow><msqrt><mrow><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup></mrow></msqrt><mo>×</mo><msqrt><mrow><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup></mrow></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>15</mn><mo>+</mo><mn>8</mn></mrow><mrow><msqrt><mn>25</mn></msqrt><mo>×</mo><msqrt><mn>29</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>23</mn><mrow><mn>5</mn><mo>×</mo><msqrt><mn>29</mn></msqrt></mrow></mfrac><mo>≈</mo><mn>0.857</mn></mrow><annotation encoding="application/x-tex">\text{cosine similarity} = \frac{3 \times 5 + 4 \times 2}{\sqrt{3^2 + 4^2} \times \sqrt{5^2 + 2^2}} = \frac{15 + 8}{\sqrt{25} \times \sqrt{29}} = \frac{23}{5 \times \sqrt{29}} \approx 0.857</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em"></span><span class="mord text"><span class="mord">cosine similarity</span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.3831em;vertical-align:-0.538em"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8451em"><span style="top:-2.5445em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord sqrt mtight"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9221em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord mtight" style="padding-left:0.833em"><span class="mord mtight"><span class="mord mtight">3</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463em"><span style="top:-2.786em;margin-right:0.0714em"><span class="pstrut" style="height:2.5em"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mbin mtight">+</span><span class="mord mtight"><span class="mord mtight">4</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463em"><span style="top:-2.786em;margin-right:0.0714em"><span class="pstrut" style="height:2.5em"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span><span style="top:-2.8821em"><span class="pstrut" style="height:3em"></span><span class="hide-tail mtight" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1179em"><span></span></span></span></span></span><span class="mbin mtight">×</span><span class="mord sqrt mtight"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9221em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord mtight" style="padding-left:0.833em"><span class="mord mtight"><span class="mord mtight">5</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463em"><span style="top:-2.786em;margin-right:0.0714em"><span class="pstrut" style="height:2.5em"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mbin mtight">+</span><span class="mord mtight"><span class="mord mtight">2</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463em"><span style="top:-2.786em;margin-right:0.0714em"><span class="pstrut" style="height:2.5em"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span><span style="top:-2.8821em"><span class="pstrut" style="height:3em"></span><span class="hide-tail mtight" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1179em"><span></span></span></span></span></span></span></span></span><span style="top:-3.23em"><span class="pstrut" style="height:3em"></span><span class="frac-line" style="border-bottom-width:0.04em"></span></span><span style="top:-3.394em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">3</span><span class="mbin mtight">×</span><span class="mord mtight">5</span><span class="mbin mtight">+</span><span class="mord mtight">4</span><span class="mbin mtight">×</span><span class="mord mtight">2</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.538em"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.3831em;vertical-align:-0.538em"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8451em"><span style="top:-2.551em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord sqrt mtight"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9128em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord mtight" style="padding-left:0.833em"><span class="mord mtight">25</span></span></span><span style="top:-2.8728em"><span class="pstrut" style="height:3em"></span><span class="hide-tail mtight" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1272em"><span></span></span></span></span></span><span class="mbin mtight">×</span><span class="mord sqrt mtight"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9128em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord mtight" style="padding-left:0.833em"><span class="mord mtight">29</span></span></span><span style="top:-2.8728em"><span class="pstrut" style="height:3em"></span><span class="hide-tail mtight" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1272em"><span></span></span></span></span></span></span></span></span><span style="top:-3.23em"><span class="pstrut" style="height:3em"></span><span class="frac-line" style="border-bottom-width:0.04em"></span></span><span style="top:-3.394em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">15</span><span class="mbin mtight">+</span><span class="mord mtight">8</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.538em"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.3831em;vertical-align:-0.538em"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8451em"><span style="top:-2.551em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">5</span><span class="mbin mtight">×</span><span class="mord sqrt mtight"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9128em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord mtight" style="padding-left:0.833em"><span class="mord mtight">29</span></span></span><span style="top:-2.8728em"><span class="pstrut" style="height:3em"></span><span class="hide-tail mtight" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1272em"><span></span></span></span></span></span></span></span></span><span style="top:-3.23em"><span class="pstrut" style="height:3em"></span><span class="frac-line" style="border-bottom-width:0.04em"></span></span><span style="top:-3.394em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">23</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.538em"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">≈</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:0.6444em"></span><span class="mord">0.857</span></span></span></span></p>
<p>For Example 2:
<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mtext>cosine similarity</mtext><mo>=</mo><mfrac><mrow><mn>1</mn><mo>×</mo><mn>0</mn><mo>+</mo><mn>0</mn><mo>×</mo><mn>1</mn></mrow><mrow><msqrt><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>0</mn><mn>2</mn></msup></mrow></msqrt><mo>×</mo><msqrt><mrow><msup><mn>0</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></mrow></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>0</mn><mrow><mn>1</mn><mo>×</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">\text{cosine similarity} = \frac{1 \times 0 + 0 \times 1}{\sqrt{1^2 + 0^2} \times \sqrt{0^2 + 1^2}} = \frac{0}{1 \times 1} = 0</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em"></span><span class="mord text"><span class="mord">cosine similarity</span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.3831em;vertical-align:-0.538em"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8451em"><span style="top:-2.5445em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord sqrt mtight"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9221em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord mtight" style="padding-left:0.833em"><span class="mord mtight"><span class="mord mtight">1</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463em"><span style="top:-2.786em;margin-right:0.0714em"><span class="pstrut" style="height:2.5em"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mbin mtight">+</span><span class="mord mtight"><span class="mord mtight">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463em"><span style="top:-2.786em;margin-right:0.0714em"><span class="pstrut" style="height:2.5em"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span><span style="top:-2.8821em"><span class="pstrut" style="height:3em"></span><span class="hide-tail mtight" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1179em"><span></span></span></span></span></span><span class="mbin mtight">×</span><span class="mord sqrt mtight"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9221em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord mtight" style="padding-left:0.833em"><span class="mord mtight"><span class="mord mtight">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463em"><span style="top:-2.786em;margin-right:0.0714em"><span class="pstrut" style="height:2.5em"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mbin mtight">+</span><span class="mord mtight"><span class="mord mtight">1</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463em"><span style="top:-2.786em;margin-right:0.0714em"><span class="pstrut" style="height:2.5em"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span><span style="top:-2.8821em"><span class="pstrut" style="height:3em"></span><span class="hide-tail mtight" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1179em"><span></span></span></span></span></span></span></span></span><span style="top:-3.23em"><span class="pstrut" style="height:3em"></span><span class="frac-line" style="border-bottom-width:0.04em"></span></span><span style="top:-3.394em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span><span class="mbin mtight">×</span><span class="mord mtight">0</span><span class="mbin mtight">+</span><span class="mord mtight">0</span><span class="mbin mtight">×</span><span class="mord mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.538em"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.2484em;vertical-align:-0.4033em"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8451em"><span style="top:-2.655em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span><span class="mbin mtight">×</span><span class="mord mtight">1</span></span></span></span><span style="top:-3.23em"><span class="pstrut" style="height:3em"></span><span class="frac-line" style="border-bottom-width:0.04em"></span></span><span style="top:-3.394em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">0</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.4033em"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:0.6444em"></span><span class="mord">0</span></span></span></span></p>
<p>For Example 3:
<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mtext>cosine similarity</mtext><mo>=</mo><mfrac><mrow><mn>2</mn><mo>×</mo><mo stretchy="false">(</mo><mo>−</mo><mn>2</mn><mo stretchy="false">)</mo><mo>+</mo><mn>3</mn><mo>×</mo><mo stretchy="false">(</mo><mo>−</mo><mn>3</mn><mo stretchy="false">)</mo></mrow><mrow><msqrt><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></mrow></msqrt><mo>×</mo><msqrt><mrow><mo stretchy="false">(</mo><mo>−</mo><mn>2</mn><msup><mo stretchy="false">)</mo><mn>2</mn></msup><mo>+</mo><mo stretchy="false">(</mo><mo>−</mo><mn>3</mn><msup><mo stretchy="false">)</mo><mn>2</mn></msup></mrow></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>−</mo><mn>4</mn><mo>−</mo><mn>9</mn></mrow><mrow><msqrt><mn>13</mn></msqrt><mo>×</mo><msqrt><mn>13</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>−</mo><mn>13</mn></mrow><mn>13</mn></mfrac><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">\text{cosine similarity} = \frac{2 \times (-2) + 3 \times (-3)}{\sqrt{2^2 + 3^2} \times \sqrt{(-2)^2 + (-3)^2}} = \frac{-4 - 9}{\sqrt{13} \times \sqrt{13}} = \frac{-13}{13} = -1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em"></span><span class="mord text"><span class="mord">cosine similarity</span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.8396em;vertical-align:-0.8296em"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.01em"><span style="top:-2.4642em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord sqrt mtight"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9221em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord mtight" style="padding-left:0.833em"><span class="mord mtight"><span class="mord mtight">2</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463em"><span style="top:-2.786em;margin-right:0.0714em"><span class="pstrut" style="height:2.5em"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mbin mtight">+</span><span class="mord mtight"><span class="mord mtight">3</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463em"><span style="top:-2.786em;margin-right:0.0714em"><span class="pstrut" style="height:2.5em"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span><span style="top:-2.8821em"><span class="pstrut" style="height:3em"></span><span class="hide-tail mtight" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1179em"><span></span></span></span></span></span><span class="mbin mtight">×</span><span class="mord sqrt mtight"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.0369em"><span class="svg-align" style="top:-3.4286em"><span class="pstrut" style="height:3.4286em"></span><span class="mord mtight" style="padding-left:1.19em"><span class="mopen mtight">(</span><span class="mord mtight">−</span><span class="mord mtight">2</span><span class="mclose mtight"><span class="mclose mtight">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463em"><span style="top:-2.786em;margin-right:0.0714em"><span class="pstrut" style="height:2.5em"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mbin mtight">+</span><span class="mopen mtight">(</span><span class="mord mtight">−</span><span class="mord mtight">3</span><span class="mclose mtight"><span class="mclose mtight">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463em"><span style="top:-2.786em;margin-right:0.0714em"><span class="pstrut" style="height:2.5em"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span><span style="top:-3.0089em"><span class="pstrut" style="height:3.4286em"></span><span class="hide-tail mtight" style="min-width:0.853em;height:1.5429em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.5429em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.4197em"><span></span></span></span></span></span></span></span></span><span style="top:-3.23em"><span class="pstrut" style="height:3em"></span><span class="frac-line" style="border-bottom-width:0.04em"></span></span><span style="top:-3.485em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2</span><span class="mbin mtight">×</span><span class="mopen mtight">(</span><span class="mord mtight">−</span><span class="mord mtight">2</span><span class="mclose mtight">)</span><span class="mbin mtight">+</span><span class="mord mtight">3</span><span class="mbin mtight">×</span><span class="mopen mtight">(</span><span class="mord mtight">−</span><span class="mord mtight">3</span><span class="mclose mtight">)</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.8296em"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.3831em;vertical-align:-0.538em"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8451em"><span style="top:-2.551em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord sqrt mtight"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9128em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord mtight" style="padding-left:0.833em"><span class="mord mtight">13</span></span></span><span style="top:-2.8728em"><span class="pstrut" style="height:3em"></span><span class="hide-tail mtight" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1272em"><span></span></span></span></span></span><span class="mbin mtight">×</span><span class="mord sqrt mtight"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9128em"><span class="svg-align" style="top:-3em"><span class="pstrut" style="height:3em"></span><span class="mord mtight" style="padding-left:0.833em"><span class="mord mtight">13</span></span></span><span style="top:-2.8728em"><span class="pstrut" style="height:3em"></span><span class="hide-tail mtight" style="min-width:0.853em;height:1.08em"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1272em"><span></span></span></span></span></span></span></span></span><span style="top:-3.23em"><span class="pstrut" style="height:3em"></span><span class="frac-line" style="border-bottom-width:0.04em"></span></span><span style="top:-3.394em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight">4</span><span class="mbin mtight">−</span><span class="mord mtight">9</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.538em"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:1.1901em;vertical-align:-0.345em"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8451em"><span style="top:-2.655em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">13</span></span></span></span><span style="top:-3.23em"><span class="pstrut" style="height:3em"></span><span class="frac-line" style="border-bottom-width:0.04em"></span></span><span style="top:-3.394em"><span class="pstrut" style="height:3em"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight">13</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em"></span></span><span class="base"><span class="strut" style="height:0.7278em;vertical-align:-0.0833em"></span><span class="mord">−</span><span class="mord">1</span></span></span></span></p>
<h2 id="complete-typescript-solution">Complete TypeScript Solution<a class="heading-link" aria-label="Link to section" href="#complete-typescript-solution"><span class="heading-link-icon">#</span></a></h2>
<p>Here’s a complete TypeScript solution that includes our cosine similarity function along with some utility methods:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#BB9AF7">class</span><span style="color:#C0CAF5"> VectorUtils</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Calculates the cosine similarity between two vectors</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  static</span><span style="color:#7AA2F7"> cosineSimilarity</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">vecA</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> vecB</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">[])</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">vecA</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#BB9AF7"> !==</span><span style="color:#C0CAF5"> vecB</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">      throw</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Error</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#89DDFF">        `</span><span style="color:#9ECE6A">Vector dimensions don&#39;t match: </span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">vecA</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A"> vs </span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">vecB</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span></span>
<span class="line"><span style="color:#9ABDF5">      )</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> dotProduct</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> vecA</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">reduce</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">sum</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> a</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> i</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> sum</span><span style="color:#89DDFF"> +</span><span style="color:#C0CAF5"> a</span><span style="color:#89DDFF"> *</span><span style="color:#C0CAF5"> vecB</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">i</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> magnitudeA</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">hypot</span><span style="color:#9ABDF5">(</span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">vecA</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> magnitudeB</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">hypot</span><span style="color:#9ABDF5">(</span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">vecB</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">magnitudeA</span><span style="color:#BB9AF7"> ===</span><span style="color:#FF9E64"> 0</span><span style="color:#BB9AF7"> ||</span><span style="color:#C0CAF5"> magnitudeB</span><span style="color:#BB9AF7"> ===</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#C0CAF5"> dotProduct</span><span style="color:#89DDFF"> /</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">magnitudeA</span><span style="color:#89DDFF"> *</span><span style="color:#C0CAF5"> magnitudeB</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Calculates the dot product of two vectors</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  static</span><span style="color:#7AA2F7"> dotProduct</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">vecA</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> vecB</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">[])</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">vecA</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#BB9AF7"> !==</span><span style="color:#C0CAF5"> vecB</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">      throw</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Error</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#89DDFF">        `</span><span style="color:#9ECE6A">Vector dimensions don&#39;t match: </span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">vecA</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A"> vs </span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">vecB</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span></span>
<span class="line"><span style="color:#9ABDF5">      )</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#C0CAF5"> vecA</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">reduce</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">sum</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> a</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> i</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> sum</span><span style="color:#89DDFF"> +</span><span style="color:#C0CAF5"> a</span><span style="color:#89DDFF"> *</span><span style="color:#C0CAF5"> vecB</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">i</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Calculates the magnitude (length) of a vector</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  static</span><span style="color:#7AA2F7"> magnitude</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">vec</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">[])</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">hypot</span><span style="color:#9ABDF5">(</span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">vec</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Normalizes a vector (converts to unit vector)</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  static</span><span style="color:#7AA2F7"> normalize</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">vec</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">[])</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">[]</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> mag</span><span style="color:#89DDFF"> =</span><span style="color:#F7768E"> this</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">magnitude</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">vec</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">mag</span><span style="color:#BB9AF7"> ===</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#7AA2F7"> Array</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">vec</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">fill</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#C0CAF5"> vec</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">map</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">v</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> v</span><span style="color:#89DDFF"> /</span><span style="color:#C0CAF5"> mag</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  /**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   * Converts cosine similarity to angular distance in degrees</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">   */</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  static</span><span style="color:#7AA2F7"> similarityToDegrees</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">similarity</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // Clamp similarity to [-1, 1] to handle floating point errors</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> clampedSimilarity</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">max</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">-</span><span style="color:#FF9E64">1</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">min</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">1</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> similarity</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">acos</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">clampedSimilarity</span><span style="color:#9ABDF5">) </span><span style="color:#89DDFF">*</span><span style="color:#9ABDF5"> (</span><span style="color:#FF9E64">180</span><span style="color:#89DDFF"> /</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#FF9E64">PI</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="class VectorUtils {
  /**
   * Calculates the cosine similarity between two vectors
   */
  static cosineSimilarity(vecA: number[], vecB: number[]): number {
    if (vecA.length !== vecB.length) {
      throw new Error(
        `Vector dimensions don't match: ${vecA.length} vs ${vecB.length}`
      );
    }

    const dotProduct = vecA.reduce((sum, a, i) => sum + a * vecB[i], 0);
    const magnitudeA = Math.hypot(...vecA);
    const magnitudeB = Math.hypot(...vecB);

    if (magnitudeA === 0 || magnitudeB === 0) {
      return 0;
    }

    return dotProduct / (magnitudeA * magnitudeB);
  }

  /**
   * Calculates the dot product of two vectors
   */
  static dotProduct(vecA: number[], vecB: number[]): number {
    if (vecA.length !== vecB.length) {
      throw new Error(
        `Vector dimensions don't match: ${vecA.length} vs ${vecB.length}`
      );
    }

    return vecA.reduce((sum, a, i) => sum + a * vecB[i], 0);
  }

  /**
   * Calculates the magnitude (length) of a vector
   */
  static magnitude(vec: number[]): number {
    return Math.hypot(...vec);
  }

  /**
   * Normalizes a vector (converts to unit vector)
   */
  static normalize(vec: number[]): number[] {
    const mag = this.magnitude(vec);

    if (mag === 0) {
      return Array(vec.length).fill(0);
    }

    return vec.map(v => v / mag);
  }

  /**
   * Converts cosine similarity to angular distance in degrees
   */
  static similarityToDegrees(similarity: number): number {
    // Clamp similarity to [-1, 1] to handle floating point errors
    const clampedSimilarity = Math.max(-1, Math.min(1, similarity));
    return Math.acos(clampedSimilarity) * (180 / Math.PI);
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="using-cosine-similarity-in-real-web-applications">Using Cosine Similarity in Real Web Applications<a class="heading-link" aria-label="Link to section" href="#using-cosine-similarity-in-real-web-applications"><span class="heading-link-icon">#</span></a></h2>
<p>When you work with AI in web applications, you’ll often need to calculate similarity between vectors. Here’s a practical example:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Example: Semantic search implementation</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> semanticSearch</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">  queryEmbedding</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  documentEmbeddings</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> DocumentWithEmbedding</span><span style="color:#9ABDF5">[]</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> SearchResult</span><span style="color:#9ABDF5">[]</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> documentEmbeddings</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">map</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">doc</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> ({</span></span>
<span class="line"><span style="color:#73DACA">      document</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> doc</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      relevance</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> VectorUtils</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">cosineSimilarity</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">queryEmbedding</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> doc</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">embedding</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }))</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">filter</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">result</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> result</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">relevance</span><span style="color:#BB9AF7"> &gt;</span><span style="color:#FF9E64"> 0.7</span><span style="color:#9ABDF5">) </span><span style="color:#51597D;font-style:italic">// Only consider relevant results</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">sort</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">a</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> b</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> b</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">relevance</span><span style="color:#89DDFF"> -</span><span style="color:#C0CAF5"> a</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">relevance</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// Example: Semantic search implementation
function semanticSearch(
  queryEmbedding: number[],
  documentEmbeddings: DocumentWithEmbedding[]
): SearchResult[] {
  return documentEmbeddings
    .map(doc => ({
      document: doc,
      relevance: VectorUtils.cosineSimilarity(queryEmbedding, doc.embedding),
    }))
    .filter(result => result.relevance > 0.7) // Only consider relevant results
    .sort((a, b) => b.relevance - a.relevance);
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="using-openai-embedding-models-with-cosine-similarity">Using OpenAI Embedding Models with Cosine Similarity<a class="heading-link" aria-label="Link to section" href="#using-openai-embedding-models-with-cosine-similarity"><span class="heading-link-icon">#</span></a></h2>
<p>While the examples above used simple vectors for clarity, real-world AI applications typically use embedding models that transform text and other data into high-dimensional vector spaces.</p>
<p>OpenAI provides powerful embedding models that you can easily incorporate into your applications. These models transform text into vectors with hundreds or thousands of dimensions that capture semantic meaning:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Example of using OpenAI embeddings with our cosine similarity function</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> compareTextSimilarity</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">  textA</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  textB</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">number</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Get embeddings from OpenAI API</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> responseA</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> fetch</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">https://api.openai.com/v1/embeddings</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    method</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">POST</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    headers</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      Authorization</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> `</span><span style="color:#9ECE6A">Bearer </span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">process</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">env</span><span style="color:#89DDFF">.</span><span style="color:#FF9E64">OPENAI_API_KEY</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#9ECE6A">Content-Type</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">application/json</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    body</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> JSON</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">stringify</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">      model</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">text-embedding-3-large</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      input</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> textA</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> responseB</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> fetch</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">https://api.openai.com/v1/embeddings</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    method</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">POST</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    headers</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      Authorization</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> `</span><span style="color:#9ECE6A">Bearer </span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">process</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">env</span><span style="color:#89DDFF">.</span><span style="color:#FF9E64">OPENAI_API_KEY</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#9ECE6A">Content-Type</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">application/json</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    body</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> JSON</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">stringify</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">      model</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">text-embedding-3-large</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      input</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> textB</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> embeddingA</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7;font-style:italic">await</span><span style="color:#C0CAF5"> responseA</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">json</span><span style="color:#9ABDF5">())</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">data</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">embedding</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> embeddingB</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7;font-style:italic">await</span><span style="color:#C0CAF5"> responseB</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">json</span><span style="color:#9ABDF5">())</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">data</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">embedding</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Calculate similarity using our function</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> VectorUtils</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">cosineSimilarity</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">embeddingA</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> embeddingB</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// Example of using OpenAI embeddings with our cosine similarity function
async function compareTextSimilarity(
  textA: string,
  textB: string
): Promise<number> {
  // Get embeddings from OpenAI API
  const responseA = await fetch(&#34;https://api.openai.com/v1/embeddings&#34;, {
    method: &#34;POST&#34;,
    headers: {
      Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
      &#34;Content-Type&#34;: &#34;application/json&#34;,
    },
    body: JSON.stringify({
      model: &#34;text-embedding-3-large&#34;,
      input: textA,
    }),
  });

  const responseB = await fetch(&#34;https://api.openai.com/v1/embeddings&#34;, {
    method: &#34;POST&#34;,
    headers: {
      Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
      &#34;Content-Type&#34;: &#34;application/json&#34;,
    },
    body: JSON.stringify({
      model: &#34;text-embedding-3-large&#34;,
      input: textB,
    }),
  });

  const embeddingA = (await responseA.json()).data[0].embedding;
  const embeddingB = (await responseB.json()).data[0].embedding;

  // Calculate similarity using our function
  return VectorUtils.cosineSimilarity(embeddingA, embeddingB);
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="alert alert-warning astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">⚠️</span> Warning </p> <div class="alert-content astro-7kdbuayl"> <p>In a production environment, you should pre-compute embeddings for your
content (like blog posts, products, or documents) and store them in a vector
database (like Pinecone, Qdrant, or Milvus). Re-computing embeddings for every
user request as shown in this example wastes resources and slows performance.
A better approach: embed your content once during indexing, store the vectors,
and only embed the user’s query when performing a search.</p> </div> </div> 
<p>OpenAI’s latest embedding models like <code>text-embedding-3-large</code> have up to 3,072 dimensions, capturing extremely nuanced semantic relationships between words and concepts. These high-dimensional embeddings enable much more accurate similarity measurements than simpler vector representations.</p>
<p>For more information on OpenAI’s embedding models, including best practices and implementation details, check out their documentation at <a href="https://platform.openai.com/docs/guides/embeddings" rel="noopener noreferrer" target="_blank">https://platform.openai.com/docs/guides/embeddings</a>.</p>
<h2 id="conclusion">Conclusion<a class="heading-link" aria-label="Link to section" href="#conclusion"><span class="heading-link-icon">#</span></a></h2>
<p>Understanding vectors and cosine similarity provides practical tools that empower you to work effectively with modern AI features. By implementing these concepts in TypeScript, you gain a deeper understanding and precise control over calculating similarity in your applications.
The interactive visualizations we’ve explored help you build intuition about these mathematical concepts, while the TypeScript implementation gives you the tools to apply them in real-world scenarios.
Whether you build recommendation systems, semantic search, or content-matching features, the foundation you’ve gained here will help you implement more intelligent, accurate, and effective AI-powered features in your web applications.</p>
<h2 id="join-the-discussion">Join the Discussion<a class="heading-link" aria-label="Link to section" href="#join-the-discussion"><span class="heading-link-icon">#</span></a></h2>
<p>This article has sparked interesting discussions across different platforms. Join the conversation to share your thoughts, ask questions, or learn from others’ perspectives about implementing cosine similarity in AI applications.</p>
<ul>
<li><a href="https://news.ycombinator.com/item?id=43307541" rel="noopener noreferrer" target="_blank">Join the discussion on Hacker News →</a></li>
<li><a href="https://www.reddit.com/r/typescript/comments/1j73whg/how_to_implement_a_cosine_similarity_function_in/" rel="noopener noreferrer" target="_blank">Discuss on Reddit r/typescript →</a></li>
</ul>
<hr/> </article> <astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/typescript/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">typescript</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/mathematics/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">mathematics</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/semantic-related-posts-astro-transformersjs/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">No Server, No Database: Smarter Related Posts in Astro with `transformers.js`</h3> <p class="related-post-description astro-vj4tpspi"> How I used Hugging Face embeddings to create smart “Related Posts” for my Astro blog—no backend, no database, just TypeScript. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-05-18T00:00:00.000Z">May 18, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> ai </span> </div> </div> </a><a href="/posts/are-llms-creative/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Are LLMs Creative?</h3> <p class="related-post-description astro-vj4tpspi"> Exploring the fundamental nature of creativity in Large Language Models compared to human creativity, sparked by reflections on OpenAI&#39;s latest image model. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-04-01T00:00:00.000Z">Apr 1, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> ai </span> </div> </div> </a><a href="/posts/xml-tagged-prompts-framework-reliable-ai-responses/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">XML-Style Tagged Prompts: A Framework for Reliable AI Responses</h3> <p class="related-post-description astro-vj4tpspi"> Learn how top AI engineers use XML-style prompts to consistently get structured, accurate responses from ChatGPT, Claude, and other LLMs. Step-by-step guide with real examples </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2024-12-22T00:00:00.000Z">Dec 22, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> ai </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison";

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
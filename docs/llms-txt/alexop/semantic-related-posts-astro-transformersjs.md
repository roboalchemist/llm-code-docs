# Source: https://alexop.dev/posts/semantic-related-posts-astro-transformersjs

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/semantic-related-posts-astro-transformersjs/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>No Server, No Database: Smarter Related Posts in Astro with `transformers.js` | alexop.dev</title><meta name="title" content="No Server, No Database: Smarter Related Posts in Astro with `transformers.js` | alexop.dev"><meta name="description" content="How I used Hugging Face embeddings to create smart “Related Posts” for my Astro blog—no backend, no database, just TypeScript."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="No Server, No Database: Smarter Related Posts in Astro with `transformers.js` | alexop.dev"><meta property="og:description" content="How I used Hugging Face embeddings to create smart “Related Posts” for my Astro blog—no backend, no database, just TypeScript."><meta property="og:url" content="https://alexop.dev/posts/semantic-related-posts-astro-transformersjs/"><meta property="og:image" content="https://alexop.dev/posts/no-server-no-database-smarter-related-posts-in-astro-with-transformers-js/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-05-18T00:00:00.000Z"><meta property="article:modified_time" content="2025-05-18T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/semantic-related-posts-astro-transformersjs/"><meta property="twitter:title" content="No Server, No Database: Smarter Related Posts in Astro with `transformers.js` | alexop.dev"><meta property="twitter:description" content="How I used Hugging Face embeddings to create smart “Related Posts” for my Astro blog—no backend, no database, just TypeScript."><meta property="twitter:image" content="https://alexop.dev/posts/no-server-no-database-smarter-related-posts-in-astro-with-transformers-js/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"No Server, No Database: Smarter Related Posts in Astro with `transformers.js` | alexop.dev","description":"How I used Hugging Face embeddings to create smart “Related Posts” for my Astro blog—no backend, no database, just TypeScript.","image":"https://alexop.dev/posts/no-server-no-database-smarter-related-posts-in-astro-with-transformers-js/index.png","datePublished":"2025-05-18T00:00:00.000Z","dateModified":"2025-05-18T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: no-server-no-database-smarter-related-posts-in-astro-with-transformers-js; }@layer astro { ::view-transition-old(no-server-no-database-smarter-related-posts-in-astro-with-transformers-js) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(no-server-no-database-smarter-related-posts-in-astro-with-transformers-js) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(no-server-no-database-smarter-related-posts-in-astro-with-transformers-js) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(no-server-no-database-smarter-related-posts-in-astro-with-transformers-js) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: ai; }@layer astro { ::view-transition-old(ai) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: astro; }@layer astro { ::view-transition-old(astro) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">No Server, No Database: Smarter Related Posts in Astro with `transformers.js`</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-05-18T00:00:00.000Z">May 18, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Z1q2jyz" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;No Server, No Database: Smarter Related Posts in Astro with `transformers.js`&quot;],&quot;content&quot;:[0,&quot;I recently read a interesting blog post about Embeddings at [Embeddings in Technical Writing](https://technicalwriting.dev/ml/embeddings/overview.html):\n\n&gt; “I could tell you exactly how to advance technical writing with embeddings, but where’s the fun in that?”\n\nChallenge accepted!\nIn this post, I show how I used **Hugging Face’s `transformers.js`** to create smarter related-post suggestions for my Astro blog, without servers or databases.\n\n## Why Embeddings Are Better Than Tags\n\nTags group posts by labels, but not by meaning. Posts about Vue 3 and deep reactivity concepts get mixed up together.\nEmbeddings capture the meaning of text using numeric vectors. Two posts become related when their content is similar, not just when tags match.\n\n### Vectors and Cosine Similarity\n\nWords like “cat” and “kitty” are close in meaning, while “dog” is slightly different:\n\n| word  | vector     |\n| ----- | ---------- |\n| cat   | `[0, 1]`   |\n| kitty | `[0, 0.9]` |\n| dog   | `[1, -1]`  |\n\nCosine similarity measures how similar these vectors are.\nFor a deeper dive into TypeScript and vectors, check out my post on [How to Implement a Cosine Similarity Function in TypeScript for Vector Comparison](../how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison/).\n\n## Transformers.js in Action\n\n`transformers.js` lets you run Hugging Face models directly in JavaScript:\n\n```ts\nimport { pipeline } from \&quot;@huggingface/transformers\&quot;;\n\nconst model = \&quot;sentence-transformers/all-MiniLM-L6-v2\&quot;;\nconst extractor = await pipeline(\&quot;feature-extraction\&quot;, model);\n\nconst embedding = await extractor(\&quot;Hello, world!\&quot;, {\n  pooling: \&quot;mean\&quot;,\n  normalize: true,\n});\n\nconsole.log(embedding); // Float32Array with 384 dimensions\n```\n\nYou don&#39;t need Python or a server. Everything runs in your browser or Node.js.\n\n## My Simple Workflow\n\nHere&#39;s how my workflow works:\n\n1. Load markdown files (`.md` or `.mdx`) from my blog.\n2. Remove markdown formatting to get plain text.\n3. Use `transformers.js` to create embeddings.\n4. Calculate cosine similarity between all posts.\n5. Find the top 5 most related posts for each post.\n6. Save the results in a JSON file (`similarities.json`).\n7. Display these related posts with Astro.\n\n### Main Script (TypeScript)\n\n```ts\nimport { pipeline, FeatureExtractionPipeline } from \&quot;@huggingface/transformers\&quot;;\nimport chalk from \&quot;chalk\&quot;;\nimport fs from \&quot;fs\&quot;;\nimport { glob } from \&quot;glob\&quot;;\nimport matter from \&quot;gray-matter\&quot;;\nimport { remark } from \&quot;remark\&quot;;\nimport strip from \&quot;strip-markdown\&quot;;\nimport path from \&quot;path\&quot;;\n\n// --------- Configurations ---------\nconst GLOB = \&quot;src/content/**/*.{md,mdx}\&quot;; // Where to find Markdown content\nconst OUT = \&quot;src/assets/similarities.json\&quot;; // Output file for results\nconst TOP_N = 5; // Number of similar docs to keep\nconst MODEL = \&quot;Snowflake/snowflake-arctic-embed-m-v2.0\&quot;; // Embedding model\n\n// --------- Type Definitions ---------\ninterface Frontmatter {\n  slug: string;\n  [k: string]: unknown;\n}\ninterface Document {\n  path: string;\n  content: string;\n  frontmatter: Frontmatter;\n}\ninterface SimilarityResult extends Frontmatter {\n  path: string;\n  similarity: number;\n}\n\n// --------- Utils ---------\n\n/**\n * Normalizes a vector to unit length (L2 norm == 1)\n * This makes cosine similarity a simple dot product!\n */\nfunction normalize(vec: Float32Array): Float32Array {\n  let len = Math.hypot(...vec); // L2 norm\n  if (!len) return vec;\n  return new Float32Array(vec.map(x =&gt; x / len));\n}\n\n/**\n * Computes dot product of two same-length vectors.\n * Vectors MUST be normalized before using this for cosine similarity!\n */\nconst dot = (a: Float32Array, b: Float32Array) =&gt;\n  a.reduce((sum, ai, i) =&gt; sum + ai * b[i], 0);\n\n/**\n * Strips markdown formatting, import/export lines, headings, tables, etc.\n * Returns plain text for semantic analysis.\n */\nconst getPlainText = async (md: string) =&gt; {\n  let txt = String(await remark().use(strip).process(md))\n    .replace(/^import .*?$/gm, \&quot;\&quot;)\n    .replace(/^export .*?$/gm, \&quot;\&quot;)\n    .replace(\n      /^\\s*(TLDR|Introduction|Conclusion|Summary|Quick Setup Guide|Rules?)\\s*$/gim,\n      \&quot;\&quot;\n    )\n    .replace(/^[A-Z\\s]{4,}$/gm, \&quot;\&quot;)\n    .replace(/^\\|.*\\|$/gm, \&quot;\&quot;)\n    .replace(/(Rule\\s\\d+:.*)(?=\\s*Rule\\s\\d+:)/g, \&quot;$1\\n\&quot;)\n    .replace(/\\n{3,}/g, \&quot;\\n\\n\&quot;)\n    .replace(/\\n{2}/g, \&quot;\\n\\n\&quot;)\n    .replace(/\\n/g, \&quot; \&quot;)\n    .replace(/\\s{2,}/g, \&quot; \&quot;)\n    .trim();\n  return txt;\n};\n\n/**\n * Parses and validates a single Markdown file.\n * - Extracts frontmatter (slug, etc.)\n * - Converts content to plain text\n * - Skips drafts or files with no slug\n */\nasync function processFile(path: string): Promise&lt;Document | null&gt; {\n  try {\n    const { content, data } = matter(fs.readFileSync(path, \&quot;utf-8\&quot;));\n    if (!data.slug || data.draft) return null;\n    const plain = await getPlainText(content);\n    return { path, content: plain, frontmatter: data as Frontmatter };\n  } catch {\n    return null;\n  }\n}\n\n/**\n * Processes an array of Markdown file paths into Documents\n */\nasync function loadDocs(paths: string[]) {\n  const docs: Document[] = [];\n  for (const p of paths) {\n    const d = await processFile(p);\n    if (d) docs.push(d);\n  }\n  return docs;\n}\n\n/**\n * Generates vector embeddings for each document&#39;s plain text.\n * - Uses HuggingFace model\n * - Normalizes each vector for fast cosine similarity search\n */\nasync function embedDocs(\n  docs: Document[],\n  extractor: FeatureExtractionPipeline\n) {\n  if (!docs.length) return [];\n  // Don&#39;t let the model normalize, we do it manually for safety\n  const res = (await extractor(\n    docs.map(d =&gt; d.content),\n    { pooling: \&quot;mean\&quot;, normalize: false }\n  )) as any;\n  const [n, dim] = res.dims;\n  // Each embedding vector is normalized for performance\n  return Array.from({ length: n }, (_, i) =&gt;\n    normalize(res.data.slice(i * dim, (i + 1) * dim))\n  );\n}\n\n/**\n * Computes the top-N most similar documents for the given document index.\n * - Uses dot product of normalized vectors for cosine similarity\n * - Returns only the top-N\n */\nfunction topSimilar(\n  idx: number,\n  docs: Document[],\n  embs: Float32Array[],\n  n: number\n): SimilarityResult[] {\n  return docs\n    .map((d, j) =&gt;\n      j === idx\n        ? null\n        : {\n            ...d.frontmatter,\n            path: d.path,\n            similarity: +dot(embs[idx], embs[j]).toFixed(2), // higher = more similar\n          }\n    )\n    .filter(Boolean)\n    .sort((a, b) =&gt; (b as any).similarity - (a as any).similarity)\n    .slice(0, n) as SimilarityResult[];\n}\n\n/**\n * Computes all similarities for every document, returns as {slug: SimilarityResult[]} map.\n */\nfunction allSimilarities(docs: Document[], embs: Float32Array[], n: number) {\n  return Object.fromEntries(\n    docs.map((d, i) =&gt; [d.frontmatter.slug, topSimilar(i, docs, embs, n)])\n  );\n}\n\n/**\n * Saves result object as JSON file.\n * - Ensures output directory exists.\n */\nasync function saveJson(obj: any, out: string) {\n  fs.mkdirSync(path.dirname(out), { recursive: true });\n  fs.writeFileSync(out, JSON.stringify(obj, null, 2));\n}\n\n// --------- Main Execution Flow ---------\nasync function main() {\n  try {\n    // 1. Load transformer model for embeddings\n    const extractor = await pipeline(\&quot;feature-extraction\&quot;, MODEL);\n\n    // 2. Find all Markdown files\n    const files = await glob(GLOB);\n    if (!files.length)\n      return console.log(chalk.yellow(\&quot;No content files found.\&quot;));\n\n    // 3. Parse and process all files\n    const docs = await loadDocs(files);\n    if (!docs.length) return console.log(chalk.red(\&quot;No documents loaded.\&quot;));\n\n    // 4. Generate &amp; normalize embeddings\n    const embs = await embedDocs(docs, extractor);\n    if (!embs.length) return console.log(chalk.red(\&quot;No embeddings.\&quot;));\n\n    // 5. Calculate similarities for each doc\n    const results = allSimilarities(docs, embs, TOP_N);\n\n    // 6. Save results to disk\n    await saveJson(results, OUT);\n    console.log(chalk.green(`Similarity results saved to ${OUT}`));\n  } catch (e) {\n    console.error(chalk.red(\&quot;Error:\&quot;), e);\n    process.exitCode = 1;\n  }\n}\n\nmain();\n```\n\n## This Will Produce a JSON file with the following structure:\n\n```json\n{\n  \&quot;vue-introduction\&quot;: [\n    {\n      \&quot;slug\&quot;: \&quot;typescript-advanced-types\&quot;,\n      \&quot;title\&quot;: \&quot;Advanced Types in TypeScript\&quot;,\n      \&quot;date\&quot;: \&quot;2024-06-03T00:00:00.000Z\&quot;,\n      \&quot;path\&quot;: \&quot;src/content/typescript-advanced-types.md\&quot;,\n      \&quot;similarity\&quot;: 0.35\n    }\n    // Additional similar documents...\n  ]\n  // Additional document entries...\n}\n```\n\n### Astro Component\n\n```astro\n---\nimport sims from \&quot;../assets/similarities.json\&quot;;\n\nif (similarities[post.slug]) {\n  mostRelatedPosts = similarities[post.slug]\n    .filter((p: RelatedPost) =&gt; !p.draft)\n    .sort(\n      (a: RelatedPost, b: RelatedPost) =&gt;\n        (b.similarity ?? 0) - (a.similarity ?? 0)\n    )\n    .slice(0, 3);\n}\n---\n\n{\n  mostRelatedPosts.length &gt; 0 &amp;&amp; (\n    &lt;div data-pagefind-ignore class=\&quot;mb-8 mt-16\&quot;&gt;\n      &lt;h2 class=\&quot;mb-6 text-3xl font-bold text-skin-accent\&quot;&gt;\n        Most Related Posts\n      &lt;/h2&gt;\n      &lt;div class=\&quot;md:grid-cols-3 grid grid-cols-1 gap-6\&quot;&gt;\n        {mostRelatedPosts.map((relatedPost: RelatedPost) =&gt; (\n          &lt;a\n            href={`/posts/${relatedPost.slug}/`}\n            class=\&quot;related-post-card group\&quot;\n          &gt;\n            &lt;div class=\&quot;p-5\&quot;&gt;\n              &lt;h3 class=\&quot;related-post-title\&quot;&gt;{relatedPost.title}&lt;/h3&gt;\n              &lt;p class=\&quot;related-post-description\&quot;&gt;{relatedPost.description}&lt;/p&gt;\n              &lt;div class=\&quot;flex items-center justify-between text-xs text-skin-base text-opacity-60\&quot;&gt;\n                &lt;Datetime\n                  pubDatetime={relatedPost.pubDatetime}\n                  modDatetime={relatedPost.modDatetime}\n                  size=\&quot;sm\&quot;\n                /&gt;\n                &lt;span class=\&quot;related-post-tag\&quot;&gt;{relatedPost.tags?.[0]}&lt;/span&gt;\n              &lt;/div&gt;\n            &lt;/div&gt;\n          &lt;/a&gt;\n        ))}\n      &lt;/div&gt;\n    &lt;/div&gt;\n  )\n}\n```\n\n## Does It Work?\n\nYes! Now, my blog suggests truly related content, not random posts.\n\n---\n\n## What I Learned\n\n- **No extra servers or databases**: Everything runs during build time.\n- **Easy to use**: Works in both browsers and Node.js.\n- **Flexible**: Quickly change the model or method.\n\nIf you have a static blog and want better recommendations, give embeddings and Astro a try. Let me know how it goes!\n\nOf course, this is far from perfect. I also don&#39;t know which model would be ideal, but at the moment I&#39;m getting much better related posts than before, so I&#39;m happy with the results.\nIf you want to play with the script yourself check out [post-matcher-ai](https://github.com/alexanderop/post-matcher-ai)&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>I recently read a interesting blog post about Embeddings at <a href="https://technicalwriting.dev/ml/embeddings/overview.html" rel="noopener noreferrer" target="_blank">Embeddings in Technical Writing</a>:</p>
<blockquote>
<p>“I could tell you exactly how to advance technical writing with embeddings, but where’s the fun in that?”</p>
</blockquote>
<p>Challenge accepted!
In this post, I show how I used <strong>Hugging Face’s <code>transformers.js</code></strong> to create smarter related-post suggestions for my Astro blog, without servers or databases.</p>
<h2 id="why-embeddings-are-better-than-tags">Why Embeddings Are Better Than Tags<a class="heading-link" aria-label="Link to section" href="#why-embeddings-are-better-than-tags"><span class="heading-link-icon">#</span></a></h2>
<p>Tags group posts by labels, but not by meaning. Posts about Vue 3 and deep reactivity concepts get mixed up together.
Embeddings capture the meaning of text using numeric vectors. Two posts become related when their content is similar, not just when tags match.</p>
<h3 id="vectors-and-cosine-similarity">Vectors and Cosine Similarity<a class="heading-link" aria-label="Link to section" href="#vectors-and-cosine-similarity"><span class="heading-link-icon">#</span></a></h3>
<p>Words like “cat” and “kitty” are close in meaning, while “dog” is slightly different:</p>





















<table><thead><tr><th>word</th><th>vector</th></tr></thead><tbody><tr><td data-label="word">cat</td><td data-label="vector"><code>[0, 1]</code></td></tr><tr><td data-label="word">kitty</td><td data-label="vector"><code>[0, 0.9]</code></td></tr><tr><td data-label="word">dog</td><td data-label="vector"><code>[1, -1]</code></td></tr></tbody></table>
<p>Cosine similarity measures how similar these vectors are.
For a deeper dive into TypeScript and vectors, check out my post on <a href="../how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison/">How to Implement a Cosine Similarity Function in TypeScript for Vector Comparison</a>.</p>
<h2 id="transformersjs-in-action">Transformers.js in Action<a class="heading-link" aria-label="Link to section" href="#transformersjs-in-action"><span class="heading-link-icon">#</span></a></h2>
<p><code>transformers.js</code> lets you run Hugging Face models directly in JavaScript:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">pipeline</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@huggingface/transformers</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> model</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">sentence-transformers/all-MiniLM-L6-v2</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> extractor</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> pipeline</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">feature-extraction</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> model</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> embedding</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> extractor</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Hello, world!</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  pooling</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">mean</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  normalize</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">embedding</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Float32Array with 384 dimensions</span></span></code><button type="button" class="copy" data-code="import { pipeline } from &#34;@huggingface/transformers&#34;;

const model = &#34;sentence-transformers/all-MiniLM-L6-v2&#34;;
const extractor = await pipeline(&#34;feature-extraction&#34;, model);

const embedding = await extractor(&#34;Hello, world!&#34;, {
  pooling: &#34;mean&#34;,
  normalize: true,
});

console.log(embedding); // Float32Array with 384 dimensions" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>You don’t need Python or a server. Everything runs in your browser or Node.js.</p>
<h2 id="my-simple-workflow">My Simple Workflow<a class="heading-link" aria-label="Link to section" href="#my-simple-workflow"><span class="heading-link-icon">#</span></a></h2>
<p>Here’s how my workflow works:</p>
<ol>
<li>Load markdown files (<code>.md</code> or <code>.mdx</code>) from my blog.</li>
<li>Remove markdown formatting to get plain text.</li>
<li>Use <code>transformers.js</code> to create embeddings.</li>
<li>Calculate cosine similarity between all posts.</li>
<li>Find the top 5 most related posts for each post.</li>
<li>Save the results in a JSON file (<code>similarities.json</code>).</li>
<li>Display these related posts with Astro.</li>
</ol>
<h3 id="main-script-typescript">Main Script (TypeScript)<a class="heading-link" aria-label="Link to section" href="#main-script-typescript"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">pipeline</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> FeatureExtractionPipeline</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@huggingface/transformers</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> chalk</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">chalk</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> fs</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">fs</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">glob</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">glob</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> matter</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">gray-matter</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">remark</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">remark</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> strip</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">strip-markdown</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> path</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">path</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// --------- Configurations ---------</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> GLOB</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">src/content/**/*.{md,mdx}</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Where to find Markdown content</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> OUT</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">src/assets/similarities.json</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Output file for results</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> TOP_N</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 5</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Number of similar docs to keep</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> MODEL</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Snowflake/snowflake-arctic-embed-m-v2.0</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Embedding model</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// --------- Type Definitions ---------</span></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> Frontmatter</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  slug</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  [</span><span style="color:#E0AF68">k</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> unknown</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> Document</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  path</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  content</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  frontmatter</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Frontmatter</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> SimilarityResult</span><span style="color:#9D7CD8;font-style:italic"> extends</span><span style="color:#BB9AF7"> Frontmatter</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  path</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  similarity</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// --------- Utils ---------</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Normalizes a vector to unit length (L2 norm == 1)</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * This makes cosine similarity a simple dot product!</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> normalize</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">vec</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Float32Array</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Float32Array</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> len</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">hypot</span><span style="color:#9ABDF5">(</span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">vec</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // L2 norm</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">len</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#C0CAF5"> vec</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Float32Array</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">vec</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">map</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">x</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> x</span><span style="color:#89DDFF"> /</span><span style="color:#C0CAF5"> len</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Computes dot product of two same-length vectors.</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Vectors MUST be normalized before using this for cosine similarity!</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#7AA2F7"> dot</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">a</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Float32Array</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> b</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Float32Array</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span></span>
<span class="line"><span style="color:#C0CAF5">  a</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">reduce</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">sum</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> ai</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> i</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> sum</span><span style="color:#89DDFF"> +</span><span style="color:#C0CAF5"> ai</span><span style="color:#89DDFF"> *</span><span style="color:#C0CAF5"> b</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">i</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Strips markdown formatting, import/export lines, headings, tables, etc.</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Returns plain text for semantic analysis.</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#7AA2F7"> getPlainText</span><span style="color:#89DDFF"> =</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">md</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> txt</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> String</span><span style="color:#9ABDF5">(</span><span style="color:#BB9AF7;font-style:italic">await</span><span style="color:#7AA2F7"> remark</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">use</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">strip</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">process</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">md</span><span style="color:#9ABDF5">))</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">replace</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">/</span><span style="color:#BB9AF7">^</span><span style="color:#B4F9F8">import </span><span style="color:#BB9AF7">.</span><span style="color:#89DDFF">*?</span><span style="color:#BB9AF7">$</span><span style="color:#89DDFF">/gm</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;&quot;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">replace</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">/</span><span style="color:#BB9AF7">^</span><span style="color:#B4F9F8">export </span><span style="color:#BB9AF7">.</span><span style="color:#89DDFF">*?</span><span style="color:#BB9AF7">$</span><span style="color:#89DDFF">/gm</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;&quot;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">replace</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#89DDFF">      /</span><span style="color:#BB9AF7">^\s</span><span style="color:#89DDFF">*</span><span style="color:#F7768E">(</span><span style="color:#B4F9F8">TLDR</span><span style="color:#BB9AF7">|</span><span style="color:#B4F9F8">Introduction</span><span style="color:#BB9AF7">|</span><span style="color:#B4F9F8">Conclusion</span><span style="color:#BB9AF7">|</span><span style="color:#B4F9F8">Summary</span><span style="color:#BB9AF7">|</span><span style="color:#B4F9F8">Quick Setup Guide</span><span style="color:#BB9AF7">|</span><span style="color:#B4F9F8">Rules</span><span style="color:#89DDFF">?</span><span style="color:#F7768E">)</span><span style="color:#BB9AF7">\s</span><span style="color:#89DDFF">*</span><span style="color:#BB9AF7">$</span><span style="color:#89DDFF">/gim</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;&quot;</span></span>
<span class="line"><span style="color:#9ABDF5">    )</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">replace</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">/</span><span style="color:#BB9AF7">^</span><span style="color:#E0AF68">[A-Z</span><span style="color:#BB9AF7">\s</span><span style="color:#E0AF68">]</span><span style="color:#89DDFF">{4,}</span><span style="color:#BB9AF7">$</span><span style="color:#89DDFF">/gm</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;&quot;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">replace</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">/</span><span style="color:#BB9AF7">^</span><span style="color:#C0CAF5">\|</span><span style="color:#BB9AF7">.</span><span style="color:#89DDFF">*</span><span style="color:#C0CAF5">\|</span><span style="color:#BB9AF7">$</span><span style="color:#89DDFF">/gm</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;&quot;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">replace</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">/</span><span style="color:#F7768E">(</span><span style="color:#B4F9F8">Rule</span><span style="color:#BB9AF7">\s\d</span><span style="color:#89DDFF">+</span><span style="color:#B4F9F8">:</span><span style="color:#BB9AF7">.</span><span style="color:#89DDFF">*</span><span style="color:#F7768E">)(?=</span><span style="color:#BB9AF7">\s</span><span style="color:#89DDFF">*</span><span style="color:#B4F9F8">Rule</span><span style="color:#BB9AF7">\s\d</span><span style="color:#89DDFF">+</span><span style="color:#B4F9F8">:</span><span style="color:#F7768E">)</span><span style="color:#89DDFF">/g</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">$1</span><span style="color:#89DDFF">\n&quot;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">replace</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">/</span><span style="color:#BB9AF7">\n</span><span style="color:#89DDFF">{3,}/g</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;\n\n&quot;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">replace</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">/</span><span style="color:#BB9AF7">\n</span><span style="color:#89DDFF">{2}/g</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;\n\n&quot;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">replace</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">/</span><span style="color:#BB9AF7">\n</span><span style="color:#89DDFF">/g</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">replace</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">/</span><span style="color:#BB9AF7">\s</span><span style="color:#89DDFF">{2,}/g</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">trim</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> txt</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Parses and validates a single Markdown file.</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * - Extracts frontmatter (slug, etc.)</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * - Converts content to plain text</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * - Skips drafts or files with no slug</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> processFile</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">path</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Promise</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">Document</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> content</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> data</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> matter</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">fs</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">readFileSync</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">path</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">utf-8</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">slug</span><span style="color:#BB9AF7"> ||</span><span style="color:#C0CAF5"> data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">draft</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> plain</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> getPlainText</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">content</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">path</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> content</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> plain</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> frontmatter</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> data</span><span style="color:#89DDFF"> as</span><span style="color:#C0CAF5"> Frontmatter</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Processes an array of Markdown file paths into Documents</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> loadDocs</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">paths</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">[])</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> docs</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Document</span><span style="color:#9ABDF5">[] </span><span style="color:#89DDFF">=</span><span style="color:#9ABDF5"> []</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">  for</span><span style="color:#9ABDF5"> (</span><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> p</span><span style="color:#89DDFF"> of</span><span style="color:#C0CAF5"> paths</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> d</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> processFile</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">p</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">d</span><span style="color:#9ABDF5">) </span><span style="color:#C0CAF5">docs</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">push</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">d</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> docs</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Generates vector embeddings for each document&#39;s plain text.</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * - Uses HuggingFace model</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * - Normalizes each vector for fast cosine similarity search</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> embedDocs</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">  docs</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Document</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  extractor</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> FeatureExtractionPipeline</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">docs</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#9ABDF5"> []</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Don&#39;t let the model normalize, we do it manually for safety</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> res</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7;font-style:italic">await</span><span style="color:#7AA2F7"> extractor</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#C0CAF5">    docs</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">map</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">d</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> d</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">content</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    { </span><span style="color:#73DACA">pooling</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">mean</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> normalize</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> false</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">  )) </span><span style="color:#89DDFF">as</span><span style="color:#0DB9D7"> any</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> [</span><span style="color:#BB9AF7">n</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> dim</span><span style="color:#89DDFF">]</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> res</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">dims</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Each embedding vector is normalized for performance</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> Array</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">from</span><span style="color:#9ABDF5">({ </span><span style="color:#73DACA">length</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> n</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">_</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> i</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span></span>
<span class="line"><span style="color:#7AA2F7">    normalize</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">res</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">data</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">slice</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">i</span><span style="color:#89DDFF"> *</span><span style="color:#C0CAF5"> dim</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">i</span><span style="color:#89DDFF"> +</span><span style="color:#FF9E64"> 1</span><span style="color:#9ABDF5">) </span><span style="color:#89DDFF">*</span><span style="color:#C0CAF5"> dim</span><span style="color:#9ABDF5">))</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Computes the top-N most similar documents for the given document index.</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * - Uses dot product of normalized vectors for cosine similarity</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * - Returns only the top-N</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> topSimilar</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#E0AF68">  idx</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  docs</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Document</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  embs</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Float32Array</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  n</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> SimilarityResult</span><span style="color:#9ABDF5">[]</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> docs</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">map</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">d</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> j</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span></span>
<span class="line"><span style="color:#C0CAF5">      j</span><span style="color:#BB9AF7"> ===</span><span style="color:#C0CAF5"> idx</span></span>
<span class="line"><span style="color:#BB9AF7">        ?</span><span style="color:#FF9E64"> null</span></span>
<span class="line"><span style="color:#BB9AF7">        :</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#F7768E;font-weight:bold">            ...</span><span style="color:#C0CAF5">d</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">frontmatter</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">            path</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> d</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">path</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">            similarity</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> +</span><span style="color:#7AA2F7">dot</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">embs</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">idx</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> embs</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">j</span><span style="color:#9ABDF5">])</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toFixed</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">2</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic"> // higher = more similar</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span></span>
<span class="line"><span style="color:#9ABDF5">    )</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">filter</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">Boolean</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">sort</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">a</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> b</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">b</span><span style="color:#89DDFF"> as</span><span style="color:#0DB9D7"> any</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">similarity</span><span style="color:#89DDFF"> -</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">a</span><span style="color:#89DDFF"> as</span><span style="color:#0DB9D7"> any</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">similarity</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">slice</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> n</span><span style="color:#9ABDF5">) </span><span style="color:#89DDFF">as</span><span style="color:#C0CAF5"> SimilarityResult</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Computes all similarities for every document, returns as {slug: SimilarityResult[]} map.</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> allSimilarities</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">docs</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Document</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> embs</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Float32Array</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> n</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> Object</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">fromEntries</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#C0CAF5">    docs</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">map</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">d</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> i</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> [</span><span style="color:#C0CAF5">d</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">frontmatter</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">slug</span><span style="color:#89DDFF">,</span><span style="color:#7AA2F7"> topSimilar</span><span style="color:#9ABDF5">(</span><span style="color:#7DCFFF">i</span><span style="color:#89DDFF">,</span><span style="color:#7DCFFF"> docs</span><span style="color:#89DDFF">,</span><span style="color:#7DCFFF"> embs</span><span style="color:#89DDFF">,</span><span style="color:#7DCFFF"> n</span><span style="color:#9ABDF5">)])</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">/**</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * Saves result object as JSON file.</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> * - Ensures output directory exists.</span></span>
<span class="line"><span style="color:#51597D;font-style:italic"> */</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> saveJson</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">obj</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> any</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> out</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  fs</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">mkdirSync</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">path</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">dirname</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">out</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">recursive</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#9ABDF5"> })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  fs</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">writeFileSync</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">out</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> JSON</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">stringify</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">obj</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 2</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// --------- Main Execution Flow ---------</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> main</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // 1. Load transformer model for embeddings</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> extractor</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> pipeline</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">feature-extraction</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> MODEL</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // 2. Find all Markdown files</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> files</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> glob</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">GLOB</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">files</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#C0CAF5"> console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">chalk</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">yellow</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">No content files found.</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // 3. Parse and process all files</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> docs</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> loadDocs</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">files</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">docs</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#C0CAF5"> console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">chalk</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">red</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">No documents loaded.</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // 4. Generate &amp; normalize embeddings</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> embs</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> embedDocs</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">docs</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> extractor</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">embs</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#C0CAF5"> console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">chalk</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">red</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">No embeddings.</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // 5. Calculate similarities for each doc</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> results</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> allSimilarities</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">docs</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> embs</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> TOP_N</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // 6. Save results to disk</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    await</span><span style="color:#7AA2F7"> saveJson</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">results</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> OUT</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">chalk</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">green</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">Similarity results saved to </span><span style="color:#7DCFFF">${</span><span style="color:#FF9E64">OUT</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">e</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">error</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">chalk</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">red</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Error:</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> e</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    process</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">exitCode</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 1</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">main</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="import { pipeline, FeatureExtractionPipeline } from &#34;@huggingface/transformers&#34;;
import chalk from &#34;chalk&#34;;
import fs from &#34;fs&#34;;
import { glob } from &#34;glob&#34;;
import matter from &#34;gray-matter&#34;;
import { remark } from &#34;remark&#34;;
import strip from &#34;strip-markdown&#34;;
import path from &#34;path&#34;;

// --------- Configurations ---------
const GLOB = &#34;src/content/**/*.{md,mdx}&#34;; // Where to find Markdown content
const OUT = &#34;src/assets/similarities.json&#34;; // Output file for results
const TOP_N = 5; // Number of similar docs to keep
const MODEL = &#34;Snowflake/snowflake-arctic-embed-m-v2.0&#34;; // Embedding model

// --------- Type Definitions ---------
interface Frontmatter {
  slug: string;
  [k: string]: unknown;
}
interface Document {
  path: string;
  content: string;
  frontmatter: Frontmatter;
}
interface SimilarityResult extends Frontmatter {
  path: string;
  similarity: number;
}

// --------- Utils ---------

/**
 * Normalizes a vector to unit length (L2 norm == 1)
 * This makes cosine similarity a simple dot product!
 */
function normalize(vec: Float32Array): Float32Array {
  let len = Math.hypot(...vec); // L2 norm
  if (!len) return vec;
  return new Float32Array(vec.map(x => x / len));
}

/**
 * Computes dot product of two same-length vectors.
 * Vectors MUST be normalized before using this for cosine similarity!
 */
const dot = (a: Float32Array, b: Float32Array) =>
  a.reduce((sum, ai, i) => sum + ai * b[i], 0);

/**
 * Strips markdown formatting, import/export lines, headings, tables, etc.
 * Returns plain text for semantic analysis.
 */
const getPlainText = async (md: string) => {
  let txt = String(await remark().use(strip).process(md))
    .replace(/^import .*?$/gm, &#34;&#34;)
    .replace(/^export .*?$/gm, &#34;&#34;)
    .replace(
      /^\s*(TLDR|Introduction|Conclusion|Summary|Quick Setup Guide|Rules?)\s*$/gim,
      &#34;&#34;
    )
    .replace(/^[A-Z\s]{4,}$/gm, &#34;&#34;)
    .replace(/^\|.*\|$/gm, &#34;&#34;)
    .replace(/(Rule\s\d+:.*)(?=\s*Rule\s\d+:)/g, &#34;$1\n&#34;)
    .replace(/\n{3,}/g, &#34;\n\n&#34;)
    .replace(/\n{2}/g, &#34;\n\n&#34;)
    .replace(/\n/g, &#34; &#34;)
    .replace(/\s{2,}/g, &#34; &#34;)
    .trim();
  return txt;
};

/**
 * Parses and validates a single Markdown file.
 * - Extracts frontmatter (slug, etc.)
 * - Converts content to plain text
 * - Skips drafts or files with no slug
 */
async function processFile(path: string): Promise<Document | null> {
  try {
    const { content, data } = matter(fs.readFileSync(path, &#34;utf-8&#34;));
    if (!data.slug || data.draft) return null;
    const plain = await getPlainText(content);
    return { path, content: plain, frontmatter: data as Frontmatter };
  } catch {
    return null;
  }
}

/**
 * Processes an array of Markdown file paths into Documents
 */
async function loadDocs(paths: string[]) {
  const docs: Document[] = [];
  for (const p of paths) {
    const d = await processFile(p);
    if (d) docs.push(d);
  }
  return docs;
}

/**
 * Generates vector embeddings for each document's plain text.
 * - Uses HuggingFace model
 * - Normalizes each vector for fast cosine similarity search
 */
async function embedDocs(
  docs: Document[],
  extractor: FeatureExtractionPipeline
) {
  if (!docs.length) return [];
  // Don't let the model normalize, we do it manually for safety
  const res = (await extractor(
    docs.map(d => d.content),
    { pooling: &#34;mean&#34;, normalize: false }
  )) as any;
  const [n, dim] = res.dims;
  // Each embedding vector is normalized for performance
  return Array.from({ length: n }, (_, i) =>
    normalize(res.data.slice(i * dim, (i + 1) * dim))
  );
}

/**
 * Computes the top-N most similar documents for the given document index.
 * - Uses dot product of normalized vectors for cosine similarity
 * - Returns only the top-N
 */
function topSimilar(
  idx: number,
  docs: Document[],
  embs: Float32Array[],
  n: number
): SimilarityResult[] {
  return docs
    .map((d, j) =>
      j === idx
        ? null
        : {
            ...d.frontmatter,
            path: d.path,
            similarity: +dot(embs[idx], embs[j]).toFixed(2), // higher = more similar
          }
    )
    .filter(Boolean)
    .sort((a, b) => (b as any).similarity - (a as any).similarity)
    .slice(0, n) as SimilarityResult[];
}

/**
 * Computes all similarities for every document, returns as {slug: SimilarityResult[]} map.
 */
function allSimilarities(docs: Document[], embs: Float32Array[], n: number) {
  return Object.fromEntries(
    docs.map((d, i) => [d.frontmatter.slug, topSimilar(i, docs, embs, n)])
  );
}

/**
 * Saves result object as JSON file.
 * - Ensures output directory exists.
 */
async function saveJson(obj: any, out: string) {
  fs.mkdirSync(path.dirname(out), { recursive: true });
  fs.writeFileSync(out, JSON.stringify(obj, null, 2));
}

// --------- Main Execution Flow ---------
async function main() {
  try {
    // 1. Load transformer model for embeddings
    const extractor = await pipeline(&#34;feature-extraction&#34;, MODEL);

    // 2. Find all Markdown files
    const files = await glob(GLOB);
    if (!files.length)
      return console.log(chalk.yellow(&#34;No content files found.&#34;));

    // 3. Parse and process all files
    const docs = await loadDocs(files);
    if (!docs.length) return console.log(chalk.red(&#34;No documents loaded.&#34;));

    // 4. Generate &#38; normalize embeddings
    const embs = await embedDocs(docs, extractor);
    if (!embs.length) return console.log(chalk.red(&#34;No embeddings.&#34;));

    // 5. Calculate similarities for each doc
    const results = allSimilarities(docs, embs, TOP_N);

    // 6. Save results to disk
    await saveJson(results, OUT);
    console.log(chalk.green(`Similarity results saved to ${OUT}`));
  } catch (e) {
    console.error(chalk.red(&#34;Error:&#34;), e);
    process.exitCode = 1;
  }
}

main();" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="this-will-produce-a-json-file-with-the-following-structure">This Will Produce a JSON file with the following structure:<a class="heading-link" aria-label="Link to section" href="#this-will-produce-a-json-file-with-the-following-structure"><span class="heading-link-icon">#</span></a></h2>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">vue-introduction</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">    {</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#0DB9D7">slug</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">typescript-advanced-types</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#0DB9D7">title</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Advanced Types in TypeScript</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#0DB9D7">date</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">2024-06-03T00:00:00.000Z</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#0DB9D7">path</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">src/content/typescript-advanced-types.md</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &quot;</span><span style="color:#0DB9D7">similarity</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0.35</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // Additional similar documents...</span></span>
<span class="line"><span style="color:#9ABDF5">  ]</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Additional document entries...</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;vue-introduction&#34;: [
    {
      &#34;slug&#34;: &#34;typescript-advanced-types&#34;,
      &#34;title&#34;: &#34;Advanced Types in TypeScript&#34;,
      &#34;date&#34;: &#34;2024-06-03T00:00:00.000Z&#34;,
      &#34;path&#34;: &#34;src/content/typescript-advanced-types.md&#34;,
      &#34;similarity&#34;: 0.35
    }
    // Additional similar documents...
  ]
  // Additional document entries...
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="astro-component">Astro Component<a class="heading-link" aria-label="Link to section" href="#astro-component"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="astro"><code><span class="line"><span style="color:#51597D;font-style:italic">---</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> sims</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">../assets/similarities.json</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">similarities</span><span style="color:#9ABDF5">[</span><span style="color:#C0CAF5">post</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">slug</span><span style="color:#9ABDF5">])</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  mostRelatedPosts</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> similarities</span><span style="color:#9ABDF5">[</span><span style="color:#C0CAF5">post</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">slug</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">filter</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">p</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> RelatedPost</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#BB9AF7"> !</span><span style="color:#C0CAF5">p</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">draft</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">sort</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#9ABDF5">      (</span><span style="color:#E0AF68">a</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> RelatedPost</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> b</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> RelatedPost</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span></span>
<span class="line"><span style="color:#9ABDF5">        (</span><span style="color:#C0CAF5">b</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">similarity</span><span style="color:#BB9AF7"> ??</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) </span><span style="color:#89DDFF">-</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">a</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">similarity</span><span style="color:#BB9AF7"> ??</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">    )</span></span>
<span class="line"><span style="color:#89DDFF">    .</span><span style="color:#7AA2F7">slice</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 3</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">{</span></span>
<span class="line"><span style="color:#C0CAF5">  mostRelatedPosts</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#BB9AF7"> &gt;</span><span style="color:#FF9E64"> 0</span><span style="color:#BB9AF7"> &amp;&amp;</span><span style="color:#9ABDF5"> (</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> data-pagefind-ignore</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">mb-8 mt-16</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">h2</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">mb-6 text-3xl font-bold text-skin-accent</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#9AA5CE">        Most Related Posts</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;/</span><span style="color:#F7768E">h2</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">md:grid-cols-3 grid grid-cols-1 gap-6</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">        {</span><span style="color:#C0CAF5">mostRelatedPosts</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">map</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">relatedPost</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> RelatedPost</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> (</span></span>
<span class="line"><span style="color:#BA3C97">          &lt;</span><span style="color:#F7768E">a</span></span>
<span class="line"><span style="color:#BB9AF7">            href</span><span style="color:#89DDFF">=</span><span style="color:#7DCFFF">{</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">/posts/</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">relatedPost</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">slug</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">/</span><span style="color:#89DDFF">`</span><span style="color:#7DCFFF">}</span></span>
<span class="line"><span style="color:#BB9AF7">            class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">related-post-card group</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BA3C97">          &gt;</span></span>
<span class="line"><span style="color:#BA3C97">            &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">p-5</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">              &lt;</span><span style="color:#F7768E">h3</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">related-post-title</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#7DCFFF">{</span><span style="color:#C0CAF5">relatedPost</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">title}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">h3</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">              &lt;</span><span style="color:#F7768E">p</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">related-post-description</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#7DCFFF">{</span><span style="color:#C0CAF5">relatedPost</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">description}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">              &lt;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">flex items-center justify-between text-xs text-skin-base text-opacity-60</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">                &lt;</span><span style="color:#DE5971">Datetime</span></span>
<span class="line"><span style="color:#BB9AF7">                  pubDatetime</span><span style="color:#89DDFF">=</span><span style="color:#7DCFFF">{</span><span style="color:#C0CAF5">relatedPost</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">pubDatetime}</span></span>
<span class="line"><span style="color:#BB9AF7">                  modDatetime</span><span style="color:#89DDFF">=</span><span style="color:#7DCFFF">{</span><span style="color:#C0CAF5">relatedPost</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">modDatetime}</span></span>
<span class="line"><span style="color:#BB9AF7">                  size</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">sm</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BA3C97">                /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">                &lt;</span><span style="color:#F7768E">span</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">related-post-tag</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#7DCFFF">{</span><span style="color:#C0CAF5">relatedPost</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">tags</span><span style="color:#89DDFF">?.</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#7DCFFF">}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">span</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">              &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">            &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">          &lt;/</span><span style="color:#F7768E">a</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#9ABDF5">        ))</span><span style="color:#7DCFFF">}</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span></span>
<span class="line"><span style="color:#7DCFFF">}</span></span></code><button type="button" class="copy" data-code="---
import sims from &#34;../assets/similarities.json&#34;;

if (similarities[post.slug]) {
  mostRelatedPosts = similarities[post.slug]
    .filter((p: RelatedPost) => !p.draft)
    .sort(
      (a: RelatedPost, b: RelatedPost) =>
        (b.similarity ?? 0) - (a.similarity ?? 0)
    )
    .slice(0, 3);
}
---

{
  mostRelatedPosts.length > 0 &#38;&#38; (
    <div data-pagefind-ignore class=&#34;mb-8 mt-16&#34;>
      <h2 class=&#34;mb-6 text-3xl font-bold text-skin-accent&#34;>
        Most Related Posts
      </h2>
      <div class=&#34;md:grid-cols-3 grid grid-cols-1 gap-6&#34;>
        {mostRelatedPosts.map((relatedPost: RelatedPost) => (
          <a
            href={`/posts/${relatedPost.slug}/`}
            class=&#34;related-post-card group&#34;
          >
            <div class=&#34;p-5&#34;>
              <h3 class=&#34;related-post-title&#34;>{relatedPost.title}</h3>
              <p class=&#34;related-post-description&#34;>{relatedPost.description}</p>
              <div class=&#34;flex items-center justify-between text-xs text-skin-base text-opacity-60&#34;>
                <Datetime
                  pubDatetime={relatedPost.pubDatetime}
                  modDatetime={relatedPost.modDatetime}
                  size=&#34;sm&#34;
                />
                <span class=&#34;related-post-tag&#34;>{relatedPost.tags?.[0]}</span>
              </div>
            </div>
          </a>
        ))}
      </div>
    </div>
  )
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="does-it-work">Does It Work?<a class="heading-link" aria-label="Link to section" href="#does-it-work"><span class="heading-link-icon">#</span></a></h2>
<p>Yes! Now, my blog suggests truly related content, not random posts.</p>
<hr/>
<h2 id="what-i-learned">What I Learned<a class="heading-link" aria-label="Link to section" href="#what-i-learned"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li><strong>No extra servers or databases</strong>: Everything runs during build time.</li>
<li><strong>Easy to use</strong>: Works in both browsers and Node.js.</li>
<li><strong>Flexible</strong>: Quickly change the model or method.</li>
</ul>
<p>If you have a static blog and want better recommendations, give embeddings and Astro a try. Let me know how it goes!</p>
<p>Of course, this is far from perfect. I also don’t know which model would be ideal, but at the moment I’m getting much better related posts than before, so I’m happy with the results.
If you want to play with the script yourself check out <a href="https://github.com/alexanderop/post-matcher-ai" rel="noopener noreferrer" target="_blank">post-matcher-ai</a></p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_semantic-related-posts-astro-transformersjs" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="semantic-related-posts-astro-transformersjs" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/astro/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">astro</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/typescript/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">typescript</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/semantic-related-posts-astro-transformersjs/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/semantic-related-posts-astro-transformersjs/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/semantic-related-posts-astro-transformersjs/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/semantic-related-posts-astro-transformersjs/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/semantic-related-posts-astro-transformersjs/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/semantic-related-posts-astro-transformersjs/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/semantic-related-posts-astro-transformersjs/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/how-i-added-llms-txt-to-my-astro-blog/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How I Added llms.txt to My Astro Blog</h3> <p class="related-post-description astro-vj4tpspi"> I built a simple way to load my blog content into any LLM with one click. This post shows how you can do it too. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-03-03T00:00:00.000Z">Mar 3, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> astro </span> </div> </div> </a><a href="/posts/how-to-implement-a-cosine-similarity-function-in-typescript-for-vector-comparison/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How to Implement a Cosine Similarity Function in TypeScript for Vector Comparison</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to build an efficient cosine similarity function in TypeScript for comparing vector embeddings. This step-by-step guide includes code examples, performance optimizations, and practical applications for semantic search and AI recommendation systems </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-03-08T00:00:00.000Z">Mar 8, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> typescript </span> </div> </div> </a><a href="/posts/excalidraw-dark-mode-astro-diagrams/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Create Dark Mode-Compatible Technical Diagrams in Astro with Excalidraw: A Complete Guide</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to create and integrate theme-aware Excalidraw diagrams into your Astro blog. This step-by-step guide shows you how to build custom components that automatically adapt to light and dark modes, perfect for technical documentation and blogs </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2024-10-27T07:00:00.000Z">Oct 27, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> astro </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "semantic-related-posts-astro-transformersjs";

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
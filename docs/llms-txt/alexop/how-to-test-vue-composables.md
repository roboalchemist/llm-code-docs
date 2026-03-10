# Source: https://alexop.dev/posts/how-to-test-vue-composables

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/how-to-test-vue-composables/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>How to Test Vue Composables: A Comprehensive Guide with Vitest | alexop.dev</title><meta name="title" content="How to Test Vue Composables: A Comprehensive Guide with Vitest | alexop.dev"><meta name="description" content="Learn how to effectively test Vue composables using Vitest. Covers independent and dependent composables, with practical examples and best practices."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="How to Test Vue Composables: A Comprehensive Guide with Vitest | alexop.dev"><meta property="og:description" content="Learn how to effectively test Vue composables using Vitest. Covers independent and dependent composables, with practical examples and best practices."><meta property="og:url" content="https://alexop.dev/posts/how-to-test-vue-composables/"><meta property="og:image" content="https://alexop.dev/posts/how-to-test-vue-composables-a-comprehensive-guide-with-vitest/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2023-11-25T15:22:00.000Z"><meta property="article:modified_time" content="2024-11-10T15:22:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/how-to-test-vue-composables/"><meta property="twitter:title" content="How to Test Vue Composables: A Comprehensive Guide with Vitest | alexop.dev"><meta property="twitter:description" content="Learn how to effectively test Vue composables using Vitest. Covers independent and dependent composables, with practical examples and best practices."><meta property="twitter:image" content="https://alexop.dev/posts/how-to-test-vue-composables-a-comprehensive-guide-with-vitest/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"How to Test Vue Composables: A Comprehensive Guide with Vitest | alexop.dev","description":"Learn how to effectively test Vue composables using Vitest. Covers independent and dependent composables, with practical examples and best practices.","image":"https://alexop.dev/posts/how-to-test-vue-composables-a-comprehensive-guide-with-vitest/index.png","datePublished":"2023-11-25T15:22:00.000Z","dateModified":"2024-11-10T15:22:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: how-to-test-vue-composables-a-comprehensive-guide-with-vitest; }@layer astro { ::view-transition-old(how-to-test-vue-composables-a-comprehensive-guide-with-vitest) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(how-to-test-vue-composables-a-comprehensive-guide-with-vitest) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(how-to-test-vue-composables-a-comprehensive-guide-with-vitest) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(how-to-test-vue-composables-a-comprehensive-guide-with-vitest) { 
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
	animation-name: astroFadeIn; }</style><style>.excalidraw-figure:where(.astro-hxyrieg5){margin-top:2rem;margin-bottom:2rem;width:100%;max-width:100%}.excalidraw-svg:where(.astro-hxyrieg5){width:100%;--excalidraw-text: rgb(var(--color-text-base));--excalidraw-fill: rgb(var(--color-card));--excalidraw-accent: rgb(var(--color-accent))}.excalidraw-svg svg.excalidraw-rendered{display:block;height:auto;width:100%}figcaption:where(.astro-hxyrieg5){margin-top:1rem;text-align:center;font-size:.875rem;line-height:1.25rem;font-style:italic;--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1))}figcaption:where(.astro-hxyrieg5) a:where(.astro-hxyrieg5){--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));transition-property:opacity;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.2s}figcaption:where(.astro-hxyrieg5) a:where(.astro-hxyrieg5):hover{opacity:.8}figcaption:where(.astro-hxyrieg5) a:where(.astro-hxyrieg5){text-decoration:underline}
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: testing; }@layer astro { ::view-transition-old(testing) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(testing) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(testing) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(testing) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">How to Test Vue Composables: A Comprehensive Guide with Vitest</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-base">Updated:</span><span class="italic text-base"><time dateTime="2024-11-10T15:22:00.000Z">Nov 10, 2024</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Z2hGAqr" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;How to Test Vue Composables: A Comprehensive Guide with Vitest&quot;],&quot;content&quot;:[0,&quot;import ExcalidrawSVG from \&quot;@features/mdx-components/components/ExcalidrawSVG.astro\&quot;;\nimport myDiagram from \&quot;../../assets/images/how-to-test-vue-composables/testing-pyramid.svg?raw\&quot;;\nimport independentComposable from \&quot;../../assets/images/how-to-test-vue-composables/independetComp.svg?raw\&quot;;\nimport dependentComposable from \&quot;../../assets/images/how-to-test-vue-composables/dependantComp.svg?raw\&quot;;\nimport mockWithSetup from \&quot;../../assets/images/how-to-test-vue-composables/mockWithLifecycles.svg?raw\&quot;;\n\n## Introduction\n\nHello, everyone; in this blog post, I want to help you better understand how to test a composable in Vue. Nowadays, much of our business logic or UI logic is often encapsulated in composables, so I think it’s important to understand how to test them.\n\n## Definitions\n\nBefore discussing the main topic, it’s important to understand some basic concepts regarding testing. This foundational knowledge will help clarify where testing Vue compostables fits into the broader landscape of software testing.\n\n### Composables\n\n**Composables** in Vue are reusable composition functions that encapsulate and manage reactive states and logic. They allow a flexible way to organize and reuse code across components, enhancing modularity and maintainability.\n\n### Testing Pyramid\n\n&lt;ExcalidrawSVG src={myDiagram} alt=\&quot;Testing Pyramid Diagram\&quot; /&gt;\nThe **Testing Pyramid** is a conceptual metaphor that illustrates the ideal\nbalance of different types of testing. It recommends a large base of unit tests,\nsupplemented by a smaller set of integration tests and capped with an even\nsmaller set of end-to-end tests. This structure ensures efficient and effective\ntest coverage.\n\n### Unit Testing and How Testing a Composable Would Be a Unit Test\n\n**Unit testing** refers to the practice of testing individual units of code in isolation. In the context of Vue, testing a composable is a form of unit testing. It involves rigorously verifying the functionality of these isolated, reusable code blocks, ensuring they function correctly without external dependencies.\n\n---\n\n## Testing Composables\n\nComposables in Vue are essentially functions, leveraging Vue&#39;s reactivity system. Given this unique nature, we can categorize composables into different types. On one hand, there are `Independent Composables`, which can be tested directly due to their standalone nature. On the other hand, we have `Dependent Composables`, which only function correctly when integrated within a component.In the sections that follow, I&#39;ll delve into these distinct types, provide examples for each, and guide you through effective testing strategies for both.\n\n---\n\n### Independent Composables\n\n&lt;ExcalidrawSVG\n  src={independentComposable}\n  alt=\&quot;Independent Composables Diagram\&quot;\n/&gt;\n\nAn Independent Composable exclusively uses Vue&#39;s Reactivity APIs. These composables operate independently of Vue component instances, making them straightforward to test.\n\n#### Example &amp; Testing Strategy\n\nHere is an example of an independent composable that calculates the sum of two reactive values:\n\n```ts\nimport { Ref, computed, ComputedRef } from \&quot;vue\&quot;;\n\nfunction useSum(a: Ref&lt;number&gt;, b: Ref&lt;number&gt;): ComputedRef&lt;number&gt; {\n  return computed(() =&gt; a.value + b.value);\n}\n```\n\nTo test this composable, you would directly invoke it and assert its returned state:\n\nTest with Vitest:\n\n```ts\ndescribe(\&quot;useSum\&quot;, () =&gt; {\n  it(\&quot;correctly computes the sum of two numbers\&quot;, () =&gt; {\n    const num1 = ref(2);\n    const num2 = ref(3);\n    const sum = useSum(num1, num2);\n\n    expect(sum.value).toBe(5);\n  });\n});\n```\n\nThis test directly checks the functionality of useSum by passing reactive references and asserting the computed result.\n\n---\n\n### Dependent Composables\n\n&lt;ExcalidrawSVG src={dependentComposable} alt=\&quot;Dependent Composables Diagram\&quot; /&gt;\n\n`Dependent Composables` are distinguished by their reliance on Vue&#39;s component instance. They often leverage features like lifecycle hooks or context for their operation. These composables are an integral part of a component and necessitate a distinct approach for testing, as opposed to Independent Composables.\n\n#### Example &amp; Usage\n\nAn exemplary Dependent Composable is `useLocalStorage`. This composable facilitates interaction with the browser&#39;s localStorage and harnesses the `onMounted` lifecycle hook for initialization:\n\n```ts\nimport { ref, computed, onMounted, watch } from \&quot;vue\&quot;;\n\nfunction useLocalStorage&lt;T&gt;(key: string, initialValue: T) {\n  const value = ref&lt;T&gt;(initialValue);\n\n  function loadFromLocalStorage() {\n    const storedValue = localStorage.getItem(key);\n    if (storedValue !== null) {\n      value.value = JSON.parse(storedValue);\n    }\n  }\n\n  onMounted(loadFromLocalStorage);\n\n  watch(value, newValue =&gt; {\n    localStorage.setItem(key, JSON.stringify(newValue));\n  });\n\n  return { value };\n}\n\nexport default useLocalStorage;\n```\n\nThis composable can be utilised within a component, for instance, to create a persistent counter:\n\n![Counter Ui](../../assets/images/how-to-test-vue-composables/counter-ui.png)\n\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\n// ... script content ...\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;div&gt;\n    &lt;h1&gt;Counter: {{ count }}&lt;/h1&gt;\n    &lt;button @click=\&quot;increment\&quot;&gt;Increment&lt;/button&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n```\n\nThe primary benefit here is the seamless synchronization of the reactive `count` property with localStorage, ensuring persistence across sessions.\n\n### Testing Strategy\n\nTo effectively test `useLocalStorage`, especially considering the `onMounted` lifecycle, we initially face a challenge. Let&#39;s start with a basic test setup:\n\n```ts\ndescribe(\&quot;useLocalStorage\&quot;, () =&gt; {\n  it(\&quot;should load the initialValue\&quot;, () =&gt; {\n    const { value } = useLocalStorage(\&quot;testKey\&quot;, \&quot;initValue\&quot;);\n    expect(value.value).toBe(\&quot;initValue\&quot;);\n  });\n\n  it(\&quot;should load from localStorage\&quot;, async () =&gt; {\n    localStorage.setItem(\&quot;testKey\&quot;, JSON.stringify(\&quot;fromStorage\&quot;));\n    const { value } = useLocalStorage(\&quot;testKey\&quot;, \&quot;initialValue\&quot;);\n    expect(value.value).toBe(\&quot;fromStorage\&quot;);\n  });\n});\n```\n\nHere, the first test will pass, asserting that the composable initialises with the given `initialValue`. However, the second test, which expects the composable to load a pre-existing value from localStorage, fails. The challenge arises because the `onMounted` lifecycle hook is not triggered during testing. To address this, we need to refactor our composable or our test setup to simulate the component mounting process.\n\n---\n\n### Enhancing Testing with the `withSetup` Helper Function\n\n&lt;ExcalidrawSVG src={mockWithSetup} alt=\&quot;Mock withSetup Diagram\&quot; /&gt;\n\nTo facilitate easier testing of composables that rely on Vue&#39;s lifecycle hooks, we&#39;ve developed a higher-order function named `withSetup`. This utility allows us to create a Vue component context programmatically, focusing primarily on the setup lifecycle function where composables are typically used.\n\n#### Introduction to `withSetup`\n\n`withSetup` is designed to simulate a Vue component&#39;s setup function, enabling us to test composables in an environment that closely mimics their real-world use. The function accepts a composable and returns both the composable&#39;s result and a Vue app instance. This setup allows for comprehensive testing, including lifecycle and reactivity features.\n\n```ts\nimport type { App } from \&quot;vue\&quot;;\nimport { createApp } from \&quot;vue\&quot;;\n\nexport function withSetup&lt;T&gt;(composable: () =&gt; T): [T, App] {\n  let result: T;\n  const app = createApp({\n    setup() {\n      result = composable();\n      return () =&gt; {};\n    },\n  });\n  app.mount(document.createElement(\&quot;div\&quot;));\n  return [result, app];\n}\n```\n\nIn this implementation, `withSetup` mounts a minimal Vue app and executes the provided composable function during the setup phase. This approach allows us to capture and return the composable&#39;s output alongside the app instance for further testing.\n\n#### Utilizing `withSetup` in Tests\n\nWith `withSetup`, we can enhance our testing strategy for composables like `useLocalStorage`, ensuring they behave as expected even when they depend on lifecycle hooks:\n\n```ts\nit(\&quot;should load the value from localStorage if it was set before\&quot;, async () =&gt; {\n  localStorage.setItem(\&quot;testKey\&quot;, JSON.stringify(\&quot;valueFromLocalStorage\&quot;));\n  const [result] = withSetup(() =&gt; useLocalStorage(\&quot;testKey\&quot;, \&quot;testValue\&quot;));\n  expect(result.value.value).toBe(\&quot;valueFromLocalStorage\&quot;);\n});\n```\n\nThis test demonstrates how `withSetup` enables the composable to execute as if it were part of a regular Vue component, ensuring the `onMounted` lifecycle hook is triggered as expected. Additionally, the robust TypeScript support enhances the development experience by providing clear type inference and error checking.\n\n---\n\n### Testing Composables with Inject\n\nAnother common scenario is testing composables that rely on Vue&#39;s dependency injection system using `inject`. These composables present unique challenges as they expect certain values to be provided by ancestor components. Let&#39;s explore how to effectively test such composables.\n\n#### Example Composable with Inject\n\nHere&#39;s an example of a composable that uses inject:\n\n```ts\nimport type { InjectionKey } from \&quot;vue\&quot;;\nimport { inject } from \&quot;vue\&quot;;\n\nexport const MessageKey: InjectionKey&lt;string&gt; = Symbol(\&quot;message\&quot;);\n\nexport function useMessage() {\n  const message = inject(MessageKey);\n\n  if (!message) {\n    throw new Error(\&quot;Message must be provided\&quot;);\n  }\n\n  const getUpperCase = () =&gt; message.toUpperCase();\n  const getReversed = () =&gt; message.split(\&quot;\&quot;).reverse().join(\&quot;\&quot;);\n\n  return {\n    message,\n    getUpperCase,\n    getReversed,\n  };\n}\n```\n\n#### Creating a Test Helper\n\nTo test composables that use inject, we need a helper function that creates a testing environment with the necessary providers. Here&#39;s a utility function that makes this possible:\n\n```ts\nimport type { InjectionKey } from \&quot;vue\&quot;;\nimport { createApp, defineComponent, h, provide } from \&quot;vue\&quot;;\n\ntype InstanceType&lt;V&gt; = V extends { new (...arg: any[]): infer X } ? X : never;\ntype VM&lt;V&gt; = InstanceType&lt;V&gt; &amp; { unmount: () =&gt; void };\n\ninterface InjectionConfig {\n  key: InjectionKey&lt;any&gt; | string;\n  value: any;\n}\n\nexport function useInjectedSetup&lt;TResult&gt;(\n  setup: () =&gt; TResult,\n  injections: InjectionConfig[] = []\n): TResult &amp; { unmount: () =&gt; void } {\n  let result!: TResult;\n\n  const Comp = defineComponent({\n    setup() {\n      result = setup();\n      return () =&gt; h(\&quot;div\&quot;);\n    },\n  });\n\n  const Provider = defineComponent({\n    setup() {\n      injections.forEach(({ key, value }) =&gt; {\n        provide(key, value);\n      });\n      return () =&gt; h(Comp);\n    },\n  });\n\n  const mounted = mount(Provider);\n\n  return {\n    ...result,\n    unmount: mounted.unmount,\n  } as TResult &amp; { unmount: () =&gt; void };\n}\n\nfunction mount&lt;V&gt;(Comp: V) {\n  const el = document.createElement(\&quot;div\&quot;);\n  const app = createApp(Comp as any);\n  const unmount = () =&gt; app.unmount();\n  const comp = app.mount(el) as any as VM&lt;V&gt;;\n  comp.unmount = unmount;\n  return comp;\n}\n```\n\n#### Writing Tests\n\nWith our helper function in place, we can now write comprehensive tests for our inject-dependent composable:\n\n```ts\nimport { describe, expect, it } from \&quot;vitest\&quot;;\nimport { useInjectedSetup } from \&quot;../helper\&quot;;\nimport { MessageKey, useMessage } from \&quot;../useMessage\&quot;;\n\ndescribe(\&quot;useMessage\&quot;, () =&gt; {\n  it(\&quot;should handle injected message\&quot;, () =&gt; {\n    const wrapper = useInjectedSetup(\n      () =&gt; useMessage(),\n      [{ key: MessageKey, value: \&quot;hello world\&quot; }]\n    );\n\n    expect(wrapper.message).toBe(\&quot;hello world\&quot;);\n    expect(wrapper.getUpperCase()).toBe(\&quot;HELLO WORLD\&quot;);\n    expect(wrapper.getReversed()).toBe(\&quot;dlrow olleh\&quot;);\n\n    wrapper.unmount();\n  });\n\n  it(\&quot;should throw error when message is not provided\&quot;, () =&gt; {\n    expect(() =&gt; {\n      useInjectedSetup(() =&gt; useMessage(), []);\n    }).toThrow(\&quot;Message must be provided\&quot;);\n  });\n});\n```\n\nThe `useInjectedSetup` helper creates a testing environment that:\n\n1. Simulates a component hierarchy\n2. Provides the necessary injection values\n3. Executes the composable in a proper Vue context\n4. Returns the composable&#39;s result along with an unmount function\n\nThis approach allows us to:\n\n- Test composables that depend on inject\n- Verify error handling when required injections are missing\n- Test the full functionality of methods that use injected values\n- Properly clean up after tests by unmounting the test component\n\nRemember to always unmount the test component after each test to prevent memory leaks and ensure test isolation.\n\n---\n\n## Summary\n\n| Independent Composables 🔓                                     | Dependent Composables 🔗                 |\n| -------------------------------------------------------------- | ---------------------------------------- |\n| - ✅ can be tested directly                                    | - 🧪 need a component to test            |\n| - 🛠️ uses everything beside of lifecycles and provide / inject | - 🔄 uses Lifecycles or Provide / Inject |\n\nIn our exploration of testing Vue composables, we uncovered two distinct categories: **Independent Composables** and **Dependent Composables**. Independent Composables stand alone and can be tested akin to regular functions, showcasing straightforward testing procedures. Meanwhile, Dependent Composables, intricately tied to Vue&#39;s component system and lifecycle hooks, require a more nuanced approach. For these, we learned the effectiveness of utilizing a helper function, such as `withSetup`, to simulate a component context, enabling comprehensive testing.\n\nI hope this blog post has been insightful and useful in enhancing your understanding of testing Vue composables. I&#39;m also keen to learn about your experiences and methods in testing composables within your projects. Your insights and approaches could provide valuable perspectives and contribute to the broader Vue community&#39;s knowledge.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <h2 id="introduction">Introduction<a class="heading-link" aria-label="Link to section" href="#introduction"><span class="heading-link-icon">#</span></a></h2>
<p>Hello, everyone; in this blog post, I want to help you better understand how to test a composable in Vue. Nowadays, much of our business logic or UI logic is often encapsulated in composables, so I think it’s important to understand how to test them.</p>
<h2 id="definitions">Definitions<a class="heading-link" aria-label="Link to section" href="#definitions"><span class="heading-link-icon">#</span></a></h2>
<p>Before discussing the main topic, it’s important to understand some basic concepts regarding testing. This foundational knowledge will help clarify where testing Vue compostables fits into the broader landscape of software testing.</p>
<h3 id="composables">Composables<a class="heading-link" aria-label="Link to section" href="#composables"><span class="heading-link-icon">#</span></a></h3>
<p><strong>Composables</strong> in Vue are reusable composition functions that encapsulate and manage reactive states and logic. They allow a flexible way to organize and reuse code across components, enhancing modularity and maintainability.</p>
<h3 id="testing-pyramid">Testing Pyramid<a class="heading-link" aria-label="Link to section" href="#testing-pyramid"><span class="heading-link-icon">#</span></a></h3>
<figure class="excalidraw-figure astro-hxyrieg5"> <div class="excalidraw-svg astro-hxyrieg5" role="img" aria-label="Testing Pyramid Diagram"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 724.9686209227143 426.2721380425992" width="100%" class="excalidraw-rendered" preserveAspectRatio="xMidYMid meet">
  <!-- svg-source:excalidraw -->
  
  <defs>
    <style class="style-fonts">
      @font-face {
        font-family: Excalifont;
        src: url(data:font/woff2;base64,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);
          }
    </style>
    
  <style>
  .ed-text { fill: var(--excalidraw-text, #222e36); }
  .ed-fill { fill: var(--excalidraw-fill, #eaced7); }
  .ed-accent-fill { fill: var(--excalidraw-accent, #d3006a); }
  .ed-accent-stroke { stroke: var(--excalidraw-accent, #d3006a); }
</style></defs>
  <g stroke-linecap="round"><g transform="translate(13.634477413743753 412.29137686640024) rotate(0 350 0)"><path d="M0.34 -2.28 C117.11 -2.79, 583.17 -2.3, 700.04 -1.57 M-2.92 2.65 C113.54 2.35, 580.58 2.03, 697.83 1.21" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g stroke-linecap="round"><g transform="translate(13.634477413743753 412.29137686640024) rotate(0 180 -200)"><path d="M-0.12 -1.42 C60.65 -68.05, 302.89 -331.09, 362.57 -397.92 M-3.63 3.98 C57.19 -63.59, 300.5 -334.37, 361.72 -401.8" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g stroke-linecap="round"><g transform="translate(713.6344774137438 412.29137686640024) rotate(0 -170 -200)"><path d="M1.33 0.44 C-54.92 -66.17, -282.24 -335.39, -339.37 -402.29 M-1.39 -1.79 C-57.79 -67.88, -284.15 -333.81, -341.26 -399.91" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g stroke-linecap="round"><g transform="translate(113.63447741374375 312.29137686640024) rotate(0 260 0)"><path d="M-2.7 -1.05 C83.93 -0.25, 430.78 2.46, 518.14 2.65 M1.03 -4.09 C88.71 -3.81, 436.96 -2.14, 523.54 -0.92" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g stroke-linecap="round"><g transform="translate(233.63447741374375 172.29137686640024) rotate(0 140 0)"><path d="M1.94 1 C49.32 0.86, 235.89 -1.51, 282.35 -1.51 M-0.46 -0.92 C46.94 -0.66, 234.76 1.81, 281.39 1.3" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g transform="translate(313.63447741374375 352.29137686640024) rotate(0 52.12996765971184 12.5)"><text x="0" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="start" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Unit tests</text></g><g transform="translate(293.63447741374375 232.29137686640024) rotate(0 87.30994108319283 12.5)"><text x="0" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="start" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Integration tests</text></g><g transform="translate(333.63447741374375 92.29137686640024) rotate(0 43.92998504638672 12.5)"><text x="0" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="start" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">End2End</text></g></svg></div>  </figure> <script type="module">function n(i){const t=new DOMParser().parseFromString(i,"image/svg+xml"),o=t.documentElement;o.removeAttribute("filter"),t.querySelectorAll("[filter]").forEach(e=>e.removeAttribute("filter")),o.classList.add("excalidraw-rendered"),o.setAttribute("width","100%"),o.removeAttribute("height"),o.setAttribute("preserveAspectRatio","xMidYMid meet"),o.getAttribute("viewBox")||o.setAttribute("viewBox","0 0 800 600"),t.querySelectorAll("text").forEach(e=>{const r=e.getAttribute("y");if(!r||r==="NaN"||isNaN(parseFloat(r))){const c=parseFloat(e.getAttribute("font-size")||"16");e.setAttribute("y",String(Math.round(c*.85)))}});const a={"#222e36":"var(--excalidraw-text)","#eaced7":"var(--excalidraw-fill)","#d3006a":"var(--excalidraw-accent)"};return t.querySelectorAll("[fill]").forEach(e=>{const r=e.getAttribute("fill")?.toLowerCase();r&&a[r]&&e.setAttribute("fill",a[r])}),t.querySelectorAll("[stroke]").forEach(e=>{const r=e.getAttribute("stroke")?.toLowerCase();r&&a[r]&&e.setAttribute("stroke",a[r])}),new XMLSerializer().serializeToString(t)}function l(){document.querySelectorAll(".excalidraw-svg[data-svg-url]").forEach(async i=>{const s=i.dataset.svgUrl;if(s)try{const t=await fetch(s);if(!t.ok)throw new Error(`Failed to fetch SVG: ${t.statusText}`);i.innerHTML=n(await t.text())}catch(t){console.error("Error in ExcalidrawSVG component:",t)}})}document.addEventListener("DOMContentLoaded",l);document.addEventListener("astro:page-load",l);</script> 
<p>The <strong>Testing Pyramid</strong> is a conceptual metaphor that illustrates the ideal
balance of different types of testing. It recommends a large base of unit tests,
supplemented by a smaller set of integration tests and capped with an even
smaller set of end-to-end tests. This structure ensures efficient and effective
test coverage.</p>
<h3 id="unit-testing-and-how-testing-a-composable-would-be-a-unit-test">Unit Testing and How Testing a Composable Would Be a Unit Test<a class="heading-link" aria-label="Link to section" href="#unit-testing-and-how-testing-a-composable-would-be-a-unit-test"><span class="heading-link-icon">#</span></a></h3>
<p><strong>Unit testing</strong> refers to the practice of testing individual units of code in isolation. In the context of Vue, testing a composable is a form of unit testing. It involves rigorously verifying the functionality of these isolated, reusable code blocks, ensuring they function correctly without external dependencies.</p>
<hr/>
<h2 id="testing-composables">Testing Composables<a class="heading-link" aria-label="Link to section" href="#testing-composables"><span class="heading-link-icon">#</span></a></h2>
<p>Composables in Vue are essentially functions, leveraging Vue’s reactivity system. Given this unique nature, we can categorize composables into different types. On one hand, there are <code>Independent Composables</code>, which can be tested directly due to their standalone nature. On the other hand, we have <code>Dependent Composables</code>, which only function correctly when integrated within a component.In the sections that follow, I’ll delve into these distinct types, provide examples for each, and guide you through effective testing strategies for both.</p>
<hr/>
<h3 id="independent-composables">Independent Composables<a class="heading-link" aria-label="Link to section" href="#independent-composables"><span class="heading-link-icon">#</span></a></h3>
<figure class="excalidraw-figure astro-hxyrieg5"> <div class="excalidraw-svg astro-hxyrieg5" role="img" aria-label="Independent Composables Diagram"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 220" width="100%" class="excalidraw-rendered" preserveAspectRatio="xMidYMid meet">
  <!-- svg-source:excalidraw -->
  
  <defs>
    <style class="style-fonts">
      @font-face {
        font-family: Excalifont;
        src: url(data:font/woff2;base64,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);
          }
    </style>
    
  <style>
  .ed-text { fill: var(--excalidraw-text, #222e36); }
  .ed-fill { fill: var(--excalidraw-fill, #eaced7); }
  .ed-accent-fill { fill: var(--excalidraw-accent, #d3006a); }
  .ed-accent-stroke { stroke: var(--excalidraw-accent, #d3006a); }
</style></defs>
  <g stroke-linecap="round" transform="translate(10 10) rotate(0 140 100)"><path d="M194.66 9.12 C209.14 12.11, 221.16 20.23, 232.93 27.31 C244.7 34.39, 257.5 42.02, 265.27 51.6 C273.03 61.19, 277.7 73.57, 279.53 84.83 C281.35 96.09, 279.98 107.91, 276.23 119.15 C272.49 130.39, 265.59 142.18, 257.05 152.28 C248.51 162.39, 237.1 172.62, 225 179.77 C212.89 186.91, 199.79 192.09, 184.43 195.17 C169.07 198.24, 148.84 198.94, 132.84 198.2 C116.83 197.46, 102.95 195, 88.42 190.74 C73.9 186.47, 57.94 180.19, 45.71 172.6 C33.48 165.01, 22.29 154.8, 15.06 145.22 C7.82 135.64, 4.05 126.45, 2.32 115.12 C0.59 103.79, 1.29 88.72, 4.68 77.25 C8.07 65.77, 14.71 55.84, 22.67 46.27 C30.63 36.7, 39.83 26.57, 52.43 19.8 C65.03 13.04, 82.79 8.76, 98.27 5.69 C113.76 2.62, 127.03 0.53, 145.35 1.39 C163.66 2.25, 195.58 7.65, 208.16 10.84 C220.74 14.03, 221.66 18.81, 220.84 20.54 M96.61 4.53 C111.08 -0.66, 133.03 -1.23, 149.18 -0.7 C165.32 -0.16, 178.9 3.63, 193.48 7.72 C208.06 11.8, 225 16.23, 236.65 23.82 C248.3 31.4, 256.46 42.23, 263.36 53.23 C270.26 64.24, 276.11 78.29, 278.06 89.83 C280 101.38, 278.67 111.81, 275.02 122.5 C271.38 133.19, 264.57 144.76, 256.18 153.97 C247.8 163.18, 237.68 170.6, 224.72 177.76 C211.76 184.92, 193.73 193.07, 178.4 196.94 C163.08 200.8, 148.49 202.07, 132.76 200.94 C117.03 199.8, 98.81 194.24, 84.04 190.12 C69.28 186, 55.56 183.47, 44.16 176.22 C32.76 168.97, 22.57 157.26, 15.64 146.63 C8.72 136.01, 4.55 123.82, 2.61 112.48 C0.68 101.14, 0.29 90.1, 4.04 78.6 C7.8 67.09, 16.98 52.72, 25.14 43.44 C33.29 34.16, 40.76 29.77, 53 22.92 C65.23 16.08, 90.51 4.74, 98.53 2.37 C106.56 0, 100.14 6.84, 101.14 8.72" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(85.66510007236002 84.78932188134513) rotate(0 64.33995056152344 25)"><text x="64.33995056152344" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Independent </text><text x="64.33995056152344" y="42.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Composable</text></g><g stroke-linecap="round" transform="translate(450 10) rotate(0 160 100)"><path d="M32 0 C103.36 -2.91, 170.31 -1.04, 288 0 M32 0 C101.68 1.26, 170.93 2.12, 288 0 M288 0 C306.75 -3.86, 321.85 10.27, 320 32 M288 0 C310.96 -2.47, 316.87 9.69, 320 32 M320 32 C322.22 85.97, 320.91 140.99, 320 168 M320 32 C319.64 85.19, 316.5 139.68, 320 168 M320 168 C323.14 191.59, 308.86 199, 288 200 M320 168 C318.17 188.54, 307.09 201.85, 288 200 M288 200 C215.24 195.61, 144.12 201.6, 32 200 M288 200 C195.43 203.09, 102.51 204.23, 32 200 M32 200 C13.35 196.5, 2.91 192.35, 0 168 M32 200 C14.54 203.75, 4.48 186.27, 0 168 M0 168 C-3.45 141.65, 1.44 107.9, 0 32 M0 168 C3.13 137.57, 2.68 109.08, 0 32 M0 32 C3.15 12.89, 11.24 -1.21, 32 0 M0 32 C4.38 9.69, 13.87 0.65, 32 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(496.07007598876953 85) rotate(0 113.92992401123047 25)"><text x="113.92992401123047" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Vues reactivity</text><text x="113.92992401123047" y="42.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">(ref, watch , computed)</text></g><g stroke-linecap="round"><g transform="translate(290 110) rotate(0 80 0)"><path d="M-0.92 1.21 C40.42 0.34, 86.73 3.08, 158.34 1.01 M-0.15 0.47 C40.46 1.84, 77.45 -2, 161.07 -1.96" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(290 110) rotate(0 80 0)"><path d="M-1.18 -13.33 C-2.23 -10.64, -1.42 -5.48, -1.54 1.59 M-0.89 -13.61 C-0.41 -9.37, -1.29 -7.13, -0.52 0.48" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(290 110) rotate(0 80 0)"><path d="M-1.35 16.67 C-2.37 11.1, -1.51 7.99, -1.54 1.59 M-1.06 16.39 C-0.57 13.26, -1.41 8.14, -0.52 0.48" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(290 110) rotate(0 80 0)"><path d="M160.79 -0.45 L148.59 5.91 L146.19 -8.29 L160.48 -1.86" stroke="none" stroke-width="0" fill-rule="evenodd" class="ed-fill"/><path d="M160.72 -1.5 C155.97 -1.27, 153.08 1.55, 146.93 4.93 M161.01 -1.78 C158.19 0.38, 154.01 0.53, 147.95 3.81 M148.62 5.64 C146.9 -0.68, 146.5 -5.49, 146.72 -8.7 M147.82 4.91 C147.03 -0.37, 147.45 -5.42, 147.74 -8.76 M146.69 -7.04 C153.38 -5.21, 159.47 -3.18, 162.1 -0.77 M146.89 -8.79 C152.67 -5.3, 157.55 -3.84, 161.2 -1.34 M161.07 -1.96 C161.07 -1.96, 161.07 -1.96, 161.07 -1.96 M161.07 -1.96 C161.07 -1.96, 161.07 -1.96, 161.07 -1.96" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g transform="translate(350 70) rotate(0 16.549988001585007 12.5)"><text x="0" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="start" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">use</text></g></svg></div>  </figure>  
<p>An Independent Composable exclusively uses Vue’s Reactivity APIs. These composables operate independently of Vue component instances, making them straightforward to test.</p>
<h4 id="example--testing-strategy">Example &amp; Testing Strategy<a class="heading-link" aria-label="Link to section" href="#example--testing-strategy"><span class="heading-link-icon">#</span></a></h4>
<p>Here is an example of an independent composable that calculates the sum of two reactive values:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">Ref</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> computed</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> ComputedRef</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> useSum</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">a</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">number</span><span style="color:#89DDFF">&gt;,</span><span style="color:#E0AF68"> b</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">number</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> ComputedRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">number</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#7AA2F7"> computed</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> a</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> +</span><span style="color:#C0CAF5"> b</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import { Ref, computed, ComputedRef } from &#34;vue&#34;;

function useSum(a: Ref<number>, b: Ref<number>): ComputedRef<number> {
  return computed(() => a.value + b.value);
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>To test this composable, you would directly invoke it and assert its returned state:</p>
<p>Test with Vitest:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">useSum</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">correctly computes the sum of two numbers</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> num1</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">2</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> num2</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">3</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> sum</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useSum</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">num1</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> num2</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">sum</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">5</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="describe(&#34;useSum&#34;, () => {
  it(&#34;correctly computes the sum of two numbers&#34;, () => {
    const num1 = ref(2);
    const num2 = ref(3);
    const sum = useSum(num1, num2);

    expect(sum.value).toBe(5);
  });
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This test directly checks the functionality of useSum by passing reactive references and asserting the computed result.</p>
<hr/>
<h3 id="dependent-composables">Dependent Composables<a class="heading-link" aria-label="Link to section" href="#dependent-composables"><span class="heading-link-icon">#</span></a></h3>
<figure class="excalidraw-figure astro-hxyrieg5"> <div class="excalidraw-svg astro-hxyrieg5" role="img" aria-label="Dependent Composables Diagram"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 220" width="100%" class="excalidraw-rendered" preserveAspectRatio="xMidYMid meet">
  <!-- svg-source:excalidraw -->
  
  <defs>
    <style class="style-fonts">
      @font-face {
        font-family: Excalifont;
        src: url(data:font/woff2;base64,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);
          }
    </style>
    
  <style>
  .ed-text { fill: var(--excalidraw-text, #222e36); }
  .ed-fill { fill: var(--excalidraw-fill, #eaced7); }
  .ed-accent-fill { fill: var(--excalidraw-accent, #d3006a); }
  .ed-accent-stroke { stroke: var(--excalidraw-accent, #d3006a); }
</style></defs>
  <g stroke-linecap="round" transform="translate(10 10) rotate(0 140 100)"><path d="M194.66 9.12 C209.14 12.11, 221.16 20.23, 232.93 27.31 C244.7 34.39, 257.5 42.02, 265.27 51.6 C273.03 61.19, 277.7 73.57, 279.53 84.83 C281.35 96.09, 279.98 107.91, 276.23 119.15 C272.49 130.39, 265.59 142.18, 257.05 152.28 C248.51 162.39, 237.1 172.62, 225 179.77 C212.89 186.91, 199.79 192.09, 184.43 195.17 C169.07 198.24, 148.84 198.94, 132.84 198.2 C116.83 197.46, 102.95 195, 88.42 190.74 C73.9 186.47, 57.94 180.19, 45.71 172.6 C33.48 165.01, 22.29 154.8, 15.06 145.22 C7.82 135.64, 4.05 126.45, 2.32 115.12 C0.59 103.79, 1.29 88.72, 4.68 77.25 C8.07 65.77, 14.71 55.84, 22.67 46.27 C30.63 36.7, 39.83 26.57, 52.43 19.8 C65.03 13.04, 82.79 8.76, 98.27 5.69 C113.76 2.62, 127.03 0.53, 145.35 1.39 C163.66 2.25, 195.58 7.65, 208.16 10.84 C220.74 14.03, 221.66 18.81, 220.84 20.54 M96.61 4.53 C111.08 -0.66, 133.03 -1.23, 149.18 -0.7 C165.32 -0.16, 178.9 3.63, 193.48 7.72 C208.06 11.8, 225 16.23, 236.65 23.82 C248.3 31.4, 256.46 42.23, 263.36 53.23 C270.26 64.24, 276.11 78.29, 278.06 89.83 C280 101.38, 278.67 111.81, 275.02 122.5 C271.38 133.19, 264.57 144.76, 256.18 153.97 C247.8 163.18, 237.68 170.6, 224.72 177.76 C211.76 184.92, 193.73 193.07, 178.4 196.94 C163.08 200.8, 148.49 202.07, 132.76 200.94 C117.03 199.8, 98.81 194.24, 84.04 190.12 C69.28 186, 55.56 183.47, 44.16 176.22 C32.76 168.97, 22.57 157.26, 15.64 146.63 C8.72 136.01, 4.55 123.82, 2.61 112.48 C0.68 101.14, 0.29 90.1, 4.04 78.6 C7.8 67.09, 16.98 52.72, 25.14 43.44 C33.29 34.16, 40.76 29.77, 53 22.92 C65.23 16.08, 90.51 4.74, 98.53 2.37 C106.56 0, 100.14 6.84, 101.14 8.72" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(89.84508465681074 84.78932188134513) rotate(0 60.159965977072716 25)"><text x="60.159965977072716" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Dependent </text><text x="60.159965977072716" y="42.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Composables</text></g><g stroke-linecap="round" transform="translate(450 10) rotate(0 160 100)"><path d="M32 0 C103.36 -2.91, 170.31 -1.04, 288 0 M32 0 C101.68 1.26, 170.93 2.12, 288 0 M288 0 C306.75 -3.86, 321.85 10.27, 320 32 M288 0 C310.96 -2.47, 316.87 9.69, 320 32 M320 32 C322.22 85.97, 320.91 140.99, 320 168 M320 32 C319.64 85.19, 316.5 139.68, 320 168 M320 168 C323.14 191.59, 308.86 199, 288 200 M320 168 C318.17 188.54, 307.09 201.85, 288 200 M288 200 C215.24 195.61, 144.12 201.6, 32 200 M288 200 C195.43 203.09, 102.51 204.23, 32 200 M32 200 C13.35 196.5, 2.91 192.35, 0 168 M32 200 C14.54 203.75, 4.48 186.27, 0 168 M0 168 C-3.45 141.65, 1.44 107.9, 0 32 M0 168 C3.13 137.57, 2.68 109.08, 0 32 M0 32 C3.15 12.89, 11.24 -1.21, 32 0 M0 32 C4.38 9.69, 13.87 0.65, 32 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(496.07007598876953 47.5) rotate(0 113.92992401123047 62.5)"><text x="113.92992401123047" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Vues reactivity</text><text x="113.92992401123047" y="42.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">(ref, watch , computed)</text><text x="113.92992401123047" y="67.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">+</text><text x="113.92992401123047" y="92.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Lifecycle (onMounted)</text><text x="113.92992401123047" y="117.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Provide / Inject</text></g><g stroke-linecap="round"><g transform="translate(290 110) rotate(0 80 0)"><path d="M-0.92 1.21 C40.42 0.34, 86.73 3.08, 158.34 1.01 M-0.15 0.47 C40.46 1.84, 77.45 -2, 161.07 -1.96" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(290 110) rotate(0 80 0)"><path d="M-1.18 -13.33 C-2.23 -10.64, -1.42 -5.48, -1.54 1.59 M-0.89 -13.61 C-0.41 -9.37, -1.29 -7.13, -0.52 0.48" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(290 110) rotate(0 80 0)"><path d="M-1.35 16.67 C-2.37 11.1, -1.51 7.99, -1.54 1.59 M-1.06 16.39 C-0.57 13.26, -1.41 8.14, -0.52 0.48" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(290 110) rotate(0 80 0)"><path d="M160.79 -0.45 L148.59 5.91 L146.19 -8.29 L160.48 -1.86" stroke="none" stroke-width="0" fill-rule="evenodd" class="ed-fill"/><path d="M160.72 -1.5 C155.97 -1.27, 153.08 1.55, 146.93 4.93 M161.01 -1.78 C158.19 0.38, 154.01 0.53, 147.95 3.81 M148.62 5.64 C146.9 -0.68, 146.5 -5.49, 146.72 -8.7 M147.82 4.91 C147.03 -0.37, 147.45 -5.42, 147.74 -8.76 M146.69 -7.04 C153.38 -5.21, 159.47 -3.18, 162.1 -0.77 M146.89 -8.79 C152.67 -5.3, 157.55 -3.84, 161.2 -1.34 M161.07 -1.96 C161.07 -1.96, 161.07 -1.96, 161.07 -1.96 M161.07 -1.96 C161.07 -1.96, 161.07 -1.96, 161.07 -1.96" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g transform="translate(350 70) rotate(0 16.549988001585007 12.5)"><text x="0" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="start" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">use</text></g></svg></div>  </figure>  
<p><code>Dependent Composables</code> are distinguished by their reliance on Vue’s component instance. They often leverage features like lifecycle hooks or context for their operation. These composables are an integral part of a component and necessitate a distinct approach for testing, as opposed to Independent Composables.</p>
<h4 id="example--usage">Example &amp; Usage<a class="heading-link" aria-label="Link to section" href="#example--usage"><span class="heading-link-icon">#</span></a></h4>
<p>An exemplary Dependent Composable is <code>useLocalStorage</code>. This composable facilitates interaction with the browser’s localStorage and harnesses the <code>onMounted</code> lifecycle hook for initialization:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ref</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> computed</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> onMounted</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> watch</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> useLocalStorage</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">key</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> initialValue</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> T</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> value</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">initialValue</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> loadFromLocalStorage</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> storedValue</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> localStorage</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getItem</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">key</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">storedValue</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> null</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">      value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#0DB9D7"> JSON</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">parse</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">storedValue</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  onMounted</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">loadFromLocalStorage</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  watch</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> newValue</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    localStorage</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">setItem</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">key</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> JSON</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">stringify</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">newValue</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">value</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#7DCFFF"> default</span><span style="color:#C0CAF5"> useLocalStorage</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="import { ref, computed, onMounted, watch } from &#34;vue&#34;;

function useLocalStorage<T>(key: string, initialValue: T) {
  const value = ref<T>(initialValue);

  function loadFromLocalStorage() {
    const storedValue = localStorage.getItem(key);
    if (storedValue !== null) {
      value.value = JSON.parse(storedValue);
    }
  }

  onMounted(loadFromLocalStorage);

  watch(value, newValue => {
    localStorage.setItem(key, JSON.stringify(newValue));
  });

  return { value };
}

export default useLocalStorage;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This composable can be utilised within a component, for instance, to create a persistent counter:</p>
<p><img src="/_astro/counter-ui.BqY9549E_Z2w60If.webp" alt="Counter Ui" loading="lazy" decoding="async" fetchpriority="auto" width="1138" height="268"></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ... script content ...</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">h1</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Counter: {{ count }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">h1</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">button</span><span style="color:#BB9AF7"> @click</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">increment</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Increment</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
// ... script content ...
</script>

<template>
  <div>
    <h1>Counter: {{ count }}</h1>
    <button @click=&#34;increment&#34;>Increment</button>
  </div>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The primary benefit here is the seamless synchronization of the reactive <code>count</code> property with localStorage, ensuring persistence across sessions.</p>
<h3 id="testing-strategy">Testing Strategy<a class="heading-link" aria-label="Link to section" href="#testing-strategy"><span class="heading-link-icon">#</span></a></h3>
<p>To effectively test <code>useLocalStorage</code>, especially considering the <code>onMounted</code> lifecycle, we initially face a challenge. Let’s start with a basic test setup:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">useLocalStorage</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should load the initialValue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> value</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useLocalStorage</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">testKey</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">initValue</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">initValue</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should load from localStorage</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    localStorage</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">setItem</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">testKey</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> JSON</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">stringify</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">fromStorage</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> value</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useLocalStorage</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">testKey</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">initialValue</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">fromStorage</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="describe(&#34;useLocalStorage&#34;, () => {
  it(&#34;should load the initialValue&#34;, () => {
    const { value } = useLocalStorage(&#34;testKey&#34;, &#34;initValue&#34;);
    expect(value.value).toBe(&#34;initValue&#34;);
  });

  it(&#34;should load from localStorage&#34;, async () => {
    localStorage.setItem(&#34;testKey&#34;, JSON.stringify(&#34;fromStorage&#34;));
    const { value } = useLocalStorage(&#34;testKey&#34;, &#34;initialValue&#34;);
    expect(value.value).toBe(&#34;fromStorage&#34;);
  });
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Here, the first test will pass, asserting that the composable initialises with the given <code>initialValue</code>. However, the second test, which expects the composable to load a pre-existing value from localStorage, fails. The challenge arises because the <code>onMounted</code> lifecycle hook is not triggered during testing. To address this, we need to refactor our composable or our test setup to simulate the component mounting process.</p>
<hr/>
<h3 id="enhancing-testing-with-the-withsetup-helper-function">Enhancing Testing with the <code>withSetup</code> Helper Function<a class="heading-link" aria-label="Link to section" href="#enhancing-testing-with-the-withsetup-helper-function"><span class="heading-link-icon">#</span></a></h3>
<figure class="excalidraw-figure astro-hxyrieg5"> <div class="excalidraw-svg astro-hxyrieg5" role="img" aria-label="Mock withSetup Diagram"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 220" width="100%" class="excalidraw-rendered" preserveAspectRatio="xMidYMid meet">
  <!-- svg-source:excalidraw -->
  
  <defs>
    <style class="style-fonts">
      @font-face {
        font-family: Excalifont;
        src: url(data:font/woff2;base64,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);
          }
    </style>
    
  <style>
  .ed-text { fill: var(--excalidraw-text, #222e36); }
  .ed-fill { fill: var(--excalidraw-fill, #eaced7); }
  .ed-accent-fill { fill: var(--excalidraw-accent, #d3006a); }
  .ed-accent-stroke { stroke: var(--excalidraw-accent, #d3006a); }
</style></defs>
  <g stroke-linecap="round" transform="translate(10 10) rotate(0 100 100)"><path d="M32 0 C65.69 -5.55, 103.48 1.56, 168 0 M32 0 C67.06 -0.52, 98.3 -1.52, 168 0 M168 0 C192.3 2.79, 198.33 14.4, 200 32 M168 0 C193.56 0.71, 203.74 14.77, 200 32 M200 32 C198.45 75.07, 201.92 120.42, 200 168 M200 32 C196.98 72.11, 197.42 110.44, 200 168 M200 168 C198.95 187.49, 191.3 196.57, 168 200 M200 168 C201.34 193.18, 185.88 200.63, 168 200 M168 200 C112.5 197.68, 65.55 193.92, 32 200 M168 200 C134.18 199.22, 97.64 197.79, 32 200 M32 200 C12.41 199.91, 0.08 189.17, 0 168 M32 200 C9.74 204.07, 3.43 186.72, 0 168 M0 168 C2.77 135.62, -0.56 94.04, 0 32 M0 168 C-1.49 138.39, -0.46 109.73, 0 32 M0 32 C-0.23 10.71, 12.89 3.52, 32 0 M0 32 C0.22 7.68, 6.38 -2.48, 32 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(30.82006624341011 72.5) rotate(0 79.17993375658989 37.5)"><text x="79.17993375658989" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">useLocalStorage</text><text x="79.17993375658989" y="42.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">doesn't has </text><text x="79.17993375658989" y="67.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">lifeCycles</text></g><g stroke-linecap="round" transform="translate(610 10) rotate(0 100 100)"><path d="M32 0 C82.16 -2.25, 126.53 -1.98, 168 0 M32 0 C61.13 1.46, 91 -0.5, 168 0 M168 0 C187.67 -1.64, 200.62 9.8, 200 32 M168 0 C188.28 -0.58, 199.76 11.54, 200 32 M200 32 C199.22 84.18, 200.64 129.85, 200 168 M200 32 C200.59 72.68, 198.99 114.7, 200 168 M200 168 C202.21 187.87, 191.3 202.24, 168 200 M200 168 C202.35 188.22, 192.43 200.15, 168 200 M168 200 C125.05 193.88, 91.53 200.83, 32 200 M168 200 C133.73 203.47, 94.87 201.28, 32 200 M32 200 C12.1 197.67, -2.37 191.38, 0 168 M32 200 C9.16 202.27, 2.63 193.19, 0 168 M0 168 C-4.97 117.41, -1.1 60.9, 0 32 M0 168 C4.17 117.58, 3.06 67.98, 0 32 M0 32 C-1.16 6.98, 8.26 3.09, 32 0 M0 32 C2.16 11.94, 13.07 -0.35, 32 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(630.8200662434101 72.5) rotate(0 79.17993375658989 37.5)"><text x="79.17993375658989" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">useLocalStorage</text><text x="79.17993375658989" y="42.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">+</text><text x="79.17993375658989" y="67.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Component</text></g><g stroke-linecap="round" transform="translate(310 10) rotate(0 100 90)"><path d="M107.86 -0.77 C120.26 -1.54, 132.66 3.48, 144 8.53 C155.34 13.58, 167.32 20.67, 175.9 29.53 C184.48 38.39, 191.33 50.8, 195.49 61.69 C199.65 72.58, 201.54 83.59, 200.85 94.87 C200.15 106.16, 197.08 119.17, 191.29 129.4 C185.51 139.62, 176.17 148.94, 166.13 156.23 C156.08 163.52, 143.36 169.05, 131.03 173.13 C118.69 177.21, 104.32 181.21, 92.12 180.72 C79.93 180.22, 69.09 175.16, 57.85 170.19 C46.61 165.22, 33.18 159.01, 24.68 150.87 C16.18 142.73, 11.25 132.44, 6.85 121.35 C2.45 110.27, -2.37 96.35, -1.72 84.38 C-1.06 72.4, 5.08 59.62, 10.77 49.51 C16.46 39.39, 23.13 30.97, 32.44 23.71 C41.75 16.45, 48.81 8.46, 66.64 5.93 C84.48 3.4, 122.76 5.23, 139.43 8.53 C156.11 11.84, 167.64 24.87, 166.7 25.75 M131.41 1.07 C143.2 3.78, 153.99 15.05, 163.28 22.96 C172.57 30.87, 181.31 38.92, 187.13 48.55 C192.96 58.18, 197.29 69.7, 198.23 80.73 C199.17 91.75, 195.95 103.37, 192.79 114.72 C189.64 126.07, 186.86 139.43, 179.32 148.83 C171.78 158.23, 159.26 165.58, 147.55 171.14 C135.85 176.7, 121.73 181.48, 109.11 182.2 C96.48 182.93, 83.68 179.26, 71.83 175.48 C59.98 171.7, 47.56 166.8, 38.01 159.52 C28.46 152.23, 21.01 141.66, 14.54 131.78 C8.06 121.9, 1.08 111.75, -0.85 100.22 C-2.78 88.69, -1.39 73.7, 2.96 62.59 C7.3 51.48, 16.95 42.01, 25.21 33.57 C33.46 25.13, 41.99 17.24, 52.49 11.93 C62.98 6.63, 75.55 3.1, 88.17 1.74 C100.79 0.38, 121.89 3.36, 128.22 3.78 C134.55 4.2, 126.9 2.82, 126.16 4.26" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(357.1093566535028 62.36038969321089) rotate(0 52.67996522784233 37.5)"><text x="52.67996522784233" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">with Setup</text><text x="52.67996522784233" y="42.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">will add</text><text x="52.67996522784233" y="67.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">LifeCycles</text></g><g stroke-linecap="round"><g transform="translate(210 110) rotate(0 50 0)"><path d="M-0.35 -3.76 C22.3 -2.2, 52.32 -2.17, 98.33 0.96 M1.88 0.96 C38.68 -0.83, 75.5 -0.95, 98.71 -1.27" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(210 110) rotate(0 50 0)"><path d="M0.15 -20.15 C-1.4 -15.77, -0.14 -11.83, -0.98 -3.4 M0.99 -18.38 C0.32 -12.94, -0.26 -7.32, -0.84 -4.23" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(210 110) rotate(0 50 0)"><path d="M-1.12 9.82 C-2.26 6.34, -0.68 2.42, -0.98 -3.4 M-0.28 11.59 C-0.32 5.72, -0.43 0.02, -0.84 -4.23" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(210 110) rotate(0 50 0)"><path d="M98.65 -0.27 L86.58 3.98 L86.57 -8.45 L97.94 -3.08" stroke="none" stroke-width="0" fill-rule="evenodd" class="ed-fill"/><path d="M98.58 -2.68 C93.67 -0.55, 91.54 1.17, 84.57 5.58 M99.42 -0.91 C93.93 1.41, 88.48 3.82, 84.71 4.75 M85.31 4.91 C85.5 0.7, 84.22 -2.74, 84.44 -8.45 M85.05 4.83 C85.49 0.8, 85.56 -3.87, 85.43 -6.95 M86.02 -6.29 C87.22 -6.32, 91.78 -6.11, 97.36 -2.41 M84.87 -7.11 C89.25 -5.42, 95.25 -3.14, 98.79 -0.79 M98.71 -1.27 C98.71 -1.27, 98.71 -1.27, 98.71 -1.27 M98.71 -1.27 C98.71 -1.27, 98.71 -1.27, 98.71 -1.27" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g stroke-linecap="round"><g transform="translate(510 110) rotate(0 50 0)"><path d="M0.23 -1.01 C28.53 1.63, 61.71 2.29, 97.96 -2.87 M1.56 -1.84 C29.05 1.13, 55.31 2.32, 101.15 1.16" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(510 110) rotate(0 50 0)"><path d="M0.61 -16.38 C-0.72 -11.17, -0.13 -6.22, -0.54 -2.09 M1.11 -16.7 C0.66 -11.94, -0.18 -7.25, 0.66 -0.57" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(510 110) rotate(0 50 0)"><path d="M0.02 13.61 C-0.94 9.42, -0.16 4.97, -0.54 -2.09 M0.52 13.3 C0.37 9.58, -0.3 5.79, 0.66 -0.57" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(510 110) rotate(0 50 0)"><path d="M102.7 1.36 L86.14 8.28 L85.76 -4.87 L101.29 2.15" stroke="none" stroke-width="0" fill-rule="evenodd" class="ed-fill"/><path d="M101.24 0.78 C95.82 3.25, 92.26 5.53, 86.87 6.58 M101.74 0.47 C97.59 2.72, 93.01 5.01, 88.07 8.09 M86.46 7.2 C88.52 3.7, 88.43 -2.45, 87.45 -4.1 M87.96 7.76 C87.52 4.65, 87.97 1.42, 87.33 -4.51 M86.92 -6.19 C92.58 -2.38, 94.86 -2.09, 102.62 2.53 M87.25 -4.45 C91.28 -3.07, 96.08 -0.5, 101.1 0.53 M101.15 1.16 C101.15 1.16, 101.15 1.16, 101.15 1.16 M101.15 1.16 C101.15 1.16, 101.15 1.16, 101.15 1.16" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/></svg></div>  </figure>  
<p>To facilitate easier testing of composables that rely on Vue’s lifecycle hooks, we’ve developed a higher-order function named <code>withSetup</code>. This utility allows us to create a Vue component context programmatically, focusing primarily on the setup lifecycle function where composables are typically used.</p>
<h4 id="introduction-to-withsetup">Introduction to <code>withSetup</code><a class="heading-link" aria-label="Link to section" href="#introduction-to-withsetup"><span class="heading-link-icon">#</span></a></h4>
<p><code>withSetup</code> is designed to simulate a Vue component’s setup function, enabling us to test composables in an environment that closely mimics their real-world use. The function accepts a composable and returns both the composable’s result and a Vue app instance. This setup allows for comprehensive testing, including lifecycle and reactivity features.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#BB9AF7"> type</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">App</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">createApp</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> withSetup</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">composable</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> T</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> App</span><span style="color:#9ABDF5">]</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> result</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> T</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> app</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createApp</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#7AA2F7">    setup</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#C0CAF5">      result</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> composable</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {}</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  app</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">mount</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">document</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">createElement</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">div</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> [</span><span style="color:#7DCFFF">result</span><span style="color:#89DDFF">,</span><span style="color:#7DCFFF"> app</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import type { App } from &#34;vue&#34;;
import { createApp } from &#34;vue&#34;;

export function withSetup<T>(composable: () => T): [T, App] {
  let result: T;
  const app = createApp({
    setup() {
      result = composable();
      return () => {};
    },
  });
  app.mount(document.createElement(&#34;div&#34;));
  return [result, app];
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>In this implementation, <code>withSetup</code> mounts a minimal Vue app and executes the provided composable function during the setup phase. This approach allows us to capture and return the composable’s output alongside the app instance for further testing.</p>
<h4 id="utilizing-withsetup-in-tests">Utilizing <code>withSetup</code> in Tests<a class="heading-link" aria-label="Link to section" href="#utilizing-withsetup-in-tests"><span class="heading-link-icon">#</span></a></h4>
<p>With <code>withSetup</code>, we can enhance our testing strategy for composables like <code>useLocalStorage</code>, ensuring they behave as expected even when they depend on lifecycle hooks:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should load the value from localStorage if it was set before</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9D7CD8;font-style:italic"> async</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  localStorage</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">setItem</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">testKey</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> JSON</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">stringify</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">valueFromLocalStorage</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> [</span><span style="color:#BB9AF7">result</span><span style="color:#89DDFF">]</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> withSetup</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#7AA2F7"> useLocalStorage</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">testKey</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">testValue</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">result</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">valueFromLocalStorage</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="it(&#34;should load the value from localStorage if it was set before&#34;, async () => {
  localStorage.setItem(&#34;testKey&#34;, JSON.stringify(&#34;valueFromLocalStorage&#34;));
  const [result] = withSetup(() => useLocalStorage(&#34;testKey&#34;, &#34;testValue&#34;));
  expect(result.value.value).toBe(&#34;valueFromLocalStorage&#34;);
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This test demonstrates how <code>withSetup</code> enables the composable to execute as if it were part of a regular Vue component, ensuring the <code>onMounted</code> lifecycle hook is triggered as expected. Additionally, the robust TypeScript support enhances the development experience by providing clear type inference and error checking.</p>
<hr/>
<h3 id="testing-composables-with-inject">Testing Composables with Inject<a class="heading-link" aria-label="Link to section" href="#testing-composables-with-inject"><span class="heading-link-icon">#</span></a></h3>
<p>Another common scenario is testing composables that rely on Vue’s dependency injection system using <code>inject</code>. These composables present unique challenges as they expect certain values to be provided by ancestor components. Let’s explore how to effectively test such composables.</p>
<h4 id="example-composable-with-inject">Example Composable with Inject<a class="heading-link" aria-label="Link to section" href="#example-composable-with-inject"><span class="heading-link-icon">#</span></a></h4>
<p>Here’s an example of a composable that uses inject:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#BB9AF7"> type</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">InjectionKey</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">inject</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> MessageKey</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> InjectionKey</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">string</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> Symbol</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">message</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useMessage</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> message</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> inject</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">MessageKey</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">message</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">    throw</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Error</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Message must be provided</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> getUpperCase</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> message</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toUpperCase</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> getReversed</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> message</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">split</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">reverse</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">join</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    message</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    getUpperCase</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">    getReversed</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import type { InjectionKey } from &#34;vue&#34;;
import { inject } from &#34;vue&#34;;

export const MessageKey: InjectionKey<string> = Symbol(&#34;message&#34;);

export function useMessage() {
  const message = inject(MessageKey);

  if (!message) {
    throw new Error(&#34;Message must be provided&#34;);
  }

  const getUpperCase = () => message.toUpperCase();
  const getReversed = () => message.split(&#34;&#34;).reverse().join(&#34;&#34;);

  return {
    message,
    getUpperCase,
    getReversed,
  };
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h4 id="creating-a-test-helper">Creating a Test Helper<a class="heading-link" aria-label="Link to section" href="#creating-a-test-helper"><span class="heading-link-icon">#</span></a></h4>
<p>To test composables that use inject, we need a helper function that creates a testing environment with the necessary providers. Here’s a utility function that makes this possible:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#BB9AF7"> type</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">InjectionKey</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">createApp</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> defineComponent</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> h</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> provide</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> InstanceType</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">V</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> V</span><span style="color:#9D7CD8;font-style:italic"> extends</span><span style="color:#9ABDF5"> {</span><span style="color:#89DDFF"> new</span><span style="color:#9ABDF5"> (</span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#E0AF68">arg</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> any</span><span style="color:#9ABDF5">[])</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> infer</span><span style="color:#C0CAF5"> X</span><span style="color:#9ABDF5"> }</span><span style="color:#BB9AF7"> ?</span><span style="color:#C0CAF5"> X</span><span style="color:#BB9AF7"> :</span><span style="color:#0DB9D7"> never</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> VM</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">V</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> InstanceType</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">V</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> &amp;</span><span style="color:#9ABDF5"> {</span><span style="color:#7AA2F7"> unmount</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> InjectionConfig</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  key</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> InjectionKey</span><span style="color:#89DDFF">&lt;</span><span style="color:#0DB9D7">any</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  value</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> any</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useInjectedSetup</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">TResult</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#7AA2F7">  setup</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> TResult</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#E0AF68">  injections</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> InjectionConfig</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> []</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> TResult</span><span style="color:#89DDFF"> &amp;</span><span style="color:#9ABDF5"> {</span><span style="color:#7AA2F7"> unmount</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#9ABDF5"> }</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> result</span><span style="color:#89DDFF">!:</span><span style="color:#C0CAF5"> TResult</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> Comp</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> defineComponent</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#7AA2F7">    setup</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#C0CAF5">      result</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> setup</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#7AA2F7"> h</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">div</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> Provider</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> defineComponent</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#7AA2F7">    setup</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#C0CAF5">      injections</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">forEach</span><span style="color:#9ABDF5">((</span><span style="color:#89DDFF">{</span><span style="color:#E0AF68"> key</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> value</span><span style="color:#89DDFF"> }</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">        provide</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">key</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">      })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#7AA2F7"> h</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">Comp</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> mounted</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> mount</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">Provider</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#F7768E;font-weight:bold">    ...</span><span style="color:#C0CAF5">result</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    unmount</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> mounted</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">unmount</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  } </span><span style="color:#89DDFF">as</span><span style="color:#C0CAF5"> TResult</span><span style="color:#89DDFF"> &amp;</span><span style="color:#9ABDF5"> { </span><span style="color:#7AA2F7">unmount</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#0DB9D7"> void</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> mount</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">V</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">Comp</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> V</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> el</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> document</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">createElement</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">div</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> app</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createApp</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">Comp</span><span style="color:#89DDFF"> as</span><span style="color:#0DB9D7"> any</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> unmount</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> app</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">unmount</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> comp</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> app</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">mount</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">el</span><span style="color:#9ABDF5">) </span><span style="color:#89DDFF">as</span><span style="color:#0DB9D7"> any</span><span style="color:#89DDFF"> as</span><span style="color:#C0CAF5"> VM</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">V</span><span style="color:#89DDFF">&gt;;</span></span>
<span class="line"><span style="color:#C0CAF5">  comp</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">unmount</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> unmount</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> comp</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import type { InjectionKey } from &#34;vue&#34;;
import { createApp, defineComponent, h, provide } from &#34;vue&#34;;

type InstanceType<V> = V extends { new (...arg: any[]): infer X } ? X : never;
type VM<V> = InstanceType<V> &#38; { unmount: () => void };

interface InjectionConfig {
  key: InjectionKey<any> | string;
  value: any;
}

export function useInjectedSetup<TResult>(
  setup: () => TResult,
  injections: InjectionConfig[] = []
): TResult &#38; { unmount: () => void } {
  let result!: TResult;

  const Comp = defineComponent({
    setup() {
      result = setup();
      return () => h(&#34;div&#34;);
    },
  });

  const Provider = defineComponent({
    setup() {
      injections.forEach(({ key, value }) => {
        provide(key, value);
      });
      return () => h(Comp);
    },
  });

  const mounted = mount(Provider);

  return {
    ...result,
    unmount: mounted.unmount,
  } as TResult &#38; { unmount: () => void };
}

function mount<V>(Comp: V) {
  const el = document.createElement(&#34;div&#34;);
  const app = createApp(Comp as any);
  const unmount = () => app.unmount();
  const comp = app.mount(el) as any as VM<V>;
  comp.unmount = unmount;
  return comp;
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h4 id="writing-tests">Writing Tests<a class="heading-link" aria-label="Link to section" href="#writing-tests"><span class="heading-link-icon">#</span></a></h4>
<p>With our helper function in place, we can now write comprehensive tests for our inject-dependent composable:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">describe</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> expect</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> it</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vitest</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useInjectedSetup</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">../helper</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">MessageKey</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> useMessage</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">../useMessage</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">useMessage</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should handle injected message</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> wrapper</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useInjectedSetup</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#9ABDF5">      () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#7AA2F7"> useMessage</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      [{ </span><span style="color:#73DACA">key</span><span style="color:#89DDFF">:</span><span style="color:#7DCFFF"> MessageKey</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> value</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">hello world</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5"> }]</span></span>
<span class="line"><span style="color:#9ABDF5">    )</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">wrapper</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">message</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">hello world</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">wrapper</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getUpperCase</span><span style="color:#9ABDF5">())</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">HELLO WORLD</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">wrapper</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getReversed</span><span style="color:#9ABDF5">())</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">dlrow olleh</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">    wrapper</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">unmount</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">should throw error when message is not provided</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">      useInjectedSetup</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#7AA2F7"> useMessage</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> [])</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toThrow</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Message must be provided</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="import { describe, expect, it } from &#34;vitest&#34;;
import { useInjectedSetup } from &#34;../helper&#34;;
import { MessageKey, useMessage } from &#34;../useMessage&#34;;

describe(&#34;useMessage&#34;, () => {
  it(&#34;should handle injected message&#34;, () => {
    const wrapper = useInjectedSetup(
      () => useMessage(),
      [{ key: MessageKey, value: &#34;hello world&#34; }]
    );

    expect(wrapper.message).toBe(&#34;hello world&#34;);
    expect(wrapper.getUpperCase()).toBe(&#34;HELLO WORLD&#34;);
    expect(wrapper.getReversed()).toBe(&#34;dlrow olleh&#34;);

    wrapper.unmount();
  });

  it(&#34;should throw error when message is not provided&#34;, () => {
    expect(() => {
      useInjectedSetup(() => useMessage(), []);
    }).toThrow(&#34;Message must be provided&#34;);
  });
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The <code>useInjectedSetup</code> helper creates a testing environment that:</p>
<ol>
<li>Simulates a component hierarchy</li>
<li>Provides the necessary injection values</li>
<li>Executes the composable in a proper Vue context</li>
<li>Returns the composable’s result along with an unmount function</li>
</ol>
<p>This approach allows us to:</p>
<ul>
<li>Test composables that depend on inject</li>
<li>Verify error handling when required injections are missing</li>
<li>Test the full functionality of methods that use injected values</li>
<li>Properly clean up after tests by unmounting the test component</li>
</ul>
<p>Remember to always unmount the test component after each test to prevent memory leaks and ensure test isolation.</p>
<hr/>
<h2 id="summary">Summary<a class="heading-link" aria-label="Link to section" href="#summary"><span class="heading-link-icon">#</span></a></h2>

















<table><thead><tr><th>Independent Composables 🔓</th><th>Dependent Composables 🔗</th></tr></thead><tbody><tr><td data-label="Independent Composables 🔓">- ✅ can be tested directly</td><td data-label="Dependent Composables 🔗">- 🧪 need a component to test</td></tr><tr><td data-label="Independent Composables 🔓">- 🛠️ uses everything beside of lifecycles and provide / inject</td><td data-label="Dependent Composables 🔗">- 🔄 uses Lifecycles or Provide / Inject</td></tr></tbody></table>
<p>In our exploration of testing Vue composables, we uncovered two distinct categories: <strong>Independent Composables</strong> and <strong>Dependent Composables</strong>. Independent Composables stand alone and can be tested akin to regular functions, showcasing straightforward testing procedures. Meanwhile, Dependent Composables, intricately tied to Vue’s component system and lifecycle hooks, require a more nuanced approach. For these, we learned the effectiveness of utilizing a helper function, such as <code>withSetup</code>, to simulate a component context, enabling comprehensive testing.</p>
<p>I hope this blog post has been insightful and useful in enhancing your understanding of testing Vue composables. I’m also keen to learn about your experiences and methods in testing composables within your projects. Your insights and approaches could provide valuable perspectives and contribute to the broader Vue community’s knowledge.</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_how-to-test-vue-composables" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="how-to-test-vue-composables" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vue</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/testing/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">testing</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/how-to-test-vue-composables/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/how-to-test-vue-composables/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/how-to-test-vue-composables/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/how-to-test-vue-composables/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/how-to-test-vue-composables/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/how-to-test-vue-composables/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/how-to-test-vue-composables/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/mastering-vue-3-composables-a-comprehensive-style-guide/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Mastering Vue 3 Composables: A Comprehensive Style Guide</h3> <p class="related-post-description astro-vj4tpspi"> Did you ever struggle how to write better composables in Vue? In this Blog post I try to give some tips how to do that </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2023-09-16T15:22:00.000Z">Sep 16, 2023</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/inline-vue-composables-refactoring/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">The Inline Vue Composables Refactoring pattern</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to apply Martin Fowler&#39;s Extract Function pattern to Vue components using inline composables, making your code cleaner and more maintainable. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-04-01T00:00:00.000Z">Apr 1, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/stop-white-box-testing-vue/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Stop White Box Testing Vue Components Use Testing Library Instead</h3> <p class="related-post-description astro-vj4tpspi"> White Box testing makes your Vue tests fragile and misleading. In this post, I’ll show you how Testing Library helps you write Black Box tests that are resilient, realistic, and focused on actual user behavior </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-04-19T00:00:00.000Z">Apr 19, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "how-to-test-vue-composables";

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
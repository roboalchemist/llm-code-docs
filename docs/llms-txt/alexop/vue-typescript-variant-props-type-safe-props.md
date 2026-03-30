# Source: https://alexop.dev/posts/vue-typescript-variant-props-type-safe-props

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/vue-typescript-variant-props-type-safe-props/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>How to Use the Variant Props Pattern in Vue | alexop.dev</title><meta name="title" content="How to Use the Variant Props Pattern in Vue | alexop.dev"><meta name="description" content="Learn how to create type-safe Vue components where prop types depend on other props using TypeScript discriminated unions. A practical guide with real-world examples."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="How to Use the Variant Props Pattern in Vue | alexop.dev"><meta property="og:description" content="Learn how to create type-safe Vue components where prop types depend on other props using TypeScript discriminated unions. A practical guide with real-world examples."><meta property="og:url" content="https://alexop.dev/posts/vue-typescript-variant-props-type-safe-props/"><meta property="og:image" content="https://alexop.dev/posts/how-to-use-the-variant-props-pattern-in-vue/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2024-12-15T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/vue-typescript-variant-props-type-safe-props/"><meta property="twitter:title" content="How to Use the Variant Props Pattern in Vue | alexop.dev"><meta property="twitter:description" content="Learn how to create type-safe Vue components where prop types depend on other props using TypeScript discriminated unions. A practical guide with real-world examples."><meta property="twitter:image" content="https://alexop.dev/posts/how-to-use-the-variant-props-pattern-in-vue/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"How to Use the Variant Props Pattern in Vue | alexop.dev","description":"Learn how to create type-safe Vue components where prop types depend on other props using TypeScript discriminated unions. A practical guide with real-world examples.","image":"https://alexop.dev/posts/how-to-use-the-variant-props-pattern-in-vue/index.png","datePublished":"2024-12-15T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: how-to-use-the-variant-props-pattern-in-vue; }@layer astro { ::view-transition-old(how-to-use-the-variant-props-pattern-in-vue) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(how-to-use-the-variant-props-pattern-in-vue) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(how-to-use-the-variant-props-pattern-in-vue) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(how-to-use-the-variant-props-pattern-in-vue) { 
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
	animation-name: astroFadeIn; }</style><style>.vue-playground-wrapper:where(.astro-y4iadjqs){border:1px solid rgb(var(--color-border));border-radius:.375rem;overflow:hidden;background-color:rgb(var(--color-card));display:flex;flex-direction:column}.iframe-container:where(.astro-y4iadjqs){flex:1;overflow:hidden;position:relative}iframe:where(.astro-y4iadjqs){border:none;position:absolute;top:0;left:0;width:100%;background-color:rgb(var(--color-fill))}.playground-footer:where(.astro-y4iadjqs){height:40px;border-top:1px solid rgb(var(--color-border));display:flex;align-items:center;justify-content:flex-end;padding:0 1rem;background-color:rgb(var(--color-card-muted));flex-shrink:0}.open-playground-button:where(.astro-y4iadjqs){display:inline-flex;align-items:center;gap:.5rem;padding:.5rem 1rem;border-radius:.375rem;font-size:.875rem;color:rgb(var(--color-text-base));text-decoration:none;transition:all .2s}.open-playground-button:where(.astro-y4iadjqs):hover{color:rgb(var(--color-accent));background-color:rgb(var(--color-card))}.external-link-icon:where(.astro-y4iadjqs){stroke:currentColor}.iframe-container:where(.astro-y4iadjqs){-ms-overflow-style:none;scrollbar-width:none}.iframe-container:where(.astro-y4iadjqs)::-webkit-scrollbar{display:none}.vue-playground-wrapper:where(.astro-y4iadjqs),.playground-footer:where(.astro-y4iadjqs),.open-playground-button:where(.astro-y4iadjqs){transition:background-color .3s ease,border-color .3s ease,color .3s ease}
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">How to Use the Variant Props Pattern in Vue</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2024-12-15T00:00:00.000Z">Dec 15, 2024</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="wrknU" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;How to Use the Variant Props Pattern in Vue&quot;],&quot;content&quot;:[0,&quot;import VuePlayground from \&quot;@features/mdx-components/components/VuePlayground.astro\&quot;;\nimport YouTube from \&quot;@features/mdx-components/components/YouTube.astro\&quot;;\n\nBuilding Vue components that handle multiple variations while maintaining type safety can be tricky. Let&#39;s dive into the Variant Props Pattern (VPP) - a powerful approach that uses TypeScript&#39;s discriminated unions with Vue&#39;s composition API to create truly type-safe component variants.\n\n## TL;DR\n\nThe Variant Props Pattern in Vue combines TypeScript&#39;s discriminated unions with Vue&#39;s prop system to create type-safe component variants. Instead of using complex type utilities, we explicitly mark incompatible props as never to prevent prop mixing at compile time:\n\n```typescript\n// Define base props\ntype BaseProps = {\n  title: string;\n};\n\n// Success variant prevents error props\ntype SuccessProps = BaseProps &amp; {\n  variant: \&quot;success\&quot;;\n  message: string;\n  errorCode?: never; // Prevents mixing\n};\n\n// Error variant prevents success props\ntype ErrorProps = BaseProps &amp; {\n  variant: \&quot;error\&quot;;\n  errorCode: string;\n  message?: never; // Prevents mixing\n};\n\ntype Props = SuccessProps | ErrorProps;\n```\n\nThis pattern provides compile-time safety, excellent IDE support, and reliable vue-tsc compatibility. Perfect for components that need multiple, mutually exclusive prop combinations.\n\n## The Problem: Mixed Props Nightmare\n\nPicture this: You&#39;re building a notification component that needs to handle both success and error states. Each state has its own specific properties:\n\n- Success notifications need a `message` and `duration`\n- Error notifications need an `errorCode` and a `retryable` flag\n\nWithout proper type safety, developers might accidentally mix these props:\n\n```html\n&lt;!-- This should fail! --&gt;\n&lt;NotificationAlert\n  variant=\&quot;primary\&quot;\n  title=\&quot;Data Saved\&quot;\n  message=\&quot;Success!\&quot;\n  errorCode=\&quot;UPLOAD_001\&quot;  &lt;!-- 🚨 Mixing success and error props --&gt;\n  :duration=\&quot;5000\&quot;\n  @close=\&quot;handleClose\&quot;\n/&gt;\n```\n\n## The Simple Solution That Doesn&#39;t Work\n\nYour first instinct might be to define separate interfaces:\n\n```typescript\ninterface SuccessProps {\n  title: string;\n  variant: \&quot;primary\&quot; | \&quot;secondary\&quot;;\n  message: string;\n  duration: number;\n}\n\ninterface ErrorProps {\n  title: string;\n  variant: \&quot;danger\&quot; | \&quot;warning\&quot;;\n  errorCode: string;\n  retryable: boolean;\n}\n\n// 🚨 This allows mixing both types!\ntype Props = SuccessProps &amp; ErrorProps;\n```\n\nThe problem? This approach allows developers to use both success and error props simultaneously - definitely not what we want!\n\n## Using Discriminated Unions with `never`\n\n&gt; **TypeScript Tip**: The `never` type is a special type in TypeScript that represents values that never occur. When a property is marked as `never`, TypeScript ensures that value can never be assigned to that property. This makes it perfect for creating mutually exclusive props, as it prevents developers from accidentally using props that shouldn&#39;t exist together.\n&gt;\n&gt; The `never` type commonly appears in TypeScript in several scenarios:\n&gt;\n&gt; - Functions that never return (throw errors or have infinite loops)\n&gt; - Exhaustive type checking in switch statements\n&gt; - Impossible type intersections (e.g., `string &amp; number`)\n&gt; - Making properties mutually exclusive, as we do in this pattern\n\nThe main trick to make it work with the current implmenation of defineProps is to use `never` to explicitly mark unused variant props.\n\n```typescript\n// Base props shared between variants\ntype BaseProps = {\n  title: string;\n};\n\n// Success variant\ntype SuccessProps = BaseProps &amp; {\n  variant: \&quot;primary\&quot; | \&quot;secondary\&quot;;\n  message: string;\n  duration: number;\n  // Explicitly mark error props as never\n  errorCode?: never;\n  retryable?: never;\n};\n\n// Error variant\ntype ErrorProps = BaseProps &amp; {\n  variant: \&quot;danger\&quot; | \&quot;warning\&quot;;\n  errorCode: string;\n  retryable: boolean;\n  // Explicitly mark success props as never\n  message?: never;\n  duration?: never;\n};\n\n// Final props type - only one variant allowed!\ntype Props = SuccessProps | ErrorProps;\n```\n\n## Important Note About Vue Components\n\nWhen implementing this pattern, you&#39;ll need to make your component generic due to a current type restriction in `defineComponent`.\nBy making the component generic, we can bypass `defineComponent` and define the component as a functional component:\n\n```vue\n&lt;script setup lang=\&quot;ts\&quot; generic=\&quot;T\&quot;&gt;\n// Now our discriminated union props will work correctly\ntype BaseProps = {\n  title: string;\n};\n\ntype SuccessProps = BaseProps &amp; {\n  variant: \&quot;primary\&quot; | \&quot;secondary\&quot;;\n  message: string;\n  duration: number;\n  errorCode?: never;\n  retryable?: never;\n};\n\n// ... rest of the types\n&lt;/script&gt;\n```\n\nThis approach allows TypeScript to properly enforce our prop variants at compile time.\n\n## Putting It All Together\n\nHere&#39;s our complete notification component using the Variant Props Pattern:\n\n&lt;VuePlayground url=\&quot;https://play.vuejs.org/#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\&quot; /&gt;\n\n## Conclusion\n\nThe Variant Props Pattern (VPP) provides a robust approach for building type-safe Vue components. While the Vue team is working on improving native support for discriminated unions [in vuejs/core#8952](https://github.com/vuejs/core/issues/8952), this pattern offers a practical solution today:\n\nUnfortunately, what currently is not working is using helper utility types like Xor so that we don&#39;t have to\nmanually mark unused variant props as never. When you do that, you will get an error from vue-tsc.\n\nExample of a helper type like Xor:\n\n```typescript\ntype Without&lt;T, U&gt; = { [P in Exclude&lt;keyof T, keyof U&gt;]?: never };\ntype XOR&lt;T, U&gt; = T | U extends object\n  ? (Without&lt;T, U&gt; &amp; U) | (Without&lt;U, T&gt; &amp; T)\n  : T | U;\n\n// Success notification properties\ntype SuccessProps = {\n  title: string;\n  variant: \&quot;primary\&quot; | \&quot;secondary\&quot;;\n  message: string;\n  duration: number;\n};\n\n// Error notification properties\ntype ErrorProps = {\n  title: string;\n  variant: \&quot;danger\&quot; | \&quot;warning\&quot;;\n  errorCode: string;\n  retryable: boolean;\n};\n\n// Final props type - only one variant allowed! ✨\ntype Props = XOR&lt;SuccessProps, ErrorProps&gt;;\n```\n\n## Video Reference\n\nIf you also prefer to learn this in video format, check out this tutorial:\n\n&lt;YouTube\n  id=\&quot;vyD5pYOa5mY\&quot;\n  title=\&quot;Understanding TypeScript Discriminated Unions in Vue\&quot;\n/&gt;&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>Building Vue components that handle multiple variations while maintaining type safety can be tricky. Let’s dive into the Variant Props Pattern (VPP) - a powerful approach that uses TypeScript’s discriminated unions with Vue’s composition API to create truly type-safe component variants.</p>
<h2 id="tldr">TL;DR<a class="heading-link" aria-label="Link to section" href="#tldr"><span class="heading-link-icon">#</span></a></h2>
<p>The Variant Props Pattern in Vue combines TypeScript’s discriminated unions with Vue’s prop system to create type-safe component variants. Instead of using complex type utilities, we explicitly mark incompatible props as never to prevent prop mixing at compile time:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Define base props</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> BaseProps</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  title</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Success variant prevents error props</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> SuccessProps</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> BaseProps</span><span style="color:#89DDFF"> &amp;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  variant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">success</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  message</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  errorCode</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> never</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Prevents mixing</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Error variant prevents success props</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> ErrorProps</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> BaseProps</span><span style="color:#89DDFF"> &amp;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  variant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  errorCode</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  message</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> never</span><span style="color:#89DDFF">;</span><span style="color:#51597D;font-style:italic"> // Prevents mixing</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> Props</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> SuccessProps</span><span style="color:#89DDFF"> |</span><span style="color:#C0CAF5"> ErrorProps</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// Define base props
type BaseProps = {
  title: string;
};

// Success variant prevents error props
type SuccessProps = BaseProps &#38; {
  variant: &#34;success&#34;;
  message: string;
  errorCode?: never; // Prevents mixing
};

// Error variant prevents success props
type ErrorProps = BaseProps &#38; {
  variant: &#34;error&#34;;
  errorCode: string;
  message?: never; // Prevents mixing
};

type Props = SuccessProps | ErrorProps;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This pattern provides compile-time safety, excellent IDE support, and reliable vue-tsc compatibility. Perfect for components that need multiple, mutually exclusive prop combinations.</p>
<h2 id="the-problem-mixed-props-nightmare">The Problem: Mixed Props Nightmare<a class="heading-link" aria-label="Link to section" href="#the-problem-mixed-props-nightmare"><span class="heading-link-icon">#</span></a></h2>
<p>Picture this: You’re building a notification component that needs to handle both success and error states. Each state has its own specific properties:</p>
<ul>
<li>Success notifications need a <code>message</code> and <code>duration</code></li>
<li>Error notifications need an <code>errorCode</code> and a <code>retryable</code> flag</li>
</ul>
<p>Without proper type safety, developers might accidentally mix these props:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="html"><code><span class="line"><span style="color:#51597D;font-style:italic">&lt;!-- This should fail! --&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#FF5370">NotificationAlert</span></span>
<span class="line"><span style="color:#BB9AF7">  variant</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">primary</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">  title</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Data Saved</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">  message</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">Success!</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">  errorCode</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">UPLOAD_001</span><span style="color:#89DDFF">&quot;</span><span style="color:#FF5370">  &lt;!--</span><span style="color:#BB9AF7"> 🚨</span><span style="color:#BB9AF7"> Mixing</span><span style="color:#BB9AF7"> success</span><span style="color:#BB9AF7"> and</span><span style="color:#BB9AF7"> error</span><span style="color:#BB9AF7"> props</span><span style="color:#BB9AF7"> --</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#9AA5CE">  :duration=&quot;5000&quot;</span></span>
<span class="line"><span style="color:#9AA5CE">  @close=&quot;handleClose&quot;</span></span>
<span class="line"><span style="color:#9AA5CE">/&gt;</span></span></code><button type="button" class="copy" data-code="<!-- This should fail! -->
<NotificationAlert
  variant=&#34;primary&#34;
  title=&#34;Data Saved&#34;
  message=&#34;Success!&#34;
  errorCode=&#34;UPLOAD_001&#34;  <!-- 🚨 Mixing success and error props -->
  :duration=&#34;5000&#34;
  @close=&#34;handleClose&#34;
/>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="the-simple-solution-that-doesnt-work">The Simple Solution That Doesn’t Work<a class="heading-link" aria-label="Link to section" href="#the-simple-solution-that-doesnt-work"><span class="heading-link-icon">#</span></a></h2>
<p>Your first instinct might be to define separate interfaces:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> SuccessProps</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  title</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  variant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">primary</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">secondary</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  message</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  duration</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> ErrorProps</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  title</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  variant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">danger</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">warning</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  errorCode</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  retryable</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// 🚨 This allows mixing both types!</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> Props</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> SuccessProps</span><span style="color:#89DDFF"> &amp;</span><span style="color:#C0CAF5"> ErrorProps</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="interface SuccessProps {
  title: string;
  variant: &#34;primary&#34; | &#34;secondary&#34;;
  message: string;
  duration: number;
}

interface ErrorProps {
  title: string;
  variant: &#34;danger&#34; | &#34;warning&#34;;
  errorCode: string;
  retryable: boolean;
}

// 🚨 This allows mixing both types!
type Props = SuccessProps &#38; ErrorProps;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The problem? This approach allows developers to use both success and error props simultaneously - definitely not what we want!</p>
<h2 id="using-discriminated-unions-with-never">Using Discriminated Unions with <code>never</code><a class="heading-link" aria-label="Link to section" href="#using-discriminated-unions-with-never"><span class="heading-link-icon">#</span></a></h2>
<blockquote>
<p><strong>TypeScript Tip</strong>: The <code>never</code> type is a special type in TypeScript that represents values that never occur. When a property is marked as <code>never</code>, TypeScript ensures that value can never be assigned to that property. This makes it perfect for creating mutually exclusive props, as it prevents developers from accidentally using props that shouldn’t exist together.</p>
<p>The <code>never</code> type commonly appears in TypeScript in several scenarios:</p>
<ul>
<li>Functions that never return (throw errors or have infinite loops)</li>
<li>Exhaustive type checking in switch statements</li>
<li>Impossible type intersections (e.g., <code>string &amp; number</code>)</li>
<li>Making properties mutually exclusive, as we do in this pattern</li>
</ul>
</blockquote>
<p>The main trick to make it work with the current implmenation of defineProps is to use <code>never</code> to explicitly mark unused variant props.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Base props shared between variants</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> BaseProps</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  title</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Success variant</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> SuccessProps</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> BaseProps</span><span style="color:#89DDFF"> &amp;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  variant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">primary</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">secondary</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  message</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  duration</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Explicitly mark error props as never</span></span>
<span class="line"><span style="color:#73DACA">  errorCode</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> never</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  retryable</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> never</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Error variant</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> ErrorProps</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> BaseProps</span><span style="color:#89DDFF"> &amp;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  variant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">danger</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">warning</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  errorCode</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  retryable</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Explicitly mark success props as never</span></span>
<span class="line"><span style="color:#73DACA">  message</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> never</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  duration</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> never</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Final props type - only one variant allowed!</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> Props</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> SuccessProps</span><span style="color:#89DDFF"> |</span><span style="color:#C0CAF5"> ErrorProps</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="// Base props shared between variants
type BaseProps = {
  title: string;
};

// Success variant
type SuccessProps = BaseProps &#38; {
  variant: &#34;primary&#34; | &#34;secondary&#34;;
  message: string;
  duration: number;
  // Explicitly mark error props as never
  errorCode?: never;
  retryable?: never;
};

// Error variant
type ErrorProps = BaseProps &#38; {
  variant: &#34;danger&#34; | &#34;warning&#34;;
  errorCode: string;
  retryable: boolean;
  // Explicitly mark success props as never
  message?: never;
  duration?: never;
};

// Final props type - only one variant allowed!
type Props = SuccessProps | ErrorProps;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="important-note-about-vue-components">Important Note About Vue Components<a class="heading-link" aria-label="Link to section" href="#important-note-about-vue-components"><span class="heading-link-icon">#</span></a></h2>
<p>When implementing this pattern, you’ll need to make your component generic due to a current type restriction in <code>defineComponent</code>.
By making the component generic, we can bypass <code>defineComponent</code> and define the component as a functional component:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> generic</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Now our discriminated union props will work correctly</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> BaseProps</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  title</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> SuccessProps</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> BaseProps</span><span style="color:#89DDFF"> &amp;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  variant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">primary</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">secondary</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  message</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  duration</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  errorCode</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> never</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  retryable</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> never</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// ... rest of the types</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34; generic=&#34;T&#34;>
// Now our discriminated union props will work correctly
type BaseProps = {
  title: string;
};

type SuccessProps = BaseProps &#38; {
  variant: &#34;primary&#34; | &#34;secondary&#34;;
  message: string;
  duration: number;
  errorCode?: never;
  retryable?: never;
};

// ... rest of the types
</script>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This approach allows TypeScript to properly enforce our prop variants at compile time.</p>
<h2 id="putting-it-all-together">Putting It All Together<a class="heading-link" aria-label="Link to section" href="#putting-it-all-together"><span class="heading-link-icon">#</span></a></h2>
<p>Here’s our complete notification component using the Variant Props Pattern:</p>
<div class="vue-playground-wrapper astro-y4iadjqs" style="width: 100%; height: calc(600px);"> <div class="iframe-container astro-y4iadjqs"> <iframe src="https://play.vuejs.org/#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" style="width: 100%; height: calc(600px - 40px + 48px); margin-top: -48px;" loading="lazy" allow="clipboard-write" title="Vue.js Playground" class="astro-y4iadjqs">
    </iframe> </div> <div class="playground-footer astro-y4iadjqs"> <a href="https://play.vuejs.org/#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" target="_blank" rel="noopener noreferrer" class="open-playground-button astro-y4iadjqs">
Open in Vue Playground
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="external-link-icon astro-y4iadjqs"> <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" class="astro-y4iadjqs"></path> <polyline points="15 3 21 3 21 9" class="astro-y4iadjqs"></polyline> <line x1="10" y1="14" x2="21" y2="3" class="astro-y4iadjqs"></line> </svg> </a> </div> </div> 
<h2 id="conclusion">Conclusion<a class="heading-link" aria-label="Link to section" href="#conclusion"><span class="heading-link-icon">#</span></a></h2>
<p>The Variant Props Pattern (VPP) provides a robust approach for building type-safe Vue components. While the Vue team is working on improving native support for discriminated unions <a href="https://github.com/vuejs/core/issues/8952" rel="noopener noreferrer" target="_blank">in vuejs/core#8952</a>, this pattern offers a practical solution today:</p>
<p>Unfortunately, what currently is not working is using helper utility types like Xor so that we don’t have to
manually mark unused variant props as never. When you do that, you will get an error from vue-tsc.</p>
<p>Example of a helper type like Xor:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> Without</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> U</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span><span style="color:#9ABDF5"> [</span><span style="color:#C0CAF5">P</span><span style="color:#89DDFF"> in</span><span style="color:#C0CAF5"> Exclude</span><span style="color:#89DDFF">&lt;keyof</span><span style="color:#C0CAF5"> T</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> keyof</span><span style="color:#C0CAF5"> U</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> never</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> XOR</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> U</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> T</span><span style="color:#89DDFF"> |</span><span style="color:#C0CAF5"> U</span><span style="color:#9D7CD8;font-style:italic"> extends</span><span style="color:#0DB9D7"> object</span></span>
<span class="line"><span style="color:#BB9AF7">  ?</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">Without</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">T</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> U</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> &amp;</span><span style="color:#C0CAF5"> U</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF"> |</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">Without</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">U</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> T</span><span style="color:#89DDFF">&gt;</span><span style="color:#89DDFF"> &amp;</span><span style="color:#C0CAF5"> T</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7">  :</span><span style="color:#C0CAF5"> T</span><span style="color:#89DDFF"> |</span><span style="color:#C0CAF5"> U</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Success notification properties</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> SuccessProps</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  title</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  variant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">primary</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">secondary</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  message</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  duration</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Error notification properties</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> ErrorProps</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  title</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  variant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">danger</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">warning</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  errorCode</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  retryable</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Final props type - only one variant allowed! ✨</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> Props</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> XOR</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">SuccessProps</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> ErrorProps</span><span style="color:#89DDFF">&gt;;</span></span></code><button type="button" class="copy" data-code="type Without<T, U> = { [P in Exclude<keyof T, keyof U>]?: never };
type XOR<T, U> = T | U extends object
  ? (Without<T, U> &#38; U) | (Without<U, T> &#38; T)
  : T | U;

// Success notification properties
type SuccessProps = {
  title: string;
  variant: &#34;primary&#34; | &#34;secondary&#34;;
  message: string;
  duration: number;
};

// Error notification properties
type ErrorProps = {
  title: string;
  variant: &#34;danger&#34; | &#34;warning&#34;;
  errorCode: string;
  retryable: boolean;
};

// Final props type - only one variant allowed! ✨
type Props = XOR<SuccessProps, ErrorProps>;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="video-reference">Video Reference<a class="heading-link" aria-label="Link to section" href="#video-reference"><span class="heading-link-icon">#</span></a></h2>
<p>If you also prefer to learn this in video format, check out this tutorial:</p>
<div class="mb-8"> <div class="relative w-full pb-[56.25%]"> <iframe src="https://www.youtube.com/embed/vyD5pYOa5mY" title="Understanding TypeScript Discriminated Unions in Vue" class="absolute left-0 top-0 h-full w-full rounded-lg" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> </div>  </div> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_vue-typescript-variant-props-type-safe-props" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="vue-typescript-variant-props-type-safe-props" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
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
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">typescript</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/vue-typescript-variant-props-type-safe-props/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/vue-typescript-variant-props-type-safe-props/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/vue-typescript-variant-props-type-safe-props/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/vue-typescript-variant-props-type-safe-props/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/vue-typescript-variant-props-type-safe-props/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/vue-typescript-variant-props-type-safe-props/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/vue-typescript-variant-props-type-safe-props/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/solving-prop-drilling-in-vue/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Solving Prop Drilling in Vue: Modern State Management Strategies</h3> <p class="related-post-description astro-vj4tpspi"> Eliminate prop drilling in Vue apps using Composition API, Provide/Inject, and Pinia. Learn when to use each approach with practical examples. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-01-25T00:00:00.000Z">Jan 25, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/inline-vue-composables-refactoring/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">The Inline Vue Composables Refactoring pattern</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to apply Martin Fowler&#39;s Extract Function pattern to Vue components using inline composables, making your code cleaner and more maintainable. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-04-01T00:00:00.000Z">Apr 1, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/how-to-write-clean-vue-components/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How to Write Clean Vue Components</h3> <p class="related-post-description astro-vj4tpspi"> There are many ways to write better Vue components. One of my favorite ways is to separate business logic into pure functions. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2024-01-28T15:22:00.000Z">Jan 28, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "vue-typescript-variant-props-type-safe-props";

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
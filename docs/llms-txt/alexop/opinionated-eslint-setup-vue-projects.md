# Source: https://alexop.dev/posts/opinionated-eslint-setup-vue-projects

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/opinionated-eslint-setup-vue-projects/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>My Opinionated ESLint Setup for Vue Projects | alexop.dev</title><meta name="title" content="My Opinionated ESLint Setup for Vue Projects | alexop.dev"><meta name="description" content="A battle-tested linting configuration that catches real bugs, enforces clean architecture, and runs fast using Oxlint and ESLint together."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="My Opinionated ESLint Setup for Vue Projects | alexop.dev"><meta property="og:description" content="A battle-tested linting configuration that catches real bugs, enforces clean architecture, and runs fast using Oxlint and ESLint together."><meta property="og:url" content="https://alexop.dev/posts/opinionated-eslint-setup-vue-projects/"><meta property="og:image" content="https://alexop.dev/posts/my-opinionated-es-lint-setup-for-vue-projects/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2026-01-31T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/opinionated-eslint-setup-vue-projects/"><meta property="twitter:title" content="My Opinionated ESLint Setup for Vue Projects | alexop.dev"><meta property="twitter:description" content="A battle-tested linting configuration that catches real bugs, enforces clean architecture, and runs fast using Oxlint and ESLint together."><meta property="twitter:image" content="https://alexop.dev/posts/my-opinionated-es-lint-setup-for-vue-projects/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"My Opinionated ESLint Setup for Vue Projects | alexop.dev","description":"A battle-tested linting configuration that catches real bugs, enforces clean architecture, and runs fast using Oxlint and ESLint together.","image":"https://alexop.dev/posts/my-opinionated-es-lint-setup-for-vue-projects/index.png","datePublished":"2026-01-31T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: my-opinionated-es-lint-setup-for-vue-projects; }@layer astro { ::view-transition-old(my-opinionated-es-lint-setup-for-vue-projects) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(my-opinionated-es-lint-setup-for-vue-projects) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(my-opinionated-es-lint-setup-for-vue-projects) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(my-opinionated-es-lint-setup-for-vue-projects) { 
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
</style><style>.comparison-code:where(.astro-qdboqi2a) pre{margin:0!important;border-radius:0!important;border:none!important}.comparison-code:where(.astro-qdboqi2a) .astro-code{margin:0!important;border-radius:0!important}.comparison-code:where(.astro-qdboqi2a) figure{margin:0!important}.comparison-code:where(.astro-qdboqi2a) figcaption{display:none}
</style><style>.collapsible:where(.astro-kncz7yy6){display:block!important;width:100%!important;max-width:100%!important;margin:1.5rem 0;border:1px solid rgb(var(--color-border));border-radius:.5rem;overflow:hidden}.collapsible-summary:where(.astro-kncz7yy6){display:flex;align-items:center;gap:.5rem;padding:.75rem 1rem;font-weight:500;cursor:pointer;background:rgb(var(--color-card));-webkit-user-select:none;-moz-user-select:none;user-select:none;list-style:none}.collapsible-summary:where(.astro-kncz7yy6)::-webkit-details-marker{display:none}.collapsible-summary:where(.astro-kncz7yy6):hover{background:rgb(var(--color-card-muted))}.collapsible-icon:where(.astro-kncz7yy6){display:flex;align-items:center;transition:transform .2s ease}.collapsible:where(.astro-kncz7yy6)[open] .collapsible-icon:where(.astro-kncz7yy6){transform:rotate(90deg)}.collapsible-content:where(.astro-kncz7yy6){width:100%!important;max-width:100%!important}.collapsible-content:where(.astro-kncz7yy6) pre{margin:0!important;border-radius:0!important;width:100%!important;max-width:100%!important}.collapsible-content:where(.astro-kncz7yy6)>*:first-child{margin-top:0}.collapsible-content:where(.astro-kncz7yy6)>*:last-child{margin-bottom:0}
</style><style>.prose details.collapsible{display:block!important;width:100%!important;max-width:100%!important}
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: tooling; }@layer astro { ::view-transition-old(tooling) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(tooling) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(tooling) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(tooling) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-5"] { view-transition-name: architecture; }@layer astro { ::view-transition-old(architecture) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(architecture) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(architecture) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(architecture) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-5"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-5"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-5"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-5"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-5"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-5"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-5"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-5"] { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">My Opinionated ESLint Setup for Vue Projects</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2026-01-31T00:00:00.000Z">Jan 31, 2026</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="XlWIU" prefix="r3" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;My Opinionated ESLint Setup for Vue Projects&quot;],&quot;content&quot;:[0,&quot;import Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\nimport InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\nimport Collapsible from \&quot;@features/mdx-components/components/Collapsible.astro\&quot;;\nimport CodeComparison from \&quot;@features/mdx-components/components/CodeComparison.astro\&quot;;\n\nOver the last 7+ years as a Vue developer, I&#39;ve developed a highly opinionated style for writing Vue components. Some of these rules might not be useful for you, but I thought it was worth sharing so you can pick what fits your project. The goal is to enforce code structure that&#39;s readable for both developers and AI agents.\n\nThese rules aren&#39;t arbitrary—they encode patterns I&#39;ve written about extensively:\n\n- &lt;InternalLink slug=\&quot;how-to-write-clean-vue-components\&quot;&gt;How to Write Clean Vue Components&lt;/InternalLink&gt; explains why I separate business logic into pure functions\n- &lt;InternalLink slug=\&quot;how-to-structure-vue-projects\&quot;&gt;How to Structure Vue Projects&lt;/InternalLink&gt; covers my feature-based architecture approach\n- &lt;InternalLink slug=\&quot;nuxt-layers-modular-monolith\&quot;&gt;Building a Modular Monolith with Nuxt Layers&lt;/InternalLink&gt; applies feature isolation to Nuxt projects\n- &lt;InternalLink slug=\&quot;the-problem-with-as-in-typescript-why-its-a-shortcut-we-should-avoid\&quot;&gt;The Problem with `as` in TypeScript&lt;/InternalLink&gt; covers why I ban type assertions\n- &lt;InternalLink slug=\&quot;robust-error-handling-in-typescript-a-journey-from-naive-to-rust-inspired-solutions\&quot;&gt;Robust Error Handling in TypeScript&lt;/InternalLink&gt; introduces the Result pattern behind my `tryCatch` rule\n- &lt;InternalLink slug=\&quot;vue3_testing_pyramid_vitest_browser_mode\&quot;&gt;Vue 3 Testing Pyramid&lt;/InternalLink&gt; explains my integration-first testing strategy\n- &lt;InternalLink slug=\&quot;frontend-testing-guide-10-essential-rules\&quot;&gt;Frontend Testing Guide&lt;/InternalLink&gt; shares my test naming conventions\n\nESLint rules are how I enforce these patterns automatically—so the codebase stays consistent even as the team grows.\n\n&lt;Alert type=\&quot;note\&quot;&gt;\n**Why linting matters more in the AI era:** As AI agents write more of our code, strict linting becomes essential. It&#39;s a form of [back pressure](https://banay.me/dont-waste-your-backpressure/?ref=ghuntley.com)—automated feedback mechanisms that tell an agent when it&#39;s made a mistake, allowing it to self-correct without your intervention. You have a limited budget of feedback (your time and attention). If you spend that budget telling the agent \&quot;you missed an import\&quot; or \&quot;that type is wrong,\&quot; you can&#39;t spend it on architectural decisions or complex logic. Type checkers, linters, and test suites act as back pressure: they push back against bad code so you don&#39;t have to. Your ESLint config is now part of your prompt—it&#39;s the automated quality gate that lets agents iterate until they pass.\n&lt;/Alert&gt;\n\n## Table of Contents\n\n## Why Two Linters? Oxlint + ESLint\n\nI run two linters: **Oxlint** first, then **ESLint**. Why? Speed and coverage.\n\n### Oxlint: The Speed Demon\n\n[Oxlint](https://oxc.rs/docs/guide/usage/linter.html) is written in Rust. It runs 50-100x faster than ESLint on large codebases. My pre-commit hook completes in milliseconds instead of seconds.\n\n```bash\n# In package.json\n\&quot;lint:oxlint\&quot;: \&quot;oxlint . --fix --ignore-path .gitignore\&quot;,\n\&quot;lint:eslint\&quot;: \&quot;eslint . --fix --cache\&quot;,\n\&quot;lint\&quot;: \&quot;run-s lint:*\&quot;  # Runs oxlint first, then eslint\n```\n\n**The tradeoff:** Oxlint supports fewer rules. It handles:\n- **Correctness &amp; suspicious patterns** - catches bugs early\n- **Core ESLint equivalents** - `no-console`, `no-explicit-any`\n- **TypeScript basics** - `array-type`, `consistent-type-definitions`\n\nBut Oxlint lacks:\n- Vue-specific rules (`vue/*`)\n- Import boundary rules (`import-x/*`)\n- Vitest testing rules (`vitest/*`)\n- i18n rules (`@intlify/vue-i18n/*`)\n- Custom local rules\n\n### The Setup\n\nOxlint runs first for fast feedback. ESLint runs second for comprehensive checks. The `eslint-plugin-oxlint` package tells ESLint to skip rules that Oxlint already handles.\n\n```typescript\n// eslint.config.ts\nimport pluginOxlint from &#39;eslint-plugin-oxlint&#39;\n\nexport default defineConfigWithVueTs(\n  // ... other configs\n  ...pluginOxlint.buildFromOxlintConfigFile(&#39;./.oxlintrc.json&#39;),\n)\n```\n\n```json\n// .oxlintrc.json\n{\n  \&quot;$schema\&quot;: \&quot;./node_modules/oxlint/configuration_schema.json\&quot;,\n  \&quot;categories\&quot;: {\n    \&quot;correctness\&quot;: \&quot;error\&quot;,\n    \&quot;suspicious\&quot;: \&quot;warn\&quot;\n  },\n  \&quot;rules\&quot;: {\n    \&quot;typescript/no-explicit-any\&quot;: \&quot;error\&quot;,\n    \&quot;eslint/no-console\&quot;: [\&quot;error\&quot;, { \&quot;allow\&quot;: [\&quot;warn\&quot;, \&quot;error\&quot;] }]\n  }\n}\n```\n\n---\n\n## Must-Have Rules\n\nThese rules catch real bugs and enforce maintainable code. Enable them on every Vue project.\n\n---\n\n### Cyclomatic Complexity\n\nComplex functions are hard to test and understand. This rule limits branching logic per function.\n\n```typescript\n// eslint.config.ts\n{\n  rules: {\n    &#39;complexity&#39;: [&#39;warn&#39;, { max: 10 }]\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\nfunction processOrder(order: Order) {\n  if (order.status === &#39;pending&#39;) {\n    if (order.items.length &gt; 0) {\n      if (order.payment) {\n        if (order.payment.verified) {\n          if (order.shipping) {\n            // 5 levels deep, complexity keeps growing...\n          }\n        }\n      }\n    }\n  }\n}\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\nfunction processOrder(order: Order) {\n  if (!isValidOrder(order)) return\n\n  processPayment(order.payment)\n  scheduleShipping(order.shipping)\n}\n\nfunction isValidOrder(order: Order): boolean {\n  return order.status === &#39;pending&#39;\n    &amp;&amp; order.items.length &gt; 0\n    &amp;&amp; order.payment?.verified === true\n}\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n**Threshold guidance:**\n- ESLint default: `20` (lenient)\n- This project uses: `10` (stricter)\n- Consider `15` as a middle ground for legacy codebases\n\n&gt; [ESLint: complexity](https://eslint.org/docs/latest/rules/complexity)\n\n---\n\n### No Nested Ternaries\n\nNested ternaries are hard to read. Use early returns or separate variables instead.\n\n```typescript\n// eslint.config.ts\n{\n  rules: {\n    &#39;no-nested-ternary&#39;: &#39;error&#39;\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\nconst label = isLoading ? &#39;Loading...&#39; : hasError ? &#39;Failed&#39; : &#39;Success&#39;\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\nfunction getLabel() {\n  if (isLoading) return &#39;Loading...&#39;\n  if (hasError) return &#39;Failed&#39;\n  return &#39;Success&#39;\n}\n\nconst label = getLabel()\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [ESLint: no-nested-ternary](https://eslint.org/docs/rules/no-nested-ternary)\n\n---\n\n### No Type Assertions\n\nType assertions (`as Type`) bypass TypeScript&#39;s type checker. They hide bugs. Use type guards or proper typing instead.\n\n```typescript\n// eslint.config.ts\n{\n  rules: {\n    &#39;@typescript-eslint/consistent-type-assertions&#39;: [&#39;error&#39;, {\n      assertionStyle: &#39;never&#39;\n    }]\n  }\n}\n```\n\n&lt;Alert type=\&quot;note\&quot;&gt;\n`as const` assertions are always allowed, even with `assertionStyle: &#39;never&#39;`. Const assertions don&#39;t bypass type checking—they make types more specific.\n&lt;/Alert&gt;\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\nconst user = response.data as User  // What if it&#39;s not a User?\n\nconst element = document.querySelector(&#39;.btn&#39;) as HTMLButtonElement\nelement.click()  // Runtime error if element is null\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\n// Use type guards\nfunction isUser(data: unknown): data is User {\n  return typeof data === &#39;object&#39;\n    &amp;&amp; data !== null\n    &amp;&amp; &#39;id&#39; in data\n    &amp;&amp; &#39;name&#39; in data\n}\n\nif (isUser(response.data)) {\n  const user = response.data  // TypeScript knows it&#39;s User\n}\n\n// Handle nulls properly\nconst element = document.querySelector(&#39;.btn&#39;)\nif (element instanceof HTMLButtonElement) {\n  element.click()\n}\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [TypeScript ESLint: consistent-type-assertions](https://typescript-eslint.io/rules/consistent-type-assertions)\n\n---\n\n### No Enums\n\nTypeScript enums have quirks. They generate JavaScript code, have numeric reverse mappings, and behave differently from union types. Use literal unions or const objects instead.\n\n```typescript\n// eslint.config.ts\n{\n  rules: {\n    &#39;no-restricted-syntax&#39;: [&#39;error&#39;, {\n      selector: &#39;TSEnumDeclaration&#39;,\n      message: &#39;Use literal unions or `as const` objects instead of enums.&#39;\n    }]\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\nenum Status {\n  Pending,\n  Active,\n  Done\n}\n\nconst status: Status = Status.Pending\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\n// Literal union - simplest\ntype Status = &#39;pending&#39; | &#39;active&#39; | &#39;done&#39;\n\n// Or const object when you need values\nconst Status = {\n  Pending: &#39;pending&#39;,\n  Active: &#39;active&#39;,\n  Done: &#39;done&#39;\n} as const\n\ntype Status = typeof Status[keyof typeof Status]\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [ESLint: no-restricted-syntax](https://eslint.org/docs/rules/no-restricted-syntax)\n\n---\n\n### No else/else-if\n\n`else` and `else-if` blocks increase nesting. Early returns are easier to read and reduce cognitive load.\n\n```typescript\n// eslint.config.ts\n{\n  rules: {\n    &#39;no-restricted-syntax&#39;: [&#39;error&#39;,\n      {\n        selector: &#39;IfStatement &gt; IfStatement.alternate&#39;,\n        message: &#39;Avoid `else if`. Prefer early returns or ternary operators.&#39;\n      },\n      {\n        selector: &#39;IfStatement &gt; :not(IfStatement).alternate&#39;,\n        message: &#39;Avoid `else`. Prefer early returns or ternary operators.&#39;\n      }\n    ]\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\nfunction getDiscount(user: User) {\n  if (user.isPremium) {\n    return 0.2\n  } else if (user.isMember) {\n    return 0.1\n  } else {\n    return 0\n  }\n}\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\nfunction getDiscount(user: User) {\n  if (user.isPremium) return 0.2\n  if (user.isMember) return 0.1\n  return 0\n}\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [ESLint: no-restricted-syntax](https://eslint.org/docs/rules/no-restricted-syntax)\n\n---\n\n### No Native try/catch\n\nNative try/catch blocks are verbose and error-prone. Use a utility function that returns a result tuple instead.\n\n```typescript\n// eslint.config.ts\n{\n  rules: {\n    &#39;no-restricted-syntax&#39;: [&#39;error&#39;, {\n      selector: &#39;TryStatement&#39;,\n      message: &#39;Use tryCatch() from @/lib/tryCatch instead of try/catch. Returns Result&lt;T&gt; tuple: [error, null] | [null, data].&#39;\n    }]\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\nasync function fetchUser(id: string) {\n  try {\n    const response = await api.get(`/users/${id}`)\n    return response.data\n  } catch (error) {\n    console.error(error)\n    return null\n  }\n}\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\nasync function fetchUser(id: string) {\n  const [error, response] = await tryCatch(api.get(`/users/${id}`))\n\n  if (error) {\n    console.error(error)\n    return null\n  }\n\n  return response.data\n}\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\nThe `tryCatch` utility returns `[error, null]` or `[null, data]`, similar to Go&#39;s error handling.\n\n&gt; [ESLint: no-restricted-syntax](https://eslint.org/docs/rules/no-restricted-syntax)\n\n---\n\n### No Direct DOM Manipulation\n\nVue manages the DOM. Calling `document.querySelector` bypasses Vue&#39;s reactivity and template refs. Use `useTemplateRef()` instead. If you&#39;re on Vue 3.5+, the built-in rule already enforces this.\n\n```typescript\n// eslint.config.ts\n{\n  files: [&#39;src/**/*.vue&#39;],\n  rules: {\n    &#39;vue/prefer-use-template-ref&#39;: &#39;error&#39;\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nfunction focusInput() {\n  const input = document.getElementById(&#39;my-input&#39;)\n  input?.focus()\n}\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;input id=\&quot;my-input\&quot; /&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { useTemplateRef } from &#39;vue&#39;\n\nconst inputRef = useTemplateRef&lt;HTMLInputElement&gt;(&#39;input&#39;)\n\nfunction focusInput() {\n  inputRef.value?.focus()\n}\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;input ref=\&quot;input\&quot; /&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [ESLint: no-restricted-syntax](https://eslint.org/docs/rules/no-restricted-syntax)\n\n---\n\n### Feature Boundary Enforcement\n\nFeatures should not import from other features. This keeps code modular and prevents circular dependencies. If you&#39;re using a feature-based architecture, this rule is essential—see &lt;InternalLink slug=\&quot;how-to-structure-vue-projects\&quot;&gt;How to Structure Vue Projects&lt;/InternalLink&gt; for more on this approach.\n\n```typescript\n// eslint.config.ts\n{\n  plugins: { &#39;import-x&#39;: pluginImportX },\n  rules: {\n    &#39;import-x/no-restricted-paths&#39;: [&#39;error&#39;, {\n      zones: [\n        // === CROSS-FEATURE ISOLATION ===\n        // Features cannot import from other features\n        { target: &#39;./src/features/workout&#39;, from: &#39;./src/features&#39;, except: [&#39;./workout&#39;] },\n        { target: &#39;./src/features/exercises&#39;, from: &#39;./src/features&#39;, except: [&#39;./exercises&#39;] },\n        { target: &#39;./src/features/settings&#39;, from: &#39;./src/features&#39;, except: [&#39;./settings&#39;] },\n        { target: &#39;./src/features/timers&#39;, from: &#39;./src/features&#39;, except: [&#39;./timers&#39;] },\n        { target: &#39;./src/features/templates&#39;, from: &#39;./src/features&#39;, except: [&#39;./templates&#39;] },\n        { target: &#39;./src/features/benchmarks&#39;, from: &#39;./src/features&#39;, except: [&#39;./benchmarks&#39;] },\n\n        // === UNIDIRECTIONAL FLOW ===\n        // Shared code cannot import from features or views\n        {\n          target: [&#39;./src/components&#39;, &#39;./src/composables&#39;, &#39;./src/lib&#39;, &#39;./src/db&#39;, &#39;./src/types&#39;, &#39;./src/stores&#39;],\n          from: [&#39;./src/features&#39;, &#39;./src/views&#39;]\n        },\n\n        // Features cannot import from views (views are top-level orchestrators)\n        { target: &#39;./src/features&#39;, from: &#39;./src/views&#39; }\n      ]\n    }]\n  }\n}\n```\n\n**Unidirectional Flow:** The architecture enforces a strict dependency hierarchy. Views orchestrate features, features use shared code, but never the reverse.\n\n```\nviews → features → shared (components, composables, lib, db, types, stores)\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\n// src/features/workout/composables/useWorkout.ts\nimport { useExerciseData } from &#39;@/features/exercises/composables/useExerciseData&#39;\n// Cross-feature import!\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\n// src/features/workout/composables/useWorkout.ts\nimport { ExerciseRepository } from &#39;@/db/repositories/ExerciseRepository&#39;\n// Use shared database layer instead\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [eslint-plugin-import-x: no-restricted-paths](https://github.com/un-ts/eslint-plugin-import-x)\n\n---\n\n### Vue Component Naming\n\nConsistent naming makes components easy to find and identify.\n\n```typescript\n// eslint.config.ts\n{\n  files: [&#39;src/**/*.vue&#39;],\n  rules: {\n    &#39;vue/multi-word-component-names&#39;: [&#39;error&#39;, {\n      ignores: [&#39;App&#39;, &#39;Layout&#39;]\n    }],\n    &#39;vue/component-definition-name-casing&#39;: [&#39;error&#39;, &#39;PascalCase&#39;],\n    &#39;vue/component-name-in-template-casing&#39;: [&#39;error&#39;, &#39;PascalCase&#39;, {\n      registeredComponentsOnly: false\n    }],\n    &#39;vue/match-component-file-name&#39;: [&#39;error&#39;, {\n      extensions: [&#39;vue&#39;],\n      shouldMatchCase: true\n    }],\n    &#39;vue/prop-name-casing&#39;: [&#39;error&#39;, &#39;camelCase&#39;],\n    &#39;vue/attribute-hyphenation&#39;: [&#39;error&#39;, &#39;always&#39;],\n    &#39;vue/custom-event-name-casing&#39;: [&#39;error&#39;, &#39;kebab-case&#39;]\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```vue\n&lt;!-- File: button.vue --&gt;\n&lt;template&gt;\n  &lt;base-button&gt;Click&lt;/base-button&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```vue\n&lt;!-- File: SubmitButton.vue --&gt;\n&lt;template&gt;\n  &lt;BaseButton&gt;Click&lt;/BaseButton&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [eslint-plugin-vue: component rules](https://eslint.vuejs.org/rules/)\n\n---\n\n### Dead Code Detection in Vue\n\nFind unused props, refs, and emits before they become tech debt.\n\n```typescript\n// eslint.config.ts\n{\n  files: [&#39;src/**/*.vue&#39;],\n  rules: {\n    &#39;vue/no-unused-properties&#39;: [&#39;error&#39;, {\n      groups: [&#39;props&#39;, &#39;data&#39;, &#39;computed&#39;, &#39;methods&#39;]\n    }],\n    &#39;vue/no-unused-refs&#39;: &#39;error&#39;,\n    &#39;vue/no-unused-emit-declarations&#39;: &#39;error&#39;\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { ref } from &#39;vue&#39;\n\nconst props = defineProps&lt;{\n  title: string\n  subtitle: string  // Never used!\n}&gt;()\n\nconst emit = defineEmits&lt;{\n  (e: &#39;click&#39;): void\n  (e: &#39;hover&#39;): void  // Never emitted!\n}&gt;()\n\nconst buttonRef = ref&lt;HTMLButtonElement&gt;()  // Never used!\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;h1&gt;{{ title }}&lt;/h1&gt;\n  &lt;button @click=\&quot;emit(&#39;click&#39;)\&quot;&gt;Click&lt;/button&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nconst props = defineProps&lt;{\n  title: string\n}&gt;()\n\nconst emit = defineEmits&lt;{\n  (e: &#39;click&#39;): void\n}&gt;()\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;h1&gt;{{ title }}&lt;/h1&gt;\n  &lt;button @click=\&quot;emit(&#39;click&#39;)\&quot;&gt;Click&lt;/button&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [eslint-plugin-vue: no-unused-properties](https://eslint.vuejs.org/rules/no-unused-properties.html)\n\n---\n\n### No Hardcoded i18n Strings\n\nHardcoded strings break internationalization. The `@intlify/vue-i18n` plugin catches them.\n\n```typescript\n// eslint.config.ts\n{\n  files: [&#39;src/**/*.vue&#39;],\n  plugins: { &#39;@intlify/vue-i18n&#39;: pluginVueI18n },\n  rules: {\n    &#39;@intlify/vue-i18n/no-raw-text&#39;: [&#39;error&#39;, {\n      ignorePattern: &#39;^[-#:()&amp;+×/°′″%]+&#39;,\n      ignoreText: [&#39;kg&#39;, &#39;lbs&#39;, &#39;cm&#39;, &#39;ft/in&#39;, &#39;—&#39;, &#39;•&#39;, &#39;✓&#39;, &#39;›&#39;, &#39;→&#39;, &#39;·&#39;, &#39;.&#39;, &#39;Close&#39;],\n      attributes: {\n        &#39;/.+/&#39;: [&#39;title&#39;, &#39;aria-label&#39;, &#39;aria-placeholder&#39;, &#39;placeholder&#39;, &#39;alt&#39;]\n      }\n    }]\n  }\n}\n```\n\nThe `attributes` option catches hardcoded strings in accessibility attributes too.\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```vue\n&lt;template&gt;\n  &lt;button&gt;Save Changes&lt;/button&gt;\n  &lt;p&gt;No items found&lt;/p&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```vue\n&lt;template&gt;\n  &lt;button&gt;{{ t(&#39;common.save&#39;) }}&lt;/button&gt;\n  &lt;p&gt;{{ t(&#39;items.empty&#39;) }}&lt;/p&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [eslint-plugin-vue-i18n](https://eslint-plugin-vue-i18n.intlify.dev/)\n\n---\n\n### No Disabling i18n Rules\n\nPrevent developers from bypassing i18n checks with `eslint-disable` comments.\n\n```typescript\n// eslint.config.ts\n{\n  files: [&#39;src/**/*.vue&#39;],\n  plugins: {\n    &#39;@eslint-community/eslint-comments&#39;: pluginEslintComments\n  },\n  rules: {\n    &#39;@eslint-community/eslint-comments/no-restricted-disable&#39;: [\n      &#39;error&#39;,\n      &#39;@intlify/vue-i18n/*&#39;\n    ]\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```vue\n&lt;!-- eslint-disable-next-line @intlify/vue-i18n/no-raw-text --&gt;\n&lt;button&gt;Save Changes&lt;/button&gt;\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```vue\n&lt;button&gt;{{ t(&#39;common.save&#39;) }}&lt;/button&gt;\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [@eslint-community/eslint-plugin-eslint-comments](https://github.com/eslint-community/eslint-plugin-eslint-comments)\n\n---\n\n### No Hardcoded Route Strings\n\nUse named routes instead of hardcoded path strings for maintainability.\n\n```typescript\n// eslint.config.ts\n{\n  rules: {\n    &#39;no-restricted-syntax&#39;: [&#39;error&#39;,\n      {\n        selector: &#39;CallExpression[callee.property.name=\&quot;push\&quot;][callee.object.name=\&quot;router\&quot;] &gt; Literal:first-child&#39;,\n        message: &#39;Use named routes with RouteNames instead of hardcoded path strings.&#39;\n      },\n      {\n        selector: &#39;CallExpression[callee.property.name=\&quot;push\&quot;][callee.object.name=\&quot;router\&quot;] &gt; TemplateLiteral:first-child&#39;,\n        message: &#39;Use named routes with RouteNames instead of template literals.&#39;\n      }\n    ]\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\nrouter.push(&#39;/workout/123&#39;)\nrouter.push(`/workout/${id}`)\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\nrouter.push({ name: RouteNames.WorkoutDetail, params: { id } })\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [ESLint: no-restricted-syntax](https://eslint.org/docs/latest/rules/no-restricted-syntax)\n\n---\n\n### Enforce Integration Test Helpers\n\nBan direct `render()` or `mount()` calls in tests. Use a centralized test helper instead. For more on testing strategies in Vue, see &lt;InternalLink slug=\&quot;vue3_testing_pyramid_vitest_browser_mode\&quot;&gt;Vue 3 Testing Pyramid: A Practical Guide with Vitest Browser Mode&lt;/InternalLink&gt;.\n\n```typescript\n// eslint.config.ts\n{\n  files: [&#39;src/**/__tests__/**/*.{ts,spec.ts}&#39;],\n  ignores: [&#39;src/__tests__/helpers/**&#39;],\n  rules: {\n    &#39;no-restricted-imports&#39;: [&#39;error&#39;, {\n      paths: [\n        {\n          name: &#39;vitest-browser-vue&#39;,\n          importNames: [&#39;render&#39;],\n          message: &#39;Use createTestApp() from @/__tests__/helpers/createTestApp instead.&#39;\n        },\n        {\n          name: &#39;@vue/test-utils&#39;,\n          importNames: [&#39;mount&#39;, &#39;shallowMount&#39;],\n          message: &#39;Use createTestApp() instead of mounting components directly.&#39;\n        }\n      ]\n    }]\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\nimport { render } from &#39;vitest-browser-vue&#39;\nimport { mount } from &#39;@vue/test-utils&#39;\n\nconst { getByText } = render(MyComponent)\nconst wrapper = mount(MyComponent)\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\nimport { createTestApp } from &#39;@/__tests__/helpers/createTestApp&#39;\n\nconst { page } = await createTestApp({ route: &#39;/workout&#39; })\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\nThis ensures all tests use consistent setup with routing, i18n, and database.\n\n&gt; [ESLint: no-restricted-imports](https://eslint.org/docs/latest/rules/no-restricted-imports)\n\n---\n\n### Enforce pnpm Catalogs\n\nWhen using pnpm workspaces, enforce that dependencies use catalog references.\n\n```typescript\n// eslint.config.ts\nimport { configs as pnpmConfigs } from &#39;eslint-plugin-pnpm&#39;\n\nexport default defineConfigWithVueTs(\n  // ... other configs\n  ...pnpmConfigs.recommended,\n)\n```\n\nThis ensures dependencies are managed centrally in `pnpm-workspace.yaml`.\n\n&gt; [eslint-plugin-pnpm](https://github.com/nickmccurdy/eslint-plugin-pnpm)\n\n---\n\n## Nice-to-Have Rules\n\nThese rules improve code quality but are less critical. Enable them after the must-haves are in place.\n\n---\n\n### Vue 3.5+ API Enforcement\n\nUse the latest Vue 3.5 APIs for cleaner code.\n\n```typescript\n// eslint.config.ts\n{\n  files: [&#39;src/**/*.vue&#39;],\n  rules: {\n    &#39;vue/define-props-destructuring&#39;: &#39;error&#39;,\n    &#39;vue/prefer-use-template-ref&#39;: &#39;error&#39;\n  }\n}\n```\n\n&lt;CodeComparison badTitle=\&quot;Before Vue 3.5\&quot; goodTitle=\&quot;Vue 3.5+\&quot;&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { ref } from &#39;vue&#39;\n\nconst props = defineProps&lt;{ count: number }&gt;()\nconst buttonRef = ref&lt;HTMLButtonElement&gt;()\n\nconsole.log(props.count)  // Using props. prefix\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;button ref=\&quot;buttonRef\&quot;&gt;Click&lt;/button&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { useTemplateRef } from &#39;vue&#39;\n\nconst { count } = defineProps&lt;{ count: number }&gt;()\nconst buttonRef = useTemplateRef&lt;HTMLButtonElement&gt;(&#39;button&#39;)\n\nconsole.log(count)  // Direct destructured access\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;button ref=\&quot;button\&quot;&gt;Click&lt;/button&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [eslint-plugin-vue: define-props-destructuring](https://eslint.vuejs.org/rules/define-props-destructuring.html)\n\n---\n\n### Explicit Component APIs\n\nRequire `defineExpose` and `defineSlots` to make component interfaces explicit.\n\n```typescript\n// eslint.config.ts\n{\n  files: [&#39;src/**/*.vue&#39;],\n  rules: {\n    &#39;vue/require-expose&#39;: &#39;warn&#39;,\n    &#39;vue/require-explicit-slots&#39;: &#39;warn&#39;\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nfunction focus() { /* ... */ }\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;slot /&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```vue\n&lt;script setup lang=\&quot;ts\&quot;&gt;\ndefineSlots&lt;{\n  default(): unknown\n}&gt;()\n\nfunction focus() { /* ... */ }\n\ndefineExpose({ focus })\n&lt;/script&gt;\n\n&lt;template&gt;\n  &lt;slot /&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [eslint-plugin-vue: require-expose](https://eslint.vuejs.org/rules/require-expose.html)\n\n---\n\n### Template Depth Limit\n\nDeep template nesting is hard to read. Extract nested sections into components. This one matters a lot—it helps you avoid ending up with components that are 2000 lines long.\n\n```typescript\n// eslint.config.ts\n{\n  files: [&#39;src/**/*.vue&#39;],\n  rules: {\n    &#39;vue/max-template-depth&#39;: [&#39;error&#39;, { maxDepth: 8 }],\n    &#39;vue/max-props&#39;: [&#39;error&#39;, { maxProps: 6 }]\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```vue\n&lt;template&gt;\n  &lt;div&gt;\n    &lt;div&gt;\n      &lt;div&gt;\n        &lt;div&gt;\n          &lt;div&gt;\n            &lt;div&gt;\n              &lt;div&gt;\n                &lt;div&gt;\n                  &lt;span&gt;Too deep!&lt;/span&gt;\n                &lt;/div&gt;\n              &lt;/div&gt;\n            &lt;/div&gt;\n          &lt;/div&gt;\n        &lt;/div&gt;\n      &lt;/div&gt;\n    &lt;/div&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```vue\n&lt;template&gt;\n  &lt;Card&gt;\n    &lt;CardHeader&gt;\n      &lt;CardTitle&gt;Title&lt;/CardTitle&gt;\n    &lt;/CardHeader&gt;\n    &lt;CardContent&gt;\n      &lt;span&gt;Content&lt;/span&gt;\n    &lt;/CardContent&gt;\n  &lt;/Card&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [eslint-plugin-vue: max-template-depth](https://eslint.vuejs.org/rules/max-template-depth.html)\n\n---\n\n### Better Assertions in Tests\n\nUse specific matchers for clearer test failures.\n\n```typescript\n// eslint.config.ts\n{\n  files: [&#39;src/**/__tests__/*&#39;],\n  rules: {\n    &#39;vitest/prefer-to-be&#39;: &#39;error&#39;,\n    &#39;vitest/prefer-to-have-length&#39;: &#39;error&#39;,\n    &#39;vitest/prefer-to-contain&#39;: &#39;error&#39;,\n    &#39;vitest/prefer-mock-promise-shorthand&#39;: &#39;error&#39;\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\nexpect(value === null).toBe(true)\nexpect(arr.length).toBe(3)\nexpect(arr.includes(&#39;foo&#39;)).toBe(true)\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\nexpect(value).toBeNull()\nexpect(arr).toHaveLength(3)\nexpect(arr).toContain(&#39;foo&#39;)\n\n// Also prefer mock shorthands\nvi.fn().mockResolvedValue(&#39;data&#39;)  // Instead of mockReturnValue(Promise.resolve(&#39;data&#39;))\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [eslint-plugin-vitest](https://github.com/veritem/eslint-plugin-vitest)\n\n---\n\n### Test Structure Rules\n\nKeep tests organized and readable.\n\n```typescript\n// eslint.config.ts\n{\n  files: [&#39;src/**/__tests__/*&#39;],\n  rules: {\n    &#39;vitest/consistent-test-it&#39;: [&#39;error&#39;, { fn: &#39;it&#39; }],\n    &#39;vitest/prefer-hooks-on-top&#39;: &#39;error&#39;,\n    &#39;vitest/prefer-hooks-in-order&#39;: &#39;error&#39;,\n    &#39;vitest/no-duplicate-hooks&#39;: &#39;error&#39;,\n    &#39;vitest/require-top-level-describe&#39;: &#39;error&#39;,\n    &#39;vitest/max-nested-describe&#39;: [&#39;error&#39;, { max: 2 }],\n    &#39;vitest/no-conditional-in-test&#39;: &#39;warn&#39;\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\ntest(&#39;works&#39;, () =&gt; {})  // Inconsistent: test vs it\nit(&#39;also works&#39;, () =&gt; {})\n\ndescribe(&#39;feature&#39;, () =&gt; {\n  it(&#39;test 1&#39;, () =&gt; {})\n\n  beforeEach(() =&gt; {})  // Hook after test!\n\n  describe(&#39;nested&#39;, () =&gt; {\n    describe(&#39;too deep&#39;, () =&gt; {\n      describe(&#39;way too deep&#39;, () =&gt; {})  // 3 levels!\n    })\n  })\n})\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\ndescribe(&#39;feature&#39;, () =&gt; {\n  beforeEach(() =&gt; {})  // Hooks first, in order\n\n  it(&#39;does something&#39;, () =&gt; {})\n  it(&#39;does another thing&#39;, () =&gt; {})\n\n  describe(&#39;edge cases&#39;, () =&gt; {\n    it(&#39;handles null&#39;, () =&gt; {})\n  })\n})\n\n// no-conditional-in-test prevents flaky tests\n// Bad: if (data.length &gt; 0) { expect(data[0]).toBeDefined() }\n// Good: expect(data).toHaveLength(3); expect(data[0]).toBeDefined()\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [eslint-plugin-vitest](https://github.com/veritem/eslint-plugin-vitest)\n\n---\n\n### Prefer Vitest Locators in Tests\n\nUse Vitest Browser locators instead of raw DOM queries.\n\n```typescript\n// eslint.config.ts\n{\n  files: [&#39;src/**/__tests__/**/*.{ts,spec.ts}&#39;],\n  rules: {\n    &#39;no-restricted-syntax&#39;: [&#39;warn&#39;, {\n      selector: &#39;CallExpression[callee.property.name=/^querySelector(All)?$/]&#39;,\n      message: &#39;Prefer page.getByRole(), page.getByText(), or page.getByTestId() over querySelector. Vitest locators are more resilient to DOM changes.&#39;\n    }]\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\nconst button = container.querySelector(&#39;.submit-btn&#39;)\nawait button?.click()\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\nconst button = page.getByRole(&#39;button&#39;, { name: &#39;Submit&#39; })\nawait button.click()\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&gt; [Vitest Browser Mode](https://vitest.dev/guide/browser/)\n\n---\n\n### Unicorn Rules\n\nThe `eslint-plugin-unicorn` package catches common mistakes and enforces modern JavaScript patterns.\n\n```typescript\n// eslint.config.ts\npluginUnicorn.configs.recommended,\n\n{\n  name: &#39;app/unicorn-overrides&#39;,\n  rules: {\n    // === Enable non-recommended rules that add value ===\n    &#39;unicorn/better-regex&#39;: &#39;warn&#39;,              // Simplify regexes: /[0-9]/ → /\\d/\n    &#39;unicorn/custom-error-definition&#39;: &#39;error&#39;,  // Correct Error subclassing\n    &#39;unicorn/no-unused-properties&#39;: &#39;warn&#39;,      // Dead code detection\n    &#39;unicorn/consistent-destructuring&#39;: &#39;warn&#39;,  // Use destructured vars consistently\n\n    // === Disable rules that conflict with project conventions ===\n    &#39;unicorn/no-null&#39;: &#39;off&#39;,                    // We use null for database values\n    &#39;unicorn/filename-case&#39;: &#39;off&#39;,              // Vue uses PascalCase, tests use camelCase\n    &#39;unicorn/prevent-abbreviations&#39;: &#39;off&#39;,      // props, e, Db are fine\n    &#39;unicorn/no-array-callback-reference&#39;: &#39;off&#39;, // arr.filter(isValid) is fine\n    &#39;unicorn/no-await-expression-member&#39;: &#39;off&#39;, // (await fetch()).json() is fine\n    &#39;unicorn/no-array-reduce&#39;: &#39;off&#39;,            // reduce is useful for aggregations\n    &#39;unicorn/no-useless-undefined&#39;: &#39;off&#39;        // mockResolvedValue(undefined) for TS\n  }\n}\n```\n\n**Examples:**\n\n```typescript\n// unicorn/better-regex\n// Bad:  /[0-9]/\n// Good: /\\d/\n\n// unicorn/consistent-destructuring\n// Bad:\nconst { foo } = object\nconsole.log(object.bar)  // Uses object.bar instead of destructuring\n\n// Good:\nconst { foo, bar } = object\nconsole.log(bar)\n```\n\n&gt; [eslint-plugin-unicorn](https://github.com/sindresorhus/eslint-plugin-unicorn)\n\n---\n\n## Custom Local Rules\n\nSometimes you need rules that don&#39;t exist. Write them yourself.\n\n### Composable Must Use Vue\n\nA file named `use*.ts` should import from Vue. If it doesn&#39;t, it&#39;s a utility, not a composable. For more on writing proper composables, see &lt;InternalLink slug=\&quot;vueuse_composables_style_guide\&quot;&gt;Vue Composables Style Guide: Lessons from VueUse&#39;s Codebase&lt;/InternalLink&gt;.\n\n```typescript\n// eslint-local-rules/composable-must-use-vue.ts\nconst VALID_VUE_SOURCES = new Set([&#39;vue&#39;, &#39;@vueuse/core&#39;, &#39;vue-router&#39;, &#39;vue-i18n&#39;])\nconst VALID_PATH_PATTERNS = [/^@\\/stores\\//]  // Global state composables count too\n\nfunction isComposableFilename(filename: string): boolean {\n  return /^use[A-Z]/.test(path.basename(filename, &#39;.ts&#39;))\n}\n\nconst rule: Rule.RuleModule = {\n  meta: {\n    messages: {\n      notAComposable: &#39;File \&quot;{{filename}}\&quot; does not import from Vue. Rename it or add Vue imports.&#39;\n    }\n  },\n  create(context) {\n    if (!isComposableFilename(context.filename)) return {}\n\n    let hasVueImport = false\n\n    return {\n      ImportDeclaration(node) {\n        if (VALID_VUE_SOURCES.has(node.source.value)) {\n          hasVueImport = true\n        }\n      },\n      &#39;Program:exit&#39;(node) {\n        if (!hasVueImport) {\n          context.report({ node, messageId: &#39;notAComposable&#39; })\n        }\n      }\n    }\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\n// src/composables/useFormatter.ts\nexport function useFormatter() {\n  return {\n    formatDate: (d: Date) =&gt; d.toISOString()  // No Vue imports!\n  }\n}\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\n// src/lib/formatter.ts (renamed)\nexport function formatDate(d: Date) {\n  return d.toISOString()\n}\n\n// OR add Vue reactivity:\n// src/composables/useFormatter.ts\nimport { computed, ref } from &#39;vue&#39;\n\nexport function useFormatter() {\n  const locale = ref(&#39;en-US&#39;)\n  const formatter = computed(() =&gt; new Intl.DateTimeFormat(locale.value))\n  return { formatter, locale }\n}\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n---\n\n### No Hardcoded Tailwind Colors\n\nHardcoded Tailwind colors (`bg-blue-500`) make theming impossible. Use semantic colors (`bg-primary`).\n\n```typescript\n// eslint-local-rules/no-hardcoded-colors.ts\n// Status colors (red, amber, yellow, green, emerald) are ALLOWED for semantic states\nconst HARDCODED_COLORS = [&#39;slate&#39;, &#39;gray&#39;, &#39;zinc&#39;, &#39;blue&#39;, &#39;purple&#39;, &#39;pink&#39;, &#39;orange&#39;, &#39;indigo&#39;, &#39;violet&#39;]\nconst COLOR_UTILITIES = [&#39;bg&#39;, &#39;text&#39;, &#39;border&#39;, &#39;ring&#39;, &#39;fill&#39;, &#39;stroke&#39;]\n\nconst rule: Rule.RuleModule = {\n  meta: {\n    messages: {\n      noHardcodedColor: &#39;Avoid \&quot;{{color}}\&quot;. Use semantic classes like bg-primary, text-foreground.&#39;\n    }\n  },\n  create(context) {\n    return {\n      Literal(node) {\n        if (typeof node.value !== &#39;string&#39;) return\n\n        const matches = findHardcodedColors(node.value)\n        for (const color of matches) {\n          context.report({ node, messageId: &#39;noHardcodedColor&#39;, data: { color } })\n        }\n      }\n    }\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```vue\n&lt;template&gt;\n  &lt;button class=\&quot;bg-blue-500 text-white\&quot;&gt;Click&lt;/button&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```vue\n&lt;template&gt;\n  &lt;button class=\&quot;bg-primary text-primary-foreground\&quot;&gt;Click&lt;/button&gt;\n&lt;/template&gt;\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&lt;Alert type=\&quot;note\&quot;&gt;\nStatus colors (`red`, `amber`, `yellow`, `green`, `emerald`) are intentionally allowed for error/warning/success states. Only use these for semantic status indication, not general styling.\n&lt;/Alert&gt;\n\n---\n\n### No let in describe Blocks\n\nMutable variables in test describe blocks create hidden state. Use setup functions instead.\n\n```typescript\n// eslint-local-rules/no-let-in-describe.ts\nconst rule: Rule.RuleModule = {\n  meta: {\n    messages: {\n      noLetInDescribe: &#39;Avoid `let` in describe blocks. Use setup functions instead.&#39;\n    }\n  },\n  create(context) {\n    let describeDepth = 0\n\n    return {\n      CallExpression(node) {\n        if (isDescribeCall(node)) describeDepth++\n      },\n      &#39;CallExpression:exit&#39;(node) {\n        if (isDescribeCall(node)) describeDepth--\n      },\n      VariableDeclaration(node) {\n        if (describeDepth &gt; 0 &amp;&amp; node.kind === &#39;let&#39;) {\n          context.report({ node, messageId: &#39;noLetInDescribe&#39; })\n        }\n      }\n    }\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\ndescribe(&#39;Login&#39;, () =&gt; {\n  let user: User\n\n  beforeEach(() =&gt; {\n    user = createUser()  // Hidden mutation!\n  })\n\n  it(&#39;works&#39;, () =&gt; {\n    expect(user.name).toBe(&#39;test&#39;)\n  })\n})\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\ndescribe(&#39;Login&#39;, () =&gt; {\n  function setup() {\n    return { user: createUser() }\n  }\n\n  it(&#39;works&#39;, () =&gt; {\n    const { user } = setup()\n    expect(user.name).toBe(&#39;test&#39;)\n  })\n})\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n---\n\n### Extract Complex Conditions\n\nComplex boolean expressions should have names. Extract them into variables.\n\n```typescript\n// eslint-local-rules/extract-condition-variable.ts\nconst OPERATOR_THRESHOLD = 2  // Conditions with 2+ logical operators need extraction\n\nconst rule: Rule.RuleModule = {\n  meta: {\n    messages: {\n      extractCondition: &#39;Complex condition should be extracted into a named const.&#39;\n    }\n  },\n  create(context) {\n    return {\n      IfStatement(node) {\n        // Skip patterns that TypeScript needs inline for narrowing\n        if (isEarlyExitGuard(node.consequent)) return  // if (!x) return\n        if (hasOptionalChaining(node.test)) return      // if (user?.name)\n        if (hasTruthyNarrowingPattern(node.test)) return // if (arr &amp;&amp; arr[0])\n\n        if (countOperators(node.test) &gt;= OPERATOR_THRESHOLD) {\n          context.report({ node: node.test, messageId: &#39;extractCondition&#39; })\n        }\n      }\n    }\n  }\n}\n```\n\n**Smart Exceptions:** The rule skips several patterns that TypeScript needs inline for type narrowing:\n- Early exit guards: `if (!user) return`\n- Optional chaining: `if (user?.name)`\n- Truthy narrowing: `if (arr &amp;&amp; arr[0])`\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\nif (user.isActive &amp;&amp; user.role === &#39;admin&#39; &amp;&amp; !user.isBanned) {\n  showAdminPanel()\n}\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\nconst canAccessAdminPanel = user.isActive &amp;&amp; user.role === &#39;admin&#39; &amp;&amp; !user.isBanned\n\nif (canAccessAdminPanel) {\n  showAdminPanel()\n}\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n---\n\n### Repository tryCatch Wrapper\n\nDatabase calls can fail. Enforce wrapping them in `tryCatch()`.\n\n```typescript\n// eslint-local-rules/repository-trycatch.ts\n// Matches pattern: get*Repository().method()\nconst REPO_PATTERN = /^get\\w+Repository$/\n\nconst rule: Rule.RuleModule = {\n  meta: {\n    messages: {\n      missingTryCatch: &#39;Repository calls must be wrapped with tryCatch().&#39;\n    }\n  },\n  create(context) {\n    return {\n      AwaitExpression(node) {\n        if (!isRepositoryMethodCall(node.argument)) return\n        if (isWrappedInTryCatch(context, node)) return\n\n        context.report({ node, messageId: &#39;missingTryCatch&#39; })\n      }\n    }\n  }\n}\n```\n\n&lt;CodeComparison&gt;\n  &lt;Fragment slot=\&quot;bad\&quot;&gt;\n```typescript\nconst workouts = await getWorkoutRepository().findAll()  // Might throw!\n```\n  &lt;/Fragment&gt;\n  &lt;Fragment slot=\&quot;good\&quot;&gt;\n```typescript\nconst [error, workouts] = await tryCatch(getWorkoutRepository().findAll())\n\nif (error) {\n  showError(&#39;Failed to load workouts&#39;)\n  return\n}\n```\n  &lt;/Fragment&gt;\n&lt;/CodeComparison&gt;\n\n&lt;Alert type=\&quot;note\&quot;&gt;\nThis rule matches the `get*Repository()` pattern. Ensure your repository factory functions follow this naming convention.\n&lt;/Alert&gt;\n\n---\n\n## The Full Config\n\n&lt;Collapsible title=\&quot;Complete eslint.config.ts example\&quot;&gt;\n\n```typescript\nimport pluginEslintComments from &#39;@eslint-community/eslint-plugin-eslint-comments&#39;\nimport pluginVueI18n from &#39;@intlify/eslint-plugin-vue-i18n&#39;\nimport pluginVitest from &#39;@vitest/eslint-plugin&#39;\nimport skipFormatting from &#39;@vue/eslint-config-prettier/skip-formatting&#39;\nimport { defineConfigWithVueTs, vueTsConfigs } from &#39;@vue/eslint-config-typescript&#39;\nimport pluginImportX from &#39;eslint-plugin-import-x&#39;\nimport pluginOxlint from &#39;eslint-plugin-oxlint&#39;\nimport { configs as pnpmConfigs } from &#39;eslint-plugin-pnpm&#39;\nimport pluginUnicorn from &#39;eslint-plugin-unicorn&#39;\nimport pluginVue from &#39;eslint-plugin-vue&#39;\nimport localRules from &#39;./eslint-local-rules&#39;\n\nexport default defineConfigWithVueTs(\n  { ignores: [&#39;**/dist/**&#39;, &#39;**/coverage/**&#39;, &#39;**/node_modules/**&#39;] },\n\n  pluginVue.configs[&#39;flat/essential&#39;],\n  vueTsConfigs.recommended,\n  pluginUnicorn.configs.recommended,\n\n  // Vue component rules\n  {\n    files: [&#39;src/**/*.vue&#39;],\n    rules: {\n      &#39;vue/multi-word-component-names&#39;: [&#39;error&#39;, { ignores: [&#39;App&#39;, &#39;Layout&#39;] }],\n      &#39;vue/component-name-in-template-casing&#39;: [&#39;error&#39;, &#39;PascalCase&#39;],\n      &#39;vue/prop-name-casing&#39;: [&#39;error&#39;, &#39;camelCase&#39;],\n      &#39;vue/custom-event-name-casing&#39;: [&#39;error&#39;, &#39;kebab-case&#39;],\n      &#39;vue/no-unused-properties&#39;: [&#39;error&#39;, { groups: [&#39;props&#39;, &#39;data&#39;, &#39;computed&#39;, &#39;methods&#39;] }],\n      &#39;vue/no-unused-refs&#39;: &#39;error&#39;,\n      &#39;vue/define-props-destructuring&#39;: &#39;error&#39;,\n      &#39;vue/prefer-use-template-ref&#39;: &#39;error&#39;,\n      &#39;vue/max-template-depth&#39;: [&#39;error&#39;, { maxDepth: 8 }],\n    },\n  },\n\n  // TypeScript style guide\n  {\n    files: [&#39;src/**/*.{ts,vue}&#39;],\n    rules: {\n      &#39;complexity&#39;: [&#39;warn&#39;, { max: 10 }],\n      &#39;no-nested-ternary&#39;: &#39;error&#39;,\n      &#39;@typescript-eslint/consistent-type-assertions&#39;: [&#39;error&#39;, { assertionStyle: &#39;never&#39; }],\n      &#39;no-restricted-syntax&#39;: [&#39;error&#39;,\n        { selector: &#39;TSEnumDeclaration&#39;, message: &#39;Use literal unions instead of enums.&#39; },\n        { selector: &#39;IfStatement &gt; :not(IfStatement).alternate&#39;, message: &#39;Avoid else. Use early returns.&#39; },\n        { selector: &#39;TryStatement&#39;, message: &#39;Use tryCatch() instead of try/catch.&#39; },\n      ],\n    },\n  },\n\n  // Feature boundaries\n  {\n    files: [&#39;src/**/*.{ts,vue}&#39;],\n    plugins: { &#39;import-x&#39;: pluginImportX },\n    rules: {\n      &#39;import-x/no-restricted-paths&#39;: [&#39;error&#39;, {\n        zones: [\n          { target: &#39;./src/features/workout&#39;, from: &#39;./src/features&#39;, except: [&#39;./workout&#39;] },\n          // ... other features\n          { target: &#39;./src/features&#39;, from: &#39;./src/views&#39; },  // Unidirectional flow\n        ]\n      }],\n    },\n  },\n\n  // i18n rules\n  {\n    files: [&#39;src/**/*.vue&#39;],\n    plugins: { &#39;@intlify/vue-i18n&#39;: pluginVueI18n },\n    rules: {\n      &#39;@intlify/vue-i18n/no-raw-text&#39;: [&#39;error&#39;, { /* config */ }],\n    },\n  },\n\n  // Prevent disabling i18n rules\n  {\n    files: [&#39;src/**/*.vue&#39;],\n    plugins: { &#39;@eslint-community/eslint-comments&#39;: pluginEslintComments },\n    rules: {\n      &#39;@eslint-community/eslint-comments/no-restricted-disable&#39;: [&#39;error&#39;, &#39;@intlify/vue-i18n/*&#39;],\n    },\n  },\n\n  // Vitest rules\n  {\n    files: [&#39;src/**/__tests__/*&#39;],\n    ...pluginVitest.configs.recommended,\n    rules: {\n      &#39;vitest/consistent-test-it&#39;: [&#39;error&#39;, { fn: &#39;it&#39; }],\n      &#39;vitest/prefer-hooks-on-top&#39;: &#39;error&#39;,\n      &#39;vitest/prefer-hooks-in-order&#39;: &#39;error&#39;,\n      &#39;vitest/no-duplicate-hooks&#39;: &#39;error&#39;,\n      &#39;vitest/max-nested-describe&#39;: [&#39;error&#39;, { max: 2 }],\n      &#39;vitest/no-conditional-in-test&#39;: &#39;warn&#39;,\n    },\n  },\n\n  // Enforce test helpers\n  {\n    files: [&#39;src/**/__tests__/**/*.{ts,spec.ts}&#39;],\n    rules: {\n      &#39;no-restricted-imports&#39;: [&#39;error&#39;, {\n        paths: [\n          { name: &#39;vitest-browser-vue&#39;, importNames: [&#39;render&#39;], message: &#39;Use createTestApp()&#39; },\n          { name: &#39;@vue/test-utils&#39;, importNames: [&#39;mount&#39;], message: &#39;Use createTestApp()&#39; },\n        ]\n      }],\n    },\n  },\n\n  // Local rules\n  {\n    files: [&#39;src/**/*.{ts,vue}&#39;],\n    plugins: { local: localRules },\n    rules: {\n      &#39;local/no-hardcoded-colors&#39;: &#39;error&#39;,\n      &#39;local/composable-must-use-vue&#39;: &#39;error&#39;,\n      &#39;local/repository-trycatch&#39;: &#39;error&#39;,\n      &#39;local/extract-condition-variable&#39;: &#39;error&#39;,\n      &#39;local/no-let-in-describe&#39;: &#39;error&#39;,\n    },\n  },\n\n  // Disable rules handled by Oxlint\n  ...pluginOxlint.buildFromOxlintConfigFile(&#39;./.oxlintrc.json&#39;),\n\n  // pnpm catalog enforcement\n  ...pnpmConfigs.recommended,\n\n  skipFormatting,\n)\n```\n\n&lt;/Collapsible&gt;\n\n---\n\n## Summary\n\n| Category | Rule | Purpose |\n|----------|------|---------|\n| **Must Have** | `complexity` | Limit function complexity |\n| **Must Have** | `no-nested-ternary` | Readable conditionals |\n| **Must Have** | `consistent-type-assertions` | No unsafe `as` casts |\n| **Must Have** | `no-restricted-syntax` (enums) | Use unions over enums |\n| **Must Have** | `no-restricted-syntax` (else) | Prefer early returns |\n| **Must Have** | `no-restricted-syntax` (routes) | Use named routes |\n| **Must Have** | `import-x/no-restricted-paths` | Feature isolation |\n| **Must Have** | `vue/no-unused-*` | Dead code detection |\n| **Must Have** | `@intlify/vue-i18n/no-raw-text` | i18n compliance |\n| **Must Have** | `no-restricted-disable` | No bypassing i18n |\n| **Must Have** | `no-restricted-imports` | Enforce test helpers |\n| **Nice to Have** | `vue/define-props-destructuring` | Vue 3.5 patterns |\n| **Nice to Have** | `vue/max-template-depth` | Template readability |\n| **Nice to Have** | `vitest/*` | Test consistency |\n| **Nice to Have** | `unicorn/*` | Modern JavaScript |\n| **Nice to Have** | `pnpm/recommended` | Catalog enforcement |\n| **Custom** | `composable-must-use-vue` | Composable validation |\n| **Custom** | `no-hardcoded-colors` | Theming support |\n| **Custom** | `no-let-in-describe` | Clean tests |\n| **Custom** | `extract-condition-variable` | Readable conditions |\n| **Custom** | `repository-trycatch` | Error handling |\n\nStart with the must-haves. Add nice-to-haves when you&#39;re ready. Write custom rules when nothing else fits.\n\nThe combination of Oxlint for speed and ESLint for coverage gives you fast feedback during development and comprehensive checks in CI.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>Over the last 7+ years as a Vue developer, I’ve developed a highly opinionated style for writing Vue components. Some of these rules might not be useful for you, but I thought it was worth sharing so you can pick what fits your project. The goal is to enforce code structure that’s readable for both developers and AI agents.</p>
<p>These rules aren’t arbitrary—they encode patterns I’ve written about extensively:</p>
<ul>
<li><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-to-write-clean-vue-components/" class="internal-link astro-3tyn5ojg"> How to Write Clean Vue Components </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Write Clean Vue Components</span> <span class="preview-description astro-3tyn5ojg">There are many ways to write better Vue components. One of my favorite ways is to separate business logic into pure functions.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">architecture</span>  </span> <time class="preview-date astro-3tyn5ojg">Jan 28, 2024</time> </span> </span> </span>  <script>
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
</script> explains why I separate business logic into pure functions</li>
<li><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-to-structure-vue-projects/" class="internal-link astro-3tyn5ojg"> How to Structure Vue Projects </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Structure Vue Projects</span> <span class="preview-description astro-3tyn5ojg">Discover best practices for structuring Vue projects of any size, from simple apps to complex enterprise solutions.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">architecture</span>  </span> <time class="preview-date astro-3tyn5ojg">May 12, 2024</time> </span> </span> </span>  <script>
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
</script> covers my feature-based architecture approach</li>
<li><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/nuxt-layers-modular-monolith/" class="internal-link astro-3tyn5ojg"> Building a Modular Monolith with Nuxt Layers </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Building a Modular Monolith with Nuxt Layers: A Practical Guide</span> <span class="preview-description astro-3tyn5ojg">Learn how to build scalable applications using Nuxt Layers to enforce clean architecture boundaries without the complexity of microservices.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">nuxt</span><span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">architecture</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 2, 2025</time> </span> </span> </span>  <script>
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
</script> applies feature isolation to Nuxt projects</li>
<li><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/the-problem-with-as-in-typescript-why-its-a-shortcut-we-should-avoid/" class="internal-link astro-3tyn5ojg"> The Problem with <code>as</code> in TypeScript </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">The Problem with as in TypeScript: Why It&#39;s a Shortcut We Should Avoid</span> <span class="preview-description astro-3tyn5ojg">Learn why as can be a Problem in Typescript</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">typescript</span>  </span> <time class="preview-date astro-3tyn5ojg">Jan 21, 2024</time> </span> </span> </span>  <script>
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
</script> covers why I ban type assertions</li>
<li><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/robust-error-handling-in-typescript-a-journey-from-naive-to-rust-inspired-solutions/" class="internal-link astro-3tyn5ojg"> Robust Error Handling in TypeScript </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Robust Error Handling in TypeScript: A Journey from Naive to Rust-Inspired Solutions</span> <span class="preview-description astro-3tyn5ojg">Learn to write robust, predictable TypeScript code using Rust&#39;s Result pattern. This post demonstrates practical examples and introduces the ts-results library, implementing Rust&#39;s powerful error management approach in TypeScript.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">typescript</span>  </span> <time class="preview-date astro-3tyn5ojg">Nov 18, 2023</time> </span> </span> </span>  <script>
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
</script> introduces the Result pattern behind my <code>tryCatch</code> rule</li>
<li><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/vue3_testing_pyramid_vitest_browser_mode/" class="internal-link astro-3tyn5ojg"> Vue 3 Testing Pyramid </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Vue 3 Testing Pyramid: A Practical Guide with Vitest Browser Mode</span> <span class="preview-description astro-3tyn5ojg">Learn a practical testing strategy for Vue 3 applications using composable unit tests, Vitest browser mode integration tests, and visual regression testing.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span><span class="preview-tag astro-3tyn5ojg">vitest</span> <span class="preview-tag-more astro-3tyn5ojg">+2</span> </span> <time class="preview-date astro-3tyn5ojg">Dec 14, 2025</time> </span> </span> </span>  <script>
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
</script> explains my integration-first testing strategy</li>
<li><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/frontend-testing-guide-10-essential-rules/" class="internal-link astro-3tyn5ojg"> Frontend Testing Guide </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Frontend Testing Guide: 10 Essential Rules for Naming Tests</span> <span class="preview-description astro-3tyn5ojg">Learn how to write clear and maintainable frontend tests with 10 practical naming rules. Includes real-world examples showing good and bad practices for component testing across any framework.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">testing</span><span class="preview-tag astro-3tyn5ojg">vitest</span>  </span> <time class="preview-date astro-3tyn5ojg">Oct 26, 2024</time> </span> </span> </span>  <script>
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
</script> shares my test naming conventions</li>
</ul>
<p>ESLint rules are how I enforce these patterns automatically—so the codebase stays consistent even as the team grows.</p>
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> Note </p> <div class="alert-content astro-7kdbuayl"> <p><strong>Why linting matters more in the AI era:</strong> As AI agents write more of our code, strict linting becomes essential. It’s a form of <a href="https://banay.me/dont-waste-your-backpressure/?ref=ghuntley.com" rel="noopener noreferrer" target="_blank">back pressure</a>—automated feedback mechanisms that tell an agent when it’s made a mistake, allowing it to self-correct without your intervention. You have a limited budget of feedback (your time and attention). If you spend that budget telling the agent “you missed an import” or “that type is wrong,” you can’t spend it on architectural decisions or complex logic. Type checkers, linters, and test suites act as back pressure: they push back against bad code so you don’t have to. Your ESLint config is now part of your prompt—it’s the automated quality gate that lets agents iterate until they pass.</p> </div> </div> 
<h2 id="table-of-contents">Table of Contents<a class="heading-link" aria-label="Link to section" href="#table-of-contents"><span class="heading-link-icon">#</span></a></h2>
<p></p><details><summary>Open Table of Contents</summary><p></p>
<ul>
<li><a href="#why-two-linters-oxlint--eslint">Why Two Linters? Oxlint + ESLint</a>
<ul>
<li><a href="#oxlint-the-speed-demon">Oxlint: The Speed Demon</a></li>
<li><a href="#the-setup">The Setup</a></li>
</ul>
</li>
<li><a href="#must-have-rules">Must-Have Rules</a>
<ul>
<li><a href="#cyclomatic-complexity">Cyclomatic Complexity</a></li>
<li><a href="#no-nested-ternaries">No Nested Ternaries</a></li>
<li><a href="#no-type-assertions">No Type Assertions</a></li>
<li><a href="#no-enums">No Enums</a></li>
<li><a href="#no-elseelse-if">No else/else-if</a></li>
<li><a href="#no-native-trycatch">No Native try/catch</a></li>
<li><a href="#no-direct-dom-manipulation">No Direct DOM Manipulation</a></li>
<li><a href="#feature-boundary-enforcement">Feature Boundary Enforcement</a></li>
<li><a href="#vue-component-naming">Vue Component Naming</a></li>
<li><a href="#dead-code-detection-in-vue">Dead Code Detection in Vue</a></li>
<li><a href="#no-hardcoded-i18n-strings">No Hardcoded i18n Strings</a></li>
<li><a href="#no-disabling-i18n-rules">No Disabling i18n Rules</a></li>
<li><a href="#no-hardcoded-route-strings">No Hardcoded Route Strings</a></li>
<li><a href="#enforce-integration-test-helpers">Enforce Integration Test Helpers</a></li>
<li><a href="#enforce-pnpm-catalogs">Enforce pnpm Catalogs</a></li>
</ul>
</li>
<li><a href="#nice-to-have-rules">Nice-to-Have Rules</a>
<ul>
<li><a href="#vue-35-api-enforcement">Vue 3.5+ API Enforcement</a></li>
<li><a href="#explicit-component-apis">Explicit Component APIs</a></li>
<li><a href="#template-depth-limit">Template Depth Limit</a></li>
<li><a href="#better-assertions-in-tests">Better Assertions in Tests</a></li>
<li><a href="#test-structure-rules">Test Structure Rules</a></li>
<li><a href="#prefer-vitest-locators-in-tests">Prefer Vitest Locators in Tests</a></li>
<li><a href="#unicorn-rules">Unicorn Rules</a></li>
</ul>
</li>
<li><a href="#custom-local-rules">Custom Local Rules</a>
<ul>
<li><a href="#composable-must-use-vue">Composable Must Use Vue</a></li>
<li><a href="#no-hardcoded-tailwind-colors">No Hardcoded Tailwind Colors</a></li>
<li><a href="#no-let-in-describe-blocks">No let in describe Blocks</a></li>
<li><a href="#extract-complex-conditions">Extract Complex Conditions</a></li>
<li><a href="#repository-trycatch-wrapper">Repository tryCatch Wrapper</a></li>
</ul>
</li>
<li><a href="#the-full-config">The Full Config</a></li>
<li><a href="#summary">Summary</a></li>
</ul>
<p></p></details><p></p>
<h2 id="why-two-linters-oxlint--eslint">Why Two Linters? Oxlint + ESLint<a class="heading-link" aria-label="Link to section" href="#why-two-linters-oxlint--eslint"><span class="heading-link-icon">#</span></a></h2>
<p>I run two linters: <strong>Oxlint</strong> first, then <strong>ESLint</strong>. Why? Speed and coverage.</p>
<h3 id="oxlint-the-speed-demon">Oxlint: The Speed Demon<a class="heading-link" aria-label="Link to section" href="#oxlint-the-speed-demon"><span class="heading-link-icon">#</span></a></h3>
<p><a href="https://oxc.rs/docs/guide/usage/linter.html" rel="noopener noreferrer" target="_blank">Oxlint</a> is written in Rust. It runs 50-100x faster than ESLint on large codebases. My pre-commit hook completes in milliseconds instead of seconds.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#51597D;font-style:italic"># In package.json</span></span>
<span class="line"><span style="color:#C0CAF5">&quot;lint:oxlint&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">oxlint . --fix --ignore-path .gitignore</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">,</span></span>
<span class="line"><span style="color:#C0CAF5">&quot;lint:eslint&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">eslint . --fix --cache</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">,</span></span>
<span class="line"><span style="color:#C0CAF5">&quot;lint&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">run-s lint:*</span><span style="color:#89DDFF">&quot;</span><span style="color:#51597D;font-style:italic">  # Runs oxlint first, then eslint</span></span></code><button type="button" class="copy" data-code="# In package.json
&#34;lint:oxlint&#34;: &#34;oxlint . --fix --ignore-path .gitignore&#34;,
&#34;lint:eslint&#34;: &#34;eslint . --fix --cache&#34;,
&#34;lint&#34;: &#34;run-s lint:*&#34;  # Runs oxlint first, then eslint" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>The tradeoff:</strong> Oxlint supports fewer rules. It handles:</p>
<ul>
<li><strong>Correctness &amp; suspicious patterns</strong> - catches bugs early</li>
<li><strong>Core ESLint equivalents</strong> - <code>no-console</code>, <code>no-explicit-any</code></li>
<li><strong>TypeScript basics</strong> - <code>array-type</code>, <code>consistent-type-definitions</code></li>
</ul>
<p>But Oxlint lacks:</p>
<ul>
<li>Vue-specific rules (<code>vue/*</code>)</li>
<li>Import boundary rules (<code>import-x/*</code>)</li>
<li>Vitest testing rules (<code>vitest/*</code>)</li>
<li>i18n rules (<code>@intlify/vue-i18n/*</code>)</li>
<li>Custom local rules</li>
</ul>
<h3 id="the-setup">The Setup<a class="heading-link" aria-label="Link to section" href="#the-setup"><span class="heading-link-icon">#</span></a></h3>
<p>Oxlint runs first for fast feedback. ESLint runs second for comprehensive checks. The <code>eslint-plugin-oxlint</code> package tells ESLint to skip rules that Oxlint already handles.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> pluginOxlint</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">eslint-plugin-oxlint</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#7DCFFF"> default</span><span style="color:#7AA2F7"> defineConfigWithVueTs</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // ... other configs</span></span>
<span class="line"><span style="color:#F7768E;font-weight:bold">  ...</span><span style="color:#C0CAF5">pluginOxlint</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">buildFromOxlintConfigFile</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">./.oxlintrc.json</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">)</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
import pluginOxlint from 'eslint-plugin-oxlint'

export default defineConfigWithVueTs(
  // ... other configs
  ...pluginOxlint.buildFromOxlintConfigFile('./.oxlintrc.json'),
)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#51597D;font-style:italic">// .oxlintrc.json</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">$schema</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">./node_modules/oxlint/configuration_schema.json</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">categories</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#0DB9D7">correctness</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#0DB9D7">suspicious</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">warn</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">rules</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#0DB9D7">typescript/no-explicit-any</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#0DB9D7">eslint/no-console</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#89DDFF"> &quot;</span><span style="color:#7DCFFF">allow</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">warn</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span><span style="color:#9ABDF5"> }]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// .oxlintrc.json
{
  &#34;$schema&#34;: &#34;./node_modules/oxlint/configuration_schema.json&#34;,
  &#34;categories&#34;: {
    &#34;correctness&#34;: &#34;error&#34;,
    &#34;suspicious&#34;: &#34;warn&#34;
  },
  &#34;rules&#34;: {
    &#34;typescript/no-explicit-any&#34;: &#34;error&#34;,
    &#34;eslint/no-console&#34;: [&#34;error&#34;, { &#34;allow&#34;: [&#34;warn&#34;, &#34;error&#34;] }]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr/>
<h2 id="must-have-rules">Must-Have Rules<a class="heading-link" aria-label="Link to section" href="#must-have-rules"><span class="heading-link-icon">#</span></a></h2>
<p>These rules catch real bugs and enforce maintainable code. Enable them on every Vue project.</p>
<hr/>
<h3 id="cyclomatic-complexity">Cyclomatic Complexity<a class="heading-link" aria-label="Link to section" href="#cyclomatic-complexity"><span class="heading-link-icon">#</span></a></h3>
<p>Complex functions are hard to test and understand. This rule limits branching logic per function.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">complexity</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">warn</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">max</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 10</span><span style="color:#9ABDF5"> }]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  rules: {
    'complexity': ['warn', { max: 10 }]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> processOrder</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">order</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Order</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">order</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">status</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">pending</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">order</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">items</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#BB9AF7"> &gt;</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">order</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">payment</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">order</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">payment</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">verified</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">          if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">order</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">shipping</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">            // 5 levels deep, complexity keeps growing...</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="function processOrder(order: Order) {
  if (order.status === 'pending') {
    if (order.items.length > 0) {
      if (order.payment) {
        if (order.payment.verified) {
          if (order.shipping) {
            // 5 levels deep, complexity keeps growing...
          }
        }
      }
    }
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> processOrder</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">order</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Order</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#7AA2F7">isValidOrder</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">order</span><span style="color:#9ABDF5">)) </span><span style="color:#BB9AF7;font-style:italic">return</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  processPayment</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">order</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">payment</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#7AA2F7">  scheduleShipping</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">order</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">shipping</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> isValidOrder</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">order</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Order</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> order</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">status</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">pending</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#BB9AF7">    &amp;&amp;</span><span style="color:#C0CAF5"> order</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">items</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#BB9AF7"> &gt;</span><span style="color:#FF9E64"> 0</span></span>
<span class="line"><span style="color:#BB9AF7">    &amp;&amp;</span><span style="color:#C0CAF5"> order</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">payment</span><span style="color:#89DDFF">?.</span><span style="color:#7DCFFF">verified</span><span style="color:#BB9AF7"> ===</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="function processOrder(order: Order) {
  if (!isValidOrder(order)) return

  processPayment(order.payment)
  scheduleShipping(order.shipping)
}

function isValidOrder(order: Order): boolean {
  return order.status === 'pending'
    &#38;&#38; order.items.length > 0
    &#38;&#38; order.payment?.verified === true
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<p><strong>Threshold guidance:</strong></p>
<ul>
<li>ESLint default: <code>20</code> (lenient)</li>
<li>This project uses: <code>10</code> (stricter)</li>
<li>Consider <code>15</code> as a middle ground for legacy codebases</li>
</ul>
<blockquote>
<p><a href="https://eslint.org/docs/latest/rules/complexity" rel="noopener noreferrer" target="_blank">ESLint: complexity</a></p>
</blockquote>
<hr/>
<h3 id="no-nested-ternaries">No Nested Ternaries<a class="heading-link" aria-label="Link to section" href="#no-nested-ternaries"><span class="heading-link-icon">#</span></a></h3>
<p>Nested ternaries are hard to read. Use early returns or separate variables instead.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">no-nested-ternary</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  rules: {
    'no-nested-ternary': 'error'
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> label</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> isLoading</span><span style="color:#BB9AF7"> ?</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Loading...</span><span style="color:#89DDFF">&#39;</span><span style="color:#BB9AF7"> :</span><span style="color:#C0CAF5"> hasError</span><span style="color:#BB9AF7"> ?</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Failed</span><span style="color:#89DDFF">&#39;</span><span style="color:#BB9AF7"> :</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Success</span><span style="color:#89DDFF">&#39;</span></span></code><button type="button" class="copy" data-code="const label = isLoading ? 'Loading...' : hasError ? 'Failed' : 'Success'" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> getLabel</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">isLoading</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Loading...</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">hasError</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Failed</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Success</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> label</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> getLabel</span><span style="color:#9ABDF5">()</span></span></code><button type="button" class="copy" data-code="function getLabel() {
  if (isLoading) return 'Loading...'
  if (hasError) return 'Failed'
  return 'Success'
}

const label = getLabel()" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://eslint.org/docs/rules/no-nested-ternary" rel="noopener noreferrer" target="_blank">ESLint: no-nested-ternary</a></p>
</blockquote>
<hr/>
<h3 id="no-type-assertions">No Type Assertions<a class="heading-link" aria-label="Link to section" href="#no-type-assertions"><span class="heading-link-icon">#</span></a></h3>
<p>Type assertions (<code>as Type</code>) bypass TypeScript’s type checker. They hide bugs. Use type guards or proper typing instead.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">@typescript-eslint/consistent-type-assertions</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      assertionStyle</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">never</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">    }]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  rules: {
    '@typescript-eslint/consistent-type-assertions': ['error', {
      assertionStyle: 'never'
    }]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> Note </p> <div class="alert-content astro-7kdbuayl"> <p><code>as const</code> assertions are always allowed, even with <code>assertionStyle: &#39;never&#39;</code>. Const assertions don’t bypass type checking—they make types more specific.</p> </div> </div> 
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> user</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> response</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">data</span><span style="color:#89DDFF"> as</span><span style="color:#C0CAF5"> User</span><span style="color:#51597D;font-style:italic">  // What if it&#39;s not a User?</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> element</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> document</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">querySelector</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">.btn</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF"> as</span><span style="color:#C0CAF5"> HTMLButtonElement</span></span>
<span class="line"><span style="color:#C0CAF5">element</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">click</span><span style="color:#9ABDF5">()</span><span style="color:#51597D;font-style:italic">  // Runtime error if element is null</span></span></code><button type="button" class="copy" data-code="const user = response.data as User  // What if it's not a User?

const element = document.querySelector('.btn') as HTMLButtonElement
element.click()  // Runtime error if element is null" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Use type guards</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> isUser</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">data</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> unknown</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#E0AF68"> data</span><span style="color:#89DDFF"> is</span><span style="color:#C0CAF5"> User</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#89DDFF"> typeof</span><span style="color:#C0CAF5"> data</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">object</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#BB9AF7">    &amp;&amp;</span><span style="color:#C0CAF5"> data</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> null</span></span>
<span class="line"><span style="color:#BB9AF7">    &amp;&amp;</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">id</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> in</span><span style="color:#C0CAF5"> data</span></span>
<span class="line"><span style="color:#BB9AF7">    &amp;&amp;</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">name</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> in</span><span style="color:#C0CAF5"> data</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">if</span><span style="color:#9ABDF5"> (</span><span style="color:#7AA2F7">isUser</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">response</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">data</span><span style="color:#9ABDF5">))</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> user</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> response</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">data</span><span style="color:#51597D;font-style:italic">  // TypeScript knows it&#39;s User</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Handle nulls properly</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> element</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> document</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">querySelector</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">.btn</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7">if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">element</span><span style="color:#89DDFF"> instanceof</span><span style="color:#C0CAF5"> HTMLButtonElement</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  element</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">click</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// Use type guards
function isUser(data: unknown): data is User {
  return typeof data === 'object'
    &#38;&#38; data !== null
    &#38;&#38; 'id' in data
    &#38;&#38; 'name' in data
}

if (isUser(response.data)) {
  const user = response.data  // TypeScript knows it's User
}

// Handle nulls properly
const element = document.querySelector('.btn')
if (element instanceof HTMLButtonElement) {
  element.click()
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://typescript-eslint.io/rules/consistent-type-assertions" rel="noopener noreferrer" target="_blank">TypeScript ESLint: consistent-type-assertions</a></p>
</blockquote>
<hr/>
<h3 id="no-enums">No Enums<a class="heading-link" aria-label="Link to section" href="#no-enums"><span class="heading-link-icon">#</span></a></h3>
<p>TypeScript enums have quirks. They generate JavaScript code, have numeric reverse mappings, and behave differently from union types. Use literal unions or const objects instead.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">no-restricted-syntax</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      selector</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">TSEnumDeclaration</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Use literal unions or `as const` objects instead of enums.</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">    }]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  rules: {
    'no-restricted-syntax': ['error', {
      selector: 'TSEnumDeclaration',
      message: 'Use literal unions or `as const` objects instead of enums.'
    }]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#BB9AF7">enum</span><span style="color:#C0CAF5"> Status</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  Pending</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">  Active</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">  Done</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> status</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Status</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> Status</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">Pending</span></span></code><button type="button" class="copy" data-code="enum Status {
  Pending,
  Active,
  Done
}

const status: Status = Status.Pending" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// Literal union - simplest</span></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> Status</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">pending</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">active</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">done</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Or const object when you need values</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> Status</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  Pending</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">pending</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  Active</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">active</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  Done</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">done</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF"> as</span><span style="color:#9D7CD8;font-style:italic"> const</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> Status</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> typeof</span><span style="color:#C0CAF5"> Status</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">keyof</span><span style="color:#89DDFF"> typeof</span><span style="color:#7DCFFF"> Status</span><span style="color:#9ABDF5">]</span></span></code><button type="button" class="copy" data-code="// Literal union - simplest
type Status = 'pending' | 'active' | 'done'

// Or const object when you need values
const Status = {
  Pending: 'pending',
  Active: 'active',
  Done: 'done'
} as const

type Status = typeof Status[keyof typeof Status]" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://eslint.org/docs/rules/no-restricted-syntax" rel="noopener noreferrer" target="_blank">ESLint: no-restricted-syntax</a></p>
</blockquote>
<hr/>
<h3 id="no-elseelse-if">No else/else-if<a class="heading-link" aria-label="Link to section" href="#no-elseelse-if"><span class="heading-link-icon">#</span></a></h3>
<p><code>else</code> and <code>else-if</code> blocks increase nesting. Early returns are easier to read and reduce cognitive load.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">no-restricted-syntax</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      {</span></span>
<span class="line"><span style="color:#73DACA">        selector</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">IfStatement &gt; IfStatement.alternate</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Avoid `else if`. Prefer early returns or ternary operators.</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      {</span></span>
<span class="line"><span style="color:#73DACA">        selector</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">IfStatement &gt; :not(IfStatement).alternate</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Avoid `else`. Prefer early returns or ternary operators.</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    ]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  rules: {
    'no-restricted-syntax': ['error',
      {
        selector: 'IfStatement > IfStatement.alternate',
        message: 'Avoid `else if`. Prefer early returns or ternary operators.'
      },
      {
        selector: 'IfStatement > :not(IfStatement).alternate',
        message: 'Avoid `else`. Prefer early returns or ternary operators.'
      }
    ]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> getDiscount</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">user</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> User</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">isPremium</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#FF9E64"> 0.2</span></span>
<span class="line"><span style="color:#9ABDF5">  } </span><span style="color:#BB9AF7">else</span><span style="color:#BB9AF7"> if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">isMember</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#FF9E64"> 0.1</span></span>
<span class="line"><span style="color:#9ABDF5">  } </span><span style="color:#BB9AF7">else</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#FF9E64"> 0</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="function getDiscount(user: User) {
  if (user.isPremium) {
    return 0.2
  } else if (user.isMember) {
    return 0.1
  } else {
    return 0
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> getDiscount</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">user</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> User</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">isPremium</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#FF9E64"> 0.2</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">isMember</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#FF9E64"> 0.1</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#FF9E64"> 0</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="function getDiscount(user: User) {
  if (user.isPremium) return 0.2
  if (user.isMember) return 0.1
  return 0
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://eslint.org/docs/rules/no-restricted-syntax" rel="noopener noreferrer" target="_blank">ESLint: no-restricted-syntax</a></p>
</blockquote>
<hr/>
<h3 id="no-native-trycatch">No Native try/catch<a class="heading-link" aria-label="Link to section" href="#no-native-trycatch"><span class="heading-link-icon">#</span></a></h3>
<p>Native try/catch blocks are verbose and error-prone. Use a utility function that returns a result tuple instead.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">no-restricted-syntax</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      selector</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">TryStatement</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Use tryCatch() from @/lib/tryCatch instead of try/catch. Returns Result&lt;T&gt; tuple: [error, null] | [null, data].</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">    }]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  rules: {
    'no-restricted-syntax': ['error', {
      selector: 'TryStatement',
      message: 'Use tryCatch() from @/lib/tryCatch instead of try/catch. Returns Result<T> tuple: [error, null] | [null, data].'
    }]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> fetchUser</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">id</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  try</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> response</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#C0CAF5"> api</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">get</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">/users/</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">id</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#C0CAF5"> response</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">data</span></span>
<span class="line"><span style="color:#9ABDF5">  } </span><span style="color:#BB9AF7">catch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">error</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">error</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">error</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#FF9E64"> null</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="async function fetchUser(id: string) {
  try {
    const response = await api.get(`/users/${id}`)
    return response.data
  } catch (error) {
    console.error(error)
    return null
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">async</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> fetchUser</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">id</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#89DDFF"> [</span><span style="color:#BB9AF7">error</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> response</span><span style="color:#89DDFF">]</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> tryCatch</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">api</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">get</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">/users/</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">id</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">))</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">error</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">error</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">error</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#FF9E64"> null</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> response</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">data</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="async function fetchUser(id: string) {
  const [error, response] = await tryCatch(api.get(`/users/${id}`))

  if (error) {
    console.error(error)
    return null
  }

  return response.data
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<p>The <code>tryCatch</code> utility returns <code>[error, null]</code> or <code>[null, data]</code>, similar to Go’s error handling.</p>
<blockquote>
<p><a href="https://eslint.org/docs/rules/no-restricted-syntax" rel="noopener noreferrer" target="_blank">ESLint: no-restricted-syntax</a></p>
</blockquote>
<hr/>
<h3 id="no-direct-dom-manipulation">No Direct DOM Manipulation<a class="heading-link" aria-label="Link to section" href="#no-direct-dom-manipulation"><span class="heading-link-icon">#</span></a></h3>
<p>Vue manages the DOM. Calling <code>document.querySelector</code> bypasses Vue’s reactivity and template refs. Use <code>useTemplateRef()</code> instead. If you’re on Vue 3.5+, the built-in rule already enforces this.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/prefer-use-template-ref</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  files: ['src/**/*.vue'],
  rules: {
    'vue/prefer-use-template-ref': 'error'
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> focusInput</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> input</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> document</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getElementById</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">my-input</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">  input</span><span style="color:#89DDFF">?.</span><span style="color:#7AA2F7">focus</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">input</span><span style="color:#BB9AF7"> id</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">my-input</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
function focusInput() {
  const input = document.getElementById('my-input')
  input?.focus()
}
</script>

<template>
  <input id=&#34;my-input&#34; />
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useTemplateRef</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> inputRef</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useTemplateRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">HTMLInputElement</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">input</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> focusInput</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  inputRef</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">?.</span><span style="color:#7AA2F7">focus</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">input</span><span style="color:#BB9AF7"> ref</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">input</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
import { useTemplateRef } from 'vue'

const inputRef = useTemplateRef<HTMLInputElement>('input')

function focusInput() {
  inputRef.value?.focus()
}
</script>

<template>
  <input ref=&#34;input&#34; />
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://eslint.org/docs/rules/no-restricted-syntax" rel="noopener noreferrer" target="_blank">ESLint: no-restricted-syntax</a></p>
</blockquote>
<hr/>
<h3 id="feature-boundary-enforcement">Feature Boundary Enforcement<a class="heading-link" aria-label="Link to section" href="#feature-boundary-enforcement"><span class="heading-link-icon">#</span></a></h3>
<p>Features should not import from other features. This keeps code modular and prevents circular dependencies. If you’re using a feature-based architecture, this rule is essential—see <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-to-structure-vue-projects/" class="internal-link astro-3tyn5ojg"> How to Structure Vue Projects </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Structure Vue Projects</span> <span class="preview-description astro-3tyn5ojg">Discover best practices for structuring Vue projects of any size, from simple apps to complex enterprise solutions.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">architecture</span>  </span> <time class="preview-date astro-3tyn5ojg">May 12, 2024</time> </span> </span> </span>  <script>
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
</script> for more on this approach.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> { </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">import-x</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#C0CAF5">pluginImportX</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">import-x/no-restricted-paths</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      zones</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">        // === CROSS-FEATURE ISOLATION ===</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">        // Features cannot import from other features</span></span>
<span class="line"><span style="color:#9ABDF5">        { </span><span style="color:#73DACA">target</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features/workout</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> from</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> except</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">./workout</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">] }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        { </span><span style="color:#73DACA">target</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features/exercises</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> from</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> except</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">./exercises</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">] }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        { </span><span style="color:#73DACA">target</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features/settings</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> from</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> except</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">./settings</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">] }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        { </span><span style="color:#73DACA">target</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features/timers</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> from</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> except</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">./timers</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">] }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        { </span><span style="color:#73DACA">target</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features/templates</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> from</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> except</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">./templates</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">] }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        { </span><span style="color:#73DACA">target</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features/benchmarks</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> from</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> except</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">./benchmarks</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">] }</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">        // === UNIDIRECTIONAL FLOW ===</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">        // Shared code cannot import from features or views</span></span>
<span class="line"><span style="color:#9ABDF5">        {</span></span>
<span class="line"><span style="color:#73DACA">          target</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">./src/components</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/composables</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/lib</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/db</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/types</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/stores</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">          from</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">./src/features</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/views</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">        // Features cannot import from views (views are top-level orchestrators)</span></span>
<span class="line"><span style="color:#9ABDF5">        { </span><span style="color:#73DACA">target</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> from</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/views</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">      ]</span></span>
<span class="line"><span style="color:#9ABDF5">    }]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  plugins: { 'import-x': pluginImportX },
  rules: {
    'import-x/no-restricted-paths': ['error', {
      zones: [
        // === CROSS-FEATURE ISOLATION ===
        // Features cannot import from other features
        { target: './src/features/workout', from: './src/features', except: ['./workout'] },
        { target: './src/features/exercises', from: './src/features', except: ['./exercises'] },
        { target: './src/features/settings', from: './src/features', except: ['./settings'] },
        { target: './src/features/timers', from: './src/features', except: ['./timers'] },
        { target: './src/features/templates', from: './src/features', except: ['./templates'] },
        { target: './src/features/benchmarks', from: './src/features', except: ['./benchmarks'] },

        // === UNIDIRECTIONAL FLOW ===
        // Shared code cannot import from features or views
        {
          target: ['./src/components', './src/composables', './src/lib', './src/db', './src/types', './src/stores'],
          from: ['./src/features', './src/views']
        },

        // Features cannot import from views (views are top-level orchestrators)
        { target: './src/features', from: './src/views' }
      ]
    }]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Unidirectional Flow:</strong> The architecture enforces a strict dependency hierarchy. Views orchestrate features, features use shared code, but never the reverse.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>views → features → shared (components, composables, lib, db, types, stores)</span></span></code><button type="button" class="copy" data-code="views → features → shared (components, composables, lib, db, types, stores)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// src/features/workout/composables/useWorkout.ts</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useExerciseData</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@/features/exercises/composables/useExerciseData</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Cross-feature import!</span></span></code><button type="button" class="copy" data-code="// src/features/workout/composables/useWorkout.ts
import { useExerciseData } from '@/features/exercises/composables/useExerciseData'
// Cross-feature import!" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// src/features/workout/composables/useWorkout.ts</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ExerciseRepository</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@/db/repositories/ExerciseRepository</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Use shared database layer instead</span></span></code><button type="button" class="copy" data-code="// src/features/workout/composables/useWorkout.ts
import { ExerciseRepository } from '@/db/repositories/ExerciseRepository'
// Use shared database layer instead" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://github.com/un-ts/eslint-plugin-import-x" rel="noopener noreferrer" target="_blank">eslint-plugin-import-x: no-restricted-paths</a></p>
</blockquote>
<hr/>
<h3 id="vue-component-naming">Vue Component Naming<a class="heading-link" aria-label="Link to section" href="#vue-component-naming"><span class="heading-link-icon">#</span></a></h3>
<p>Consistent naming makes components easy to find and identify.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/multi-word-component-names</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      ignores</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">App</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Layout</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#9ABDF5">    }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/component-definition-name-casing</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">PascalCase</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/component-name-in-template-casing</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">PascalCase</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      registeredComponentsOnly</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> false</span></span>
<span class="line"><span style="color:#9ABDF5">    }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/match-component-file-name</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      extensions</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      shouldMatchCase</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#9ABDF5">    }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/prop-name-casing</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">camelCase</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/attribute-hyphenation</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">always</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/custom-event-name-casing</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">kebab-case</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  files: ['src/**/*.vue'],
  rules: {
    'vue/multi-word-component-names': ['error', {
      ignores: ['App', 'Layout']
    }],
    'vue/component-definition-name-casing': ['error', 'PascalCase'],
    'vue/component-name-in-template-casing': ['error', 'PascalCase', {
      registeredComponentsOnly: false
    }],
    'vue/match-component-file-name': ['error', {
      extensions: ['vue'],
      shouldMatchCase: true
    }],
    'vue/prop-name-casing': ['error', 'camelCase'],
    'vue/attribute-hyphenation': ['error', 'always'],
    'vue/custom-event-name-casing': ['error', 'kebab-case']
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#51597D;font-style:italic">&lt;!-- File: button.vue --&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#DE5971">base-button</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Click</span><span style="color:#BA3C97">&lt;/</span><span style="color:#DE5971">base-button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<!-- File: button.vue -->
<template>
  <base-button>Click</base-button>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#51597D;font-style:italic">&lt;!-- File: SubmitButton.vue --&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#DE5971">BaseButton</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Click</span><span style="color:#BA3C97">&lt;/</span><span style="color:#DE5971">BaseButton</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<!-- File: SubmitButton.vue -->
<template>
  <BaseButton>Click</BaseButton>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://eslint.vuejs.org/rules/" rel="noopener noreferrer" target="_blank">eslint-plugin-vue: component rules</a></p>
</blockquote>
<hr/>
<h3 id="dead-code-detection-in-vue">Dead Code Detection in Vue<a class="heading-link" aria-label="Link to section" href="#dead-code-detection-in-vue"><span class="heading-link-icon">#</span></a></h3>
<p>Find unused props, refs, and emits before they become tech debt.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/no-unused-properties</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      groups</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">props</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">data</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">computed</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">methods</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#9ABDF5">    }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/no-unused-refs</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/no-unused-emit-declarations</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  files: ['src/**/*.vue'],
  rules: {
    'vue/no-unused-properties': ['error', {
      groups: ['props', 'data', 'computed', 'methods']
    }],
    'vue/no-unused-refs': 'error',
    'vue/no-unused-emit-declarations': 'error'
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> props</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> defineProps</span><span style="color:#89DDFF">&lt;</span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  title</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span></span>
<span class="line"><span style="color:#73DACA">  subtitle</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#51597D;font-style:italic">  // Never used!</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> emit</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> defineEmits</span><span style="color:#89DDFF">&lt;</span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#9ABDF5">  (</span><span style="color:#E0AF68">e</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">click</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#9ABDF5">  (</span><span style="color:#E0AF68">e</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">hover</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> void</span><span style="color:#51597D;font-style:italic">  // Never emitted!</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> buttonRef</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">HTMLButtonElement</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span><span style="color:#51597D;font-style:italic">  // Never used!</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">h1</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">{{ title }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">h1</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">button</span><span style="color:#BB9AF7"> @click</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">emit(&#39;click&#39;)</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Click</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
import { ref } from 'vue'

const props = defineProps<{
  title: string
  subtitle: string  // Never used!
}>()

const emit = defineEmits<{
  (e: 'click'): void
  (e: 'hover'): void  // Never emitted!
}>()

const buttonRef = ref<HTMLButtonElement>()  // Never used!
</script>

<template>
  <h1>{{ title }}</h1>
  <button @click=&#34;emit('click')&#34;>Click</button>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> props</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> defineProps</span><span style="color:#89DDFF">&lt;</span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  title</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> emit</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> defineEmits</span><span style="color:#89DDFF">&lt;</span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#9ABDF5">  (</span><span style="color:#E0AF68">e</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">click</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> void</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">h1</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">{{ title }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">h1</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">button</span><span style="color:#BB9AF7"> @click</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">emit(&#39;click&#39;)</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Click</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
const props = defineProps<{
  title: string
}>()

const emit = defineEmits<{
  (e: 'click'): void
}>()
</script>

<template>
  <h1>{{ title }}</h1>
  <button @click=&#34;emit('click')&#34;>Click</button>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://eslint.vuejs.org/rules/no-unused-properties.html" rel="noopener noreferrer" target="_blank">eslint-plugin-vue: no-unused-properties</a></p>
</blockquote>
<hr/>
<h3 id="no-hardcoded-i18n-strings">No Hardcoded i18n Strings<a class="heading-link" aria-label="Link to section" href="#no-hardcoded-i18n-strings"><span class="heading-link-icon">#</span></a></h3>
<p>Hardcoded strings break internationalization. The <code>@intlify/vue-i18n</code> plugin catches them.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> { </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">@intlify/vue-i18n</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#C0CAF5">pluginVueI18n</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">@intlify/vue-i18n/no-raw-text</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      ignorePattern</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">^[-#:()&amp;+×/°′″%]+</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      ignoreText</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">kg</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">lbs</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">cm</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">ft/in</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">—</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">•</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">✓</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">›</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">→</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">·</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">.</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Close</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      attributes</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">        &#39;</span><span style="color:#9ECE6A">/.+/</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">title</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">aria-label</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">aria-placeholder</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">placeholder</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">alt</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    }]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  files: ['src/**/*.vue'],
  plugins: { '@intlify/vue-i18n': pluginVueI18n },
  rules: {
    '@intlify/vue-i18n/no-raw-text': ['error', {
      ignorePattern: '^[-#:()&#38;+×/°′″%]+',
      ignoreText: ['kg', 'lbs', 'cm', 'ft/in', '—', '•', '✓', '›', '→', '·', '.', 'Close'],
      attributes: {
        '/.+/': ['title', 'aria-label', 'aria-placeholder', 'placeholder', 'alt']
      }
    }]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The <code>attributes</code> option catches hardcoded strings in accessibility attributes too.</p>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Save Changes</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">No items found</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<template>
  <button>Save Changes</button>
  <p>No items found</p>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">{{ t(&#39;common.save&#39;) }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">{{ t(&#39;items.empty&#39;) }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">p</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<template>
  <button>{{ t('common.save') }}</button>
  <p>{{ t('items.empty') }}</p>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://eslint-plugin-vue-i18n.intlify.dev/" rel="noopener noreferrer" target="_blank">eslint-plugin-vue-i18n</a></p>
</blockquote>
<hr/>
<h3 id="no-disabling-i18n-rules">No Disabling i18n Rules<a class="heading-link" aria-label="Link to section" href="#no-disabling-i18n-rules"><span class="heading-link-icon">#</span></a></h3>
<p>Prevent developers from bypassing i18n checks with <code>eslint-disable</code> comments.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">@eslint-community/eslint-comments</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#C0CAF5">pluginEslintComments</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">@eslint-community/eslint-comments/no-restricted-disable</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">@intlify/vue-i18n/*</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">    ]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  files: ['src/**/*.vue'],
  plugins: {
    '@eslint-community/eslint-comments': pluginEslintComments
  },
  rules: {
    '@eslint-community/eslint-comments/no-restricted-disable': [
      'error',
      '@intlify/vue-i18n/*'
    ]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#51597D;font-style:italic">&lt;!-- eslint-disable-next-line @intlify/vue-i18n/no-raw-text --&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Save Changes</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<!-- eslint-disable-next-line @intlify/vue-i18n/no-raw-text -->
<button>Save Changes</button>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">{{ t(&#39;common.save&#39;) }}</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<button>{{ t('common.save') }}</button>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://github.com/eslint-community/eslint-plugin-eslint-comments" rel="noopener noreferrer" target="_blank">@eslint-community/eslint-plugin-eslint-comments</a></p>
</blockquote>
<hr/>
<h3 id="no-hardcoded-route-strings">No Hardcoded Route Strings<a class="heading-link" aria-label="Link to section" href="#no-hardcoded-route-strings"><span class="heading-link-icon">#</span></a></h3>
<p>Use named routes instead of hardcoded path strings for maintainability.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">no-restricted-syntax</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      {</span></span>
<span class="line"><span style="color:#73DACA">        selector</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">CallExpression[callee.property.name=&quot;push&quot;][callee.object.name=&quot;router&quot;] &gt; Literal:first-child</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Use named routes with RouteNames instead of hardcoded path strings.</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      {</span></span>
<span class="line"><span style="color:#73DACA">        selector</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">CallExpression[callee.property.name=&quot;push&quot;][callee.object.name=&quot;router&quot;] &gt; TemplateLiteral:first-child</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">        message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Use named routes with RouteNames instead of template literals.</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    ]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  rules: {
    'no-restricted-syntax': ['error',
      {
        selector: 'CallExpression[callee.property.name=&#34;push&#34;][callee.object.name=&#34;router&#34;] > Literal:first-child',
        message: 'Use named routes with RouteNames instead of hardcoded path strings.'
      },
      {
        selector: 'CallExpression[callee.property.name=&#34;push&#34;][callee.object.name=&#34;router&#34;] > TemplateLiteral:first-child',
        message: 'Use named routes with RouteNames instead of template literals.'
      }
    ]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#C0CAF5">router</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">push</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">/workout/123</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#C0CAF5">router</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">push</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">/workout/</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">id</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span></span></code><button type="button" class="copy" data-code="router.push('/workout/123')
router.push(`/workout/${id}`)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#C0CAF5">router</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">push</span><span style="color:#9ABDF5">({</span><span style="color:#73DACA"> name</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> RouteNames</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">WorkoutDetail</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> params</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span><span style="color:#C0CAF5"> id</span><span style="color:#9ABDF5"> }</span><span style="color:#9ABDF5"> })</span></span></code><button type="button" class="copy" data-code="router.push({ name: RouteNames.WorkoutDetail, params: { id } })" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://eslint.org/docs/latest/rules/no-restricted-syntax" rel="noopener noreferrer" target="_blank">ESLint: no-restricted-syntax</a></p>
</blockquote>
<hr/>
<h3 id="enforce-integration-test-helpers">Enforce Integration Test Helpers<a class="heading-link" aria-label="Link to section" href="#enforce-integration-test-helpers"><span class="heading-link-icon">#</span></a></h3>
<p>Ban direct <code>render()</code> or <code>mount()</code> calls in tests. Use a centralized test helper instead. For more on testing strategies in Vue, see <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/vue3_testing_pyramid_vitest_browser_mode/" class="internal-link astro-3tyn5ojg"> Vue 3 Testing Pyramid: A Practical Guide with Vitest Browser Mode </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Vue 3 Testing Pyramid: A Practical Guide with Vitest Browser Mode</span> <span class="preview-description astro-3tyn5ojg">Learn a practical testing strategy for Vue 3 applications using composable unit tests, Vitest browser mode integration tests, and visual regression testing.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span><span class="preview-tag astro-3tyn5ojg">vitest</span> <span class="preview-tag-more astro-3tyn5ojg">+2</span> </span> <time class="preview-date astro-3tyn5ojg">Dec 14, 2025</time> </span> </span> </span>  <script>
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
</script>.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/__tests__/**/*.{ts,spec.ts}</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  ignores</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/__tests__/helpers/**</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">no-restricted-imports</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      paths</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">        {</span></span>
<span class="line"><span style="color:#73DACA">          name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vitest-browser-vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">          importNames</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">render</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">          message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Use createTestApp() from @/__tests__/helpers/createTestApp instead.</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        {</span></span>
<span class="line"><span style="color:#73DACA">          name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@vue/test-utils</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">          importNames</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">mount</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">shallowMount</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">          message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Use createTestApp() instead of mounting components directly.</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span></span>
<span class="line"><span style="color:#9ABDF5">      ]</span></span>
<span class="line"><span style="color:#9ABDF5">    }]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  files: ['src/**/__tests__/**/*.{ts,spec.ts}'],
  ignores: ['src/__tests__/helpers/**'],
  rules: {
    'no-restricted-imports': ['error', {
      paths: [
        {
          name: 'vitest-browser-vue',
          importNames: ['render'],
          message: 'Use createTestApp() from @/__tests__/helpers/createTestApp instead.'
        },
        {
          name: '@vue/test-utils',
          importNames: ['mount', 'shallowMount'],
          message: 'Use createTestApp() instead of mounting components directly.'
        }
      ]
    }]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">render</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vitest-browser-vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">mount</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@vue/test-utils</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> getByText</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> render</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">MyComponent</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> wrapper</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> mount</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">MyComponent</span><span style="color:#9ABDF5">)</span></span></code><button type="button" class="copy" data-code="import { render } from 'vitest-browser-vue'
import { mount } from '@vue/test-utils'

const { getByText } = render(MyComponent)
const wrapper = mount(MyComponent)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">createTestApp</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@/__tests__/helpers/createTestApp</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> page</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> createTestApp</span><span style="color:#9ABDF5">({</span><span style="color:#73DACA"> route</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">/workout</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> })</span></span></code><button type="button" class="copy" data-code="import { createTestApp } from '@/__tests__/helpers/createTestApp'

const { page } = await createTestApp({ route: '/workout' })" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<p>This ensures all tests use consistent setup with routing, i18n, and database.</p>
<blockquote>
<p><a href="https://eslint.org/docs/latest/rules/no-restricted-imports" rel="noopener noreferrer" target="_blank">ESLint: no-restricted-imports</a></p>
</blockquote>
<hr/>
<h3 id="enforce-pnpm-catalogs">Enforce pnpm Catalogs<a class="heading-link" aria-label="Link to section" href="#enforce-pnpm-catalogs"><span class="heading-link-icon">#</span></a></h3>
<p>When using pnpm workspaces, enforce that dependencies use catalog references.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">configs</span><span style="color:#89DDFF"> as</span><span style="color:#0DB9D7"> pnpmConfigs</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">eslint-plugin-pnpm</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#7DCFFF"> default</span><span style="color:#7AA2F7"> defineConfigWithVueTs</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // ... other configs</span></span>
<span class="line"><span style="color:#F7768E;font-weight:bold">  ...</span><span style="color:#C0CAF5">pnpmConfigs</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">recommended</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">)</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
import { configs as pnpmConfigs } from 'eslint-plugin-pnpm'

export default defineConfigWithVueTs(
  // ... other configs
  ...pnpmConfigs.recommended,
)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This ensures dependencies are managed centrally in <code>pnpm-workspace.yaml</code>.</p>
<blockquote>
<p><a href="https://github.com/nickmccurdy/eslint-plugin-pnpm" rel="noopener noreferrer" target="_blank">eslint-plugin-pnpm</a></p>
</blockquote>
<hr/>
<h2 id="nice-to-have-rules">Nice-to-Have Rules<a class="heading-link" aria-label="Link to section" href="#nice-to-have-rules"><span class="heading-link-icon">#</span></a></h2>
<p>These rules improve code quality but are less critical. Enable them after the must-haves are in place.</p>
<hr/>
<h3 id="vue-35-api-enforcement">Vue 3.5+ API Enforcement<a class="heading-link" aria-label="Link to section" href="#vue-35-api-enforcement"><span class="heading-link-icon">#</span></a></h3>
<p>Use the latest Vue 3.5 APIs for cleaner code.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/define-props-destructuring</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/prefer-use-template-ref</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  files: ['src/**/*.vue'],
  rules: {
    'vue/define-props-destructuring': 'error',
    'vue/prefer-use-template-ref': 'error'
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Before Vue 3.5</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> props</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> defineProps</span><span style="color:#89DDFF">&lt;</span><span style="color:#9ABDF5">{</span><span style="color:#73DACA"> count</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> buttonRef</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">HTMLButtonElement</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">props</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">count</span><span style="color:#9ABDF5">)</span><span style="color:#51597D;font-style:italic">  // Using props. prefix</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">button</span><span style="color:#BB9AF7"> ref</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">buttonRef</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Click</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
import { ref } from 'vue'

const props = defineProps<{ count: number }>()
const buttonRef = ref<HTMLButtonElement>()

console.log(props.count)  // Using props. prefix
</script>

<template>
  <button ref=&#34;buttonRef&#34;>Click</button>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Vue 3.5+</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useTemplateRef</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> count</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> defineProps</span><span style="color:#89DDFF">&lt;</span><span style="color:#9ABDF5">{</span><span style="color:#73DACA"> count</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> buttonRef</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useTemplateRef</span><span style="color:#89DDFF">&lt;</span><span style="color:#C0CAF5">HTMLButtonElement</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">button</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">count</span><span style="color:#9ABDF5">)</span><span style="color:#51597D;font-style:italic">  // Direct destructured access</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">button</span><span style="color:#BB9AF7"> ref</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">button</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Click</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
import { useTemplateRef } from 'vue'

const { count } = defineProps<{ count: number }>()
const buttonRef = useTemplateRef<HTMLButtonElement>('button')

console.log(count)  // Direct destructured access
</script>

<template>
  <button ref=&#34;button&#34;>Click</button>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://eslint.vuejs.org/rules/define-props-destructuring.html" rel="noopener noreferrer" target="_blank">eslint-plugin-vue: define-props-destructuring</a></p>
</blockquote>
<hr/>
<h3 id="explicit-component-apis">Explicit Component APIs<a class="heading-link" aria-label="Link to section" href="#explicit-component-apis"><span class="heading-link-icon">#</span></a></h3>
<p>Require <code>defineExpose</code> and <code>defineSlots</code> to make component interfaces explicit.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/require-expose</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">warn</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/require-explicit-slots</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">warn</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  files: ['src/**/*.vue'],
  rules: {
    'vue/require-expose': 'warn',
    'vue/require-explicit-slots': 'warn'
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> focus</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> { </span><span style="color:#51597D;font-style:italic">/* ... */</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">slot</span><span style="color:#FF5370"> /</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
function focus() { /* ... */ }
</script>

<template>
  <slot />
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#7AA2F7">defineSlots</span><span style="color:#89DDFF">&lt;</span><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#7AA2F7">  default</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> unknown</span></span>
<span class="line"><span style="color:#9ABDF5">}</span><span style="color:#89DDFF">&gt;</span><span style="color:#9ABDF5">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> focus</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> { </span><span style="color:#51597D;font-style:italic">/* ... */</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">defineExpose</span><span style="color:#9ABDF5">({</span><span style="color:#C0CAF5"> focus</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">slot</span><span style="color:#FF5370"> /</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<script setup lang=&#34;ts&#34;>
defineSlots<{
  default(): unknown
}>()

function focus() { /* ... */ }

defineExpose({ focus })
</script>

<template>
  <slot />
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://eslint.vuejs.org/rules/require-expose.html" rel="noopener noreferrer" target="_blank">eslint-plugin-vue: require-expose</a></p>
</blockquote>
<hr/>
<h3 id="template-depth-limit">Template Depth Limit<a class="heading-link" aria-label="Link to section" href="#template-depth-limit"><span class="heading-link-icon">#</span></a></h3>
<p>Deep template nesting is hard to read. Extract nested sections into components. This one matters a lot—it helps you avoid ending up with components that are 2000 lines long.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/max-template-depth</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">maxDepth</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 8</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vue/max-props</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">maxProps</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 6</span><span style="color:#9ABDF5"> }]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  files: ['src/**/*.vue'],
  rules: {
    'vue/max-template-depth': ['error', { maxDepth: 8 }],
    'vue/max-props': ['error', { maxProps: 6 }]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">          &lt;</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">            &lt;</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">              &lt;</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">                &lt;</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">                  &lt;</span><span style="color:#F7768E">span</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Too deep!</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">span</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">                &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">              &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">            &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">          &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">        &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<template>
  <div>
    <div>
      <div>
        <div>
          <div>
            <div>
              <div>
                <div>
                  <span>Too deep!</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#DE5971">Card</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#DE5971">CardHeader</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#DE5971">CardTitle</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Title</span><span style="color:#BA3C97">&lt;/</span><span style="color:#DE5971">CardTitle</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#DE5971">CardHeader</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#DE5971">CardContent</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">      &lt;</span><span style="color:#F7768E">span</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Content</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">span</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#DE5971">CardContent</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#DE5971">Card</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<template>
  <Card>
    <CardHeader>
      <CardTitle>Title</CardTitle>
    </CardHeader>
    <CardContent>
      <span>Content</span>
    </CardContent>
  </Card>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://eslint.vuejs.org/rules/max-template-depth.html" rel="noopener noreferrer" target="_blank">eslint-plugin-vue: max-template-depth</a></p>
</blockquote>
<hr/>
<h3 id="better-assertions-in-tests">Better Assertions in Tests<a class="heading-link" aria-label="Link to section" href="#better-assertions-in-tests"><span class="heading-link-icon">#</span></a></h3>
<p>Use specific matchers for clearer test failures.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/__tests__/*</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vitest/prefer-to-be</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vitest/prefer-to-have-length</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vitest/prefer-to-contain</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vitest/prefer-mock-promise-shorthand</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  files: ['src/**/__tests__/*'],
  rules: {
    'vitest/prefer-to-be': 'error',
    'vitest/prefer-to-have-length': 'error',
    'vitest/prefer-to-contain': 'error',
    'vitest/prefer-mock-promise-shorthand': 'error'
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7AA2F7">expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">value</span><span style="color:#BB9AF7"> ===</span><span style="color:#FF9E64"> null</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">true</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#7AA2F7">expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">arr</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">3</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#7AA2F7">expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">arr</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">includes</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">foo</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">))</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">true</span><span style="color:#9ABDF5">)</span></span></code><button type="button" class="copy" data-code="expect(value === null).toBe(true)
expect(arr.length).toBe(3)
expect(arr.includes('foo')).toBe(true)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7AA2F7">expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBeNull</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#7AA2F7">expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">arr</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toHaveLength</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">3</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#7AA2F7">expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">arr</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toContain</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">foo</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Also prefer mock shorthands</span></span>
<span class="line"><span style="color:#C0CAF5">vi</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">fn</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">mockResolvedValue</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">data</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#51597D;font-style:italic">  // Instead of mockReturnValue(Promise.resolve(&#39;data&#39;))</span></span></code><button type="button" class="copy" data-code="expect(value).toBeNull()
expect(arr).toHaveLength(3)
expect(arr).toContain('foo')

// Also prefer mock shorthands
vi.fn().mockResolvedValue('data')  // Instead of mockReturnValue(Promise.resolve('data'))" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://github.com/veritem/eslint-plugin-vitest" rel="noopener noreferrer" target="_blank">eslint-plugin-vitest</a></p>
</blockquote>
<hr/>
<h3 id="test-structure-rules">Test Structure Rules<a class="heading-link" aria-label="Link to section" href="#test-structure-rules"><span class="heading-link-icon">#</span></a></h3>
<p>Keep tests organized and readable.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/__tests__/*</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vitest/consistent-test-it</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">fn</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">it</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vitest/prefer-hooks-on-top</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vitest/prefer-hooks-in-order</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vitest/no-duplicate-hooks</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vitest/require-top-level-describe</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vitest/max-nested-describe</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">max</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 2</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">vitest/no-conditional-in-test</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">warn</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  files: ['src/**/__tests__/*'],
  rules: {
    'vitest/consistent-test-it': ['error', { fn: 'it' }],
    'vitest/prefer-hooks-on-top': 'error',
    'vitest/prefer-hooks-in-order': 'error',
    'vitest/no-duplicate-hooks': 'error',
    'vitest/require-top-level-describe': 'error',
    'vitest/max-nested-describe': ['error', { max: 2 }],
    'vitest/no-conditional-in-test': 'warn'
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7AA2F7">test</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">works</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span><span style="color:#51597D;font-style:italic">  // Inconsistent: test vs it</span></span>
<span class="line"><span style="color:#7AA2F7">it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">also works</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {})</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">feature</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">test 1</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  beforeEach</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})  </span><span style="color:#51597D;font-style:italic">// Hook after test!</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">nested</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">too deep</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">      describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">way too deep</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})  </span><span style="color:#51597D;font-style:italic">// 3 levels!</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="test('works', () => {})  // Inconsistent: test vs it
it('also works', () => {})

describe('feature', () => {
  it('test 1', () => {})

  beforeEach(() => {})  // Hook after test!

  describe('nested', () => {
    describe('too deep', () => {
      describe('way too deep', () => {})  // 3 levels!
    })
  })
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">feature</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  beforeEach</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})  </span><span style="color:#51597D;font-style:italic">// Hooks first, in order</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">does something</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">does another thing</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">edge cases</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">handles null</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {})</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// no-conditional-in-test prevents flaky tests</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Bad: if (data.length &gt; 0) { expect(data[0]).toBeDefined() }</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Good: expect(data).toHaveLength(3); expect(data[0]).toBeDefined()</span></span></code><button type="button" class="copy" data-code="describe('feature', () => {
  beforeEach(() => {})  // Hooks first, in order

  it('does something', () => {})
  it('does another thing', () => {})

  describe('edge cases', () => {
    it('handles null', () => {})
  })
})

// no-conditional-in-test prevents flaky tests
// Bad: if (data.length > 0) { expect(data[0]).toBeDefined() }
// Good: expect(data).toHaveLength(3); expect(data[0]).toBeDefined()" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://github.com/veritem/eslint-plugin-vitest" rel="noopener noreferrer" target="_blank">eslint-plugin-vitest</a></p>
</blockquote>
<hr/>
<h3 id="prefer-vitest-locators-in-tests">Prefer Vitest Locators in Tests<a class="heading-link" aria-label="Link to section" href="#prefer-vitest-locators-in-tests"><span class="heading-link-icon">#</span></a></h3>
<p>Use Vitest Browser locators instead of raw DOM queries.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/__tests__/**/*.{ts,spec.ts}</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">no-restricted-syntax</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">warn</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      selector</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">CallExpression[callee.property.name=/^querySelector(All)?$/]</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Prefer page.getByRole(), page.getByText(), or page.getByTestId() over querySelector. Vitest locators are more resilient to DOM changes.</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">    }]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
{
  files: ['src/**/__tests__/**/*.{ts,spec.ts}'],
  rules: {
    'no-restricted-syntax': ['warn', {
      selector: 'CallExpression[callee.property.name=/^querySelector(All)?$/]',
      message: 'Prefer page.getByRole(), page.getByText(), or page.getByTestId() over querySelector. Vitest locators are more resilient to DOM changes.'
    }]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> button</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> container</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">querySelector</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">.submit-btn</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">await</span><span style="color:#C0CAF5"> button</span><span style="color:#89DDFF">?.</span><span style="color:#7AA2F7">click</span><span style="color:#9ABDF5">()</span></span></code><button type="button" class="copy" data-code="const button = container.querySelector('.submit-btn')
await button?.click()" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> button</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> page</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getByRole</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">button</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Submit</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">await</span><span style="color:#C0CAF5"> button</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">click</span><span style="color:#9ABDF5">()</span></span></code><button type="button" class="copy" data-code="const button = page.getByRole('button', { name: 'Submit' })
await button.click()" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<blockquote>
<p><a href="https://vitest.dev/guide/browser/" rel="noopener noreferrer" target="_blank">Vitest Browser Mode</a></p>
</blockquote>
<hr/>
<h3 id="unicorn-rules">Unicorn Rules<a class="heading-link" aria-label="Link to section" href="#unicorn-rules"><span class="heading-link-icon">#</span></a></h3>
<p>The <code>eslint-plugin-unicorn</code> package catches common mistakes and enforces modern JavaScript patterns.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint.config.ts</span></span>
<span class="line"><span style="color:#C0CAF5">pluginUnicorn</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">configs</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">recommended</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">app/unicorn-overrides</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // === Enable non-recommended rules that add value ===</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">unicorn/better-regex</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">warn</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic">              // Simplify regexes: /[0-9]/ → /\d/</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">unicorn/custom-error-definition</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic">  // Correct Error subclassing</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">unicorn/no-unused-properties</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">warn</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic">      // Dead code detection</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">unicorn/consistent-destructuring</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">warn</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic">  // Use destructured vars consistently</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">    // === Disable rules that conflict with project conventions ===</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">unicorn/no-null</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">off</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic">                    // We use null for database values</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">unicorn/filename-case</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">off</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic">              // Vue uses PascalCase, tests use camelCase</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">unicorn/prevent-abbreviations</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">off</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic">      // props, e, Db are fine</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">unicorn/no-array-callback-reference</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">off</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic"> // arr.filter(isValid) is fine</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">unicorn/no-await-expression-member</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">off</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic"> // (await fetch()).json() is fine</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">unicorn/no-array-reduce</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">off</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic">            // reduce is useful for aggregations</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">unicorn/no-useless-undefined</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: </span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">off</span><span style="color:#89DDFF">&#39;</span><span style="color:#51597D;font-style:italic">        // mockResolvedValue(undefined) for TS</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint.config.ts
pluginUnicorn.configs.recommended,

{
  name: 'app/unicorn-overrides',
  rules: {
    // === Enable non-recommended rules that add value ===
    'unicorn/better-regex': 'warn',              // Simplify regexes: /[0-9]/ → /\d/
    'unicorn/custom-error-definition': 'error',  // Correct Error subclassing
    'unicorn/no-unused-properties': 'warn',      // Dead code detection
    'unicorn/consistent-destructuring': 'warn',  // Use destructured vars consistently

    // === Disable rules that conflict with project conventions ===
    'unicorn/no-null': 'off',                    // We use null for database values
    'unicorn/filename-case': 'off',              // Vue uses PascalCase, tests use camelCase
    'unicorn/prevent-abbreviations': 'off',      // props, e, Db are fine
    'unicorn/no-array-callback-reference': 'off', // arr.filter(isValid) is fine
    'unicorn/no-await-expression-member': 'off', // (await fetch()).json() is fine
    'unicorn/no-array-reduce': 'off',            // reduce is useful for aggregations
    'unicorn/no-useless-undefined': 'off'        // mockResolvedValue(undefined) for TS
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Examples:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// unicorn/better-regex</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Bad:  /[0-9]/</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Good: /\d/</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// unicorn/consistent-destructuring</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Bad:</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> foo</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> object</span></span>
<span class="line"><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">object</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">bar</span><span style="color:#9ABDF5">)</span><span style="color:#51597D;font-style:italic">  // Uses object.bar instead of destructuring</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Good:</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> foo</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> bar</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> object</span></span>
<span class="line"><span style="color:#C0CAF5">console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">log</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">bar</span><span style="color:#9ABDF5">)</span></span></code><button type="button" class="copy" data-code="// unicorn/better-regex
// Bad:  /[0-9]/
// Good: /\d/

// unicorn/consistent-destructuring
// Bad:
const { foo } = object
console.log(object.bar)  // Uses object.bar instead of destructuring

// Good:
const { foo, bar } = object
console.log(bar)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<blockquote>
<p><a href="https://github.com/sindresorhus/eslint-plugin-unicorn" rel="noopener noreferrer" target="_blank">eslint-plugin-unicorn</a></p>
</blockquote>
<hr/>
<h2 id="custom-local-rules">Custom Local Rules<a class="heading-link" aria-label="Link to section" href="#custom-local-rules"><span class="heading-link-icon">#</span></a></h2>
<p>Sometimes you need rules that don’t exist. Write them yourself.</p>
<h3 id="composable-must-use-vue">Composable Must Use Vue<a class="heading-link" aria-label="Link to section" href="#composable-must-use-vue"><span class="heading-link-icon">#</span></a></h3>
<p>A file named <code>use*.ts</code> should import from Vue. If it doesn’t, it’s a utility, not a composable. For more on writing proper composables, see <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/vueuse_composables_style_guide/" class="internal-link astro-3tyn5ojg"> Vue Composables Style Guide: Lessons from VueUse’s Codebase </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Vue Composables Style Guide: Lessons from VueUse&#39;s Codebase</span> <span class="preview-description astro-3tyn5ojg">A practical guide for writing production-quality Vue 3 composables, distilled from studying VueUse&#39;s patterns for SSR safety, cleanup, and TypeScript.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">typescript</span>  </span> <time class="preview-date astro-3tyn5ojg">Dec 13, 2025</time> </span> </span> </span>  <script>
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
</script>.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint-local-rules/composable-must-use-vue.ts</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> VALID_VUE_SOURCES</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Set</span><span style="color:#9ABDF5">([</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@vueuse/core</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue-router</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue-i18n</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">])</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> VALID_PATH_PATTERNS</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">/</span><span style="color:#BB9AF7">^</span><span style="color:#B4F9F8">@</span><span style="color:#C0CAF5">\/</span><span style="color:#B4F9F8">stores</span><span style="color:#C0CAF5">\/</span><span style="color:#89DDFF">/</span><span style="color:#9ABDF5">]</span><span style="color:#51597D;font-style:italic">  // Global state composables count too</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> isComposableFilename</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">filename</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#89DDFF"> /</span><span style="color:#BB9AF7">^</span><span style="color:#B4F9F8">use</span><span style="color:#E0AF68">[A-Z]</span><span style="color:#89DDFF">/</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">test</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">path</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">basename</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">filename</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">.ts</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">))</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> rule</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Rule</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">RuleModule</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  meta</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    messages</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">      notAComposable</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">File &quot;{{filename}}&quot; does not import from Vue. Rename it or add Vue imports.</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">  create</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">context</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#7AA2F7">isComposableFilename</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">context</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">filename</span><span style="color:#9ABDF5">)) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#9ABDF5"> {}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    let</span><span style="color:#BB9AF7"> hasVueImport</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> false</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">      ImportDeclaration</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">node</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#0DB9D7">VALID_VUE_SOURCES</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">has</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">node</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">source</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)) {</span></span>
<span class="line"><span style="color:#C0CAF5">          hasVueImport</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> true</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">Program:exit</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">node</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">hasVueImport</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">          context</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">report</span><span style="color:#9ABDF5">({ </span><span style="color:#C0CAF5">node</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> messageId</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">notAComposable</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint-local-rules/composable-must-use-vue.ts
const VALID_VUE_SOURCES = new Set(['vue', '@vueuse/core', 'vue-router', 'vue-i18n'])
const VALID_PATH_PATTERNS = [/^@\/stores\//]  // Global state composables count too

function isComposableFilename(filename: string): boolean {
  return /^use[A-Z]/.test(path.basename(filename, '.ts'))
}

const rule: Rule.RuleModule = {
  meta: {
    messages: {
      notAComposable: 'File &#34;{{filename}}&#34; does not import from Vue. Rename it or add Vue imports.'
    }
  },
  create(context) {
    if (!isComposableFilename(context.filename)) return {}

    let hasVueImport = false

    return {
      ImportDeclaration(node) {
        if (VALID_VUE_SOURCES.has(node.source.value)) {
          hasVueImport = true
        }
      },
      'Program:exit'(node) {
        if (!hasVueImport) {
          context.report({ node, messageId: 'notAComposable' })
        }
      }
    }
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// src/composables/useFormatter.ts</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useFormatter</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    formatDate</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">d</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Date</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#C0CAF5"> d</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toISOString</span><span style="color:#9ABDF5">()  </span><span style="color:#51597D;font-style:italic">// No Vue imports!</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// src/composables/useFormatter.ts
export function useFormatter() {
  return {
    formatDate: (d: Date) => d.toISOString()  // No Vue imports!
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// src/lib/formatter.ts (renamed)</span></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> formatDate</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">d</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Date</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> d</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toISOString</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">// OR add Vue reactivity:</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// src/composables/useFormatter.ts</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">computed</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useFormatter</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> locale</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">en-US</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> formatter</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> computed</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#89DDFF"> new</span><span style="color:#C0CAF5"> Intl</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">DateTimeFormat</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">locale</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">))</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">formatter</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> locale</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// src/lib/formatter.ts (renamed)
export function formatDate(d: Date) {
  return d.toISOString()
}

// OR add Vue reactivity:
// src/composables/useFormatter.ts
import { computed, ref } from 'vue'

export function useFormatter() {
  const locale = ref('en-US')
  const formatter = computed(() => new Intl.DateTimeFormat(locale.value))
  return { formatter, locale }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<hr/>
<h3 id="no-hardcoded-tailwind-colors">No Hardcoded Tailwind Colors<a class="heading-link" aria-label="Link to section" href="#no-hardcoded-tailwind-colors"><span class="heading-link-icon">#</span></a></h3>
<p>Hardcoded Tailwind colors (<code>bg-blue-500</code>) make theming impossible. Use semantic colors (<code>bg-primary</code>).</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint-local-rules/no-hardcoded-colors.ts</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Status colors (red, amber, yellow, green, emerald) are ALLOWED for semantic states</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> HARDCODED_COLORS</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">slate</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">gray</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">zinc</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">blue</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">purple</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">pink</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">orange</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">indigo</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">violet</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> COLOR_UTILITIES</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">bg</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">text</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">border</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">ring</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">fill</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">stroke</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> rule</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Rule</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">RuleModule</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  meta</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    messages</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">      noHardcodedColor</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Avoid &quot;{{color}}&quot;. Use semantic classes like bg-primary, text-foreground.</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">  create</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">context</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">      Literal</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">node</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#89DDFF">typeof</span><span style="color:#C0CAF5"> node</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#BB9AF7"> !==</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">string</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">        const</span><span style="color:#BB9AF7"> matches</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> findHardcodedColors</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">node</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7">        for</span><span style="color:#9ABDF5"> (</span><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> color</span><span style="color:#89DDFF"> of</span><span style="color:#C0CAF5"> matches</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">          context</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">report</span><span style="color:#9ABDF5">({ </span><span style="color:#C0CAF5">node</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> messageId</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">noHardcodedColor</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> data</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">color</span><span style="color:#9ABDF5"> } })</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint-local-rules/no-hardcoded-colors.ts
// Status colors (red, amber, yellow, green, emerald) are ALLOWED for semantic states
const HARDCODED_COLORS = ['slate', 'gray', 'zinc', 'blue', 'purple', 'pink', 'orange', 'indigo', 'violet']
const COLOR_UTILITIES = ['bg', 'text', 'border', 'ring', 'fill', 'stroke']

const rule: Rule.RuleModule = {
  meta: {
    messages: {
      noHardcodedColor: 'Avoid &#34;{{color}}&#34;. Use semantic classes like bg-primary, text-foreground.'
    }
  },
  create(context) {
    return {
      Literal(node) {
        if (typeof node.value !== 'string') return

        const matches = findHardcodedColors(node.value)
        for (const color of matches) {
          context.report({ node, messageId: 'noHardcodedColor', data: { color } })
        }
      }
    }
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">button</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">bg-blue-500 text-white</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Click</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<template>
  <button class=&#34;bg-blue-500 text-white&#34;>Click</button>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">button</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">bg-primary text-primary-foreground</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97">&gt;</span><span style="color:#9AA5CE">Click</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">button</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<template>
  <button class=&#34;bg-primary text-primary-foreground&#34;>Click</button>
</template>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> Note </p> <div class="alert-content astro-7kdbuayl"> <p>Status colors (<code>red</code>, <code>amber</code>, <code>yellow</code>, <code>green</code>, <code>emerald</code>) are intentionally allowed for error/warning/success states. Only use these for semantic status indication, not general styling.</p> </div> </div> 
<hr/>
<h3 id="no-let-in-describe-blocks">No let in describe Blocks<a class="heading-link" aria-label="Link to section" href="#no-let-in-describe-blocks"><span class="heading-link-icon">#</span></a></h3>
<p>Mutable variables in test describe blocks create hidden state. Use setup functions instead.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint-local-rules/no-let-in-describe.ts</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> rule</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Rule</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">RuleModule</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  meta</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    messages</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">      noLetInDescribe</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Avoid `let` in describe blocks. Use setup functions instead.</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">  create</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">context</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    let</span><span style="color:#BB9AF7"> describeDepth</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 0</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">      CallExpression</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">node</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#7AA2F7">isDescribeCall</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">node</span><span style="color:#9ABDF5">)) </span><span style="color:#C0CAF5">describeDepth</span><span style="color:#89DDFF">++</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">CallExpression:exit</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">node</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#7AA2F7">isDescribeCall</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">node</span><span style="color:#9ABDF5">)) </span><span style="color:#C0CAF5">describeDepth</span><span style="color:#89DDFF">--</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">      VariableDeclaration</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">node</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">describeDepth</span><span style="color:#BB9AF7"> &gt;</span><span style="color:#FF9E64"> 0</span><span style="color:#BB9AF7"> &amp;&amp;</span><span style="color:#C0CAF5"> node</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">kind</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">let</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">          context</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">report</span><span style="color:#9ABDF5">({ </span><span style="color:#C0CAF5">node</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> messageId</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">noLetInDescribe</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint-local-rules/no-let-in-describe.ts
const rule: Rule.RuleModule = {
  meta: {
    messages: {
      noLetInDescribe: 'Avoid `let` in describe blocks. Use setup functions instead.'
    }
  },
  create(context) {
    let describeDepth = 0

    return {
      CallExpression(node) {
        if (isDescribeCall(node)) describeDepth++
      },
      'CallExpression:exit'(node) {
        if (isDescribeCall(node)) describeDepth--
      },
      VariableDeclaration(node) {
        if (describeDepth > 0 &#38;&#38; node.kind === 'let') {
          context.report({ node, messageId: 'noLetInDescribe' })
        }
      }
    }
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Login</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> user</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> User</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  beforeEach</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    user</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> createUser</span><span style="color:#9ABDF5">()  </span><span style="color:#51597D;font-style:italic">// Hidden mutation!</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">works</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">name</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">test</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="describe('Login', () => {
  let user: User

  beforeEach(() => {
    user = createUser()  // Hidden mutation!
  })

  it('works', () => {
    expect(user.name).toBe('test')
  })
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7AA2F7">describe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Login</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  function</span><span style="color:#7AA2F7"> setup</span><span style="color:#9ABDF5">() {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">user</span><span style="color:#89DDFF">:</span><span style="color:#7AA2F7"> createUser</span><span style="color:#9ABDF5">() }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  it</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">works</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=&gt;</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> user</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> setup</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#7AA2F7">    expect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">name</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">toBe</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">test</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span></span>
<span class="line"><span style="color:#9ABDF5">})</span></span></code><button type="button" class="copy" data-code="describe('Login', () => {
  function setup() {
    return { user: createUser() }
  }

  it('works', () => {
    const { user } = setup()
    expect(user.name).toBe('test')
  })
})" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<hr/>
<h3 id="extract-complex-conditions">Extract Complex Conditions<a class="heading-link" aria-label="Link to section" href="#extract-complex-conditions"><span class="heading-link-icon">#</span></a></h3>
<p>Complex boolean expressions should have names. Extract them into variables.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint-local-rules/extract-condition-variable.ts</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> OPERATOR_THRESHOLD</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 2</span><span style="color:#51597D;font-style:italic">  // Conditions with 2+ logical operators need extraction</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> rule</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Rule</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">RuleModule</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  meta</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    messages</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">      extractCondition</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Complex condition should be extracted into a named const.</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">  create</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">context</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">      IfStatement</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">node</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">        // Skip patterns that TypeScript needs inline for narrowing</span></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#7AA2F7">isEarlyExitGuard</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">node</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">consequent</span><span style="color:#9ABDF5">)) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#51597D;font-style:italic">  // if (!x) return</span></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#7AA2F7">hasOptionalChaining</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">node</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">test</span><span style="color:#9ABDF5">)) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#51597D;font-style:italic">      // if (user?.name)</span></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#7AA2F7">hasTruthyNarrowingPattern</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">node</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">test</span><span style="color:#9ABDF5">)) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#51597D;font-style:italic"> // if (arr &amp;&amp; arr[0])</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#7AA2F7">countOperators</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">node</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">test</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">&gt;=</span><span style="color:#FF9E64"> OPERATOR_THRESHOLD</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">          context</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">report</span><span style="color:#9ABDF5">({ </span><span style="color:#73DACA">node</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> node</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">test</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> messageId</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">extractCondition</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint-local-rules/extract-condition-variable.ts
const OPERATOR_THRESHOLD = 2  // Conditions with 2+ logical operators need extraction

const rule: Rule.RuleModule = {
  meta: {
    messages: {
      extractCondition: 'Complex condition should be extracted into a named const.'
    }
  },
  create(context) {
    return {
      IfStatement(node) {
        // Skip patterns that TypeScript needs inline for narrowing
        if (isEarlyExitGuard(node.consequent)) return  // if (!x) return
        if (hasOptionalChaining(node.test)) return      // if (user?.name)
        if (hasTruthyNarrowingPattern(node.test)) return // if (arr &#38;&#38; arr[0])

        if (countOperators(node.test) >= OPERATOR_THRESHOLD) {
          context.report({ node: node.test, messageId: 'extractCondition' })
        }
      }
    }
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Smart Exceptions:</strong> The rule skips several patterns that TypeScript needs inline for type narrowing:</p>
<ul>
<li>Early exit guards: <code>if (!user) return</code></li>
<li>Optional chaining: <code>if (user?.name)</code></li>
<li>Truthy narrowing: <code>if (arr &amp;&amp; arr[0])</code></li>
</ul>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#BB9AF7">if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">isActive</span><span style="color:#BB9AF7"> &amp;&amp;</span><span style="color:#C0CAF5"> user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">role</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">admin</span><span style="color:#89DDFF">&#39;</span><span style="color:#BB9AF7"> &amp;&amp;</span><span style="color:#BB9AF7"> !</span><span style="color:#C0CAF5">user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">isBanned</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  showAdminPanel</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="if (user.isActive &#38;&#38; user.role === 'admin' &#38;&#38; !user.isBanned) {
  showAdminPanel()
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> canAccessAdminPanel</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">isActive</span><span style="color:#BB9AF7"> &amp;&amp;</span><span style="color:#C0CAF5"> user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">role</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">admin</span><span style="color:#89DDFF">&#39;</span><span style="color:#BB9AF7"> &amp;&amp;</span><span style="color:#BB9AF7"> !</span><span style="color:#C0CAF5">user</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">isBanned</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">canAccessAdminPanel</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  showAdminPanel</span><span style="color:#9ABDF5">()</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="const canAccessAdminPanel = user.isActive &#38;&#38; user.role === 'admin' &#38;&#38; !user.isBanned

if (canAccessAdminPanel) {
  showAdminPanel()
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<hr/>
<h3 id="repository-trycatch-wrapper">Repository tryCatch Wrapper<a class="heading-link" aria-label="Link to section" href="#repository-trycatch-wrapper"><span class="heading-link-icon">#</span></a></h3>
<p>Database calls can fail. Enforce wrapping them in <code>tryCatch()</code>.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#51597D;font-style:italic">// eslint-local-rules/repository-trycatch.ts</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">// Matches pattern: get*Repository().method()</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> REPO_PATTERN</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> /</span><span style="color:#BB9AF7">^</span><span style="color:#B4F9F8">get</span><span style="color:#BB9AF7">\w</span><span style="color:#89DDFF">+</span><span style="color:#B4F9F8">Repository</span><span style="color:#BB9AF7">$</span><span style="color:#89DDFF">/</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> rule</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Rule</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">RuleModule</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  meta</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    messages</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">      missingTryCatch</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Repository calls must be wrapped with tryCatch().</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">  create</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">context</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">      AwaitExpression</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">node</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#7AA2F7">isRepositoryMethodCall</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">node</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">argument</span><span style="color:#9ABDF5">)) </span><span style="color:#BB9AF7;font-style:italic">return</span></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#7AA2F7">isWrappedInTryCatch</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">context</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> node</span><span style="color:#9ABDF5">)) </span><span style="color:#BB9AF7;font-style:italic">return</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">        context</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">report</span><span style="color:#9ABDF5">({ </span><span style="color:#C0CAF5">node</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> messageId</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">missingTryCatch</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> })</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// eslint-local-rules/repository-trycatch.ts
// Matches pattern: get*Repository().method()
const REPO_PATTERN = /^get\w+Repository$/

const rule: Rule.RuleModule = {
  meta: {
    messages: {
      missingTryCatch: 'Repository calls must be wrapped with tryCatch().'
    }
  },
  create(context) {
    return {
      AwaitExpression(node) {
        if (!isRepositoryMethodCall(node.argument)) return
        if (isWrappedInTryCatch(context, node)) return

        context.report({ node, messageId: 'missingTryCatch' })
      }
    }
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="code-comparison my-6 grid grid-cols-1 gap-4 md:grid-cols-2 astro-qdboqi2a"> <div class="comparison-card comparison-card--bad overflow-hidden rounded-lg border-l-[3px] border-red-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-red-500/30 bg-red-500/20 px-4 py-2 text-red-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✗</span> <span class="text-sm font-medium astro-qdboqi2a">Bad</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> workouts</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> getWorkoutRepository</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">findAll</span><span style="color:#9ABDF5">()</span><span style="color:#51597D;font-style:italic">  // Might throw!</span></span></code><button type="button" class="copy" data-code="const workouts = await getWorkoutRepository().findAll()  // Might throw!" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> <div class="comparison-card comparison-card--good overflow-hidden rounded-lg border-l-[3px] border-emerald-500 bg-skin-card astro-qdboqi2a"> <div class="flex items-center gap-2 border-b border-emerald-500/30 bg-emerald-500/20 px-4 py-2 text-emerald-400 astro-qdboqi2a"> <span class="text-sm astro-qdboqi2a">✓</span> <span class="text-sm font-medium astro-qdboqi2a">Good</span> </div> <div class="comparison-code astro-qdboqi2a"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> [</span><span style="color:#BB9AF7">error</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> workouts</span><span style="color:#89DDFF">]</span><span style="color:#89DDFF"> =</span><span style="color:#BB9AF7;font-style:italic"> await</span><span style="color:#7AA2F7"> tryCatch</span><span style="color:#9ABDF5">(</span><span style="color:#7AA2F7">getWorkoutRepository</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">findAll</span><span style="color:#9ABDF5">())</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">error</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  showError</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">Failed to load workouts</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="const [error, workouts] = await tryCatch(getWorkoutRepository().findAll())

if (error) {
  showError('Failed to load workouts')
  return
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </div> </div> 
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> Note </p> <div class="alert-content astro-7kdbuayl"> <p>This rule matches the <code>get*Repository()</code> pattern. Ensure your repository factory functions follow this naming convention.</p> </div> </div> 
<hr/>
<h2 id="the-full-config">The Full Config<a class="heading-link" aria-label="Link to section" href="#the-full-config"><span class="heading-link-icon">#</span></a></h2>
<details class="collapsible astro-kncz7yy6"> <summary class="collapsible-summary astro-kncz7yy6"> <span class="collapsible-icon astro-kncz7yy6"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="astro-kncz7yy6"> <polyline points="9 18 15 12 9 6" class="astro-kncz7yy6"></polyline> </svg> </span> Complete eslint.config.ts example </summary> <div class="collapsible-content astro-kncz7yy6"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> pluginEslintComments</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@eslint-community/eslint-plugin-eslint-comments</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> pluginVueI18n</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@intlify/eslint-plugin-vue-i18n</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> pluginVitest</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@vitest/eslint-plugin</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> skipFormatting</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@vue/eslint-config-prettier/skip-formatting</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">defineConfigWithVueTs</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> vueTsConfigs</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@vue/eslint-config-typescript</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> pluginImportX</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">eslint-plugin-import-x</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> pluginOxlint</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">eslint-plugin-oxlint</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">configs</span><span style="color:#89DDFF"> as</span><span style="color:#0DB9D7"> pnpmConfigs</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">eslint-plugin-pnpm</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> pluginUnicorn</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">eslint-plugin-unicorn</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> pluginVue</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">eslint-plugin-vue</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> localRules</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./eslint-local-rules</span><span style="color:#89DDFF">&#39;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#7DCFFF"> default</span><span style="color:#7AA2F7"> defineConfigWithVueTs</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span><span style="color:#73DACA"> ignores</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">**/dist/**</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">**/coverage/**</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">**/node_modules/**</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">  pluginVue</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">configs</span><span style="color:#9ABDF5">[</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">flat/essential</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">  vueTsConfigs</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">recommended</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#C0CAF5">  pluginUnicorn</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">configs</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">recommended</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Vue component rules</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vue/multi-word-component-names</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#41A6B5"> ignores</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">App</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Layout</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vue/component-name-in-template-casing</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">PascalCase</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vue/prop-name-casing</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">camelCase</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vue/custom-event-name-casing</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">kebab-case</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vue/no-unused-properties</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#41A6B5"> groups</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">props</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">data</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">computed</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">methods</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vue/no-unused-refs</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vue/define-props-destructuring</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vue/prefer-use-template-ref</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vue/max-template-depth</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#41A6B5"> maxDepth</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 8</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // TypeScript style guide</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.{ts,vue}</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">complexity</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">warn</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#41A6B5"> max</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 10</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">no-nested-ternary</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">@typescript-eslint/consistent-type-assertions</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#41A6B5"> assertionStyle</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">never</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">no-restricted-syntax</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        {</span><span style="color:#41A6B5"> selector</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">TSEnumDeclaration</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#41A6B5"> message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Use literal unions instead of enums.</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        {</span><span style="color:#41A6B5"> selector</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">IfStatement &gt; :not(IfStatement).alternate</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#41A6B5"> message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Avoid else. Use early returns.</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        {</span><span style="color:#41A6B5"> selector</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">TryStatement</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#41A6B5"> message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Use tryCatch() instead of try/catch.</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      ]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Feature boundaries</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.{ts,vue}</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">import-x</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> pluginImportX</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">import-x/no-restricted-paths</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">        zones</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span><span style="color:#41A6B5"> target</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features/workout</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#41A6B5"> from</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#41A6B5"> except</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">./workout</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">          // ... other features</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span><span style="color:#41A6B5"> target</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/features</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#41A6B5"> from</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">./src/views</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic">  // Unidirectional flow</span></span>
<span class="line"><span style="color:#9ABDF5">        ]</span></span>
<span class="line"><span style="color:#9ABDF5">      }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // i18n rules</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@intlify/vue-i18n</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> pluginVueI18n</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">@intlify/vue-i18n/no-raw-text</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#51597D;font-style:italic"> /* config */</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Prevent disabling i18n rules</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@eslint-community/eslint-comments</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> pluginEslintComments</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">@eslint-community/eslint-comments/no-restricted-disable</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@intlify/vue-i18n/*</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Vitest rules</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/__tests__/*</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#F7768E;font-weight:bold">    ...</span><span style="color:#C0CAF5">pluginVitest</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">configs</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">recommended</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vitest/consistent-test-it</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#41A6B5"> fn</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">it</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vitest/prefer-hooks-on-top</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vitest/prefer-hooks-in-order</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vitest/no-duplicate-hooks</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vitest/max-nested-describe</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span><span style="color:#41A6B5"> max</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 2</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">vitest/no-conditional-in-test</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">warn</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Enforce test helpers</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/__tests__/**/*.{ts,spec.ts}</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">no-restricted-imports</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">        paths</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span><span style="color:#41A6B5"> name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">vitest-browser-vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#41A6B5"> importNames</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">render</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span><span style="color:#41A6B5"> message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Use createTestApp()</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span><span style="color:#41A6B5"> name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">@vue/test-utils</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#41A6B5"> importNames</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">mount</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span><span style="color:#41A6B5"> message</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">Use createTestApp()</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        ]</span></span>
<span class="line"><span style="color:#9ABDF5">      }]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Local rules</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span></span>
<span class="line"><span style="color:#73DACA">    files</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">src/**/*.{ts,vue}</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> local</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> localRules</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">local/no-hardcoded-colors</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">local/composable-must-use-vue</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">local/repository-trycatch</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">local/extract-condition-variable</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">      &#39;</span><span style="color:#9ECE6A">local/no-let-in-describe</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Disable rules handled by Oxlint</span></span>
<span class="line"><span style="color:#F7768E;font-weight:bold">  ...</span><span style="color:#C0CAF5">pluginOxlint</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">buildFromOxlintConfigFile</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">./.oxlintrc.json</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // pnpm catalog enforcement</span></span>
<span class="line"><span style="color:#F7768E;font-weight:bold">  ...</span><span style="color:#C0CAF5">pnpmConfigs</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">recommended</span><span style="color:#89DDFF">,</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">  skipFormatting</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">)</span></span></code><button type="button" class="copy" data-code="import pluginEslintComments from '@eslint-community/eslint-plugin-eslint-comments'
import pluginVueI18n from '@intlify/eslint-plugin-vue-i18n'
import pluginVitest from '@vitest/eslint-plugin'
import skipFormatting from '@vue/eslint-config-prettier/skip-formatting'
import { defineConfigWithVueTs, vueTsConfigs } from '@vue/eslint-config-typescript'
import pluginImportX from 'eslint-plugin-import-x'
import pluginOxlint from 'eslint-plugin-oxlint'
import { configs as pnpmConfigs } from 'eslint-plugin-pnpm'
import pluginUnicorn from 'eslint-plugin-unicorn'
import pluginVue from 'eslint-plugin-vue'
import localRules from './eslint-local-rules'

export default defineConfigWithVueTs(
  { ignores: ['**/dist/**', '**/coverage/**', '**/node_modules/**'] },

  pluginVue.configs['flat/essential'],
  vueTsConfigs.recommended,
  pluginUnicorn.configs.recommended,

  // Vue component rules
  {
    files: ['src/**/*.vue'],
    rules: {
      'vue/multi-word-component-names': ['error', { ignores: ['App', 'Layout'] }],
      'vue/component-name-in-template-casing': ['error', 'PascalCase'],
      'vue/prop-name-casing': ['error', 'camelCase'],
      'vue/custom-event-name-casing': ['error', 'kebab-case'],
      'vue/no-unused-properties': ['error', { groups: ['props', 'data', 'computed', 'methods'] }],
      'vue/no-unused-refs': 'error',
      'vue/define-props-destructuring': 'error',
      'vue/prefer-use-template-ref': 'error',
      'vue/max-template-depth': ['error', { maxDepth: 8 }],
    },
  },

  // TypeScript style guide
  {
    files: ['src/**/*.{ts,vue}'],
    rules: {
      'complexity': ['warn', { max: 10 }],
      'no-nested-ternary': 'error',
      '@typescript-eslint/consistent-type-assertions': ['error', { assertionStyle: 'never' }],
      'no-restricted-syntax': ['error',
        { selector: 'TSEnumDeclaration', message: 'Use literal unions instead of enums.' },
        { selector: 'IfStatement > :not(IfStatement).alternate', message: 'Avoid else. Use early returns.' },
        { selector: 'TryStatement', message: 'Use tryCatch() instead of try/catch.' },
      ],
    },
  },

  // Feature boundaries
  {
    files: ['src/**/*.{ts,vue}'],
    plugins: { 'import-x': pluginImportX },
    rules: {
      'import-x/no-restricted-paths': ['error', {
        zones: [
          { target: './src/features/workout', from: './src/features', except: ['./workout'] },
          // ... other features
          { target: './src/features', from: './src/views' },  // Unidirectional flow
        ]
      }],
    },
  },

  // i18n rules
  {
    files: ['src/**/*.vue'],
    plugins: { '@intlify/vue-i18n': pluginVueI18n },
    rules: {
      '@intlify/vue-i18n/no-raw-text': ['error', { /* config */ }],
    },
  },

  // Prevent disabling i18n rules
  {
    files: ['src/**/*.vue'],
    plugins: { '@eslint-community/eslint-comments': pluginEslintComments },
    rules: {
      '@eslint-community/eslint-comments/no-restricted-disable': ['error', '@intlify/vue-i18n/*'],
    },
  },

  // Vitest rules
  {
    files: ['src/**/__tests__/*'],
    ...pluginVitest.configs.recommended,
    rules: {
      'vitest/consistent-test-it': ['error', { fn: 'it' }],
      'vitest/prefer-hooks-on-top': 'error',
      'vitest/prefer-hooks-in-order': 'error',
      'vitest/no-duplicate-hooks': 'error',
      'vitest/max-nested-describe': ['error', { max: 2 }],
      'vitest/no-conditional-in-test': 'warn',
    },
  },

  // Enforce test helpers
  {
    files: ['src/**/__tests__/**/*.{ts,spec.ts}'],
    rules: {
      'no-restricted-imports': ['error', {
        paths: [
          { name: 'vitest-browser-vue', importNames: ['render'], message: 'Use createTestApp()' },
          { name: '@vue/test-utils', importNames: ['mount'], message: 'Use createTestApp()' },
        ]
      }],
    },
  },

  // Local rules
  {
    files: ['src/**/*.{ts,vue}'],
    plugins: { local: localRules },
    rules: {
      'local/no-hardcoded-colors': 'error',
      'local/composable-must-use-vue': 'error',
      'local/repository-trycatch': 'error',
      'local/extract-condition-variable': 'error',
      'local/no-let-in-describe': 'error',
    },
  },

  // Disable rules handled by Oxlint
  ...pluginOxlint.buildFromOxlintConfigFile('./.oxlintrc.json'),

  // pnpm catalog enforcement
  ...pnpmConfigs.recommended,

  skipFormatting,
)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </details>  
<hr/>
<h2 id="summary">Summary<a class="heading-link" aria-label="Link to section" href="#summary"><span class="heading-link-icon">#</span></a></h2>



















































































































<table><thead><tr><th>Category</th><th>Rule</th><th>Purpose</th></tr></thead><tbody><tr><td data-label="Category"><strong>Must Have</strong></td><td data-label="Rule"><code>complexity</code></td><td data-label="Purpose">Limit function complexity</td></tr><tr><td data-label="Category"><strong>Must Have</strong></td><td data-label="Rule"><code>no-nested-ternary</code></td><td data-label="Purpose">Readable conditionals</td></tr><tr><td data-label="Category"><strong>Must Have</strong></td><td data-label="Rule"><code>consistent-type-assertions</code></td><td data-label="Purpose">No unsafe <code>as</code> casts</td></tr><tr><td data-label="Category"><strong>Must Have</strong></td><td data-label="Rule"><code>no-restricted-syntax</code> (enums)</td><td data-label="Purpose">Use unions over enums</td></tr><tr><td data-label="Category"><strong>Must Have</strong></td><td data-label="Rule"><code>no-restricted-syntax</code> (else)</td><td data-label="Purpose">Prefer early returns</td></tr><tr><td data-label="Category"><strong>Must Have</strong></td><td data-label="Rule"><code>no-restricted-syntax</code> (routes)</td><td data-label="Purpose">Use named routes</td></tr><tr><td data-label="Category"><strong>Must Have</strong></td><td data-label="Rule"><code>import-x/no-restricted-paths</code></td><td data-label="Purpose">Feature isolation</td></tr><tr><td data-label="Category"><strong>Must Have</strong></td><td data-label="Rule"><code>vue/no-unused-*</code></td><td data-label="Purpose">Dead code detection</td></tr><tr><td data-label="Category"><strong>Must Have</strong></td><td data-label="Rule"><code>@intlify/vue-i18n/no-raw-text</code></td><td data-label="Purpose">i18n compliance</td></tr><tr><td data-label="Category"><strong>Must Have</strong></td><td data-label="Rule"><code>no-restricted-disable</code></td><td data-label="Purpose">No bypassing i18n</td></tr><tr><td data-label="Category"><strong>Must Have</strong></td><td data-label="Rule"><code>no-restricted-imports</code></td><td data-label="Purpose">Enforce test helpers</td></tr><tr><td data-label="Category"><strong>Nice to Have</strong></td><td data-label="Rule"><code>vue/define-props-destructuring</code></td><td data-label="Purpose">Vue 3.5 patterns</td></tr><tr><td data-label="Category"><strong>Nice to Have</strong></td><td data-label="Rule"><code>vue/max-template-depth</code></td><td data-label="Purpose">Template readability</td></tr><tr><td data-label="Category"><strong>Nice to Have</strong></td><td data-label="Rule"><code>vitest/*</code></td><td data-label="Purpose">Test consistency</td></tr><tr><td data-label="Category"><strong>Nice to Have</strong></td><td data-label="Rule"><code>unicorn/*</code></td><td data-label="Purpose">Modern JavaScript</td></tr><tr><td data-label="Category"><strong>Nice to Have</strong></td><td data-label="Rule"><code>pnpm/recommended</code></td><td data-label="Purpose">Catalog enforcement</td></tr><tr><td data-label="Category"><strong>Custom</strong></td><td data-label="Rule"><code>composable-must-use-vue</code></td><td data-label="Purpose">Composable validation</td></tr><tr><td data-label="Category"><strong>Custom</strong></td><td data-label="Rule"><code>no-hardcoded-colors</code></td><td data-label="Purpose">Theming support</td></tr><tr><td data-label="Category"><strong>Custom</strong></td><td data-label="Rule"><code>no-let-in-describe</code></td><td data-label="Purpose">Clean tests</td></tr><tr><td data-label="Category"><strong>Custom</strong></td><td data-label="Rule"><code>extract-condition-variable</code></td><td data-label="Purpose">Readable conditions</td></tr><tr><td data-label="Category"><strong>Custom</strong></td><td data-label="Rule"><code>repository-trycatch</code></td><td data-label="Purpose">Error handling</td></tr></tbody></table>
<p>Start with the must-haves. Add nice-to-haves when you’re ready. Write custom rules when nothing else fits.</p>
<p>The combination of Oxlint for speed and ESLint for coverage gives you fast feedback during development and comprehensive checks in CI.</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_opinionated-eslint-setup-vue-projects" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="opinionated-eslint-setup-vue-projects" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
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
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">typescript</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/tooling/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">tooling</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/architecture/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-5"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">architecture</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/opinionated-eslint-setup-vue-projects/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/opinionated-eslint-setup-vue-projects/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/opinionated-eslint-setup-vue-projects/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/opinionated-eslint-setup-vue-projects/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/opinionated-eslint-setup-vue-projects/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/opinionated-eslint-setup-vue-projects/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/opinionated-eslint-setup-vue-projects/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on LinkedIn</span> </a> </div> </div>  </div> <section id="comments-section" class="giscus-container"></section> <script type="module">function a(){const e=document.getElementById("comments-section");if(!e)return;e.querySelector(".giscus, iframe")&&(e.innerHTML="");const t=document.createElement("script");t.src="https://giscus.app/client.js",t.setAttribute("data-repo","alexanderop/blog-comments"),t.setAttribute("data-repo-id","R_kgDON-LviQ"),t.setAttribute("data-category","Q&A"),t.setAttribute("data-category-id","DIC_kwDON-Lvic4CnPll"),t.setAttribute("data-mapping","url"),t.setAttribute("data-strict","0"),t.setAttribute("data-reactions-enabled","1"),t.setAttribute("data-emit-metadata","0"),t.setAttribute("data-input-position","bottom"),t.setAttribute("data-theme","dark"),t.setAttribute("data-lang","en"),t.setAttribute("data-loading","lazy"),t.setAttribute("crossorigin","anonymous"),t.async=!0,e.appendChild(t)}a();document.addEventListener("astro:page-load",a);</script>  </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "opinionated-eslint-setup-vue-projects";

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
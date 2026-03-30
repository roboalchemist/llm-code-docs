# Source: https://alexop.dev/posts/how-to-write-clean-vue-components

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/how-to-write-clean-vue-components/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>How to Write Clean Vue Components | alexop.dev</title><meta name="title" content="How to Write Clean Vue Components | alexop.dev"><meta name="description" content="There are many ways to write better Vue components. One of my favorite ways is to separate business logic into pure functions."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="How to Write Clean Vue Components | alexop.dev"><meta property="og:description" content="There are many ways to write better Vue components. One of my favorite ways is to separate business logic into pure functions."><meta property="og:url" content="https://alexop.dev/posts/how-to-write-clean-vue-components/"><meta property="og:image" content="https://alexop.dev/posts/how-to-write-clean-vue-components/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2024-01-28T15:22:00.000Z"><meta property="article:modified_time" content="2024-01-28T15:22:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/how-to-write-clean-vue-components/"><meta property="twitter:title" content="How to Write Clean Vue Components | alexop.dev"><meta property="twitter:description" content="There are many ways to write better Vue components. One of my favorite ways is to separate business logic into pure functions."><meta property="twitter:image" content="https://alexop.dev/posts/how-to-write-clean-vue-components/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"How to Write Clean Vue Components | alexop.dev","description":"There are many ways to write better Vue components. One of my favorite ways is to separate business logic into pure functions.","image":"https://alexop.dev/posts/how-to-write-clean-vue-components/index.png","datePublished":"2024-01-28T15:22:00.000Z","dateModified":"2024-01-28T15:22:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: how-to-write-clean-vue-components; }@layer astro { ::view-transition-old(how-to-write-clean-vue-components) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(how-to-write-clean-vue-components) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(how-to-write-clean-vue-components) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(how-to-write-clean-vue-components) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: vue; }@layer astro { ::view-transition-old(vue) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: architecture; }@layer astro { ::view-transition-old(architecture) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">How to Write Clean Vue Components</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2024-01-28T15:22:00.000Z">Jan 28, 2024</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="1LUrJS" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;How to Write Clean Vue Components&quot;],&quot;content&quot;:[0,&quot;## Table of Contents\n\n## Introduction\n\nWriting code that&#39;s both easy to test and easy to read can be a challenge, with Vue components. In this blog post, I&#39;m going to share a design idea that will make your Vue components better. This method won&#39;t speed up your code, but it will make it simpler to test and understand. Think of it as a big-picture way to improve your Vue coding style. It&#39;s going to make your life easier when you need to fix or update your components.\n\nWhether you&#39;re new to Vue or have been using it for some time, this tip will help you make your Vue components cleaner and more straightforward.\n\n---\n\n## Understanding Vue Components\n\nA Vue component is like a reusable puzzle piece in your app. It has three main parts:\n\n1. **View**: This is the template section where you design the user interface.\n2. **Reactivity**: Here, Vue&#39;s features like `ref` make the interface interactive.\n3. **Business Logic**: This is where you process data or manage user actions.\n\n![Architecture](../../assets/images/how-to-write-clean-vue-components/architecture.png)\n\n---\n\n## Case Study: `snakeGame.vue`\n\nLet&#39;s look at a common Vue component, `snakeGame.vue`. It mixes the view, reactivity, and business logic, which can make it complex and hard to work with.\n\n### Code Sample: Traditional Approach\n\n```vue\n&lt;template&gt;\n  &lt;div class=\&quot;game-container\&quot;&gt;\n    &lt;canvas ref=\&quot;canvas\&quot; width=\&quot;400\&quot; height=\&quot;400\&quot;&gt;&lt;/canvas&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { onMounted, onUnmounted, ref } from \&quot;vue\&quot;;\n\nconst canvas = ref&lt;HTMLCanvasElement | null&gt;(null);\nconst ctx = ref&lt;CanvasRenderingContext2D | null&gt;(null);\nlet snake = [{ x: 200, y: 200 }];\nlet direction = { x: 0, y: 0 };\nlet lastDirection = { x: 0, y: 0 };\nlet food = { x: 0, y: 0 };\nconst gridSize = 20;\nlet gameInterval: number | null = null;\n\nonMounted(() =&gt; {\n  if (canvas.value) {\n    ctx.value = canvas.value.getContext(\&quot;2d\&quot;);\n    resetFoodPosition();\n    gameInterval = window.setInterval(gameLoop, 100);\n  }\n  window.addEventListener(\&quot;keydown\&quot;, handleKeydown);\n});\n\nonUnmounted(() =&gt; {\n  if (gameInterval !== null) {\n    window.clearInterval(gameInterval);\n  }\n  window.removeEventListener(\&quot;keydown\&quot;, handleKeydown);\n});\n\nfunction handleKeydown(e: KeyboardEvent) {\n  e.preventDefault();\n  switch (e.key) {\n    case \&quot;ArrowUp\&quot;:\n      if (lastDirection.y !== 0) break;\n      direction = { x: 0, y: -gridSize };\n      break;\n    case \&quot;ArrowDown\&quot;:\n      if (lastDirection.y !== 0) break;\n      direction = { x: 0, y: gridSize };\n      break;\n    case \&quot;ArrowLeft\&quot;:\n      if (lastDirection.x !== 0) break;\n      direction = { x: -gridSize, y: 0 };\n      break;\n    case \&quot;ArrowRight\&quot;:\n      if (lastDirection.x !== 0) break;\n      direction = { x: gridSize, y: 0 };\n      break;\n  }\n}\n\nfunction gameLoop() {\n  updateSnakePosition();\n  if (checkCollision()) {\n    endGame();\n    return;\n  }\n  checkFoodCollision();\n  draw();\n  lastDirection = { ...direction };\n}\n\nfunction updateSnakePosition() {\n  for (let i = snake.length - 2; i &gt;= 0; i--) {\n    snake[i + 1] = { ...snake[i] };\n  }\n  snake[0].x += direction.x;\n  snake[0].y += direction.y;\n}\n\nfunction checkCollision() {\n  return (\n    snake[0].x &lt; 0 ||\n    snake[0].x &gt;= 400 ||\n    snake[0].y &lt; 0 ||\n    snake[0].y &gt;= 400 ||\n    snake\n      .slice(1)\n      .some(segment =&gt; segment.x === snake[0].x &amp;&amp; segment.y === snake[0].y)\n  );\n}\n\nfunction checkFoodCollision() {\n  if (snake[0].x === food.x &amp;&amp; snake[0].y === food.y) {\n    snake.push({ ...snake[snake.length - 1] });\n    resetFoodPosition();\n  }\n}\n\nfunction resetFoodPosition() {\n  food = {\n    x: Math.floor(Math.random() * 20) * gridSize,\n    y: Math.floor(Math.random() * 20) * gridSize,\n  };\n}\n\nfunction draw() {\n  if (!ctx.value) return;\n  ctx.value.clearRect(0, 0, 400, 400);\n  drawGrid();\n  drawSnake();\n  drawFood();\n}\n\nfunction drawGrid() {\n  if (!ctx.value) return;\n  ctx.value.strokeStyle = \&quot;#ddd\&quot;;\n  for (let i = 0; i &lt;= 400; i += gridSize) {\n    ctx.value.beginPath();\n    ctx.value.moveTo(i, 0);\n    ctx.value.lineTo(i, 400);\n    ctx.value.stroke();\n    ctx.value.moveTo(0, i);\n    ctx.value.lineTo(400, i);\n    ctx.value.stroke();\n  }\n}\n\nfunction drawSnake() {\n  if (!ctx.value) return;\n  ctx.value.fillStyle = \&quot;green\&quot;;\n  snake.forEach(segment =&gt; {\n    ctx.value?.fillRect(segment.x, segment.y, gridSize, gridSize);\n  });\n}\n\nfunction drawFood() {\n  if (!ctx.value) return;\n  ctx.value.fillStyle = \&quot;red\&quot;;\n  ctx.value.fillRect(food.x, food.y, gridSize, gridSize);\n}\n\nfunction endGame() {\n  if (gameInterval !== null) {\n    window.clearInterval(gameInterval);\n  }\n  alert(\&quot;Game Over\&quot;);\n}\n&lt;/script&gt;\n\n&lt;style&gt;\n.game-container {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  height: 100vh;\n}\n&lt;/style&gt;\n```\n\n### Screenshot from the game\n\n![Snake Game Screenshot](./../../assets/images/how-to-write-clean-vue-components/snakeGameImage.png)\n\n### Challenges with the Traditional Approach\n\nWhen you mix the view, reactivity, and business logic all in one file, the component becomes bulky and hard to maintain. Unit tests become more complex, requiring integration tests for comprehensive coverage.\n\n---\n\n## Introducing the Functional Core, Imperative Shell Pattern\n\nTo solve these problems in Vue, we use the \&quot;Functional Core, Imperative Shell\&quot; pattern. This pattern is key in software architecture and helps you structure your code better:\n\n&gt; **Functional Core, Imperative Shell Pattern**: In this design, the main logic of your app (the &#39;Functional Core&#39;) stays pure and without side effects, making it testable. The &#39;Imperative Shell&#39; handles the outside world, like the UI or databases, and talks to the pure core.\n\n![Functional core Diagram](./../../assets/images/how-to-write-clean-vue-components/functional-core-diagram.png)\n\n### What Are Pure Functions?\n\nIn this pattern, **pure functions** are at the heart of the &#39;Functional Core&#39;. A pure function is a concept from functional programming, and it has two key characteristics:\n\n1. **Predictability**: If you give a pure function the same inputs, it always gives back the same output.\n2. **No Side Effects**: Pure functions don&#39;t change anything outside them. They don&#39;t alter external variables, call APIs, or do any input/output.\n\nPure functions simplify testing, debugging, and code comprehension. They form the foundation of the Functional Core, keeping your app&#39;s business logic clean and manageable.\n\n---\n\n### Applying the Pattern in Vue\n\nIn Vue, this pattern has two parts:\n\n- **Imperative Shell** (`useGameSnake.ts`): This part handles the Vue-specific reactive bits. It&#39;s where your components interact with Vue, managing operations like state changes and events.\n- **Functional Core** (`pureGameSnake.ts`): This is where your pure business logic lives. It&#39;s separate from Vue, which makes it easier to test and think about your app&#39;s main functions, independent of the UI.\n\n---\n\n### Implementing `pureGameSnake.ts`\n\nThe `pureGameSnake.ts` file encapsulates the game&#39;s business logic without any Vue-specific reactivity. This separation means easier testing and clearer logic.\n\n```typescript\nexport const gridSize = 20;\n\ninterface Position {\n  x: number;\n  y: number;\n}\n\ntype Snake = Position[];\n\nexport function initializeSnake(): Snake {\n  return [{ x: 200, y: 200 }];\n}\n\nexport function moveSnake(snake: Snake, direction: Position): Snake {\n  return snake.map((segment, index) =&gt; {\n    if (index === 0) {\n      return { x: segment.x + direction.x, y: segment.y + direction.y };\n    }\n    return { ...snake[index - 1] };\n  });\n}\n\nexport function isCollision(snake: Snake): boolean {\n  const head = snake[0];\n  return (\n    head.x &lt; 0 ||\n    head.x &gt;= 400 ||\n    head.y &lt; 0 ||\n    head.y &gt;= 400 ||\n    snake.slice(1).some(segment =&gt; segment.x === head.x &amp;&amp; segment.y === head.y)\n  );\n}\n\nexport function randomFoodPosition(): Position {\n  return {\n    x: Math.floor(Math.random() * 20) * gridSize,\n    y: Math.floor(Math.random() * 20) * gridSize,\n  };\n}\n\nexport function isFoodEaten(snake: Snake, food: Position): boolean {\n  const head = snake[0];\n  return head.x === food.x &amp;&amp; head.y === food.y;\n}\n```\n\n### Implementing `useGameSnake.ts`\n\nIn `useGameSnake.ts`, we manage the Vue-specific state and reactivity, leveraging the pure functions from `pureGameSnake.ts`.\n\n```typescript\nimport { onMounted, onUnmounted, ref, Ref } from \&quot;vue\&quot;;\nimport * as GameLogic from \&quot;./pureGameSnake\&quot;;\n\ninterface Position {\n  x: number;\n  y: number;\n}\n\ntype Snake = Position[];\n\ninterface GameState {\n  snake: Ref&lt;Snake&gt;;\n  direction: Ref&lt;Position&gt;;\n  food: Ref&lt;Position&gt;;\n  gameState: Ref&lt;\&quot;over\&quot; | \&quot;playing\&quot;&gt;;\n}\n\nexport function useGameSnake(): GameState {\n  const snake: Ref&lt;Snake&gt; = ref(GameLogic.initializeSnake());\n  const direction: Ref&lt;Position&gt; = ref({ x: 0, y: 0 });\n  const food: Ref&lt;Position&gt; = ref(GameLogic.randomFoodPosition());\n  const gameState: Ref&lt;\&quot;over\&quot; | \&quot;playing\&quot;&gt; = ref(\&quot;playing\&quot;);\n  let gameInterval: number | null = null;\n\n  const startGame = (): void =&gt; {\n    gameInterval = window.setInterval(() =&gt; {\n      snake.value = GameLogic.moveSnake(snake.value, direction.value);\n\n      if (GameLogic.isCollision(snake.value)) {\n        gameState.value = \&quot;over\&quot;;\n        if (gameInterval !== null) {\n          clearInterval(gameInterval);\n        }\n      } else if (GameLogic.isFoodEaten(snake.value, food.value)) {\n        snake.value.push({ ...snake.value[snake.value.length - 1] });\n        food.value = GameLogic.randomFoodPosition();\n      }\n    }, 100);\n  };\n\n  onMounted(startGame);\n\n  onUnmounted(() =&gt; {\n    if (gameInterval !== null) {\n      clearInterval(gameInterval);\n    }\n  });\n\n  return { snake, direction, food, gameState };\n}\n```\n\n### Refactoring `gameSnake.vue`\n\nNow, our `gameSnake.vue` is more focused, using `useGameSnake.ts` for managing state and reactivity, while the view remains within the template.\n\n```vue\n&lt;template&gt;\n  &lt;div class=\&quot;game-container\&quot;&gt;\n    &lt;canvas ref=\&quot;canvas\&quot; width=\&quot;400\&quot; height=\&quot;400\&quot;&gt;&lt;/canvas&gt;\n  &lt;/div&gt;\n&lt;/template&gt;\n\n&lt;script setup lang=\&quot;ts\&quot;&gt;\nimport { ref, onMounted, watch, onUnmounted } from \&quot;vue\&quot;;\nimport { useGameSnake } from \&quot;./useGameSnake.ts\&quot;;\nimport { gridSize } from \&quot;./pureGameSnake\&quot;;\n\nconst { snake, direction, food, gameState } = useGameSnake();\nconst canvas = ref&lt;HTMLCanvasElement | null&gt;(null);\nconst ctx = ref&lt;CanvasRenderingContext2D | null&gt;(null);\nlet lastDirection = { x: 0, y: 0 };\n\nonMounted(() =&gt; {\n  if (canvas.value) {\n    ctx.value = canvas.value.getContext(\&quot;2d\&quot;);\n    draw();\n  }\n  window.addEventListener(\&quot;keydown\&quot;, handleKeydown);\n});\n\nonUnmounted(() =&gt; {\n  window.removeEventListener(\&quot;keydown\&quot;, handleKeydown);\n});\n\nwatch(gameState, state =&gt; {\n  if (state === \&quot;over\&quot;) {\n    alert(\&quot;Game Over\&quot;);\n  }\n});\n\nfunction handleKeydown(e: KeyboardEvent) {\n  e.preventDefault();\n  switch (e.key) {\n    case \&quot;ArrowUp\&quot;:\n      if (lastDirection.y !== 0) break;\n      direction.value = { x: 0, y: -gridSize };\n      break;\n    case \&quot;ArrowDown\&quot;:\n      if (lastDirection.y !== 0) break;\n      direction.value = { x: 0, y: gridSize };\n      break;\n    case \&quot;ArrowLeft\&quot;:\n      if (lastDirection.x !== 0) break;\n      direction.value = { x: -gridSize, y: 0 };\n      break;\n    case \&quot;ArrowRight\&quot;:\n      if (lastDirection.x !== 0) break;\n      direction.value = { x: gridSize, y: 0 };\n      break;\n  }\n  lastDirection = { ...direction.value };\n}\n\nwatch(\n  [snake, food],\n  () =&gt; {\n    draw();\n  },\n  { deep: true }\n);\n\nfunction draw() {\n  if (!ctx.value) return;\n  ctx.value.clearRect(0, 0, 400, 400);\n  drawGrid();\n  drawSnake();\n  drawFood();\n}\n\nfunction drawGrid() {\n  if (!ctx.value) return;\n  ctx.value.strokeStyle = \&quot;#ddd\&quot;;\n  for (let i = 0; i &lt;= 400; i += gridSize) {\n    ctx.value.beginPath();\n    ctx.value.moveTo(i, 0);\n    ctx.value.lineTo(i, 400);\n    ctx.value.stroke();\n    ctx.value.moveTo(0, i);\n    ctx.value.lineTo(400, i);\n    ctx.value.stroke();\n  }\n}\n\nfunction drawSnake() {\n  ctx.value.fillStyle = \&quot;green\&quot;;\n  snake.value.forEach(segment =&gt; {\n    ctx.value.fillRect(segment.x, segment.y, gridSize, gridSize);\n  });\n}\n\nfunction drawFood() {\n  ctx.value.fillStyle = \&quot;red\&quot;;\n  ctx.value.fillRect(food.value.x, food.value.y, gridSize, gridSize);\n}\n&lt;/script&gt;\n\n&lt;style&gt;\n.game-container {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  height: 100vh;\n}\n&lt;/style&gt;\n```\n\n---\n\n## Advantages of the Functional Core, Imperative Shell Pattern\n\nThe Functional Core, Imperative Shell pattern enhances the **testability** and **maintainability** of Vue components. By separating the business logic from the framework-specific code, this pattern offers key advantages:\n\n### Simplified Testing\n\nBusiness logic combined with Vue&#39;s reactivity and component structure makes testing complex. Traditional unit testing becomes challenging, leading to integration tests that lack precision. By extracting the core logic into pure functions (as in `pureGameSnake.ts`), we write focused unit tests for each function. This isolation streamlines testing, as each piece of logic operates independently of Vue&#39;s reactivity system.\n\n### Enhanced Maintainability\n\nThe Functional Core, Imperative Shell pattern creates a clear **separation of concerns**. Vue components focus on the user interface and reactivity, while the pure business logic lives in separate, framework-agnostic files. This separation improves code readability and understanding. Maintenance becomes straightforward as the application grows.\n\n### Framework Agnosticism\n\nA key advantage of this pattern is the **portability** of your business logic. The pure functions in the Functional Core remain independent of any UI framework. If you need to switch from Vue to another framework, or if Vue changes, your core logic remains intact. This flexibility protects your code against changes and shifts in technology.\n\n## Testing Complexities in Traditional Vue Components vs. Functional Core, Imperative Shell Pattern\n\n### Challenges in Testing Traditional Components\n\nTesting traditional Vue components, where view, reactivity, and business logic combine, presents specific challenges. In such components, unit tests face these obstacles:\n\n- Tests function more like integration tests, reducing precision\n- Vue&#39;s reactivity system creates complex mocking requirements\n- Test coverage must span reactive behavior and side effects\n\nThese challenges reduce confidence in tests and component stability.\n\n### Simplified Testing with Functional Core, Imperative Shell Pattern\n\nThe Functional Core, Imperative Shell pattern transforms testing:\n\n- **Isolated Business Logic**: Pure functions in the Functional Core enable direct unit tests without Vue&#39;s reactivity or component states.\n- **Predictable Outcomes**: Pure functions deliver consistent outputs for given inputs.\n- **Clear Separation**: The reactive and side-effect code stays in the Imperative Shell, enabling focused testing of Vue interactions.\n\nThis approach creates a modular, testable codebase where each component undergoes thorough testing, improving reliability.\n\n---\n\n### Conclusion\n\nThe Functional Core, Imperative Shell pattern strengthens Vue applications through improved testing and maintenance. It prepares your code for future changes and growth. While restructuring requires initial effort, the pattern delivers long-term benefits, making it valuable for Vue developers aiming to enhance their application&#39;s architecture and quality.\n\n![Blog Conclusion Diagram](./../../assets/images/how-to-write-clean-vue-components/conclusionDiagram.png)&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <h2 id="table-of-contents">Table of Contents<a class="heading-link" aria-label="Link to section" href="#table-of-contents"><span class="heading-link-icon">#</span></a></h2>
<p></p><details><summary>Open Table of Contents</summary><p></p>
<ul>
<li><a href="#introduction">Introduction</a></li>
<li><a href="#understanding-vue-components">Understanding Vue Components</a></li>
<li><a href="#case-study-snakegamevue">Case Study: <code>snakeGame.vue</code></a>
<ul>
<li><a href="#code-sample-traditional-approach">Code Sample: Traditional Approach</a></li>
<li><a href="#screenshot-from-the-game">Screenshot from the game</a></li>
<li><a href="#challenges-with-the-traditional-approach">Challenges with the Traditional Approach</a></li>
</ul>
</li>
<li><a href="#introducing-the-functional-core-imperative-shell-pattern">Introducing the Functional Core, Imperative Shell Pattern</a>
<ul>
<li><a href="#what-are-pure-functions">What Are Pure Functions?</a></li>
<li><a href="#applying-the-pattern-in-vue">Applying the Pattern in Vue</a></li>
<li><a href="#implementing-puregamesnakets">Implementing <code>pureGameSnake.ts</code></a></li>
<li><a href="#implementing-usegamesnakets">Implementing <code>useGameSnake.ts</code></a></li>
<li><a href="#refactoring-gamesnakevue">Refactoring <code>gameSnake.vue</code></a></li>
</ul>
</li>
<li><a href="#advantages-of-the-functional-core-imperative-shell-pattern">Advantages of the Functional Core, Imperative Shell Pattern</a>
<ul>
<li><a href="#simplified-testing">Simplified Testing</a></li>
<li><a href="#enhanced-maintainability">Enhanced Maintainability</a></li>
<li><a href="#framework-agnosticism">Framework Agnosticism</a></li>
</ul>
</li>
<li><a href="#testing-complexities-in-traditional-vue-components-vs-functional-core-imperative-shell-pattern">Testing Complexities in Traditional Vue Components vs. Functional Core, Imperative Shell Pattern</a>
<ul>
<li><a href="#challenges-in-testing-traditional-components">Challenges in Testing Traditional Components</a></li>
<li><a href="#simplified-testing-with-functional-core-imperative-shell-pattern">Simplified Testing with Functional Core, Imperative Shell Pattern</a></li>
<li><a href="#conclusion">Conclusion</a></li>
</ul>
</li>
</ul>
<p></p></details><p></p>
<h2 id="introduction">Introduction<a class="heading-link" aria-label="Link to section" href="#introduction"><span class="heading-link-icon">#</span></a></h2>
<p>Writing code that’s both easy to test and easy to read can be a challenge, with Vue components. In this blog post, I’m going to share a design idea that will make your Vue components better. This method won’t speed up your code, but it will make it simpler to test and understand. Think of it as a big-picture way to improve your Vue coding style. It’s going to make your life easier when you need to fix or update your components.</p>
<p>Whether you’re new to Vue or have been using it for some time, this tip will help you make your Vue components cleaner and more straightforward.</p>
<hr>
<h2 id="understanding-vue-components">Understanding Vue Components<a class="heading-link" aria-label="Link to section" href="#understanding-vue-components"><span class="heading-link-icon">#</span></a></h2>
<p>A Vue component is like a reusable puzzle piece in your app. It has three main parts:</p>
<ol>
<li><strong>View</strong>: This is the template section where you design the user interface.</li>
<li><strong>Reactivity</strong>: Here, Vue’s features like <code>ref</code> make the interface interactive.</li>
<li><strong>Business Logic</strong>: This is where you process data or manage user actions.</li>
</ol>
<p><img alt="Architecture" loading="lazy" decoding="async" fetchpriority="auto" width="3014" height="1610" src="/_astro/architecture.CO59unq1_cJB53.webp" ></p>
<hr>
<h2 id="case-study-snakegamevue">Case Study: <code>snakeGame.vue</code><a class="heading-link" aria-label="Link to section" href="#case-study-snakegamevue"><span class="heading-link-icon">#</span></a></h2>
<p>Let’s look at a common Vue component, <code>snakeGame.vue</code>. It mixes the view, reactivity, and business logic, which can make it complex and hard to work with.</p>
<h3 id="code-sample-traditional-approach">Code Sample: Traditional Approach<a class="heading-link" aria-label="Link to section" href="#code-sample-traditional-approach"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&#x3C;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">></span></span>
<span class="line"><span style="color:#BA3C97">  &#x3C;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">game-container</span><span style="color:#89DDFF">"</span><span style="color:#BA3C97">></span></span>
<span class="line"><span style="color:#BA3C97">    &#x3C;</span><span style="color:#F7768E">canvas</span><span style="color:#BB9AF7"> ref</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">canvas</span><span style="color:#89DDFF">"</span><span style="color:#BB9AF7"> width</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">400</span><span style="color:#89DDFF">"</span><span style="color:#BB9AF7"> height</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">400</span><span style="color:#89DDFF">"</span><span style="color:#BA3C97">>&#x3C;/</span><span style="color:#F7768E">canvas</span><span style="color:#BA3C97">></span></span>
<span class="line"><span style="color:#BA3C97">  &#x3C;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">></span></span>
<span class="line"><span style="color:#BA3C97">&#x3C;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">></span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&#x3C;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">"</span><span style="color:#BA3C97">></span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">onMounted</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> onUnmounted</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> canvas</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&#x3C;</span><span style="color:#C0CAF5">HTMLCanvasElement</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">></span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> ctx</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&#x3C;</span><span style="color:#C0CAF5">CanvasRenderingContext2D</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">></span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">let</span><span style="color:#BB9AF7"> snake</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> [{</span><span style="color:#73DACA"> x</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 200</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 200</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">let</span><span style="color:#BB9AF7"> direction</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> x</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">let</span><span style="color:#BB9AF7"> lastDirection</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> x</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">let</span><span style="color:#BB9AF7"> food</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> x</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> gridSize</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 20</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">let</span><span style="color:#BB9AF7"> gameInterval</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">onMounted</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">canvas</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> canvas</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getContext</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">2d</span><span style="color:#89DDFF">"</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    resetFoodPosition</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    gameInterval</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> window</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">setInterval</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">gameLoop</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 100</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#C0CAF5">  window</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">addEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">keydown</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> handleKeydown</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">onUnmounted</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">gameInterval</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> null</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    window</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">clearInterval</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">gameInterval</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#C0CAF5">  window</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">removeEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">keydown</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> handleKeydown</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> handleKeydown</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">e</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> KeyboardEvent</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  e</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">preventDefault</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">  switch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">e</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">key</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">ArrowUp</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">lastDirection</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      direction</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">x</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> -</span><span style="color:#C0CAF5">gridSize</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">ArrowDown</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">lastDirection</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      direction</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">x</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">ArrowLeft</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">lastDirection</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      direction</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">x</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> -</span><span style="color:#C0CAF5">gridSize</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">ArrowRight</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">lastDirection</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      direction</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">x</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> gameLoop</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  updateSnakePosition</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#7AA2F7">checkCollision</span><span style="color:#9ABDF5">()) {</span></span>
<span class="line"><span style="color:#7AA2F7">    endGame</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#7AA2F7">  checkFoodCollision</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  draw</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  lastDirection</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> { </span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">direction</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> updateSnakePosition</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  for</span><span style="color:#9ABDF5"> (</span><span style="color:#9D7CD8;font-style:italic">let</span><span style="color:#BB9AF7"> i</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> snake</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#89DDFF"> -</span><span style="color:#FF9E64"> 2</span><span style="color:#89DDFF">;</span><span style="color:#C0CAF5"> i</span><span style="color:#BB9AF7"> >=</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">;</span><span style="color:#C0CAF5"> i</span><span style="color:#89DDFF">--</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    snake</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">i</span><span style="color:#89DDFF"> +</span><span style="color:#FF9E64"> 1</span><span style="color:#9ABDF5">] </span><span style="color:#89DDFF">=</span><span style="color:#9ABDF5"> { </span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">snake</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">i</span><span style="color:#9ABDF5">] }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#C0CAF5">  snake</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#89DDFF"> +=</span><span style="color:#C0CAF5"> direction</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  snake</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#89DDFF"> +=</span><span style="color:#C0CAF5"> direction</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> checkCollision</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> (</span></span>
<span class="line"><span style="color:#C0CAF5">    snake</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> &#x3C;</span><span style="color:#FF9E64"> 0</span><span style="color:#BB9AF7"> ||</span></span>
<span class="line"><span style="color:#C0CAF5">    snake</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> >=</span><span style="color:#FF9E64"> 400</span><span style="color:#BB9AF7"> ||</span></span>
<span class="line"><span style="color:#C0CAF5">    snake</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#BB9AF7"> &#x3C;</span><span style="color:#FF9E64"> 0</span><span style="color:#BB9AF7"> ||</span></span>
<span class="line"><span style="color:#C0CAF5">    snake</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#BB9AF7"> >=</span><span style="color:#FF9E64"> 400</span><span style="color:#BB9AF7"> ||</span></span>
<span class="line"><span style="color:#E0AF68">    snake</span></span>
<span class="line"><span style="color:#89DDFF">      .</span><span style="color:#7AA2F7">slice</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">1</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#89DDFF">      .</span><span style="color:#7AA2F7">some</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">segment</span><span style="color:#BB9AF7"> =></span><span style="color:#C0CAF5"> segment</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> ===</span><span style="color:#C0CAF5"> snake</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> &#x26;&#x26;</span><span style="color:#C0CAF5"> segment</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#BB9AF7"> ===</span><span style="color:#C0CAF5"> snake</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> checkFoodCollision</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">snake</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> ===</span><span style="color:#C0CAF5"> food</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> &#x26;&#x26;</span><span style="color:#C0CAF5"> snake</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#BB9AF7"> ===</span><span style="color:#C0CAF5"> food</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    snake</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">push</span><span style="color:#9ABDF5">({ </span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">snake</span><span style="color:#9ABDF5">[</span><span style="color:#C0CAF5">snake</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#89DDFF"> -</span><span style="color:#FF9E64"> 1</span><span style="color:#9ABDF5">] })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    resetFoodPosition</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> resetFoodPosition</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  food</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    x</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">floor</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">random</span><span style="color:#9ABDF5">() </span><span style="color:#89DDFF">*</span><span style="color:#FF9E64"> 20</span><span style="color:#9ABDF5">) </span><span style="color:#89DDFF">*</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    y</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">floor</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">random</span><span style="color:#9ABDF5">() </span><span style="color:#89DDFF">*</span><span style="color:#FF9E64"> 20</span><span style="color:#9ABDF5">) </span><span style="color:#89DDFF">*</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> draw</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">clearRect</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 400</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 400</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  drawGrid</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  drawSnake</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  drawFood</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> drawGrid</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  ctx</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">strokeStyle</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">#ddd</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">  for</span><span style="color:#9ABDF5"> (</span><span style="color:#9D7CD8;font-style:italic">let</span><span style="color:#BB9AF7"> i</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">;</span><span style="color:#C0CAF5"> i</span><span style="color:#BB9AF7"> &#x3C;=</span><span style="color:#FF9E64"> 400</span><span style="color:#89DDFF">;</span><span style="color:#C0CAF5"> i</span><span style="color:#89DDFF"> +=</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">beginPath</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">moveTo</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">i</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">lineTo</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">i</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 400</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">stroke</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">moveTo</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> i</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">lineTo</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">400</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> i</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">stroke</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> drawSnake</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  ctx</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">fillStyle</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">green</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  snake</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">forEach</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">segment</span><span style="color:#BB9AF7"> =></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">?.</span><span style="color:#7AA2F7">fillRect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">segment</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> segment</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> drawFood</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  ctx</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">fillStyle</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">red</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">fillRect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">food</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> food</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> endGame</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">gameInterval</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> null</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    window</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">clearInterval</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">gameInterval</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#7AA2F7">  alert</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">Game Over</span><span style="color:#89DDFF">"</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BA3C97">&#x3C;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">></span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&#x3C;</span><span style="color:#F7768E">style</span><span style="color:#BA3C97">></span></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">game-container</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  display</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> flex</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  justify-content</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> center</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  align-items</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> center</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  height</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 100</span><span style="color:#F7768E">vh</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BA3C97">&#x3C;/</span><span style="color:#F7768E">style</span><span style="color:#BA3C97">></span></span></code><button type="button" class="copy" data-code="<template>
  <div class=&#x22;game-container&#x22;>
    <canvas ref=&#x22;canvas&#x22; width=&#x22;400&#x22; height=&#x22;400&#x22;></canvas>
  </div>
</template>

<script setup lang=&#x22;ts&#x22;>
import { onMounted, onUnmounted, ref } from &#x22;vue&#x22;;

const canvas = ref<HTMLCanvasElement | null>(null);
const ctx = ref<CanvasRenderingContext2D | null>(null);
let snake = [{ x: 200, y: 200 }];
let direction = { x: 0, y: 0 };
let lastDirection = { x: 0, y: 0 };
let food = { x: 0, y: 0 };
const gridSize = 20;
let gameInterval: number | null = null;

onMounted(() => {
  if (canvas.value) {
    ctx.value = canvas.value.getContext(&#x22;2d&#x22;);
    resetFoodPosition();
    gameInterval = window.setInterval(gameLoop, 100);
  }
  window.addEventListener(&#x22;keydown&#x22;, handleKeydown);
});

onUnmounted(() => {
  if (gameInterval !== null) {
    window.clearInterval(gameInterval);
  }
  window.removeEventListener(&#x22;keydown&#x22;, handleKeydown);
});

function handleKeydown(e: KeyboardEvent) {
  e.preventDefault();
  switch (e.key) {
    case &#x22;ArrowUp&#x22;:
      if (lastDirection.y !== 0) break;
      direction = { x: 0, y: -gridSize };
      break;
    case &#x22;ArrowDown&#x22;:
      if (lastDirection.y !== 0) break;
      direction = { x: 0, y: gridSize };
      break;
    case &#x22;ArrowLeft&#x22;:
      if (lastDirection.x !== 0) break;
      direction = { x: -gridSize, y: 0 };
      break;
    case &#x22;ArrowRight&#x22;:
      if (lastDirection.x !== 0) break;
      direction = { x: gridSize, y: 0 };
      break;
  }
}

function gameLoop() {
  updateSnakePosition();
  if (checkCollision()) {
    endGame();
    return;
  }
  checkFoodCollision();
  draw();
  lastDirection = { ...direction };
}

function updateSnakePosition() {
  for (let i = snake.length - 2; i >= 0; i--) {
    snake[i + 1] = { ...snake[i] };
  }
  snake[0].x += direction.x;
  snake[0].y += direction.y;
}

function checkCollision() {
  return (
    snake[0].x < 0 ||
    snake[0].x >= 400 ||
    snake[0].y < 0 ||
    snake[0].y >= 400 ||
    snake
      .slice(1)
      .some(segment => segment.x === snake[0].x &#x26;&#x26; segment.y === snake[0].y)
  );
}

function checkFoodCollision() {
  if (snake[0].x === food.x &#x26;&#x26; snake[0].y === food.y) {
    snake.push({ ...snake[snake.length - 1] });
    resetFoodPosition();
  }
}

function resetFoodPosition() {
  food = {
    x: Math.floor(Math.random() * 20) * gridSize,
    y: Math.floor(Math.random() * 20) * gridSize,
  };
}

function draw() {
  if (!ctx.value) return;
  ctx.value.clearRect(0, 0, 400, 400);
  drawGrid();
  drawSnake();
  drawFood();
}

function drawGrid() {
  if (!ctx.value) return;
  ctx.value.strokeStyle = &#x22;#ddd&#x22;;
  for (let i = 0; i <= 400; i += gridSize) {
    ctx.value.beginPath();
    ctx.value.moveTo(i, 0);
    ctx.value.lineTo(i, 400);
    ctx.value.stroke();
    ctx.value.moveTo(0, i);
    ctx.value.lineTo(400, i);
    ctx.value.stroke();
  }
}

function drawSnake() {
  if (!ctx.value) return;
  ctx.value.fillStyle = &#x22;green&#x22;;
  snake.forEach(segment => {
    ctx.value?.fillRect(segment.x, segment.y, gridSize, gridSize);
  });
}

function drawFood() {
  if (!ctx.value) return;
  ctx.value.fillStyle = &#x22;red&#x22;;
  ctx.value.fillRect(food.x, food.y, gridSize, gridSize);
}

function endGame() {
  if (gameInterval !== null) {
    window.clearInterval(gameInterval);
  }
  alert(&#x22;Game Over&#x22;);
}
</script>

<style>
.game-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="screenshot-from-the-game">Screenshot from the game<a class="heading-link" aria-label="Link to section" href="#screenshot-from-the-game"><span class="heading-link-icon">#</span></a></h3>
<p><img alt="Snake Game Screenshot" loading="lazy" decoding="async" fetchpriority="auto" width="1156" height="888" src="/_astro/snakeGameImage.D5kNsPv3_ZuOg5O.webp" ></p>
<h3 id="challenges-with-the-traditional-approach">Challenges with the Traditional Approach<a class="heading-link" aria-label="Link to section" href="#challenges-with-the-traditional-approach"><span class="heading-link-icon">#</span></a></h3>
<p>When you mix the view, reactivity, and business logic all in one file, the component becomes bulky and hard to maintain. Unit tests become more complex, requiring integration tests for comprehensive coverage.</p>
<hr>
<h2 id="introducing-the-functional-core-imperative-shell-pattern">Introducing the Functional Core, Imperative Shell Pattern<a class="heading-link" aria-label="Link to section" href="#introducing-the-functional-core-imperative-shell-pattern"><span class="heading-link-icon">#</span></a></h2>
<p>To solve these problems in Vue, we use the “Functional Core, Imperative Shell” pattern. This pattern is key in software architecture and helps you structure your code better:</p>
<blockquote>
<p><strong>Functional Core, Imperative Shell Pattern</strong>: In this design, the main logic of your app (the ‘Functional Core’) stays pure and without side effects, making it testable. The ‘Imperative Shell’ handles the outside world, like the UI or databases, and talks to the pure core.</p>
</blockquote>
<p><img alt="Functional core Diagram" loading="lazy" decoding="async" fetchpriority="auto" width="2498" height="2296" src="/_astro/functional-core-diagram.DSmnfL4m_Z1XwW0M.webp" ></p>
<h3 id="what-are-pure-functions">What Are Pure Functions?<a class="heading-link" aria-label="Link to section" href="#what-are-pure-functions"><span class="heading-link-icon">#</span></a></h3>
<p>In this pattern, <strong>pure functions</strong> are at the heart of the ‘Functional Core’. A pure function is a concept from functional programming, and it has two key characteristics:</p>
<ol>
<li><strong>Predictability</strong>: If you give a pure function the same inputs, it always gives back the same output.</li>
<li><strong>No Side Effects</strong>: Pure functions don’t change anything outside them. They don’t alter external variables, call APIs, or do any input/output.</li>
</ol>
<p>Pure functions simplify testing, debugging, and code comprehension. They form the foundation of the Functional Core, keeping your app’s business logic clean and manageable.</p>
<hr>
<h3 id="applying-the-pattern-in-vue">Applying the Pattern in Vue<a class="heading-link" aria-label="Link to section" href="#applying-the-pattern-in-vue"><span class="heading-link-icon">#</span></a></h3>
<p>In Vue, this pattern has two parts:</p>
<ul>
<li><strong>Imperative Shell</strong> (<code>useGameSnake.ts</code>): This part handles the Vue-specific reactive bits. It’s where your components interact with Vue, managing operations like state changes and events.</li>
<li><strong>Functional Core</strong> (<code>pureGameSnake.ts</code>): This is where your pure business logic lives. It’s separate from Vue, which makes it easier to test and think about your app’s main functions, independent of the UI.</li>
</ul>
<hr>
<h3 id="implementing-puregamesnakets">Implementing <code>pureGameSnake.ts</code><a class="heading-link" aria-label="Link to section" href="#implementing-puregamesnakets"><span class="heading-link-icon">#</span></a></h3>
<p>The <code>pureGameSnake.ts</code> file encapsulates the game’s business logic without any Vue-specific reactivity. This separation means easier testing and clearer logic.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">export</span><span style="color:#9D7CD8;font-style:italic"> const</span><span style="color:#BB9AF7"> gridSize</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 20</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> Position</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  x</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  y</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> Snake</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> Position</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> initializeSnake</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Snake</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> [{ </span><span style="color:#73DACA">x</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 200</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 200</span><span style="color:#9ABDF5"> }]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> moveSnake</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">snake</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Snake</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> direction</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Position</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Snake</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> snake</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">map</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">segment</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> index</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">index</span><span style="color:#BB9AF7"> ===</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">      return</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">x</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> segment</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#89DDFF"> +</span><span style="color:#C0CAF5"> direction</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> segment</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#89DDFF"> +</span><span style="color:#C0CAF5"> direction</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">    return</span><span style="color:#9ABDF5"> { </span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">snake</span><span style="color:#9ABDF5">[</span><span style="color:#7DCFFF">index</span><span style="color:#89DDFF"> -</span><span style="color:#FF9E64"> 1</span><span style="color:#9ABDF5">] }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> isCollision</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">snake</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Snake</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> head</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> snake</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> (</span></span>
<span class="line"><span style="color:#C0CAF5">    head</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> &#x3C;</span><span style="color:#FF9E64"> 0</span><span style="color:#BB9AF7"> ||</span></span>
<span class="line"><span style="color:#C0CAF5">    head</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> >=</span><span style="color:#FF9E64"> 400</span><span style="color:#BB9AF7"> ||</span></span>
<span class="line"><span style="color:#C0CAF5">    head</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#BB9AF7"> &#x3C;</span><span style="color:#FF9E64"> 0</span><span style="color:#BB9AF7"> ||</span></span>
<span class="line"><span style="color:#C0CAF5">    head</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#BB9AF7"> >=</span><span style="color:#FF9E64"> 400</span><span style="color:#BB9AF7"> ||</span></span>
<span class="line"><span style="color:#C0CAF5">    snake</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">slice</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">1</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">some</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">segment</span><span style="color:#BB9AF7"> =></span><span style="color:#C0CAF5"> segment</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> ===</span><span style="color:#C0CAF5"> head</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> &#x26;&#x26;</span><span style="color:#C0CAF5"> segment</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#BB9AF7"> ===</span><span style="color:#C0CAF5"> head</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#9ABDF5">)</span></span>
<span class="line"><span style="color:#9ABDF5">  )</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> randomFoodPosition</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Position</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    x</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">floor</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">random</span><span style="color:#9ABDF5">() </span><span style="color:#89DDFF">*</span><span style="color:#FF9E64"> 20</span><span style="color:#9ABDF5">) </span><span style="color:#89DDFF">*</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">    y</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">floor</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">Math</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">random</span><span style="color:#9ABDF5">() </span><span style="color:#89DDFF">*</span><span style="color:#FF9E64"> 20</span><span style="color:#9ABDF5">) </span><span style="color:#89DDFF">*</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> isFoodEaten</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">snake</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Snake</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> food</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Position</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> boolean</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> head</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> snake</span><span style="color:#9ABDF5">[</span><span style="color:#FF9E64">0</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> head</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> ===</span><span style="color:#C0CAF5"> food</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> &#x26;&#x26;</span><span style="color:#C0CAF5"> head</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#BB9AF7"> ===</span><span style="color:#C0CAF5"> food</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="export const gridSize = 20;

interface Position {
  x: number;
  y: number;
}

type Snake = Position[];

export function initializeSnake(): Snake {
  return [{ x: 200, y: 200 }];
}

export function moveSnake(snake: Snake, direction: Position): Snake {
  return snake.map((segment, index) => {
    if (index === 0) {
      return { x: segment.x + direction.x, y: segment.y + direction.y };
    }
    return { ...snake[index - 1] };
  });
}

export function isCollision(snake: Snake): boolean {
  const head = snake[0];
  return (
    head.x < 0 ||
    head.x >= 400 ||
    head.y < 0 ||
    head.y >= 400 ||
    snake.slice(1).some(segment => segment.x === head.x &#x26;&#x26; segment.y === head.y)
  );
}

export function randomFoodPosition(): Position {
  return {
    x: Math.floor(Math.random() * 20) * gridSize,
    y: Math.floor(Math.random() * 20) * gridSize,
  };
}

export function isFoodEaten(snake: Snake, food: Position): boolean {
  const head = snake[0];
  return head.x === food.x &#x26;&#x26; head.y === food.y;
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="implementing-usegamesnakets">Implementing <code>useGameSnake.ts</code><a class="heading-link" aria-label="Link to section" href="#implementing-usegamesnakets"><span class="heading-link-icon">#</span></a></h3>
<p>In <code>useGameSnake.ts</code>, we manage the Vue-specific state and reactivity, leveraging the pure functions from <code>pureGameSnake.ts</code>.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">onMounted</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> onUnmounted</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> ref</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> Ref</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#FF9E64"> *</span><span style="color:#89DDFF"> as</span><span style="color:#0DB9D7"> GameLogic</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">./pureGameSnake</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> Position</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  x</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#73DACA">  y</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">type</span><span style="color:#C0CAF5"> Snake</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> Position</span><span style="color:#9ABDF5">[]</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">interface</span><span style="color:#C0CAF5"> GameState</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">  snake</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&#x3C;</span><span style="color:#C0CAF5">Snake</span><span style="color:#89DDFF">>;</span></span>
<span class="line"><span style="color:#73DACA">  direction</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&#x3C;</span><span style="color:#C0CAF5">Position</span><span style="color:#89DDFF">>;</span></span>
<span class="line"><span style="color:#73DACA">  food</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&#x3C;</span><span style="color:#C0CAF5">Position</span><span style="color:#89DDFF">>;</span></span>
<span class="line"><span style="color:#73DACA">  gameState</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&#x3C;</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">over</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">playing</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">>;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> useGameSnake</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> GameState</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> snake</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&#x3C;</span><span style="color:#C0CAF5">Snake</span><span style="color:#89DDFF">></span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">GameLogic</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">initializeSnake</span><span style="color:#9ABDF5">())</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> direction</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&#x3C;</span><span style="color:#C0CAF5">Position</span><span style="color:#89DDFF">></span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">({ </span><span style="color:#73DACA">x</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5"> })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> food</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&#x3C;</span><span style="color:#C0CAF5">Position</span><span style="color:#89DDFF">></span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">GameLogic</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">randomFoodPosition</span><span style="color:#9ABDF5">())</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> gameState</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> Ref</span><span style="color:#89DDFF">&#x3C;</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">over</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF"> |</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">playing</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">></span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">playing</span><span style="color:#89DDFF">"</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> gameInterval</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> number</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> null</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#7AA2F7"> startGame</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> ()</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> void</span><span style="color:#BB9AF7"> =></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    gameInterval</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> window</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">setInterval</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">      snake</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> GameLogic</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">moveSnake</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">snake</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> direction</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">GameLogic</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">isCollision</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">snake</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)) {</span></span>
<span class="line"><span style="color:#C0CAF5">        gameState</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">over</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">        if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">gameInterval</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> null</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#7AA2F7">          clearInterval</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">gameInterval</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">        }</span></span>
<span class="line"><span style="color:#9ABDF5">      } </span><span style="color:#BB9AF7">else</span><span style="color:#BB9AF7"> if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">GameLogic</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">isFoodEaten</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">snake</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> food</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">)) {</span></span>
<span class="line"><span style="color:#C0CAF5">        snake</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">push</span><span style="color:#9ABDF5">({ </span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">snake</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">[</span><span style="color:#C0CAF5">snake</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#89DDFF"> -</span><span style="color:#FF9E64"> 1</span><span style="color:#9ABDF5">] })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">        food</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> GameLogic</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">randomFoodPosition</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 100</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  onMounted</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">startGame</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">  onUnmounted</span><span style="color:#9ABDF5">(() </span><span style="color:#BB9AF7">=></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">gameInterval</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> null</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#7AA2F7">      clearInterval</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">gameInterval</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">snake</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> direction</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> food</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> gameState</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="import { onMounted, onUnmounted, ref, Ref } from &#x22;vue&#x22;;
import * as GameLogic from &#x22;./pureGameSnake&#x22;;

interface Position {
  x: number;
  y: number;
}

type Snake = Position[];

interface GameState {
  snake: Ref<Snake>;
  direction: Ref<Position>;
  food: Ref<Position>;
  gameState: Ref<&#x22;over&#x22; | &#x22;playing&#x22;>;
}

export function useGameSnake(): GameState {
  const snake: Ref<Snake> = ref(GameLogic.initializeSnake());
  const direction: Ref<Position> = ref({ x: 0, y: 0 });
  const food: Ref<Position> = ref(GameLogic.randomFoodPosition());
  const gameState: Ref<&#x22;over&#x22; | &#x22;playing&#x22;> = ref(&#x22;playing&#x22;);
  let gameInterval: number | null = null;

  const startGame = (): void => {
    gameInterval = window.setInterval(() => {
      snake.value = GameLogic.moveSnake(snake.value, direction.value);

      if (GameLogic.isCollision(snake.value)) {
        gameState.value = &#x22;over&#x22;;
        if (gameInterval !== null) {
          clearInterval(gameInterval);
        }
      } else if (GameLogic.isFoodEaten(snake.value, food.value)) {
        snake.value.push({ ...snake.value[snake.value.length - 1] });
        food.value = GameLogic.randomFoodPosition();
      }
    }, 100);
  };

  onMounted(startGame);

  onUnmounted(() => {
    if (gameInterval !== null) {
      clearInterval(gameInterval);
    }
  });

  return { snake, direction, food, gameState };
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="refactoring-gamesnakevue">Refactoring <code>gameSnake.vue</code><a class="heading-link" aria-label="Link to section" href="#refactoring-gamesnakevue"><span class="heading-link-icon">#</span></a></h3>
<p>Now, our <code>gameSnake.vue</code> is more focused, using <code>useGameSnake.ts</code> for managing state and reactivity, while the view remains within the template.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="vue"><code><span class="line"><span style="color:#BA3C97">&#x3C;</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">></span></span>
<span class="line"><span style="color:#BA3C97">  &#x3C;</span><span style="color:#F7768E">div</span><span style="color:#BB9AF7"> class</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">game-container</span><span style="color:#89DDFF">"</span><span style="color:#BA3C97">></span></span>
<span class="line"><span style="color:#BA3C97">    &#x3C;</span><span style="color:#F7768E">canvas</span><span style="color:#BB9AF7"> ref</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">canvas</span><span style="color:#89DDFF">"</span><span style="color:#BB9AF7"> width</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">400</span><span style="color:#89DDFF">"</span><span style="color:#BB9AF7"> height</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">400</span><span style="color:#89DDFF">"</span><span style="color:#BA3C97">>&#x3C;/</span><span style="color:#F7768E">canvas</span><span style="color:#BA3C97">></span></span>
<span class="line"><span style="color:#BA3C97">  &#x3C;/</span><span style="color:#F7768E">div</span><span style="color:#BA3C97">></span></span>
<span class="line"><span style="color:#BA3C97">&#x3C;/</span><span style="color:#F7768E">template</span><span style="color:#BA3C97">></span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&#x3C;</span><span style="color:#F7768E">script</span><span style="color:#BB9AF7"> setup</span><span style="color:#BB9AF7"> lang</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">ts</span><span style="color:#89DDFF">"</span><span style="color:#BA3C97">></span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">ref</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> onMounted</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> watch</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> onUnmounted</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">vue</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">useGameSnake</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">./useGameSnake.ts</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">gridSize</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">./pureGameSnake</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> snake</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> direction</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> food</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> gameState</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> useGameSnake</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> canvas</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&#x3C;</span><span style="color:#C0CAF5">HTMLCanvasElement</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">></span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> ctx</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> ref</span><span style="color:#89DDFF">&#x3C;</span><span style="color:#C0CAF5">CanvasRenderingContext2D</span><span style="color:#89DDFF"> |</span><span style="color:#0DB9D7"> null</span><span style="color:#89DDFF">></span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">null</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">let</span><span style="color:#BB9AF7"> lastDirection</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> {</span><span style="color:#73DACA"> x</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">onMounted</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">canvas</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> canvas</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">getContext</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">2d</span><span style="color:#89DDFF">"</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">    draw</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#C0CAF5">  window</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">addEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">keydown</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> handleKeydown</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">onUnmounted</span><span style="color:#9ABDF5">(()</span><span style="color:#BB9AF7"> =></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  window</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">removeEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">keydown</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> handleKeydown</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">watch</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">gameState</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> state</span><span style="color:#BB9AF7"> =></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">state</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">over</span><span style="color:#89DDFF">"</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#7AA2F7">    alert</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">Game Over</span><span style="color:#89DDFF">"</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> handleKeydown</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">e</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> KeyboardEvent</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  e</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">preventDefault</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">  switch</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">e</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">key</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">ArrowUp</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">lastDirection</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      direction</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">x</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> -</span><span style="color:#C0CAF5">gridSize</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">ArrowDown</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">lastDirection</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      direction</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">x</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">ArrowLeft</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">lastDirection</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      direction</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">x</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> -</span><span style="color:#C0CAF5">gridSize</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    case</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">ArrowRight</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">lastDirection</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#BB9AF7"> !==</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      direction</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">x</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#89DDFF">,</span><span style="color:#73DACA"> y</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      break</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#C0CAF5">  lastDirection</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> { </span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">direction</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7">watch</span><span style="color:#9ABDF5">(</span></span>
<span class="line"><span style="color:#9ABDF5">  [</span><span style="color:#7DCFFF">snake</span><span style="color:#89DDFF">,</span><span style="color:#7DCFFF"> food</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  ()</span><span style="color:#BB9AF7"> =></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    draw</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  {</span><span style="color:#73DACA"> deep</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#9ABDF5"> }</span></span>
<span class="line"><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> draw</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">clearRect</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 400</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 400</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  drawGrid</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  drawSnake</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  drawFood</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> drawGrid</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  ctx</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">strokeStyle</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">#ddd</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">  for</span><span style="color:#9ABDF5"> (</span><span style="color:#9D7CD8;font-style:italic">let</span><span style="color:#BB9AF7"> i</span><span style="color:#89DDFF"> =</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">;</span><span style="color:#C0CAF5"> i</span><span style="color:#BB9AF7"> &#x3C;=</span><span style="color:#FF9E64"> 400</span><span style="color:#89DDFF">;</span><span style="color:#C0CAF5"> i</span><span style="color:#89DDFF"> +=</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#9ABDF5">) {</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">beginPath</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">moveTo</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">i</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">lineTo</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">i</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 400</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">stroke</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">moveTo</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">0</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> i</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">lineTo</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">400</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> i</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">stroke</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> drawSnake</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  ctx</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">fillStyle</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">green</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  snake</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">forEach</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">segment</span><span style="color:#BB9AF7"> =></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">fillRect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">segment</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> segment</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> drawFood</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  ctx</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">fillStyle</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">red</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">  ctx</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">fillRect</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">food</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">x</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> food</span><span style="color:#89DDFF">.</span><span style="color:#C0CAF5">value</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">y</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> gridSize</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BA3C97">&#x3C;/</span><span style="color:#F7768E">script</span><span style="color:#BA3C97">></span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&#x3C;</span><span style="color:#F7768E">style</span><span style="color:#BA3C97">></span></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">game-container</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  display</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> flex</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  justify-content</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> center</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  align-items</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> center</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  height</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 100</span><span style="color:#F7768E">vh</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#BA3C97">&#x3C;/</span><span style="color:#F7768E">style</span><span style="color:#BA3C97">></span></span></code><button type="button" class="copy" data-code="<template>
  <div class=&#x22;game-container&#x22;>
    <canvas ref=&#x22;canvas&#x22; width=&#x22;400&#x22; height=&#x22;400&#x22;></canvas>
  </div>
</template>

<script setup lang=&#x22;ts&#x22;>
import { ref, onMounted, watch, onUnmounted } from &#x22;vue&#x22;;
import { useGameSnake } from &#x22;./useGameSnake.ts&#x22;;
import { gridSize } from &#x22;./pureGameSnake&#x22;;

const { snake, direction, food, gameState } = useGameSnake();
const canvas = ref<HTMLCanvasElement | null>(null);
const ctx = ref<CanvasRenderingContext2D | null>(null);
let lastDirection = { x: 0, y: 0 };

onMounted(() => {
  if (canvas.value) {
    ctx.value = canvas.value.getContext(&#x22;2d&#x22;);
    draw();
  }
  window.addEventListener(&#x22;keydown&#x22;, handleKeydown);
});

onUnmounted(() => {
  window.removeEventListener(&#x22;keydown&#x22;, handleKeydown);
});

watch(gameState, state => {
  if (state === &#x22;over&#x22;) {
    alert(&#x22;Game Over&#x22;);
  }
});

function handleKeydown(e: KeyboardEvent) {
  e.preventDefault();
  switch (e.key) {
    case &#x22;ArrowUp&#x22;:
      if (lastDirection.y !== 0) break;
      direction.value = { x: 0, y: -gridSize };
      break;
    case &#x22;ArrowDown&#x22;:
      if (lastDirection.y !== 0) break;
      direction.value = { x: 0, y: gridSize };
      break;
    case &#x22;ArrowLeft&#x22;:
      if (lastDirection.x !== 0) break;
      direction.value = { x: -gridSize, y: 0 };
      break;
    case &#x22;ArrowRight&#x22;:
      if (lastDirection.x !== 0) break;
      direction.value = { x: gridSize, y: 0 };
      break;
  }
  lastDirection = { ...direction.value };
}

watch(
  [snake, food],
  () => {
    draw();
  },
  { deep: true }
);

function draw() {
  if (!ctx.value) return;
  ctx.value.clearRect(0, 0, 400, 400);
  drawGrid();
  drawSnake();
  drawFood();
}

function drawGrid() {
  if (!ctx.value) return;
  ctx.value.strokeStyle = &#x22;#ddd&#x22;;
  for (let i = 0; i <= 400; i += gridSize) {
    ctx.value.beginPath();
    ctx.value.moveTo(i, 0);
    ctx.value.lineTo(i, 400);
    ctx.value.stroke();
    ctx.value.moveTo(0, i);
    ctx.value.lineTo(400, i);
    ctx.value.stroke();
  }
}

function drawSnake() {
  ctx.value.fillStyle = &#x22;green&#x22;;
  snake.value.forEach(segment => {
    ctx.value.fillRect(segment.x, segment.y, gridSize, gridSize);
  });
}

function drawFood() {
  ctx.value.fillStyle = &#x22;red&#x22;;
  ctx.value.fillRect(food.value.x, food.value.y, gridSize, gridSize);
}
</script>

<style>
.game-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<hr>
<h2 id="advantages-of-the-functional-core-imperative-shell-pattern">Advantages of the Functional Core, Imperative Shell Pattern<a class="heading-link" aria-label="Link to section" href="#advantages-of-the-functional-core-imperative-shell-pattern"><span class="heading-link-icon">#</span></a></h2>
<p>The Functional Core, Imperative Shell pattern enhances the <strong>testability</strong> and <strong>maintainability</strong> of Vue components. By separating the business logic from the framework-specific code, this pattern offers key advantages:</p>
<h3 id="simplified-testing">Simplified Testing<a class="heading-link" aria-label="Link to section" href="#simplified-testing"><span class="heading-link-icon">#</span></a></h3>
<p>Business logic combined with Vue’s reactivity and component structure makes testing complex. Traditional unit testing becomes challenging, leading to integration tests that lack precision. By extracting the core logic into pure functions (as in <code>pureGameSnake.ts</code>), we write focused unit tests for each function. This isolation streamlines testing, as each piece of logic operates independently of Vue’s reactivity system.</p>
<h3 id="enhanced-maintainability">Enhanced Maintainability<a class="heading-link" aria-label="Link to section" href="#enhanced-maintainability"><span class="heading-link-icon">#</span></a></h3>
<p>The Functional Core, Imperative Shell pattern creates a clear <strong>separation of concerns</strong>. Vue components focus on the user interface and reactivity, while the pure business logic lives in separate, framework-agnostic files. This separation improves code readability and understanding. Maintenance becomes straightforward as the application grows.</p>
<h3 id="framework-agnosticism">Framework Agnosticism<a class="heading-link" aria-label="Link to section" href="#framework-agnosticism"><span class="heading-link-icon">#</span></a></h3>
<p>A key advantage of this pattern is the <strong>portability</strong> of your business logic. The pure functions in the Functional Core remain independent of any UI framework. If you need to switch from Vue to another framework, or if Vue changes, your core logic remains intact. This flexibility protects your code against changes and shifts in technology.</p>
<h2 id="testing-complexities-in-traditional-vue-components-vs-functional-core-imperative-shell-pattern">Testing Complexities in Traditional Vue Components vs. Functional Core, Imperative Shell Pattern<a class="heading-link" aria-label="Link to section" href="#testing-complexities-in-traditional-vue-components-vs-functional-core-imperative-shell-pattern"><span class="heading-link-icon">#</span></a></h2>
<h3 id="challenges-in-testing-traditional-components">Challenges in Testing Traditional Components<a class="heading-link" aria-label="Link to section" href="#challenges-in-testing-traditional-components"><span class="heading-link-icon">#</span></a></h3>
<p>Testing traditional Vue components, where view, reactivity, and business logic combine, presents specific challenges. In such components, unit tests face these obstacles:</p>
<ul>
<li>Tests function more like integration tests, reducing precision</li>
<li>Vue’s reactivity system creates complex mocking requirements</li>
<li>Test coverage must span reactive behavior and side effects</li>
</ul>
<p>These challenges reduce confidence in tests and component stability.</p>
<h3 id="simplified-testing-with-functional-core-imperative-shell-pattern">Simplified Testing with Functional Core, Imperative Shell Pattern<a class="heading-link" aria-label="Link to section" href="#simplified-testing-with-functional-core-imperative-shell-pattern"><span class="heading-link-icon">#</span></a></h3>
<p>The Functional Core, Imperative Shell pattern transforms testing:</p>
<ul>
<li><strong>Isolated Business Logic</strong>: Pure functions in the Functional Core enable direct unit tests without Vue’s reactivity or component states.</li>
<li><strong>Predictable Outcomes</strong>: Pure functions deliver consistent outputs for given inputs.</li>
<li><strong>Clear Separation</strong>: The reactive and side-effect code stays in the Imperative Shell, enabling focused testing of Vue interactions.</li>
</ul>
<p>This approach creates a modular, testable codebase where each component undergoes thorough testing, improving reliability.</p>
<hr>
<h3 id="conclusion">Conclusion<a class="heading-link" aria-label="Link to section" href="#conclusion"><span class="heading-link-icon">#</span></a></h3>
<p>The Functional Core, Imperative Shell pattern strengthens Vue applications through improved testing and maintenance. It prepares your code for future changes and growth. While restructuring requires initial effort, the pattern delivers long-term benefits, making it valuable for Vue developers aiming to enhance their application’s architecture and quality.</p>
<p><img alt="Blog Conclusion Diagram" loading="lazy" decoding="async" fetchpriority="auto" width="3024" height="2088" src="/_astro/conclusionDiagram.RJuZzm-e_Z13kWSW.webp" ></p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_how-to-write-clean-vue-components" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="how-to-write-clean-vue-components" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vue</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/architecture/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">architecture</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/how-to-write-clean-vue-components/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/how-to-write-clean-vue-components/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/how-to-write-clean-vue-components/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/how-to-write-clean-vue-components/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/how-to-write-clean-vue-components/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/how-to-write-clean-vue-components/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/how-to-write-clean-vue-components/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/inline-vue-composables-refactoring/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">The Inline Vue Composables Refactoring pattern</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to apply Martin Fowler&#39;s Extract Function pattern to Vue components using inline composables, making your code cleaner and more maintainable. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-04-01T00:00:00.000Z">Apr 1, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/mastering-vue-3-composables-a-comprehensive-style-guide/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Mastering Vue 3 Composables: A Comprehensive Style Guide</h3> <p class="related-post-description astro-vj4tpspi"> Did you ever struggle how to write better composables in Vue? In this Blog post I try to give some tips how to do that </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2023-09-16T15:22:00.000Z">Sep 16, 2023</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/computed-inlining-refactoring-pattern-in-vue/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">The Computed Inlining Refactoring Pattern in Vue</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to improve Vue component performance and readability by applying the Computed Inlining pattern - a technique inspired by Martin Fowler&#39;s Inline Function pattern. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-04-03T00:00:00.000Z">Apr 3, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "how-to-write-clean-vue-components";

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
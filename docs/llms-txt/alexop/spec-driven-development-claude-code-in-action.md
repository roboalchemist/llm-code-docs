# Source: https://alexop.dev/posts/spec-driven-development-claude-code-in-action

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/spec-driven-development-claude-code-in-action/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Spec-Driven Development with Claude Code in Action | alexop.dev</title><meta name="title" content="Spec-Driven Development with Claude Code in Action | alexop.dev"><meta name="description" content="A practical workflow for tackling large refactors with Claude Code using parallel research subagents, written specs, and the new task system for context-efficient implementation."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Spec-Driven Development with Claude Code in Action | alexop.dev"><meta property="og:description" content="A practical workflow for tackling large refactors with Claude Code using parallel research subagents, written specs, and the new task system for context-efficient implementation."><meta property="og:url" content="https://alexop.dev/posts/spec-driven-development-claude-code-in-action/"><meta property="og:image" content="https://alexop.dev/posts/spec-driven-development-with-claude-code-in-action/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2026-02-01T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/spec-driven-development-claude-code-in-action/"><meta property="twitter:title" content="Spec-Driven Development with Claude Code in Action | alexop.dev"><meta property="twitter:description" content="A practical workflow for tackling large refactors with Claude Code using parallel research subagents, written specs, and the new task system for context-efficient implementation."><meta property="twitter:image" content="https://alexop.dev/posts/spec-driven-development-with-claude-code-in-action/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Spec-Driven Development with Claude Code in Action | alexop.dev","description":"A practical workflow for tackling large refactors with Claude Code using parallel research subagents, written specs, and the new task system for context-efficient implementation.","image":"https://alexop.dev/posts/spec-driven-development-with-claude-code-in-action/index.png","datePublished":"2026-02-01T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: spec-driven-development-with-claude-code-in-action; }@layer astro { ::view-transition-old(spec-driven-development-with-claude-code-in-action) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(spec-driven-development-with-claude-code-in-action) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(spec-driven-development-with-claude-code-in-action) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(spec-driven-development-with-claude-code-in-action) { 
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
</style><style>.internal-link-wrapper:where(.astro-3tyn5ojg){position:relative;display:inline-block}.internal-link:where(.astro-3tyn5ojg){--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));text-decoration-line:underline;text-decoration-style:dashed;text-decoration-thickness:1px;text-underline-offset:4px;transition-property:all;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.15s}.internal-link:where(.astro-3tyn5ojg):hover{text-decoration-style:solid}.internal-link:where(.astro-3tyn5ojg){cursor:pointer;display:inline}.preview-card:where(.astro-3tyn5ojg){display:block;position:absolute;bottom:calc(100% + 8px);left:50%;transform:translate(-50%);z-index:9999;width:320px;max-width:90vw;border-radius:.5rem;border-width:1px;--tw-border-opacity: 1;border-color:rgba(var(--color-border),var(--tw-border-opacity, 1));--tw-bg-opacity: 1;background-color:rgba(var(--color-card),var(--tw-bg-opacity, 1));--tw-shadow: 0 10px 15px -3px rgb(0 0 0 / .1), 0 4px 6px -4px rgb(0 0 0 / .1);--tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000),var(--tw-ring-shadow, 0 0 #0000),var(--tw-shadow);opacity:0;visibility:hidden;transition:opacity .2s ease-in-out,visibility .2s ease-in-out}.preview-card:where(.astro-3tyn5ojg).is-fixed{position:fixed!important;bottom:auto!important;top:var(--pc-top, 0px)!important;left:var(--pc-left, 0px)!important;transform:none!important}.preview-content:where(.astro-3tyn5ojg){display:block;padding:1rem}.preview-title:where(.astro-3tyn5ojg){display:block;margin-bottom:.5rem;font-size:1rem;line-height:1.5rem;font-weight:600;--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1));line-height:1.3}.preview-title:where(.astro-3tyn5ojg) .heading-link:where(.astro-3tyn5ojg){display:none!important}.preview-description:where(.astro-3tyn5ojg){display:block;margin-bottom:.75rem;font-size:.875rem;line-height:1.25rem;color:rgba(var(--color-text-base),.8);line-height:1.4;overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical}.preview-tags:where(.astro-3tyn5ojg){margin-bottom:.5rem;display:flex;flex-wrap:wrap;gap:.375rem}.preview-tag:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;background-color:rgba(var(--color-accent),.1);--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));font-weight:500}.preview-tag-more:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;--tw-bg-opacity: 1;background-color:rgba(var(--color-fill),var(--tw-bg-opacity, 1));color:rgba(var(--color-text-base),.6);font-weight:500}.preview-date:where(.astro-3tyn5ojg){font-size:.75rem;line-height:1rem;color:rgba(var(--color-text-base),.6);display:block;margin-top:8px;font-style:italic}.preview-card:where(.astro-3tyn5ojg):after{content:"";position:absolute;top:100%;left:50%;transform:translate(-50%);border:6px solid transparent;border-top-color:var(--color-card)}.preview-card:where(.astro-3tyn5ojg).is-fixed:after{display:none}
</style><style>.prompt-block:where(.astro-7uk2cqts){margin-top:1.25rem;margin-bottom:1.25rem;border-left-width:2px;border-color:rgba(var(--color-accent),.4);padding-left:1rem}.prompt-label:where(.astro-7uk2cqts){margin-bottom:.25rem;display:flex;align-items:center;gap:.25rem;font-size:.75rem;line-height:1rem;text-transform:uppercase;letter-spacing:.05em;color:rgba(var(--color-text-base),.5)}.prompt-chevron:where(.astro-7uk2cqts){font-size:.875rem;line-height:1.25rem;font-weight:700;color:rgba(var(--color-accent),.6)}.prompt-content:where(.astro-7uk2cqts){font-family:IBM Plex Mono,monospace;font-size:.875rem;line-height:1.25rem;line-height:1.625;color:rgba(var(--color-text-base),.9)}.prompt-content:where(.astro-7uk2cqts) p{margin:0}
</style><link rel="stylesheet" href="/_astro/ContextUsage_astro_astro_type_style_index_0_lang.9z0zpfaJ.css"><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: claude-code; }@layer astro { ::view-transition-old(claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(claude-code) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: local-first; }@layer astro { ::view-transition-old(local-first) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(local-first) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(local-first) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(local-first) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Spec-Driven Development with Claude Code in Action</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2026-02-01T00:00:00.000Z">Feb 1, 2026</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Z3L21c" prefix="r3" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Spec-Driven Development with Claude Code in Action&quot;],&quot;content&quot;:[0,&quot;import InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\nimport Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\nimport Figure from \&quot;@features/mdx-components/components/Figure.astro\&quot;;\nimport Prompt from \&quot;@features/mdx-components/components/Prompt.astro\&quot;;\nimport ContextUsage from \&quot;@features/llm-education/components/ContextUsage.astro\&quot;;\nimport specDrivenDevelopmentImg from \&quot;@assets/images/specClaude/spec-driven-development.png\&quot;;\nimport taskOrchestrationImg from \&quot;@assets/images/specClaude/task-orchestration.png\&quot;;\nimport ralphArchitectureImg from \&quot;@assets/images/specClaude/ralph-architecture.png\&quot;;\nimport researchPhaseImg from \&quot;@assets/images/specClaude/research-phase.png\&quot;;\nimport orchestratorFlowImg from \&quot;@assets/images/specClaude/orchestrator-flow.png\&quot;;\n\nI&#39;m building a [simplified sync engine from scratch](https://github.com/alexanderop/nuxt-sync-engine) using Nuxt 4.\nMy approach: study how production-grade frameworks solve the hard problems, then implement a minimal version myself.\n\n[Jazz](https://jazz.tools) is my primary reference a local-first framework with elegant patterns for persistence, conflict resolution, and cross-tab sync. Rather than reading through their codebase manually, \nI use Claude Code to research, extract patterns, and help me implement them.\n\nThis post documents the workflow I call **Spec-Driven Development with Claude Code** the exact prompts, tools, and patterns I used to migrate my storage layer from SQLite/WASM to IndexedDB in a single day.\n\n## The Problem\n\nMy sync engine was using `sql.js` (SQLite compiled to WASM) for client-side storage. It worked, but had issues:\n- Large WASM bundle (~1MB)\n- Complex COOP/COEP header requirements\n- No native cross-tab sync\n\nI wanted to migrate to IndexedDB, borrowing patterns from Jazz. But this was a significant refactor touching 15+ files. (For background on &lt;InternalLink slug=\&quot;what-is-local-first-web-development\&quot;&gt;local-first web development&lt;/InternalLink&gt; and why it matters, see my earlier post.)\n\n## The Workflow\n\nInstead of diving into code, I used Claude Code as an **AI development team**with myself as the product owner, Claude as the tech lead, and subagents as developers.\n\nImportant: I also cloned the source code of Jazz into my Project so Claude could reference it during research and implementation.\n\n&lt;Figure\n  src={specDrivenDevelopmentImg}\n  alt=\&quot;Spec-Driven Development workflow: Research Phase with parallel subagents, Spec Creation with written document, Refine with Q&amp;A interview pattern, and Implement with task-per-subagent\&quot;\n  caption=\&quot;The four phases of Spec-Driven Development with Claude Code\&quot;\n/&gt;\n\n## Phase 1: Research with Parallel Subagents\n\n### The Prompt\n\n&lt;Prompt&gt;\nyou have access to jazz source repo explain to me how they use\nindexdb in the client to persist state our project is using sqlite\nbut we want to change to indexdb with jazz your goal is to write\na report spin up multiple subagents for your research task\n&lt;/Prompt&gt;\n\n### What Happened\n\nClaude spawned **5 parallel research agents**, each investigating a specific aspect of Jazz:\n\n&lt;Alert type=\&quot;info\&quot; title=\&quot;No custom agents needed\&quot;&gt;\nThese are Claude Code&#39;s **built-in subagents**. The `Task` tool is a native tool in Claude Code, just like `Read` or `Bash`. When you ask Claude to \&quot;spin up subagents,\&quot; it uses this built-in tool automatically with the `general-purpose` subagent type. No custom agent definition or setup is required.\n&lt;/Alert&gt;\n\n&lt;Figure\n  src={researchPhaseImg}\n  alt=\&quot;Research Phase: Five parallel agents (CRDT, WebSocket, Push/Pull, Storage, Architecture) each investigating independently, converging into a consolidated research report\&quot;\n  caption=\&quot;Parallel research agents converging into a consolidated report\&quot;\n/&gt;\n\nEach agent explored the Jazz codebase independently and reported back:\n\n| Agent | Focus | Key Findings |\n|-------|-------|--------------|\n| CRDT | Data structures | CoMap, CoList use operation-based CRDTs with LWW |\n| WebSocket | Real-time sync | 4-message protocol: load, known, content, done |\n| Push/Pull | Sync strategy | Hybrid model with known-state tracking |\n| Storage | Persistence | IndexedDB with `coValues`, `sessions`, `transactions` stores |\n| Architecture | Overall design | Monorepo with platform adapters |\n\n### Follow-up Prompt\n\n&lt;Prompt&gt;\nresearch longer and improve the plan\n&lt;/Prompt&gt;\n\nThis triggered deeper investigation into edge cases and implementation details.\n\n## Phase 2: Spec Creation\n\nAfter research, Claude wrote a comprehensive technical specification to `docs/indexeddb-migration-spec.md`:\n[Full spec](https://gist.github.com/alexanderop/70ef80ac6dda5166c5085cc9bb269df1)\n\n```markdown\n# IndexedDB Migration Specification\n\n## Part 1: How Jazz Uses IndexedDB\n- Database schema (coValues, sessions, transactions stores)\n- Transaction queuing pattern\n- Entity caching layer\n- Session-based conflict resolution\n\n## Part 2: Current SQLite Architecture Analysis\n- sql.js WASM setup\n- Existing sync protocol\n- Pain points and limitations\n\n## Part 3: Migration Plan (4 Phases)\n- Phase 1: Core IndexedDB utilities\n- Phase 2: Composables layer\n- Phase 3: Cross-tab sync\n- Phase 4: Cleanup and testing\n\n## Part 4: Implementation Checklist\n- [ ] idb-helpers.ts\n- [ ] useIndexedDB.ts\n- [ ] useSessionTracking.ts\n- ... (14 items total)\n```\n\n**Key insight**: The spec becomes the source of truth. It&#39;s a document Claude can reference during implementation, ensuring consistency across all tasks.\nIt also becomes a Pin that we can use if something went wrong during implementation.\n\n## Phase 3: Spec Refinement via Interview\n\nBefore implementation, I wanted to ensure the spec was solid. I used Claude&#39;s `AskUserQuestion` tool:\n\n### The Prompt\n\n&lt;Prompt&gt;\nuse the ask_user_question tool do you have any questions regarding\n@docs/indexeddb-migration-spec.md before we implement it we want\nto improve the specs\n&lt;/Prompt&gt;\n\nClaude asked clarifying questions:\n- Should we support migration from existing SQLite data?\n- What&#39;s the preferred conflict resolution strategy?\n- Should cross-tab sync use BroadcastChannel or SharedWorker?\n\nAfter answering, I requested Vue-specific improvements:\n\n&lt;Prompt&gt;\nwe want to use provide and inject you have access to the source\ncode of pinia spin up multiple subagents how they do it so we can\nuse same patterns\n&lt;/Prompt&gt;\n\nClaude researched Pinia&#39;s patterns and updated the spec with:\n- Symbol-based injection keys\n- Provider composables with fallback patterns\n- Proper cleanup on unmount\n\n## Phase 4: Implementation with Task Delegation\n\nThis is where the new **Claude Code Task System** shines. (If you&#39;re unfamiliar with subagents and how they work in Claude Code, my &lt;InternalLink slug=\&quot;claude-code-customization-guide-claudemd-skills-subagents\&quot;&gt;customization guide&lt;/InternalLink&gt; covers the fundamentals.)\n\n### The Prompt\n\n&lt;Prompt&gt;\nimplement @docs/indexeddb-migration-spec.md use the task tool and\neach task should only be done by a subagent so that context is\nclear after each task do a commit before you continue you are the\nmain agent and your subagents are your devs\n&lt;/Prompt&gt;\n\n### Understanding Claude Code&#39;s Task System\n\nClaude Code&#39;s task systeminspired by [Beads](https://github.com/beads-ai/beads), Steve Yegge&#39;s distributed git-backed issue trackersolves two critical problems with AI coding agents:\n\n**Agent Amnesia**: Starting a new session mid-task loses all progress unless you manually document remaining work.\n\n**Context Pollution**: A full context window makes the agent drop discovered bugs instead of tracking them.\n\nThe previous todo list lived in session memory and vanished on restart. The new task system persists tasks to disk, making them shareable across sessions and subagents.\n\n### How Tasks Persist\n\nTasks are stored in `.claude/tasks/{session-id}/` as JSON files:\n\n```json\n{\n  \&quot;id\&quot;: \&quot;task-1\&quot;,\n  \&quot;subject\&quot;: \&quot;Create idb-helpers.ts\&quot;,\n  \&quot;description\&quot;: \&quot;Implement IndexedDB promise wrappers...\&quot;,\n  \&quot;status\&quot;: \&quot;pending | in_progress | completed\&quot;,\n  \&quot;blocks\&quot;: [\&quot;task-3\&quot;, \&quot;task-4\&quot;],\n  \&quot;blockedBy\&quot;: [\&quot;task-0\&quot;]\n}\n```\n\n### The Four Task Tools\n\n| Tool | Purpose |\n|------|---------|\n| `TaskCreate` | Create a new task with subject, description, and dependencies |\n| `TaskUpdate` | Update status (pending → in_progress → completed) or modify dependencies |\n| `TaskList` | View all tasks, their status, and what&#39;s blocked |\n| `TaskGet` | Get full details of a specific task including description |\n\n### Task System Architecture\n\n&lt;Figure\n  src={taskOrchestrationImg}\n  alt=\&quot;Task Orchestration: Main Session orchestrator connects to Task List in .claude/tasks/, which delegates to Subagent 1, 2, and 3 each with fresh context. Below shows a dependency graph with Wave 1 (T1, T2, T3 in parallel), Wave 2 (T4, T5, T6 dependent), and Wave 3 (T7)\&quot;\n  caption=\&quot;Task orchestration with dependency-aware parallel execution\&quot;\n/&gt;\n\n### Why Subagents + Tasks = Context Efficiency\n\nBy delegating each task to a subagent, the main session stays leanit only handles orchestration (creating tasks, tracking progress, committing). Each subagent gets a fresh context window focused entirely on its specific task, reads what it needs, implements, and returns. This means the main agent won&#39;t run out of context even for larger refactors with dozens of tasks.\n\nFor truly massive projects spanning days or weeks, a full autonomous agent like [Ralph](https://ghuntley.com/ralph/) would be more appropriate. Ralph is elegantly simplea bash loop that feeds a markdown file into Claude Code repeatedly:\n\n&lt;Figure\n  src={ralphArchitectureImg}\n  alt=\&quot;Ralph Architecture: A bash loop (while :; do cat PROMPT.md | claude-code ; done) where PROMPT.md feeds into Claude Code which produces output, and the loop continues indefinitely\&quot;\n  caption=\&quot;Ralph&#39;s stateless architecture using markdown as persistent memory\&quot;\n/&gt;\n\nThe key difference: Ralph executes each iteration in a completely new Claude session, using the markdown file as the only persistent memory. This makes it truly stateless and capable of running for days.\n\nThis spec-driven approach hits a middle ground: subagents get fresh context but the main orchestrator maintains state within a single session. Structured enough to maintain coherence, flexible enough to handle complexity, without the setup overhead of a full autonomous system.\n\n### The Execution Flow\n\n&lt;Figure\n  src={orchestratorFlowImg}\n  alt=\&quot;Main Agent Orchestrator flow: TaskCreate spawns Subagent 1 which implements and returns, then TaskUpdate marks complete and commits, then TaskCreate spawns Subagent 2 with dependencies, repeating for all tasks\&quot;\n  caption=\&quot;The orchestrator delegates each task to a subagent with atomic commits\&quot;\n  size=\&quot;medium\&quot;\n/&gt;\n\n### Why This Pattern Works\n\n1. **Context isolation**: Each subagent starts fresh, reading only what it needsno accumulated cruft\n2. **Persistent progress**: Tasks survive session restarts; pick up where you left off\n3. **Dependency-aware parallelism**: Claude identifies which tasks can run concurrently\n4. **Atomic commits**: Every task = one commit, making rollbacks trivial\n5. **Spec as contract**: Subagents reference the spec, ensuring consistency\n\n### Backpressure: Let the System Catch Mistakes\n\nOne crucial element that makes atomic commits powerful: [backpressure](https://banay.me/dont-waste-your-backpressure/). Instead of manually reviewing every change, set up pre-commit hooks that run tests, linting, and type checking automatically.\n\n```bash\n# .husky/pre-commit\npnpm typecheck &amp;&amp; pnpm lint &amp;&amp; pnpm test-run\n```\n\nWhen a subagent commits, the hook runs immediately. If tests fail, the commit is rejected and the agent sees the error outputgiving it a chance to self-correct before moving on. This creates automated feedback that catches issues at the source rather than accumulating bugs across multiple tasks.\n\nThe result: you stop being the bottleneck for quality control. The system validates correctness while you focus on higher-level decisions.\n\n### When Things Go Wrong\n\nThe first execution wasn&#39;t perfectI started the project and hit some errors. But here&#39;s where the spec pays off: I opened a new chat, pinned the spec document, pasted the error, and Claude fixed it immediately. No context rebuilding, no re-explaining the architecture.\n\nThe spec acts as a recovery point. When a session goes sideways or context gets polluted, you don&#39;t lose everythingyou have a document that captures the full intent and design decisions.\n\n### The Results\n\nAfter ~45 minutes:\n\n```\n$ git log-oneline | head20\n\n9dc1c96 refactor: clean up code structure\n9fce16b feat(storage): migrate from SQLite to IndexedDB\n835c494 feat: integrate IDB sync engine provider\nd2cd7b7 refactor: remove SQLite/sql.js dependencies\n2fb7656 feat: add browser mode test stubs\n... (14 commits total)\n```\n\n**14 tasks completed**, **14 commits**, **15+ files changed**, **one PR ready for review**. See the [full pull request](https://github.com/alexanderop/nuxt-sync-engine/pull/3) (includes additional manual changes).\n\nAnd despite orchestrating 14 subagents, the main session&#39;s context stayed manageable:\n\n&lt;ContextUsage\n  model=\&quot;claude-opus-4-5-20251101\&quot;\n  used=\&quot;143k\&quot;\n  total=\&quot;200k\&quot;\n  percent={71}\n  categories={[\n    { name: \&quot;System prompt\&quot;, tokens: \&quot;2.8k\&quot;, percent: 1.4, color: \&quot;system-prompt\&quot; },\n    { name: \&quot;System tools\&quot;, tokens: \&quot;16.2k\&quot;, percent: 8.1, color: \&quot;system-tools\&quot; },\n    { name: \&quot;MCP tools\&quot;, tokens: \&quot;293\&quot;, percent: 0.1, color: \&quot;mcp-tools\&quot; },\n    { name: \&quot;Custom agents\&quot;, tokens: \&quot;641\&quot;, percent: 0.3, color: \&quot;custom-agents\&quot; },\n    { name: \&quot;Memory files\&quot;, tokens: \&quot;431\&quot;, percent: 0.2, color: \&quot;memory-files\&quot; },\n    { name: \&quot;Skills\&quot;, tokens: \&quot;1.6k\&quot;, percent: 0.8, color: \&quot;skills\&quot; },\n    { name: \&quot;Messages\&quot;, tokens: \&quot;122.9k\&quot;, percent: 61.4, color: \&quot;messages\&quot; },\n    { name: \&quot;Free space\&quot;, tokens: \&quot;22k\&quot;, percent: 11.1, color: \&quot;free\&quot; },\n    { name: \&quot;Autocompact buffer\&quot;, tokens: \&quot;33.0k\&quot;, percent: 16.5, color: \&quot;buffer\&quot; },\n  ]}\n/&gt;\n\nThis proves the delegation pattern worksthe main agent handled orchestration while subagents did the heavy lifting in isolated contexts.\n\n## The Prompt Patterns\n\nHere are the key prompt patterns that make this workflow effective:\n\n### 1. Parallel Research\n\n&lt;Prompt&gt;\nspin up multiple subagents for your research task\n&lt;/Prompt&gt;\n\nTriggers Claude to spawn parallel agents, each investigating independently. Much faster than sequential research.\n\n### 2. Spec-First Development\n\n&lt;Prompt&gt;\nyour goal is to write a report/document\n&lt;/Prompt&gt;\n\nForces Claude to produce a written artifact before any code. This becomes the source of truth.\n\n### 3. Interview Before Implementation\n\n&lt;Prompt&gt;\nuse the ask_user_question tool... before we implement\n&lt;/Prompt&gt;\n\nSurfaces ambiguities and design decisions before they become bugs.\n\n### 4. Task Delegation with Commits\n\n&lt;Prompt&gt;\nuse the task tool and each task should only be done by a subagent\nafter each task do a commit before you continue\n&lt;/Prompt&gt;\n\nCreates the orchestration pattern with atomic commits.\n\n### 5. Role Assignment\n\n&lt;Prompt&gt;\nyou are the main agent and your subagents are your devs\n&lt;/Prompt&gt;\n\nSets expectations for how Claude should behaveas a coordinator, not a solo implementer.\n\n## Comparison: Traditional vs Spec-Driven\n\n| | Traditional AI Coding | Spec-Driven Development |\n|---|---|---|\n| **Flow** | Prompt → Code → Debug → Repeat | Research → Spec → Refine → Tasks → Done |\n| **Context** | Fills up with failed attempts | Each task gets fresh context |\n| **Memory** | No persistence across sessions | Spec is persistent source of truth |\n| **Bug tracking** | Discovered late, forgotten | Bugs become new tasks |\n| **Completion** | No clear stopping point | Clear completion criteria |\n\n## Advanced: Multi-Session Workflows\n\nThe task system supports coordination across multiple Claude Code sessions. Set a shared task list ID:\n\n```bash\nCLAUDE_CODE_TASK_LIST_ID=myproject claude\n```\n\nOr add to `.claude/settings.json`:\n\n```json\n{\n  \&quot;env\&quot;: {\n    \&quot;CLAUDE_CODE_TASK_LIST_ID\&quot;: \&quot;myproject\&quot;\n  }\n}\n```\n\nOne session acts as **orchestrator**; another becomes a **checker** that monitors completed tasks, verifies implementation quality, and adds follow-up tasks for anything missing.\n\n## When to Use This Workflow\n\nThis pattern excels for:\n\n- **Large refactors** touching many files\n- **Migrations** requiring research into external codebases\n- **Feature implementations** with unclear requirements\n- **Learning new libraries** by studying their source\n\nIt&#39;s overkill for:\n\n- Small bug fixes\n- Single-file changes\n- Well-defined, simple features\n\n## The Tools You Need\n\n1. **Claude Code CLI** (latest version with task tools)\n2. **A spec document** (markdown works great)\n3. **Reference codebases** if learning from existing implementations\n4. **Git** for atomic commits\n\n## Further Reading\n\n- [Beads](https://github.com/beads-ai/beads) Steve Yegge&#39;s git-backed issue tracker that inspired the task system\n- [12 Factor Agents](https://www.humanlayer.dev/blog/12-factor-agents) Design principles for AI coding agents\n- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) Anthropic&#39;s research on agent architectures\n- For a broader overview of Claude Code&#39;s feature stack, see my &lt;InternalLink slug=\&quot;understanding-claude-code-full-stack\&quot;&gt;comprehensive guide&lt;/InternalLink&gt;\n\n## Conclusion\n\nSpec-Driven Development with Claude Code mirrors real engineering workflows: parallel work, handoffs, blockers, and dependencies. Instead of treating Claude as a solo coder, you treat it as a team.\n\nThe key insight from Beads applies here:\n\n&gt; \&quot;By having each task that you give a coding agent isolated into its own context window, you can now give it the ability to log any bugs for later.\&quot;\n\nThe SQLite to IndexedDB migration would have taken me 2-3 days manually. With this workflow, it took one afternoonand produced better code thanks to the research phase uncovering patterns from Jazz I wouldn&#39;t have found on my own.\n\n---\n\n*Try it yourself: Start your next significant feature with \&quot;write a spec for X, spin up subagents for research\&quot; and see how it changes your workflow.*&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>I’m building a <a href="https://github.com/alexanderop/nuxt-sync-engine" rel="noopener noreferrer" target="_blank">simplified sync engine from scratch</a> using Nuxt 4.
My approach: study how production-grade frameworks solve the hard problems, then implement a minimal version myself.</p>
<p><a href="https://jazz.tools" rel="noopener noreferrer" target="_blank">Jazz</a> is my primary reference a local-first framework with elegant patterns for persistence, conflict resolution, and cross-tab sync. Rather than reading through their codebase manually,
I use Claude Code to research, extract patterns, and help me implement them.</p>
<p>This post documents the workflow I call <strong>Spec-Driven Development with Claude Code</strong> the exact prompts, tools, and patterns I used to migrate my storage layer from SQLite/WASM to IndexedDB in a single day.</p>
<h2 id="the-problem">The Problem<a class="heading-link" aria-label="Link to section" href="#the-problem"><span class="heading-link-icon">#</span></a></h2>
<p>My sync engine was using <code>sql.js</code> (SQLite compiled to WASM) for client-side storage. It worked, but had issues:</p>
<ul>
<li>Large WASM bundle (~1MB)</li>
<li>Complex COOP/COEP header requirements</li>
<li>No native cross-tab sync</li>
</ul>
<p>I wanted to migrate to IndexedDB, borrowing patterns from Jazz. But this was a significant refactor touching 15+ files. (For background on <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/what-is-local-first-web-development/" class="internal-link astro-3tyn5ojg"> local-first web development </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">What is Local-first Web Development?</span> <span class="preview-description astro-3tyn5ojg">What is local-first software and why does it matter? This guide covers local-first architecture, offline-capable apps with automatic sync, data ownership, and how to build a local-first web app with Vue step by step.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">local-first</span><span class="preview-tag astro-3tyn5ojg">architecture</span><span class="preview-tag astro-3tyn5ojg">vue</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">May 29, 2024</time> </span> </span> </span>  <script>
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
</script> and why it matters, see my earlier post.)</p>
<h2 id="the-workflow">The Workflow<a class="heading-link" aria-label="Link to section" href="#the-workflow"><span class="heading-link-icon">#</span></a></h2>
<p>Instead of diving into code, I used Claude Code as an <strong>AI development team</strong>with myself as the product owner, Claude as the tech lead, and subagents as developers.</p>
<p>Important: I also cloned the source code of Jazz into my Project so Claude could reference it during research and implementation.</p>
<figure class=" mx-auto "> <img src="/_astro/spec-driven-development.EL8Gt6jf_2jQara.webp" alt="Spec-Driven Development workflow: Research Phase with parallel subagents, Spec Creation with written document, Refine with Q&#38;A interview pattern, and Implement with task-per-subagent" loading="lazy" decoding="async" fetchpriority="auto" width="1840" height="640" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> The four phases of Spec-Driven Development with Claude Code </figcaption> </figure>
<h2 id="phase-1-research-with-parallel-subagents">Phase 1: Research with Parallel Subagents<a class="heading-link" aria-label="Link to section" href="#phase-1-research-with-parallel-subagents"><span class="heading-link-icon">#</span></a></h2>
<h3 id="the-prompt">The Prompt<a class="heading-link" aria-label="Link to section" href="#the-prompt"><span class="heading-link-icon">#</span></a></h3>
<div class="prompt-block astro-7uk2cqts"> <span class="prompt-label astro-7uk2cqts"> <span class="prompt-chevron astro-7uk2cqts">›</span> Prompt </span> <div class="prompt-content astro-7uk2cqts"> <p>you have access to jazz source repo explain to me how they use
indexdb in the client to persist state our project is using sqlite
but we want to change to indexdb with jazz your goal is to write
a report spin up multiple subagents for your research task</p> </div> </div> 
<h3 id="what-happened">What Happened<a class="heading-link" aria-label="Link to section" href="#what-happened"><span class="heading-link-icon">#</span></a></h3>
<p>Claude spawned <strong>5 parallel research agents</strong>, each investigating a specific aspect of Jazz:</p>
<div class="alert alert-info astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl"></span> No custom agents needed </p> <div class="alert-content astro-7kdbuayl"> <p>These are Claude Code’s <strong>built-in subagents</strong>. The <code>Task</code> tool is a native tool in Claude Code, just like <code>Read</code> or <code>Bash</code>. When you ask Claude to “spin up subagents,” it uses this built-in tool automatically with the <code>general-purpose</code> subagent type. No custom agent definition or setup is required.</p> </div> </div> 
<figure class=" mx-auto "> <img src="/_astro/research-phase.DfqUpCdn_Z1eotCM.webp" alt="Research Phase: Five parallel agents (CRDT, WebSocket, Push/Pull, Storage, Architecture) each investigating independently, converging into a consolidated research report" loading="lazy" decoding="async" fetchpriority="auto" width="1790" height="1309" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> Parallel research agents converging into a consolidated report </figcaption> </figure>
<p>Each agent explored the Jazz codebase independently and reported back:</p>



































<table><thead><tr><th>Agent</th><th>Focus</th><th>Key Findings</th></tr></thead><tbody><tr><td data-label="Agent">CRDT</td><td data-label="Focus">Data structures</td><td data-label="Key Findings">CoMap, CoList use operation-based CRDTs with LWW</td></tr><tr><td data-label="Agent">WebSocket</td><td data-label="Focus">Real-time sync</td><td data-label="Key Findings">4-message protocol: load, known, content, done</td></tr><tr><td data-label="Agent">Push/Pull</td><td data-label="Focus">Sync strategy</td><td data-label="Key Findings">Hybrid model with known-state tracking</td></tr><tr><td data-label="Agent">Storage</td><td data-label="Focus">Persistence</td><td data-label="Key Findings">IndexedDB with <code>coValues</code>, <code>sessions</code>, <code>transactions</code> stores</td></tr><tr><td data-label="Agent">Architecture</td><td data-label="Focus">Overall design</td><td data-label="Key Findings">Monorepo with platform adapters</td></tr></tbody></table>
<h3 id="follow-up-prompt">Follow-up Prompt<a class="heading-link" aria-label="Link to section" href="#follow-up-prompt"><span class="heading-link-icon">#</span></a></h3>
<div class="prompt-block astro-7uk2cqts"> <span class="prompt-label astro-7uk2cqts"> <span class="prompt-chevron astro-7uk2cqts">›</span> Prompt </span> <div class="prompt-content astro-7uk2cqts"> <p>research longer and improve the plan</p> </div> </div> 
<p>This triggered deeper investigation into edge cases and implementation details.</p>
<h2 id="phase-2-spec-creation">Phase 2: Spec Creation<a class="heading-link" aria-label="Link to section" href="#phase-2-spec-creation"><span class="heading-link-icon">#</span></a></h2>
<p>After research, Claude wrote a comprehensive technical specification to <code>docs/indexeddb-migration-spec.md</code>:
<a href="https://gist.github.com/alexanderop/70ef80ac6dda5166c5085cc9bb269df1" rel="noopener noreferrer" target="_blank">Full spec</a></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> IndexedDB Migration Specification</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Part 1: How Jazz Uses IndexedDB</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Database schema (coValues, sessions, transactions stores)</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Transaction queuing pattern</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Entity caching layer</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Session-based conflict resolution</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Part 2: Current SQLite Architecture Analysis</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> sql.js WASM setup</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Existing sync protocol</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Pain points and limitations</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Part 3: Migration Plan (4 Phases)</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Phase 1: Core IndexedDB utilities</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Phase 2: Composables layer</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Phase 3: Cross-tab sync</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Phase 4: Cleanup and testing</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Part 4: Implementation Checklist</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> [ ] idb-helpers.ts</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> [ ] useIndexedDB.ts</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> [ ] useSessionTracking.ts</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> ... (14 items total)</span></span></code><button type="button" class="copy" data-code="# IndexedDB Migration Specification

## Part 1: How Jazz Uses IndexedDB
- Database schema (coValues, sessions, transactions stores)
- Transaction queuing pattern
- Entity caching layer
- Session-based conflict resolution

## Part 2: Current SQLite Architecture Analysis
- sql.js WASM setup
- Existing sync protocol
- Pain points and limitations

## Part 3: Migration Plan (4 Phases)
- Phase 1: Core IndexedDB utilities
- Phase 2: Composables layer
- Phase 3: Cross-tab sync
- Phase 4: Cleanup and testing

## Part 4: Implementation Checklist
- [ ] idb-helpers.ts
- [ ] useIndexedDB.ts
- [ ] useSessionTracking.ts
- ... (14 items total)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Key insight</strong>: The spec becomes the source of truth. It’s a document Claude can reference during implementation, ensuring consistency across all tasks.
It also becomes a Pin that we can use if something went wrong during implementation.</p>
<h2 id="phase-3-spec-refinement-via-interview">Phase 3: Spec Refinement via Interview<a class="heading-link" aria-label="Link to section" href="#phase-3-spec-refinement-via-interview"><span class="heading-link-icon">#</span></a></h2>
<p>Before implementation, I wanted to ensure the spec was solid. I used Claude’s <code>AskUserQuestion</code> tool:</p>
<h3 id="the-prompt-1">The Prompt<a class="heading-link" aria-label="Link to section" href="#the-prompt-1"><span class="heading-link-icon">#</span></a></h3>
<div class="prompt-block astro-7uk2cqts"> <span class="prompt-label astro-7uk2cqts"> <span class="prompt-chevron astro-7uk2cqts">›</span> Prompt </span> <div class="prompt-content astro-7uk2cqts"> <p>use the ask_user_question tool do you have any questions regarding
@docs/indexeddb-migration-spec.md before we implement it we want
to improve the specs</p> </div> </div> 
<p>Claude asked clarifying questions:</p>
<ul>
<li>Should we support migration from existing SQLite data?</li>
<li>What’s the preferred conflict resolution strategy?</li>
<li>Should cross-tab sync use BroadcastChannel or SharedWorker?</li>
</ul>
<p>After answering, I requested Vue-specific improvements:</p>
<div class="prompt-block astro-7uk2cqts"> <span class="prompt-label astro-7uk2cqts"> <span class="prompt-chevron astro-7uk2cqts">›</span> Prompt </span> <div class="prompt-content astro-7uk2cqts"> <p>we want to use provide and inject you have access to the source
code of pinia spin up multiple subagents how they do it so we can
use same patterns</p> </div> </div> 
<p>Claude researched Pinia’s patterns and updated the spec with:</p>
<ul>
<li>Symbol-based injection keys</li>
<li>Provider composables with fallback patterns</li>
<li>Proper cleanup on unmount</li>
</ul>
<h2 id="phase-4-implementation-with-task-delegation">Phase 4: Implementation with Task Delegation<a class="heading-link" aria-label="Link to section" href="#phase-4-implementation-with-task-delegation"><span class="heading-link-icon">#</span></a></h2>
<p>This is where the new <strong>Claude Code Task System</strong> shines. (If you’re unfamiliar with subagents and how they work in Claude Code, my <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/claude-code-customization-guide-claudemd-skills-subagents/" class="internal-link astro-3tyn5ojg"> customization guide </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents</span> <span class="preview-description astro-3tyn5ojg">The complete guide to customizing Claude Code. Compare CLAUDE.md, slash commands, skills, and subagents with practical examples showing when to use each.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">tooling</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Dec 21, 2025</time> </span> </span> </span>  <script>
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
</script> covers the fundamentals.)</p>
<h3 id="the-prompt-2">The Prompt<a class="heading-link" aria-label="Link to section" href="#the-prompt-2"><span class="heading-link-icon">#</span></a></h3>
<div class="prompt-block astro-7uk2cqts"> <span class="prompt-label astro-7uk2cqts"> <span class="prompt-chevron astro-7uk2cqts">›</span> Prompt </span> <div class="prompt-content astro-7uk2cqts"> <p>implement @docs/indexeddb-migration-spec.md use the task tool and
each task should only be done by a subagent so that context is
clear after each task do a commit before you continue you are the
main agent and your subagents are your devs</p> </div> </div> 
<h3 id="understanding-claude-codes-task-system">Understanding Claude Code’s Task System<a class="heading-link" aria-label="Link to section" href="#understanding-claude-codes-task-system"><span class="heading-link-icon">#</span></a></h3>
<p>Claude Code’s task systeminspired by <a href="https://github.com/beads-ai/beads" rel="noopener noreferrer" target="_blank">Beads</a>, Steve Yegge’s distributed git-backed issue trackersolves two critical problems with AI coding agents:</p>
<p><strong>Agent Amnesia</strong>: Starting a new session mid-task loses all progress unless you manually document remaining work.</p>
<p><strong>Context Pollution</strong>: A full context window makes the agent drop discovered bugs instead of tracking them.</p>
<p>The previous todo list lived in session memory and vanished on restart. The new task system persists tasks to disk, making them shareable across sessions and subagents.</p>
<h3 id="how-tasks-persist">How Tasks Persist<a class="heading-link" aria-label="Link to section" href="#how-tasks-persist"><span class="heading-link-icon">#</span></a></h3>
<p>Tasks are stored in <code>.claude/tasks/{session-id}/</code> as JSON files:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">id</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">task-1</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">subject</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Create idb-helpers.ts</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">description</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Implement IndexedDB promise wrappers...</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">status</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">pending | in_progress | completed</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">blocks</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">task-3</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">task-4</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">blockedBy</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">task-0</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;id&#34;: &#34;task-1&#34;,
  &#34;subject&#34;: &#34;Create idb-helpers.ts&#34;,
  &#34;description&#34;: &#34;Implement IndexedDB promise wrappers...&#34;,
  &#34;status&#34;: &#34;pending | in_progress | completed&#34;,
  &#34;blocks&#34;: [&#34;task-3&#34;, &#34;task-4&#34;],
  &#34;blockedBy&#34;: [&#34;task-0&#34;]
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="the-four-task-tools">The Four Task Tools<a class="heading-link" aria-label="Link to section" href="#the-four-task-tools"><span class="heading-link-icon">#</span></a></h3>

























<table><thead><tr><th>Tool</th><th>Purpose</th></tr></thead><tbody><tr><td data-label="Tool"><code>TaskCreate</code></td><td data-label="Purpose">Create a new task with subject, description, and dependencies</td></tr><tr><td data-label="Tool"><code>TaskUpdate</code></td><td data-label="Purpose">Update status (pending → in_progress → completed) or modify dependencies</td></tr><tr><td data-label="Tool"><code>TaskList</code></td><td data-label="Purpose">View all tasks, their status, and what’s blocked</td></tr><tr><td data-label="Tool"><code>TaskGet</code></td><td data-label="Purpose">Get full details of a specific task including description</td></tr></tbody></table>
<h3 id="task-system-architecture">Task System Architecture<a class="heading-link" aria-label="Link to section" href="#task-system-architecture"><span class="heading-link-icon">#</span></a></h3>
<figure class=" mx-auto "> <img src="/_astro/task-orchestration.kPR51Ibt_23Fy12.webp" alt="Task Orchestration: Main Session orchestrator connects to Task List in .claude/tasks/, which delegates to Subagent 1, 2, and 3 each with fresh context. Below shows a dependency graph with Wave 1 (T1, T2, T3 in parallel), Wave 2 (T4, T5, T6 dependent), and Wave 3 (T7)" loading="lazy" decoding="async" fetchpriority="auto" width="1640" height="1440" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> Task orchestration with dependency-aware parallel execution </figcaption> </figure>
<h3 id="why-subagents--tasks--context-efficiency">Why Subagents + Tasks = Context Efficiency<a class="heading-link" aria-label="Link to section" href="#why-subagents--tasks--context-efficiency"><span class="heading-link-icon">#</span></a></h3>
<p>By delegating each task to a subagent, the main session stays leanit only handles orchestration (creating tasks, tracking progress, committing). Each subagent gets a fresh context window focused entirely on its specific task, reads what it needs, implements, and returns. This means the main agent won’t run out of context even for larger refactors with dozens of tasks.</p>
<p>For truly massive projects spanning days or weeks, a full autonomous agent like <a href="https://ghuntley.com/ralph/" rel="noopener noreferrer" target="_blank">Ralph</a> would be more appropriate. Ralph is elegantly simplea bash loop that feeds a markdown file into Claude Code repeatedly:</p>
<figure class=" mx-auto "> <img src="/_astro/ralph-architecture.BT-Jeu2J_Z6tFUa.webp" alt="Ralph Architecture: A bash loop (while :; do cat PROMPT.md | claude-code ; done) where PROMPT.md feeds into Claude Code which produces output, and the loop continues indefinitely" loading="lazy" decoding="async" fetchpriority="auto" width="1520" height="826" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> Ralph&#39;s stateless architecture using markdown as persistent memory </figcaption> </figure>
<p>The key difference: Ralph executes each iteration in a completely new Claude session, using the markdown file as the only persistent memory. This makes it truly stateless and capable of running for days.</p>
<p>This spec-driven approach hits a middle ground: subagents get fresh context but the main orchestrator maintains state within a single session. Structured enough to maintain coherence, flexible enough to handle complexity, without the setup overhead of a full autonomous system.</p>
<h3 id="the-execution-flow">The Execution Flow<a class="heading-link" aria-label="Link to section" href="#the-execution-flow"><span class="heading-link-icon">#</span></a></h3>
<figure class="max-w-2xl mx-auto "> <img src="/_astro/orchestrator-flow.4urm3Izv_1tXB7o.webp" alt="Main Agent Orchestrator flow: TaskCreate spawns Subagent 1 which implements and returns, then TaskUpdate marks complete and commits, then TaskCreate spawns Subagent 2 with dependencies, repeating for all tasks" loading="lazy" decoding="async" fetchpriority="auto" width="1220" height="2058" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> The orchestrator delegates each task to a subagent with atomic commits </figcaption> </figure>
<h3 id="why-this-pattern-works">Why This Pattern Works<a class="heading-link" aria-label="Link to section" href="#why-this-pattern-works"><span class="heading-link-icon">#</span></a></h3>
<ol>
<li><strong>Context isolation</strong>: Each subagent starts fresh, reading only what it needsno accumulated cruft</li>
<li><strong>Persistent progress</strong>: Tasks survive session restarts; pick up where you left off</li>
<li><strong>Dependency-aware parallelism</strong>: Claude identifies which tasks can run concurrently</li>
<li><strong>Atomic commits</strong>: Every task = one commit, making rollbacks trivial</li>
<li><strong>Spec as contract</strong>: Subagents reference the spec, ensuring consistency</li>
</ol>
<h3 id="backpressure-let-the-system-catch-mistakes">Backpressure: Let the System Catch Mistakes<a class="heading-link" aria-label="Link to section" href="#backpressure-let-the-system-catch-mistakes"><span class="heading-link-icon">#</span></a></h3>
<p>One crucial element that makes atomic commits powerful: <a href="https://banay.me/dont-waste-your-backpressure/" rel="noopener noreferrer" target="_blank">backpressure</a>. Instead of manually reviewing every change, set up pre-commit hooks that run tests, linting, and type checking automatically.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#51597D;font-style:italic"># .husky/pre-commit</span></span>
<span class="line"><span style="color:#C0CAF5">pnpm</span><span style="color:#9ECE6A"> typecheck</span><span style="color:#89DDFF"> &amp;&amp;</span><span style="color:#C0CAF5"> pnpm</span><span style="color:#9ECE6A"> lint</span><span style="color:#89DDFF"> &amp;&amp;</span><span style="color:#C0CAF5"> pnpm</span><span style="color:#9ECE6A"> test-run</span></span></code><button type="button" class="copy" data-code="# .husky/pre-commit
pnpm typecheck &#38;&#38; pnpm lint &#38;&#38; pnpm test-run" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>When a subagent commits, the hook runs immediately. If tests fail, the commit is rejected and the agent sees the error outputgiving it a chance to self-correct before moving on. This creates automated feedback that catches issues at the source rather than accumulating bugs across multiple tasks.</p>
<p>The result: you stop being the bottleneck for quality control. The system validates correctness while you focus on higher-level decisions.</p>
<h3 id="when-things-go-wrong">When Things Go Wrong<a class="heading-link" aria-label="Link to section" href="#when-things-go-wrong"><span class="heading-link-icon">#</span></a></h3>
<p>The first execution wasn’t perfectI started the project and hit some errors. But here’s where the spec pays off: I opened a new chat, pinned the spec document, pasted the error, and Claude fixed it immediately. No context rebuilding, no re-explaining the architecture.</p>
<p>The spec acts as a recovery point. When a session goes sideways or context gets polluted, you don’t lose everythingyou have a document that captures the full intent and design decisions.</p>
<h3 id="the-results">The Results<a class="heading-link" aria-label="Link to section" href="#the-results"><span class="heading-link-icon">#</span></a></h3>
<p>After ~45 minutes:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>$ git log-oneline | head20</span></span>
<span class="line"><span></span></span>
<span class="line"><span>9dc1c96 refactor: clean up code structure</span></span>
<span class="line"><span>9fce16b feat(storage): migrate from SQLite to IndexedDB</span></span>
<span class="line"><span>835c494 feat: integrate IDB sync engine provider</span></span>
<span class="line"><span>d2cd7b7 refactor: remove SQLite/sql.js dependencies</span></span>
<span class="line"><span>2fb7656 feat: add browser mode test stubs</span></span>
<span class="line"><span>... (14 commits total)</span></span></code><button type="button" class="copy" data-code="$ git log-oneline | head20

9dc1c96 refactor: clean up code structure
9fce16b feat(storage): migrate from SQLite to IndexedDB
835c494 feat: integrate IDB sync engine provider
d2cd7b7 refactor: remove SQLite/sql.js dependencies
2fb7656 feat: add browser mode test stubs
... (14 commits total)" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>14 tasks completed</strong>, <strong>14 commits</strong>, <strong>15+ files changed</strong>, <strong>one PR ready for review</strong>. See the <a href="https://github.com/alexanderop/nuxt-sync-engine/pull/3" rel="noopener noreferrer" target="_blank">full pull request</a> (includes additional manual changes).</p>
<p>And despite orchestrating 14 subagents, the main session’s context stayed manageable:</p>
<div class="context-usage astro-wu3jzyoo"> <div class="context-header astro-wu3jzyoo"> <span class="context-icon astro-wu3jzyoo">⎿</span> <span class="context-title astro-wu3jzyoo">Context Usage</span> <span class="usage-badge astro-wu3jzyoo">71%</span> </div> <div class="context-body astro-wu3jzyoo"> <!-- Main usage display --> <div class="main-display astro-wu3jzyoo"> <div class="model-info astro-wu3jzyoo"> <span class="model-name astro-wu3jzyoo">claude-opus-4-5-20251101</span> <span class="usage-text astro-wu3jzyoo">143k / 200k tokens</span> </div> </div> <!-- Full-width segmented progress bar --> <div class="progress-container astro-wu3jzyoo"> <div class="progress-bar astro-wu3jzyoo"> <div class="progress-segment system-prompt astro-wu3jzyoo" style="width: 1.4%" title="System prompt: 2.8k (1.4%)"></div><div class="progress-segment system-tools astro-wu3jzyoo" style="width: 8.1%" title="System tools: 16.2k (8.1%)"></div><div class="progress-segment mcp-tools astro-wu3jzyoo" style="width: 0.1%" title="MCP tools: 293 (0.1%)"></div><div class="progress-segment custom-agents astro-wu3jzyoo" style="width: 0.3%" title="Custom agents: 641 (0.3%)"></div><div class="progress-segment memory-files astro-wu3jzyoo" style="width: 0.2%" title="Memory files: 431 (0.2%)"></div><div class="progress-segment skills astro-wu3jzyoo" style="width: 0.8%" title="Skills: 1.6k (0.8%)"></div><div class="progress-segment messages astro-wu3jzyoo" style="width: 61.4%" title="Messages: 122.9k (61.4%)"></div> <div class="progress-segment free astro-wu3jzyoo" style="width: 11.1%" title="Free space: 22k (11.1%)"></div> <div class="progress-segment buffer astro-wu3jzyoo" style="width: 16.5%" title="Autocompact buffer: 33.0k (16.5%)"></div> </div> </div> <!-- Category breakdown in grid --> <div class="breakdown-section astro-wu3jzyoo"> <div class="breakdown-grid astro-wu3jzyoo"> <div class="breakdown-item astro-wu3jzyoo"> <span class="breakdown-bar system-prompt astro-wu3jzyoo"></span> <span class="breakdown-name astro-wu3jzyoo">System prompt</span> <span class="breakdown-value astro-wu3jzyoo">2.8k (1.4%)</span> </div><div class="breakdown-item astro-wu3jzyoo"> <span class="breakdown-bar system-tools astro-wu3jzyoo"></span> <span class="breakdown-name astro-wu3jzyoo">System tools</span> <span class="breakdown-value astro-wu3jzyoo">16.2k (8.1%)</span> </div><div class="breakdown-item astro-wu3jzyoo"> <span class="breakdown-bar mcp-tools astro-wu3jzyoo"></span> <span class="breakdown-name astro-wu3jzyoo">MCP tools</span> <span class="breakdown-value astro-wu3jzyoo">293 (0.1%)</span> </div><div class="breakdown-item astro-wu3jzyoo"> <span class="breakdown-bar custom-agents astro-wu3jzyoo"></span> <span class="breakdown-name astro-wu3jzyoo">Custom agents</span> <span class="breakdown-value astro-wu3jzyoo">641 (0.3%)</span> </div><div class="breakdown-item astro-wu3jzyoo"> <span class="breakdown-bar memory-files astro-wu3jzyoo"></span> <span class="breakdown-name astro-wu3jzyoo">Memory files</span> <span class="breakdown-value astro-wu3jzyoo">431 (0.2%)</span> </div><div class="breakdown-item astro-wu3jzyoo"> <span class="breakdown-bar skills astro-wu3jzyoo"></span> <span class="breakdown-name astro-wu3jzyoo">Skills</span> <span class="breakdown-value astro-wu3jzyoo">1.6k (0.8%)</span> </div><div class="breakdown-item astro-wu3jzyoo"> <span class="breakdown-bar messages astro-wu3jzyoo"></span> <span class="breakdown-name astro-wu3jzyoo">Messages</span> <span class="breakdown-value astro-wu3jzyoo">122.9k (61.4%)</span> </div><div class="breakdown-item astro-wu3jzyoo"> <span class="breakdown-bar free astro-wu3jzyoo"></span> <span class="breakdown-name astro-wu3jzyoo">Free space</span> <span class="breakdown-value astro-wu3jzyoo">22k (11.1%)</span> </div><div class="breakdown-item astro-wu3jzyoo"> <span class="breakdown-bar buffer astro-wu3jzyoo"></span> <span class="breakdown-name astro-wu3jzyoo">Autocompact buffer</span> <span class="breakdown-value astro-wu3jzyoo">33.0k (16.5%)</span> </div> </div> </div> </div> </div> 
<p>This proves the delegation pattern worksthe main agent handled orchestration while subagents did the heavy lifting in isolated contexts.</p>
<h2 id="the-prompt-patterns">The Prompt Patterns<a class="heading-link" aria-label="Link to section" href="#the-prompt-patterns"><span class="heading-link-icon">#</span></a></h2>
<p>Here are the key prompt patterns that make this workflow effective:</p>
<h3 id="1-parallel-research">1. Parallel Research<a class="heading-link" aria-label="Link to section" href="#1-parallel-research"><span class="heading-link-icon">#</span></a></h3>
<div class="prompt-block astro-7uk2cqts"> <span class="prompt-label astro-7uk2cqts"> <span class="prompt-chevron astro-7uk2cqts">›</span> Prompt </span> <div class="prompt-content astro-7uk2cqts"> <p>spin up multiple subagents for your research task</p> </div> </div> 
<p>Triggers Claude to spawn parallel agents, each investigating independently. Much faster than sequential research.</p>
<h3 id="2-spec-first-development">2. Spec-First Development<a class="heading-link" aria-label="Link to section" href="#2-spec-first-development"><span class="heading-link-icon">#</span></a></h3>
<div class="prompt-block astro-7uk2cqts"> <span class="prompt-label astro-7uk2cqts"> <span class="prompt-chevron astro-7uk2cqts">›</span> Prompt </span> <div class="prompt-content astro-7uk2cqts"> <p>your goal is to write a report/document</p> </div> </div> 
<p>Forces Claude to produce a written artifact before any code. This becomes the source of truth.</p>
<h3 id="3-interview-before-implementation">3. Interview Before Implementation<a class="heading-link" aria-label="Link to section" href="#3-interview-before-implementation"><span class="heading-link-icon">#</span></a></h3>
<div class="prompt-block astro-7uk2cqts"> <span class="prompt-label astro-7uk2cqts"> <span class="prompt-chevron astro-7uk2cqts">›</span> Prompt </span> <div class="prompt-content astro-7uk2cqts"> <p>use the ask_user_question tool… before we implement</p> </div> </div> 
<p>Surfaces ambiguities and design decisions before they become bugs.</p>
<h3 id="4-task-delegation-with-commits">4. Task Delegation with Commits<a class="heading-link" aria-label="Link to section" href="#4-task-delegation-with-commits"><span class="heading-link-icon">#</span></a></h3>
<div class="prompt-block astro-7uk2cqts"> <span class="prompt-label astro-7uk2cqts"> <span class="prompt-chevron astro-7uk2cqts">›</span> Prompt </span> <div class="prompt-content astro-7uk2cqts"> <p>use the task tool and each task should only be done by a subagent
after each task do a commit before you continue</p> </div> </div> 
<p>Creates the orchestration pattern with atomic commits.</p>
<h3 id="5-role-assignment">5. Role Assignment<a class="heading-link" aria-label="Link to section" href="#5-role-assignment"><span class="heading-link-icon">#</span></a></h3>
<div class="prompt-block astro-7uk2cqts"> <span class="prompt-label astro-7uk2cqts"> <span class="prompt-chevron astro-7uk2cqts">›</span> Prompt </span> <div class="prompt-content astro-7uk2cqts"> <p>you are the main agent and your subagents are your devs</p> </div> </div> 
<p>Sets expectations for how Claude should behaveas a coordinator, not a solo implementer.</p>
<h2 id="comparison-traditional-vs-spec-driven">Comparison: Traditional vs Spec-Driven<a class="heading-link" aria-label="Link to section" href="#comparison-traditional-vs-spec-driven"><span class="heading-link-icon">#</span></a></h2>



































<table><thead><tr><th></th><th>Traditional AI Coding</th><th>Spec-Driven Development</th></tr></thead><tbody><tr><td><strong>Flow</strong></td><td data-label="Traditional AI Coding">Prompt → Code → Debug → Repeat</td><td data-label="Spec-Driven Development">Research → Spec → Refine → Tasks → Done</td></tr><tr><td><strong>Context</strong></td><td data-label="Traditional AI Coding">Fills up with failed attempts</td><td data-label="Spec-Driven Development">Each task gets fresh context</td></tr><tr><td><strong>Memory</strong></td><td data-label="Traditional AI Coding">No persistence across sessions</td><td data-label="Spec-Driven Development">Spec is persistent source of truth</td></tr><tr><td><strong>Bug tracking</strong></td><td data-label="Traditional AI Coding">Discovered late, forgotten</td><td data-label="Spec-Driven Development">Bugs become new tasks</td></tr><tr><td><strong>Completion</strong></td><td data-label="Traditional AI Coding">No clear stopping point</td><td data-label="Spec-Driven Development">Clear completion criteria</td></tr></tbody></table>
<h2 id="advanced-multi-session-workflows">Advanced: Multi-Session Workflows<a class="heading-link" aria-label="Link to section" href="#advanced-multi-session-workflows"><span class="heading-link-icon">#</span></a></h2>
<p>The task system supports coordination across multiple Claude Code sessions. Set a shared task list ID:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">CLAUDE_CODE_TASK_LIST_ID</span><span style="color:#89DDFF">=</span><span style="color:#9ECE6A">myproject</span><span style="color:#C0CAF5"> claude</span></span></code><button type="button" class="copy" data-code="CLAUDE_CODE_TASK_LIST_ID=myproject claude" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Or add to <code>.claude/settings.json</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">env</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#0DB9D7">CLAUDE_CODE_TASK_LIST_ID</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">myproject</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;env&#34;: {
    &#34;CLAUDE_CODE_TASK_LIST_ID&#34;: &#34;myproject&#34;
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>One session acts as <strong>orchestrator</strong>; another becomes a <strong>checker</strong> that monitors completed tasks, verifies implementation quality, and adds follow-up tasks for anything missing.</p>
<h2 id="when-to-use-this-workflow">When to Use This Workflow<a class="heading-link" aria-label="Link to section" href="#when-to-use-this-workflow"><span class="heading-link-icon">#</span></a></h2>
<p>This pattern excels for:</p>
<ul>
<li><strong>Large refactors</strong> touching many files</li>
<li><strong>Migrations</strong> requiring research into external codebases</li>
<li><strong>Feature implementations</strong> with unclear requirements</li>
<li><strong>Learning new libraries</strong> by studying their source</li>
</ul>
<p>It’s overkill for:</p>
<ul>
<li>Small bug fixes</li>
<li>Single-file changes</li>
<li>Well-defined, simple features</li>
</ul>
<h2 id="the-tools-you-need">The Tools You Need<a class="heading-link" aria-label="Link to section" href="#the-tools-you-need"><span class="heading-link-icon">#</span></a></h2>
<ol>
<li><strong>Claude Code CLI</strong> (latest version with task tools)</li>
<li><strong>A spec document</strong> (markdown works great)</li>
<li><strong>Reference codebases</strong> if learning from existing implementations</li>
<li><strong>Git</strong> for atomic commits</li>
</ol>
<h2 id="further-reading">Further Reading<a class="heading-link" aria-label="Link to section" href="#further-reading"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li><a href="https://github.com/beads-ai/beads" rel="noopener noreferrer" target="_blank">Beads</a> Steve Yegge’s git-backed issue tracker that inspired the task system</li>
<li><a href="https://www.humanlayer.dev/blog/12-factor-agents" rel="noopener noreferrer" target="_blank">12 Factor Agents</a> Design principles for AI coding agents</li>
<li><a href="https://www.anthropic.com/research/building-effective-agents" rel="noopener noreferrer" target="_blank">Building Effective Agents</a> Anthropic’s research on agent architectures</li>
<li>For a broader overview of Claude Code’s feature stack, see my <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/understanding-claude-code-full-stack/" class="internal-link astro-3tyn5ojg"> comprehensive guide </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Understanding Claude Code&#39;s Full Stack: MCP, Skills, Subagents, and Hooks Explained</span> <span class="preview-description astro-3tyn5ojg">A practical guide to Claude Code&#39;s features — explained in the order they were introduced: MCP (2024), Claude Code core (Feb 2025), Plugins (2025), and Agent Skills (Oct 2025). What each does, how they fit together, and when to use what.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">mcp</span> <span class="preview-tag-more astro-3tyn5ojg">+2</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 9, 2025</time> </span> </span> </span>  <script>
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
</script></li>
</ul>
<h2 id="conclusion">Conclusion<a class="heading-link" aria-label="Link to section" href="#conclusion"><span class="heading-link-icon">#</span></a></h2>
<p>Spec-Driven Development with Claude Code mirrors real engineering workflows: parallel work, handoffs, blockers, and dependencies. Instead of treating Claude as a solo coder, you treat it as a team.</p>
<p>The key insight from Beads applies here:</p>
<blockquote>
<p>“By having each task that you give a coding agent isolated into its own context window, you can now give it the ability to log any bugs for later.”</p>
</blockquote>
<p>The SQLite to IndexedDB migration would have taken me 2-3 days manually. With this workflow, it took one afternoonand produced better code thanks to the research phase uncovering patterns from Jazz I wouldn’t have found on my own.</p>
<hr/>
<p><em>Try it yourself: Start your next significant feature with “write a spec for X, spin up subagents for research” and see how it changes your workflow.</em></p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_spec-driven-development-claude-code-in-action" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="spec-driven-development-claude-code-in-action" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/claude-code/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">claude-code</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/local-first/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">local-first</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/architecture/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-5"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">architecture</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/spec-driven-development-claude-code-in-action/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/spec-driven-development-claude-code-in-action/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/spec-driven-development-claude-code-in-action/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/spec-driven-development-claude-code-in-action/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/spec-driven-development-claude-code-in-action/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/spec-driven-development-claude-code-in-action/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/spec-driven-development-claude-code-in-action/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "spec-driven-development-claude-code-in-action";

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
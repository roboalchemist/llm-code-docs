# Source: https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Stop Bloating Your CLAUDE.md: Progressive Disclosure for AI Coding Tools | alexop.dev</title><meta name="title" content="Stop Bloating Your CLAUDE.md: Progressive Disclosure for AI Coding Tools | alexop.dev"><meta name="description" content="AI coding tools are stateless—every session starts fresh. The solution isn't cramming everything into CLAUDE.md, but building a layered context system where learnings accumulate in docs and specialized agents load on-demand."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Stop Bloating Your CLAUDE.md: Progressive Disclosure for AI Coding Tools | alexop.dev"><meta property="og:description" content="AI coding tools are stateless—every session starts fresh. The solution isn't cramming everything into CLAUDE.md, but building a layered context system where learnings accumulate in docs and specialized agents load on-demand."><meta property="og:url" content="https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/"><meta property="og:image" content="https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-for-ai-coding-tools/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2026-01-18T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/"><meta property="twitter:title" content="Stop Bloating Your CLAUDE.md: Progressive Disclosure for AI Coding Tools | alexop.dev"><meta property="twitter:description" content="AI coding tools are stateless—every session starts fresh. The solution isn't cramming everything into CLAUDE.md, but building a layered context system where learnings accumulate in docs and specialized agents load on-demand."><meta property="twitter:image" content="https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-for-ai-coding-tools/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Stop Bloating Your CLAUDE.md: Progressive Disclosure for AI Coding Tools | alexop.dev","description":"AI coding tools are stateless—every session starts fresh. The solution isn't cramming everything into CLAUDE.md, but building a layered context system where learnings accumulate in docs and specialized agents load on-demand.","image":"https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-for-ai-coding-tools/index.png","datePublished":"2026-01-18T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: stop-bloating-your-claude-md-progressive-disclosure-for-ai-coding-tools; }@layer astro { ::view-transition-old(stop-bloating-your-claude-md-progressive-disclosure-for-ai-coding-tools) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(stop-bloating-your-claude-md-progressive-disclosure-for-ai-coding-tools) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(stop-bloating-your-claude-md-progressive-disclosure-for-ai-coding-tools) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(stop-bloating-your-claude-md-progressive-disclosure-for-ai-coding-tools) { 
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
</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: claude-code; }@layer astro { ::view-transition-old(claude-code) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: ai-tools; }@layer astro { ::view-transition-old(ai-tools) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(ai-tools) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(ai-tools) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(ai-tools) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: developer-experience; }@layer astro { ::view-transition-old(developer-experience) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(developer-experience) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(developer-experience) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(developer-experience) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-5"] { view-transition-name: productivity; }@layer astro { ::view-transition-old(productivity) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(productivity) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(productivity) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(productivity) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Stop Bloating Your CLAUDE.md: Progressive Disclosure for AI Coding Tools</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2026-01-18T00:00:00.000Z">Jan 18, 2026</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="1w3oin" prefix="r7" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Stop Bloating Your CLAUDE.md: Progressive Disclosure for AI Coding Tools&quot;],&quot;content&quot;:[0,&quot;import Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\nimport InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\nimport ContextWindowVisualizer from \&quot;@features/llm-education/components/ContextWindowVisualizer\&quot;;\nimport TokenBudgetMeter from \&quot;@features/llm-education/components/TokenBudgetMeter\&quot;;\nimport ProgressiveDisclosureExplorer from \&quot;@features/llm-education/components/ProgressiveDisclosureExplorer\&quot;;\nimport FeedbackLoopAnimator from \&quot;@features/agent-teams/components/FeedbackLoopAnimator\&quot;;\n\nYesterday I spent an hour debugging a Nuxt Content gotcha with Claude. We figured it out together—you need to use `stem` instead of `slug` in page collection queries. Today? Claude made the same mistake. Yesterday&#39;s session was gone.\n\n&lt;Alert type=\&quot;info\&quot;&gt;\nThe examples in this post come from my [Second Brain](https://second-brain-nuxt.vercel.app/)—a personal wiki built with Nuxt and Nuxt Content that uses Zettelkasten-style wiki-links for knowledge management. You can see the actual [CLAUDE.md file](https://github.com/alexanderop/second-brain-nuxt/blob/main/CLAUDE.md) on GitHub.\n&lt;/Alert&gt;\n\nThat&#39;s the constraint. **Your context is just an array of tokens**—a sliding window that forgets everything the moment the conversation ends.[^1]\n\n&lt;ContextWindowVisualizer client:load /&gt;\n\n&lt;Alert type=\&quot;info\&quot;&gt;\nThe percentages shown in these visualizations are illustrative examples—not real measurements. Actual system prompt overhead varies by tool version and configuration. The key insight is the relative proportions, not the exact numbers.\n&lt;/Alert&gt;\n\nThere&#39;s no hidden memory. No database of past conversations. Just this array, rebuilt fresh every session.\n\nDex Horthy calls this \&quot;context engineering\&quot;—since LLMs are stateless, the only way to improve output is optimizing input.[^6] The array is all you have. Everything outside it doesn&#39;t exist to the model.\n\nBut that array has a size limit. Fill it with noise, and you&#39;re working in what Dex calls the \&quot;dumb zone\&quot;—where performance degrades because irrelevant context competes for attention.\n\nMost developers respond to this by putting every lesson learned into their `CLAUDE.md` file. I&#39;ve seen files balloon to 2000 lines. Style guides, architectural decisions, war stories from that one bug that took three days to fix.\n\nThis makes things worse.\n\n## Bloated CLAUDE.md Makes Things Worse\n\nWhen Claude makes a mistake, the instinct is to add a rule: \&quot;Never use `slug` in page collection queries—use `stem` instead.\&quot;\n\nThen another mistake, another rule. Then another.\n\nBefore long, your CLAUDE.md looks like this:\n\n```markdown\n# CLAUDE.md\n\n## Project Overview\n...50 lines...\n\n## Code Style\n...200 lines of formatting rules...\n\n## Architecture Decisions\n...150 lines of historical context...\n\n## Gotchas\n...300 lines of edge cases...\n\n## Testing Conventions\n...100 lines...\n```\n\n**Half your context budget is gone before any work begins.**\n\n&lt;TokenBudgetMeter client:load /&gt;\n\nHumanLayer keeps their CLAUDE.md under 60 lines.[^2] Frontier LLMs reliably follow 150-200 instructions—and Claude Code&#39;s system prompt already uses about 50 of those.[^2]\n\nThe math doesn&#39;t work. You can&#39;t stuff everything in one file.\n\n## Stop Writing Prose About Lint Rules\n\nWhy write two hundred lines about code style when one line handles it? I stopped putting anything a tool can enforce in CLAUDE.md.\n\n❌ **Don&#39;t write prose about style rules:**\n```markdown\n## Code Style\n- Use 2-space indentation\n- Prefer single quotes\n- Always add trailing commas\n- Maximum line length: 100 characters\n```\n\n✅ **Let ESLint handle it:**\n```json\n{\n  \&quot;extends\&quot;: [\&quot;@nuxt/eslint-config\&quot;]\n}\n```\n\nThe rules are already there—you just don&#39;t repeat them in prose:\n```js\n// What @nuxt/eslint-config contains:\n{\n  rules: {\n    &#39;indent&#39;: [&#39;error&#39;, 2],\n    &#39;quotes&#39;: [&#39;error&#39;, &#39;single&#39;],\n    &#39;comma-dangle&#39;: [&#39;error&#39;, &#39;always-multiline&#39;],\n    &#39;max-len&#39;: [&#39;error&#39;, { code: 100 }]\n  }\n}\n```\n\nThe AI can run `pnpm lint:fix &amp;&amp; pnpm typecheck` and know immediately if it violated a rule. No interpretation needed. No ambiguity.\n\n**If a tool can enforce it, don&#39;t write prose about it.** ESLint for style. TypeScript for types. Prettier for formatting. These rules are verifiable, not interpretable.\n\nMoss calls this *backpressure*—automated feedback mechanisms that let agents self-correct.[^7] Without a linter, you waste your time typing messages like \&quot;you forgot to add the import\&quot; or \&quot;that should be a const, not let.\&quot; With backpressure, the agent runs the build, reads the error, and fixes itself. You remove yourself from trivial corrections and focus on higher-level decisions.\n\nMy CLAUDE.md now just says:\n\n```markdown\nRun `pnpm lint:fix &amp;&amp; pnpm typecheck` after code changes.\n```\n\nOne line instead of two hundred. Or skip it entirely—use husky to run checks automatically on commit. This is especially useful for techniques like Ralph, where AI works autonomously through a queue of tasks.[^8]\n\n## The Gotchas ESLint Won&#39;t Catch\n\nESLint won&#39;t catch this:\n\n&gt; \&quot;Nuxt Content v3 caches aggressively in `.data/`. When you modify transformation logic in hooks, you must clear the cache to test changes.\&quot;\n\nOr this:\n\n{/* &gt; \&quot;Don&#39;t mock `@nuxt/content/server` internals in tests—it breaks when Nuxt Content updates. Extract pure logic to `server/utils/` instead.\&quot; */}\n\nOr this:\n\n&gt; \&quot;Wiki-links to data collections require path prefixes. Use `[[authors/john-doe]]`, not `[[john-doe]]`.\&quot;\n\nThese are *gotchas*—non-obvious behaviors that bite you once. The kind of thing you&#39;d tell a new team member on their first day. They need documentation, but they don&#39;t belong in CLAUDE.md.\n\n**The insight: CLAUDE.md is for universal context. Gotchas are situational.**\n\nYou don&#39;t need the wiki-link prefix rule in every conversation—only when you&#39;re writing content with author links. Loading it every time wastes tokens.\n\nSo where do these gotchas go? And how do you capture them without breaking your flow?\n\n## My /learn Skill\n\nMy system: when I notice Claude struggling with something we&#39;ve solved before, I run `/learn`.\n\nThis is a Claude Code skill I built ([see full prompt](/prompts/claude/claude-learn-command)). It:\n\n1. Analyzes the conversation for reusable, non-obvious insights\n2. Finds the right place in `/docs` to save it (or proposes a new file)\n3. Asks for my approval before saving\n\nI end up with a growing knowledge base in my docs folder:\n\n```\ndocs/\n├── nuxt-content-gotchas.md    # 15 hard-won lessons\n├── nuxt-component-gotchas.md  # Vue-specific pitfalls\n├── testing-strategy.md        # When to use which test type\n└── SYSTEM_KNOWLEDGE_MAP.md    # Architecture overview\n```\n\n**CLAUDE.md stays stable.** It just tells Claude where to look:\n\n```markdown\n## Further Reading\n\n**IMPORTANT:** Before starting any task, identify which docs below are relevant and read them first. Load the full context before making changes.\n\n- `docs/nuxt-content-gotchas.md` - Nuxt Content v3 pitfalls\n- `docs/testing-strategy.md` - Test layers and when to use each\n```\n\nThe **IMPORTANT** instruction is critical—without it, Claude won&#39;t automatically read these docs. With it, Claude identifies relevant docs before starting work: content queries trigger the gotchas doc, testing tasks trigger the testing strategy. Progressive disclosure—the right context at the right time.[^2]\n\nAnother approach: build skills that load domain-specific gotchas automatically. A `nuxt-content` skill that injects the gotchas doc whenever you&#39;re working with content queries. In theory, this is cleaner—context loads without you thinking about it. In practice, I&#39;ve found skills don&#39;t always activate when expected. The trigger conditions can be fuzzy, and sometimes Claude just doesn&#39;t invoke them. Vercel&#39;s agent evals confirmed this: skills were never invoked in 56% of their test cases, producing zero improvement over baseline.[^9] The docs-based setup is more predictable: I know Claude will read what I point it to.\n\n## One Agent Per Domain\n\nI take this further with custom agents. Each agent has its own documentation file that loads only when needed. If you&#39;re new to how these customization layers work together, I wrote a &lt;InternalLink slug=\&quot;claude-code-customization-guide-claudemd-skills-subagents\&quot;&gt;detailed comparison of CLAUDE.md, skills, and subagents&lt;/InternalLink&gt;.\n\n```\n.claude/agents/\n├── nuxt-content-specialist.md   # Content queries, MDC, search\n├── nuxt-ui-specialist.md        # Component styling, theming\n├── vue-specialist.md            # Reactivity, composables\n└── nuxt-specialist.md           # Routing, config, deployment\n```\n\nWhen I&#39;m debugging a content query, Claude loads the nuxt-content-specialist. When I&#39;m styling a component, it loads nuxt-ui-specialist. The specialist agents know to fetch the latest documentation from official sources—they don&#39;t rely on stale training data.\n\nThis is why I don&#39;t use MCPs like context7 for documentation. Agents can fetch llms.txt directly from official docs sites and find what they need. No tool definition bloat, no intermediate tokens—just a focused research task in its own context window. I wrote more about &lt;InternalLink slug=\&quot;why-you-dont-need-nuxt-mcp-claude-code\&quot;&gt;why I use custom research agents instead of MCPs&lt;/InternalLink&gt;.\n\nSkills work similarly—with `context:fork`, they run in isolated contexts without polluting your main conversation. The agent has both the ability and motivation to read real documentation. No context7, no MCP overhead.\n\n&lt;ProgressiveDisclosureExplorer client:load /&gt;\n\n## It Compounds\n\nThis system creates a feedback loop:\n\n&lt;FeedbackLoopAnimator client:load /&gt;\n\nOver time, my `/docs` folder becomes a curated knowledge base of *exactly the things AI coding tools get wrong* in my codebase. It&#39;s like fine-tuning, but under my control.\n\nI got this idea from a pattern for self-improving skills where agents automatically analyze sessions and update themselves.[^5] I adapted it to use markdown documentation and a `/learn` command instead—giving me explicit control over what gets captured and where it goes.\n\nAn actual entry from my `nuxt-content-gotchas.md`:\n\n```markdown\n## Page Collection Queries: Use `stem` Not `slug`\n\nThe `slug` field doesn&#39;t exist in page-type collections.\nUse `stem` (file path without extension) instead:\n\n// ❌ Fails: \&quot;no such column: slug\&quot;\nqueryCollection(&#39;content&#39;).select(&#39;slug&#39;, &#39;title&#39;).all()\n\n// ✅ Works\nqueryCollection(&#39;content&#39;).select(&#39;stem&#39;, &#39;title&#39;).all()\n```\n\nClaude will never make this mistake again in my project. Not because I added it to CLAUDE.md—but because when it&#39;s working with content queries, it reads the gotchas doc first.\n\n## My 50-Line CLAUDE.md\n\nThe structure:\n\n```markdown\n# CLAUDE.md\n\nSecond Brain is a personal knowledge base using\nZettelkasten-style wiki-links.\n\n## Commands\npnpm dev          # Start dev server\npnpm lint:fix     # Auto-fix linting issues\npnpm typecheck    # Verify type safety\n\nRun `pnpm lint:fix &amp;&amp; pnpm typecheck` after code changes.\n\n## Stack\n- Nuxt 4, @nuxt/content v3, @nuxt/ui v3\n\n## Structure\n- `app/` - Vue application\n- `content/` - Markdown files\n- `content.config.ts` - Collection schemas\n\n## Further Reading\n\n**IMPORTANT:** Read relevant docs below before starting any task.\n\n- `docs/nuxt-content-gotchas.md`\n- `docs/testing-strategy.md`\n- `docs/SYSTEM_KNOWLEDGE_MAP.md`\n```\n\nThat&#39;s it. Universal context only. Everything else lives in docs, agents, or tooling.\n\n## Cross-Tool Compatibility\n\nIf you use multiple AI coding tools, you don&#39;t need separate config files. VS Code Copilot and Cursor both support `agents.md` for project-level instructions. You can symlink it to share the same configuration:\n\n```bash\n# Create a symlink so all tools read the same file\nln -s CLAUDE.md agents.md\n```\n\nNow your minimal, focused instructions work across Claude Code, Copilot, and Cursor. One source of truth, no drift between tools.\n\n## How This Played Out Last Week\n\nLast week I was implementing semantic search. When Claude started working on content queries, it read `nuxt-content-gotchas.md` first—as my CLAUDE.md instructs. The stem/slug gotcha was already there.\n\nNo mistake. No correction needed.\n\nBut during the session, we discovered something new: `queryCollectionSearchSections` returns IDs with a leading slash. Don&#39;t add another slash when constructing URLs.\n\nI ran `/learn`. Claude proposed:\n\n```markdown\n## Search Section IDs\n\nReturns IDs with leading slash (`/slug#section`).\nDon&#39;t add another slash when constructing URLs.\n```\n\nAdded. Next time I work on search, Claude will know.\n\n---\n\nAI tools being stateless isn&#39;t a bug to fight. It&#39;s a design constraint—like limited screen real estate or slow network connections. Accept it, and you can build systems that work with it.\n\n**Keep CLAUDE.md minimal. Let tooling enforce what it can. Capture learnings as you go. Load context on demand.**\n\nOne caveat: you can never be 100% sure agents will read your docs when they face issues. For tricky domains like Nuxt Content—where training data is sparse or outdated—I&#39;ve learned to be explicit in my prompts. When I know I&#39;m working on something with poor training coverage, I&#39;ll add to the plan: \&quot;If you encounter issues with Nuxt Content APIs, read `docs/nuxt-content-gotchas.md` first.\&quot; This nudge makes the difference between the agent guessing based on outdated patterns and actually consulting current knowledge.\n\nThe AI forgets. Your documentation doesn&#39;t.\n\n---\n\n[^1]: LLMs have no memory between sessions—context is just tokens in a sliding window. See Factory&#39;s analysis in [The Context Window Problem](https://factory.ai/news/context-window-problem).\n\n[^2]: HumanLayer&#39;s guide on [Writing a Good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md) recommends keeping files under 60 lines and using progressive disclosure for detailed instructions.\n\n[^5]: Developers Digest, [Self-Improving Skills in Claude Code](https://www.youtube.com/watch?v=-4nUCaMNBR8). A pattern for capturing learnings automatically: skills analyze sessions, extract corrections, and update themselves.\n\n[^6]: Dex Horthy, [No Vibes Allowed: Solving Hard Problems in Complex Codebases](https://www.youtube.com/watch?v=rmvDxxNubIg). Dex is the founder of HumanLayer and creator of the Ralph technique for autonomous AI coding. His [12 Factor Agents](https://www.humanlayer.dev/blog/12-factor-agents) manifesto includes \&quot;Make Your Agent a Stateless Reducer\&quot; as Factor 12.\n\n[^7]: Moss, [Don&#39;t Waste Your Back Pressure](https://banay.me/dont-waste-your-backpressure). Backpressure—automated feedback from type systems, linters, and build tools—is what enables agents to work on longer-horizon tasks without constant human intervention.\n\n[^8]: Geoffrey Huntley, [Ralph](https://ghuntley.com/ralph/). Ralph is a technique for autonomous AI coding where tasks are queued and executed without human intervention, making automated checks on commit essential.\n\n[^9]: Jude Gao, [AGENTS.md outperforms skills in our agent evals](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals). Vercel&#39;s evals found that a compressed docs index embedded directly in AGENTS.md achieved 100% pass rate, while skills maxed out at 79% even with explicit instructions—and performed no better than baseline when left to trigger naturally.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>Yesterday I spent an hour debugging a Nuxt Content gotcha with Claude. We figured it out together—you need to use <code>stem</code> instead of <code>slug</code> in page collection queries. Today? Claude made the same mistake. Yesterday’s session was gone.</p>
<div class="alert alert-info astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl"></span>  </p> <div class="alert-content astro-7kdbuayl"> <p>The examples in this post come from my <a href="https://second-brain-nuxt.vercel.app/" rel="noopener noreferrer" target="_blank">Second Brain</a>—a personal wiki built with Nuxt and Nuxt Content that uses Zettelkasten-style wiki-links for knowledge management. You can see the actual <a href="https://github.com/alexanderop/second-brain-nuxt/blob/main/CLAUDE.md" rel="noopener noreferrer" target="_blank">CLAUDE.md file</a> on GitHub.</p> </div> </div> 
<p>That’s the constraint. <strong>Your context is just an array of tokens</strong>—a sliding window that forgets everything the moment the conversation ends.<sup><a href="#user-content-fn-1" id="user-content-fnref-1" data-footnote-ref aria-describedby="footnote-label">1</a></sup></p>
<astro-island uid="ZidCPP" prefix="r8" component-url="/_astro/ContextWindowVisualizer.YlsTKjWa.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{}" ssr client="load" opts="{&quot;name&quot;:&quot;ContextWindowVisualizer&quot;,&quot;value&quot;:true}" await-children><div class="w-full max-w-3xl mx-auto my-8"><div class="rounded-lg overflow-hidden border border-[rgb(var(--color-border))] shadow-2xl"><div class="flex items-center gap-2 px-4 py-3 bg-[rgb(var(--color-card))] border-b border-[rgb(var(--color-border))]"><div class="flex gap-2"><div class="w-3 h-3 rounded-full bg-red-500/80"></div><div class="w-3 h-3 rounded-full bg-yellow-500/80"></div><div class="w-3 h-3 rounded-full bg-green-500/80"></div></div><div class="flex-1 text-center"><span class="text-sm text-[rgb(var(--color-text-base))] opacity-60 font-mono">context-window-demo</span></div><button class="text-xs px-2 py-1 rounded border border-[rgb(var(--color-border))]
                       text-[rgb(var(--color-text-base))] opacity-60 hover:opacity-100
                       hover:border-[rgb(var(--color-accent))] transition-all">Reset</button></div><div class="bg-[rgb(var(--color-fill))] font-mono text-sm"><div class="px-4 py-3 border-b border-[rgb(var(--color-border))]"><div class="flex items-center justify-between mb-2"><span class="text-[rgb(var(--color-accent))]">CONTEXT WINDOW</span><span class="text-[rgb(var(--color-text-base))] opacity-70">3.1k<!-- --> / <!-- -->200.0k<!-- --> tokens (<!-- -->1.6<!-- -->%)</span></div><div class="h-2 bg-[rgb(var(--color-card))] rounded-full overflow-hidden"><div class="h-full bg-[rgb(var(--color-accent))] transition-all duration-300" style="width:1.55%"></div></div><div class="flex justify-between mt-1 text-xs text-[rgb(var(--color-text-base))] opacity-50"><span>Used: <!-- -->1.6<!-- -->%</span><span>Remaining: <!-- -->98.5<!-- -->%</span></div></div><div class="p-4 max-h-80 overflow-y-auto"><div class="border border-[rgb(var(--color-border))] rounded"><div class="px-3 py-2 bg-[rgb(var(--color-card))] border-b border-[rgb(var(--color-border))] text-xs text-[rgb(var(--color-text-base))] opacity-70">messages: Message[] = [</div><div class="divide-y divide-[rgb(var(--color-border))]"><div class="px-3 py-2 flex items-start gap-3 hover:bg-[rgb(var(--color-card))] transition-colors"><span class="text-[rgb(var(--color-text-base))] opacity-50 w-16 flex-shrink-0">[<!-- -->0<!-- -->]</span><div class="flex-1 min-w-0"><span class="text-purple-400 font-medium">System<!-- -->:</span><span class="text-[rgb(var(--color-text-base))] ml-2 break-words">&quot;<!-- -->System prompt + CLAUDE.md<!-- -->&quot;</span></div><span class="text-[rgb(var(--color-text-base))] opacity-50 text-xs flex-shrink-0">3100<!-- --> tok</span></div><div class="px-3 py-2 flex items-center gap-3 text-[rgb(var(--color-accent))]"><span class="opacity-50 w-16 flex-shrink-0">[<!-- -->1<!-- -->]</span><span class="flex items-center"><span class="mr-2">← You are here</span><span class="inline-block w-2 h-4 bg-[rgb(var(--color-accent))] opacity-100 transition-opacity duration-100"></span></span></div></div><div class="px-3 py-2 bg-[rgb(var(--color-card))] border-t border-[rgb(var(--color-border))] text-xs text-[rgb(var(--color-text-base))] opacity-70">]</div></div><div class="mt-4 border border-dashed border-[rgb(var(--color-border))] rounded p-3 text-center"><div class="text-[rgb(var(--color-text-base))] opacity-50 text-xs mb-1">Yesterday&#x27;s session?</div><div class="text-[rgb(var(--color-text-base))] opacity-70">∅ Not in the array. Doesn&#x27;t exist.</div></div></div><form class="border-t border-[rgb(var(--color-border))]"><div class="flex items-center px-4 py-3"><span class="text-[rgb(var(--color-accent))] mr-2">❯</span><input type="text" placeholder="Type a message to see context fill up..." class="flex-1 bg-transparent text-[rgb(var(--color-text-base))] outline-none
                           placeholder:text-[rgb(var(--color-text-base))] placeholder:opacity-30" value=""/><button type="submit" class="ml-2 px-3 py-1 rounded border border-[rgb(var(--color-accent))]
                           text-[rgb(var(--color-accent))] text-sm hover:bg-[rgb(var(--color-accent))]
                           hover:text-[rgb(var(--color-fill))] transition-all">Send</button></div></form></div></div><p class="text-center mt-4 text-sm text-[rgb(var(--color-text-base))] opacity-50">Each message you send adds to the array. The context window is just a sliding array of messages.</p></div><!--astro:end--></astro-island>
<div class="alert alert-info astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl"></span>  </p> <div class="alert-content astro-7kdbuayl"> <p>The percentages shown in these visualizations are illustrative examples—not real measurements. Actual system prompt overhead varies by tool version and configuration. The key insight is the relative proportions, not the exact numbers.</p> </div> </div> 
<p>There’s no hidden memory. No database of past conversations. Just this array, rebuilt fresh every session.</p>
<p>Dex Horthy calls this “context engineering”—since LLMs are stateless, the only way to improve output is optimizing input.<sup><a href="#user-content-fn-6" id="user-content-fnref-6" data-footnote-ref aria-describedby="footnote-label">2</a></sup> The array is all you have. Everything outside it doesn’t exist to the model.</p>
<p>But that array has a size limit. Fill it with noise, and you’re working in what Dex calls the “dumb zone”—where performance degrades because irrelevant context competes for attention.</p>
<p>Most developers respond to this by putting every lesson learned into their <code>CLAUDE.md</code> file. I’ve seen files balloon to 2000 lines. Style guides, architectural decisions, war stories from that one bug that took three days to fix.</p>
<p>This makes things worse.</p>
<h2 id="bloated-claudemd-makes-things-worse">Bloated CLAUDE.md Makes Things Worse<a class="heading-link" aria-label="Link to section" href="#bloated-claudemd-makes-things-worse"><span class="heading-link-icon">#</span></a></h2>
<p>When Claude makes a mistake, the instinct is to add a rule: “Never use <code>slug</code> in page collection queries—use <code>stem</code> instead.”</p>
<p>Then another mistake, another rule. Then another.</p>
<p>Before long, your CLAUDE.md looks like this:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> CLAUDE.md</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Project Overview</span></span>
<span class="line"><span style="color:#9AA5CE">...50 lines...</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Code Style</span></span>
<span class="line"><span style="color:#9AA5CE">...200 lines of formatting rules...</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Architecture Decisions</span></span>
<span class="line"><span style="color:#9AA5CE">...150 lines of historical context...</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Gotchas</span></span>
<span class="line"><span style="color:#9AA5CE">...300 lines of edge cases...</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Testing Conventions</span></span>
<span class="line"><span style="color:#9AA5CE">...100 lines...</span></span></code><button type="button" class="copy" data-code="# CLAUDE.md

## Project Overview
...50 lines...

## Code Style
...200 lines of formatting rules...

## Architecture Decisions
...150 lines of historical context...

## Gotchas
...300 lines of edge cases...

## Testing Conventions
...100 lines..." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Half your context budget is gone before any work begins.</strong></p>
<astro-island uid="ZVc02m" prefix="r9" component-url="/_astro/TokenBudgetMeter.CZI1HRLw.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{}" ssr client="load" opts="{&quot;name&quot;:&quot;TokenBudgetMeter&quot;,&quot;value&quot;:true}" await-children><div class="w-full max-w-3xl mx-auto my-8"><div class="rounded-lg overflow-hidden border border-[rgb(var(--color-border))] shadow-2xl"><div class="flex items-center gap-2 px-4 py-3 bg-[rgb(var(--color-card))] border-b border-[rgb(var(--color-border))]"><div class="flex gap-2"><div class="w-3 h-3 rounded-full bg-red-500/80"></div><div class="w-3 h-3 rounded-full bg-yellow-500/80"></div><div class="w-3 h-3 rounded-full bg-green-500/80"></div></div><div class="flex-1 text-center"><span class="text-sm text-[rgb(var(--color-text-base))] opacity-60 font-mono">token-budget-meter</span></div></div><div class="bg-[rgb(var(--color-fill))] font-mono text-sm p-4"><div class="mb-6"><div class="flex items-center justify-between mb-2"><span class="text-[rgb(var(--color-accent))]">CLAUDE.md SIZE</span><span class="text-[rgb(var(--color-text-base))]">50<!-- --> lines (~<!-- -->500<!-- --> tokens)</span></div><input type="range" min="50" max="2000" step="10" class="w-full h-2 bg-[rgb(var(--color-card))] rounded-lg appearance-none cursor-pointer
                         [&amp;::-webkit-slider-thumb]:appearance-none
                         [&amp;::-webkit-slider-thumb]:w-4
                         [&amp;::-webkit-slider-thumb]:h-4
                         [&amp;::-webkit-slider-thumb]:rounded-full
                         [&amp;::-webkit-slider-thumb]:bg-[rgb(var(--color-accent))]
                         [&amp;::-webkit-slider-thumb]:cursor-pointer
                         [&amp;::-webkit-slider-thumb]:transition-transform
                         [&amp;::-webkit-slider-thumb]:hover:scale-110
                         [&amp;::-moz-range-thumb]:w-4
                         [&amp;::-moz-range-thumb]:h-4
                         [&amp;::-moz-range-thumb]:rounded-full
                         [&amp;::-moz-range-thumb]:bg-[rgb(var(--color-accent))]
                         [&amp;::-moz-range-thumb]:border-0
                         [&amp;::-moz-range-thumb]:cursor-pointer" value="50"/><div class="flex justify-between text-xs text-[rgb(var(--color-text-base))] opacity-50 mt-1"><span>50 lines</span><span>2000 lines</span></div></div><div class="mb-4"><div class="flex items-center justify-between mb-2"><span class="text-[rgb(var(--color-accent))]">CONTEXT BUDGET</span><span class="text-[rgb(var(--color-text-base))] opacity-70">200.0k<!-- --> tokens total</span></div><div class="h-6 bg-[rgb(var(--color-card))] rounded-lg overflow-hidden flex"><div class="h-full bg-purple-500 transition-all duration-300 flex items-center justify-center" style="width:1.55%" title="System prompt: 3.1k tokens"></div><div class="h-full bg-[rgb(var(--color-accent))] transition-all duration-300 flex items-center justify-center" style="width:0.25%" title="CLAUDE.md: 500 tokens"></div><div class="h-full bg-green-500/30 transition-all duration-300 flex items-center justify-center" style="width:98.2%" title="Remaining: 196.4k tokens"><span class="text-xs text-green-400 font-medium truncate px-1">Conversation space</span></div></div></div><div class="grid grid-cols-3 gap-2 mb-4 text-xs"><div class="flex items-center gap-2"><div class="w-3 h-3 rounded bg-purple-500"></div><span class="text-[rgb(var(--color-text-base))] opacity-70">System: <!-- -->3.1k</span></div><div class="flex items-center gap-2"><div class="w-3 h-3 rounded bg-[rgb(var(--color-accent))]"></div><span class="text-[rgb(var(--color-text-base))] opacity-70">CLAUDE.md: <!-- -->500</span></div><div class="flex items-center gap-2"><div class="w-3 h-3 rounded bg-green-500/30"></div><span class="text-[rgb(var(--color-text-base))] opacity-70">Free: <!-- -->196.4k</span></div></div><div class="border border-[rgb(var(--color-border))] rounded-lg p-4"><div class="grid grid-cols-2 gap-4"><div><div class="text-[rgb(var(--color-text-base))] opacity-50 text-xs mb-1">Budget Used Before Work</div><div class="text-2xl text-[rgb(var(--color-accent))]">1.8<!-- -->%</div></div><div><div class="text-[rgb(var(--color-text-base))] opacity-50 text-xs mb-1">Estimated Turns Remaining</div><div class="text-2xl text-green-400">~<!-- -->130<!-- --> turns</div></div></div><div class="mt-3 text-xs text-[rgb(var(--color-text-base))] opacity-50">Based on ~<!-- -->1.5k<!-- --> tokens per turn (user message + assistant response + tool calls)</div></div></div></div><p class="text-center mt-4 text-sm text-[rgb(var(--color-text-base))] opacity-50">Drag the slider to see how CLAUDE.md size affects your available context budget.</p></div><!--astro:end--></astro-island>
<p>HumanLayer keeps their CLAUDE.md under 60 lines.<sup><a href="#user-content-fn-2" id="user-content-fnref-2" data-footnote-ref aria-describedby="footnote-label">3</a></sup> Frontier LLMs reliably follow 150-200 instructions—and Claude Code’s system prompt already uses about 50 of those.<sup><a href="#user-content-fn-2" id="user-content-fnref-2-2" data-footnote-ref aria-describedby="footnote-label">3</a></sup></p>
<p>The math doesn’t work. You can’t stuff everything in one file.</p>
<h2 id="stop-writing-prose-about-lint-rules">Stop Writing Prose About Lint Rules<a class="heading-link" aria-label="Link to section" href="#stop-writing-prose-about-lint-rules"><span class="heading-link-icon">#</span></a></h2>
<p>Why write two hundred lines about code style when one line handles it? I stopped putting anything a tool can enforce in CLAUDE.md.</p>
<p>❌ <strong>Don’t write prose about style rules:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Code Style</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Use 2-space indentation</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Prefer single quotes</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Always add trailing commas</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Maximum line length: 100 characters</span></span></code><button type="button" class="copy" data-code="## Code Style
- Use 2-space indentation
- Prefer single quotes
- Always add trailing commas
- Maximum line length: 100 characters" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>✅ <strong>Let ESLint handle it:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">extends</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">@nuxt/eslint-config</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;extends&#34;: [&#34;@nuxt/eslint-config&#34;]
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The rules are already there—you just don’t repeat them in prose:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="js"><code><span class="line"><span style="color:#51597D;font-style:italic">// What @nuxt/eslint-config contains:</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#73DACA">  rules</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">indent</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 2</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">quotes</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">single</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">comma-dangle</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">always-multiline</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">    &#39;</span><span style="color:#9ECE6A">max-len</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ABDF5">: [</span><span style="color:#89DDFF">&#39;</span><span style="color:#9ECE6A">error</span><span style="color:#89DDFF">&#39;</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">code</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 100</span><span style="color:#9ABDF5"> }]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// What @nuxt/eslint-config contains:
{
  rules: {
    'indent': ['error', 2],
    'quotes': ['error', 'single'],
    'comma-dangle': ['error', 'always-multiline'],
    'max-len': ['error', { code: 100 }]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The AI can run <code>pnpm lint:fix &amp;&amp; pnpm typecheck</code> and know immediately if it violated a rule. No interpretation needed. No ambiguity.</p>
<p><strong>If a tool can enforce it, don’t write prose about it.</strong> ESLint for style. TypeScript for types. Prettier for formatting. These rules are verifiable, not interpretable.</p>
<p>Moss calls this <em>backpressure</em>—automated feedback mechanisms that let agents self-correct.<sup><a href="#user-content-fn-7" id="user-content-fnref-7" data-footnote-ref aria-describedby="footnote-label">4</a></sup> Without a linter, you waste your time typing messages like “you forgot to add the import” or “that should be a const, not let.” With backpressure, the agent runs the build, reads the error, and fixes itself. You remove yourself from trivial corrections and focus on higher-level decisions.</p>
<p>My CLAUDE.md now just says:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#9AA5CE">Run </span><span style="color:#89DDFF">`pnpm lint:fix &amp;&amp; pnpm typecheck`</span><span style="color:#9AA5CE"> after code changes.</span></span></code><button type="button" class="copy" data-code="Run `pnpm lint:fix &#38;&#38; pnpm typecheck` after code changes." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>One line instead of two hundred. Or skip it entirely—use husky to run checks automatically on commit. This is especially useful for techniques like Ralph, where AI works autonomously through a queue of tasks.<sup><a href="#user-content-fn-8" id="user-content-fnref-8" data-footnote-ref aria-describedby="footnote-label">5</a></sup></p>
<h2 id="the-gotchas-eslint-wont-catch">The Gotchas ESLint Won’t Catch<a class="heading-link" aria-label="Link to section" href="#the-gotchas-eslint-wont-catch"><span class="heading-link-icon">#</span></a></h2>
<p>ESLint won’t catch this:</p>
<blockquote>
<p>“Nuxt Content v3 caches aggressively in <code>.data/</code>. When you modify transformation logic in hooks, you must clear the cache to test changes.”</p>
</blockquote>
<p>Or this:</p>

<p>Or this:</p>
<blockquote>
<p>“Wiki-links to data collections require path prefixes. Use <code>[[authors/john-doe]]</code>, not <code>[[john-doe]]</code>.”</p>
</blockquote>
<p>These are <em>gotchas</em>—non-obvious behaviors that bite you once. The kind of thing you’d tell a new team member on their first day. They need documentation, but they don’t belong in CLAUDE.md.</p>
<p><strong>The insight: CLAUDE.md is for universal context. Gotchas are situational.</strong></p>
<p>You don’t need the wiki-link prefix rule in every conversation—only when you’re writing content with author links. Loading it every time wastes tokens.</p>
<p>So where do these gotchas go? And how do you capture them without breaking your flow?</p>
<h2 id="my-learn-skill">My /learn Skill<a class="heading-link" aria-label="Link to section" href="#my-learn-skill"><span class="heading-link-icon">#</span></a></h2>
<p>My system: when I notice Claude struggling with something we’ve solved before, I run <code>/learn</code>.</p>
<p>This is a Claude Code skill I built (<a href="/prompts/claude/claude-learn-command">see full prompt</a>). It:</p>
<ol>
<li>Analyzes the conversation for reusable, non-obvious insights</li>
<li>Finds the right place in <code>/docs</code> to save it (or proposes a new file)</li>
<li>Asks for my approval before saving</li>
</ol>
<p>I end up with a growing knowledge base in my docs folder:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>docs/</span></span>
<span class="line"><span>├── nuxt-content-gotchas.md    # 15 hard-won lessons</span></span>
<span class="line"><span>├── nuxt-component-gotchas.md  # Vue-specific pitfalls</span></span>
<span class="line"><span>├── testing-strategy.md        # When to use which test type</span></span>
<span class="line"><span>└── SYSTEM_KNOWLEDGE_MAP.md    # Architecture overview</span></span></code><button type="button" class="copy" data-code="docs/
├── nuxt-content-gotchas.md    # 15 hard-won lessons
├── nuxt-component-gotchas.md  # Vue-specific pitfalls
├── testing-strategy.md        # When to use which test type
└── SYSTEM_KNOWLEDGE_MAP.md    # Architecture overview" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>CLAUDE.md stays stable.</strong> It just tells Claude where to look:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Further Reading</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**IMPORTANT:**</span><span style="color:#9AA5CE"> Before starting any task, identify which docs below are relevant and read them first. Load the full context before making changes.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `docs/nuxt-content-gotchas.md`</span><span style="color:#9AA5CE"> - Nuxt Content v3 pitfalls</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `docs/testing-strategy.md`</span><span style="color:#9AA5CE"> - Test layers and when to use each</span></span></code><button type="button" class="copy" data-code="## Further Reading

**IMPORTANT:** Before starting any task, identify which docs below are relevant and read them first. Load the full context before making changes.

- `docs/nuxt-content-gotchas.md` - Nuxt Content v3 pitfalls
- `docs/testing-strategy.md` - Test layers and when to use each" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The <strong>IMPORTANT</strong> instruction is critical—without it, Claude won’t automatically read these docs. With it, Claude identifies relevant docs before starting work: content queries trigger the gotchas doc, testing tasks trigger the testing strategy. Progressive disclosure—the right context at the right time.<sup><a href="#user-content-fn-2" id="user-content-fnref-2-3" data-footnote-ref aria-describedby="footnote-label">3</a></sup></p>
<p>Another approach: build skills that load domain-specific gotchas automatically. A <code>nuxt-content</code> skill that injects the gotchas doc whenever you’re working with content queries. In theory, this is cleaner—context loads without you thinking about it. In practice, I’ve found skills don’t always activate when expected. The trigger conditions can be fuzzy, and sometimes Claude just doesn’t invoke them. Vercel’s agent evals confirmed this: skills were never invoked in 56% of their test cases, producing zero improvement over baseline.<sup><a href="#user-content-fn-9" id="user-content-fnref-9" data-footnote-ref aria-describedby="footnote-label">6</a></sup> The docs-based setup is more predictable: I know Claude will read what I point it to.</p>
<h2 id="one-agent-per-domain">One Agent Per Domain<a class="heading-link" aria-label="Link to section" href="#one-agent-per-domain"><span class="heading-link-icon">#</span></a></h2>
<p>I take this further with custom agents. Each agent has its own documentation file that loads only when needed. If you’re new to how these customization layers work together, I wrote a <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/claude-code-customization-guide-claudemd-skills-subagents/" class="internal-link astro-3tyn5ojg"> detailed comparison of CLAUDE.md, skills, and subagents </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents</span> <span class="preview-description astro-3tyn5ojg">The complete guide to customizing Claude Code. Compare CLAUDE.md, slash commands, skills, and subagents with practical examples showing when to use each.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">tooling</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Dec 21, 2025</time> </span> </span> </span>  <script>
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
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>.claude/agents/</span></span>
<span class="line"><span>├── nuxt-content-specialist.md   # Content queries, MDC, search</span></span>
<span class="line"><span>├── nuxt-ui-specialist.md        # Component styling, theming</span></span>
<span class="line"><span>├── vue-specialist.md            # Reactivity, composables</span></span>
<span class="line"><span>└── nuxt-specialist.md           # Routing, config, deployment</span></span></code><button type="button" class="copy" data-code=".claude/agents/
├── nuxt-content-specialist.md   # Content queries, MDC, search
├── nuxt-ui-specialist.md        # Component styling, theming
├── vue-specialist.md            # Reactivity, composables
└── nuxt-specialist.md           # Routing, config, deployment" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>When I’m debugging a content query, Claude loads the nuxt-content-specialist. When I’m styling a component, it loads nuxt-ui-specialist. The specialist agents know to fetch the latest documentation from official sources—they don’t rely on stale training data.</p>
<p>This is why I don’t use MCPs like context7 for documentation. Agents can fetch llms.txt directly from official docs sites and find what they need. No tool definition bloat, no intermediate tokens—just a focused research task in its own context window. I wrote more about <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/why-you-dont-need-nuxt-mcp-claude-code/" class="internal-link astro-3tyn5ojg"> why I use custom research agents instead of MCPs </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Why You Don&#39;t Need the Nuxt MCP When You Use Claude Code</span> <span class="preview-description astro-3tyn5ojg">Why I use custom research agents instead of MCP servers for AI-assisted development. Learn how llms.txt enables context-efficient documentation fetching with a practical Nuxt Content agent example.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">nuxt</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Dec 31, 2025</time> </span> </span> </span>  <script>
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
<p>Skills work similarly—with <code>context:fork</code>, they run in isolated contexts without polluting your main conversation. The agent has both the ability and motivation to read real documentation. No context7, no MCP overhead.</p>
<astro-island uid="1aLDj8" prefix="r10" component-url="/_astro/ProgressiveDisclosureExplorer.BcFIFvIM.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{}" ssr client="load" opts="{&quot;name&quot;:&quot;ProgressiveDisclosureExplorer&quot;,&quot;value&quot;:true}" await-children><div class="w-full max-w-3xl mx-auto my-8"><div class="rounded-lg overflow-hidden border border-[rgb(var(--color-border))] shadow-2xl"><div class="flex items-center gap-2 px-4 py-3 bg-[rgb(var(--color-card))] border-b border-[rgb(var(--color-border))]"><div class="flex gap-2"><div class="w-3 h-3 rounded-full bg-red-500/80"></div><div class="w-3 h-3 rounded-full bg-yellow-500/80"></div><div class="w-3 h-3 rounded-full bg-green-500/80"></div></div><div class="flex-1 text-center"><span class="text-sm text-[rgb(var(--color-text-base))] opacity-60 font-mono">progressive-disclosure</span></div><button class="text-xs px-2 py-1 rounded border border-[rgb(var(--color-border))]
                       text-[rgb(var(--color-text-base))] opacity-60 hover:opacity-100
                       hover:border-[rgb(var(--color-accent))] transition-all">Animate</button></div><div class="bg-[rgb(var(--color-fill))] font-mono text-sm p-4"><div class="flex items-center gap-4 mb-4 text-xs"><div class="flex items-center gap-2"><div class="w-2 h-2 rounded-full bg-green-400 animate-pulse"></div><span class="text-[rgb(var(--color-text-base))] opacity-70">Always loaded</span></div><div class="flex items-center gap-2"><div class="w-2 h-2 rounded-full bg-[rgb(var(--color-text-base))] opacity-30"></div><span class="text-[rgb(var(--color-text-base))] opacity-70">On-demand</span></div></div><div class="space-y-3"><div><button class="w-full text-left rounded-lg border transition-all duration-300 overflow-hidden border-[rgb(var(--color-accent))]  hover:border-[rgb(var(--color-accent))] hover:bg-[rgb(var(--color-card))]"><div class="p-3 flex items-center justify-between"><div class="flex items-center gap-3"><div class="w-3 h-3 rounded-full bg-green-400 animate-pulse "></div><span class="font-bold" style="color:rgb(var(--color-accent))">CLAUDE.md</span><span class="text-[rgb(var(--color-text-base))] opacity-50 text-xs">~500 tokens</span></div><div class="flex items-center gap-2"><span class="text-xs px-2 py-0.5 rounded bg-green-500/20 text-green-400">LOADED</span><svg class="w-4 h-4 text-[rgb(var(--color-text-base))] opacity-50 transition-transform rotate-180" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></div></div><div class="transition-all duration-300 max-h-96 opacity-100 overflow-hidden"><div class="px-3 pb-3 border-t border-[rgb(var(--color-border))]"><p class="text-[rgb(var(--color-text-base))] opacity-70 text-xs mt-3 mb-3">Entry point loaded every session. Keep minimal.</p><div class="text-xs text-[rgb(var(--color-text-base))] opacity-50 mb-2">Contents:</div><div class="space-y-1"><div class="flex items-center gap-2 text-xs pl-2"><span class="text-[rgb(var(--color-accent))]">→</span><span class="text-[rgb(var(--color-text-base))] opacity-80">Project overview</span></div><div class="flex items-center gap-2 text-xs pl-2"><span class="text-[rgb(var(--color-accent))]">→</span><span class="text-[rgb(var(--color-text-base))] opacity-80">Essential commands</span></div><div class="flex items-center gap-2 text-xs pl-2"><span class="text-[rgb(var(--color-accent))]">→</span><span class="text-[rgb(var(--color-text-base))] opacity-80">Stack info</span></div><div class="flex items-center gap-2 text-xs pl-2"><span class="text-[rgb(var(--color-accent))]">→</span><span class="text-[rgb(var(--color-text-base))] opacity-80">Pointers to docs</span></div></div></div></div></button></div><div><div class="flex justify-center -my-1"><div class="w-px h-4 transition-all duration-500 bg-[rgb(var(--color-border))]"></div></div><button class="w-full text-left rounded-lg border transition-all duration-300 overflow-hidden border-[rgb(var(--color-border))]  hover:border-[rgb(var(--color-accent))] hover:bg-[rgb(var(--color-card))]"><div class="p-3 flex items-center justify-between"><div class="flex items-center gap-3"><div class="w-3 h-3 rounded-full bg-[rgb(var(--color-text-base))] opacity-30 "></div><span class="font-bold" style="color:#22c55e">/docs</span><span class="text-[rgb(var(--color-text-base))] opacity-50 text-xs">~200-500 tokens per file</span></div><div class="flex items-center gap-2"><span class="text-xs px-2 py-0.5 rounded bg-[rgb(var(--color-card))] text-[rgb(var(--color-text-base))] opacity-50">ON-DEMAND</span><svg class="w-4 h-4 text-[rgb(var(--color-text-base))] opacity-50 transition-transform " fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></div></div><div class="transition-all duration-300 max-h-0 opacity-0 overflow-hidden"><div class="px-3 pb-3 border-t border-[rgb(var(--color-border))]"><p class="text-[rgb(var(--color-text-base))] opacity-70 text-xs mt-3 mb-3">Learnings and gotchas. Read when relevant.</p><div class="text-xs text-[rgb(var(--color-text-base))] opacity-50 mb-2">Contents:</div><div class="space-y-1"><div class="flex items-center gap-2 text-xs pl-2"><span class="text-[rgb(var(--color-accent))]">→</span><span class="text-[rgb(var(--color-text-base))] opacity-80">nuxt-content-gotchas.md</span></div><div class="flex items-center gap-2 text-xs pl-2"><span class="text-[rgb(var(--color-accent))]">→</span><span class="text-[rgb(var(--color-text-base))] opacity-80">testing-strategy.md</span></div><div class="flex items-center gap-2 text-xs pl-2"><span class="text-[rgb(var(--color-accent))]">→</span><span class="text-[rgb(var(--color-text-base))] opacity-80">SYSTEM_KNOWLEDGE_MAP.md</span></div></div></div></div></button></div><div><div class="flex justify-center -my-1"><div class="w-px h-4 transition-all duration-500 bg-[rgb(var(--color-border))]"></div></div><button class="w-full text-left rounded-lg border transition-all duration-300 overflow-hidden border-[rgb(var(--color-border))]  hover:border-[rgb(var(--color-accent))] hover:bg-[rgb(var(--color-card))]"><div class="p-3 flex items-center justify-between"><div class="flex items-center gap-3"><div class="w-3 h-3 rounded-full bg-[rgb(var(--color-text-base))] opacity-30 "></div><span class="font-bold" style="color:#a855f7">.claude/agents</span><span class="text-[rgb(var(--color-text-base))] opacity-50 text-xs">~300-800 tokens per agent</span></div><div class="flex items-center gap-2"><span class="text-xs px-2 py-0.5 rounded bg-[rgb(var(--color-card))] text-[rgb(var(--color-text-base))] opacity-50">ON-DEMAND</span><svg class="w-4 h-4 text-[rgb(var(--color-text-base))] opacity-50 transition-transform " fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></div></div><div class="transition-all duration-300 max-h-0 opacity-0 overflow-hidden"><div class="px-3 pb-3 border-t border-[rgb(var(--color-border))]"><p class="text-[rgb(var(--color-text-base))] opacity-70 text-xs mt-3 mb-3">Domain specialists. Loaded via Task tool.</p><div class="text-xs text-[rgb(var(--color-text-base))] opacity-50 mb-2">Contents:</div><div class="space-y-1"><div class="flex items-center gap-2 text-xs pl-2"><span class="text-[rgb(var(--color-accent))]">→</span><span class="text-[rgb(var(--color-text-base))] opacity-80">nuxt-content-specialist.md</span></div><div class="flex items-center gap-2 text-xs pl-2"><span class="text-[rgb(var(--color-accent))]">→</span><span class="text-[rgb(var(--color-text-base))] opacity-80">nuxt-ui-specialist.md</span></div><div class="flex items-center gap-2 text-xs pl-2"><span class="text-[rgb(var(--color-accent))]">→</span><span class="text-[rgb(var(--color-text-base))] opacity-80">vue-specialist.md</span></div></div></div></div></button></div></div><div class="mt-6 p-3 border border-dashed border-[rgb(var(--color-border))] rounded-lg"><div class="flex items-start gap-2"><span class="text-[rgb(var(--color-accent))]">↓</span><div class="text-xs text-[rgb(var(--color-text-base))] opacity-70"><strong class="text-[rgb(var(--color-text-base))] opacity-90">Loaded on demand:</strong> <!-- -->Claude reads /docs files when you reference them. Agents load via the Task tool. Only the top layer (CLAUDE.md) consumes tokens in every session.</div></div></div></div></div><p class="text-center mt-4 text-sm text-[rgb(var(--color-text-base))] opacity-50">Click each layer to expand. Press &quot;Animate&quot; to see on-demand loading.</p></div><!--astro:end--></astro-island>
<h2 id="it-compounds">It Compounds<a class="heading-link" aria-label="Link to section" href="#it-compounds"><span class="heading-link-icon">#</span></a></h2>
<p>This system creates a feedback loop:</p>
<astro-island uid="Zob4VM" prefix="r11" component-url="/_astro/FeedbackLoopAnimator.MEFfbYL1.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{}" ssr client="load" opts="{&quot;name&quot;:&quot;FeedbackLoopAnimator&quot;,&quot;value&quot;:true}" await-children><div class="w-full max-w-3xl mx-auto my-8"><div class="rounded-lg overflow-hidden border border-[rgb(var(--color-border))] shadow-2xl"><div class="flex items-center gap-2 px-4 py-3 bg-[rgb(var(--color-card))] border-b border-[rgb(var(--color-border))]"><div class="flex gap-2"><div class="w-3 h-3 rounded-full bg-red-500/80"></div><div class="w-3 h-3 rounded-full bg-yellow-500/80"></div><div class="w-3 h-3 rounded-full bg-green-500/80"></div></div><div class="flex-1 text-center"><span class="text-sm text-[rgb(var(--color-text-base))] opacity-60 font-mono">feedback-loop</span></div><div class="flex gap-2"><button class="text-xs px-2 py-1 rounded border border-[rgb(var(--color-border))]
                         text-[rgb(var(--color-text-base))] opacity-60 hover:opacity-100
                         hover:border-[rgb(var(--color-accent))] transition-all
                         disabled:opacity-30 disabled:cursor-not-allowed">Auto</button><button class="text-xs px-2 py-1 rounded border border-[rgb(var(--color-border))]
                         text-[rgb(var(--color-text-base))] opacity-60 hover:opacity-100
                         hover:border-[rgb(var(--color-accent))] transition-all">Reset</button></div></div><div class="bg-[rgb(var(--color-fill))] font-mono text-sm p-4"><div class="flex items-center justify-center gap-2 mb-6"><div class="flex items-center"><div class="w-8 h-8 rounded-full flex items-center justify-center text-sm transition-all duration-300 bg-[rgb(var(--color-accent))] text-[rgb(var(--color-fill))] scale-110">1</div><div class="w-8 h-0.5 transition-all duration-300 bg-[rgb(var(--color-border))]"></div></div><div class="flex items-center"><div class="w-8 h-8 rounded-full flex items-center justify-center text-sm transition-all duration-300 bg-[rgb(var(--color-card))] text-[rgb(var(--color-text-base))] opacity-30">2</div><div class="w-8 h-0.5 transition-all duration-300 bg-[rgb(var(--color-border))]"></div></div><div class="flex items-center"><div class="w-8 h-8 rounded-full flex items-center justify-center text-sm transition-all duration-300 bg-[rgb(var(--color-card))] text-[rgb(var(--color-text-base))] opacity-30">3</div><div class="w-8 h-0.5 transition-all duration-300 bg-[rgb(var(--color-border))]"></div></div><div class="flex items-center"><div class="w-8 h-8 rounded-full flex items-center justify-center text-sm transition-all duration-300 bg-[rgb(var(--color-card))] text-[rgb(var(--color-text-base))] opacity-30">4</div><div class="w-8 h-0.5 transition-all duration-300 bg-[rgb(var(--color-border))]"></div></div><div class="flex items-center"><div class="w-8 h-8 rounded-full flex items-center justify-center text-sm transition-all duration-300 bg-[rgb(var(--color-card))] text-[rgb(var(--color-text-base))] opacity-30">5</div></div></div><div class="space-y-2 mb-6"><div class="p-3 rounded-lg border transition-all duration-300 border-[rgb(var(--color-accent))] bg-[rgb(var(--color-accent))]/10"><div class="flex items-start gap-3"><div class="text-xl transition-all duration-300 scale-125">⚠</div><div class="flex-1"><div class="font-bold mb-1 transition-colors text-[rgb(var(--color-accent))]">1<!-- -->. <!-- -->Claude makes a mistake</div><div class="text-xs transition-all duration-300 text-[rgb(var(--color-text-base))] opacity-70 max-h-20">Uses `slug` instead of `stem` in a page collection query</div></div></div></div><div class="p-3 rounded-lg border transition-all duration-300 border-[rgb(var(--color-border))] opacity-40"><div class="flex items-start gap-3"><div class="text-xl transition-all duration-300 ">🔧</div><div class="flex-1"><div class="font-bold mb-1 transition-colors text-[rgb(var(--color-text-base))]">2<!-- -->. <!-- -->We fix it together</div><div class="text-xs transition-all duration-300 text-[rgb(var(--color-text-base))] opacity-30 max-h-0 overflow-hidden">Correct the query in conversation, explain why it failed</div></div></div></div><div class="p-3 rounded-lg border transition-all duration-300 border-[rgb(var(--color-border))] opacity-40"><div class="flex items-start gap-3"><div class="text-xl transition-all duration-300 ">💡</div><div class="flex-1"><div class="font-bold mb-1 transition-colors text-[rgb(var(--color-text-base))]">3<!-- -->. <!-- -->Run /learn to capture insight</div><div class="text-xs transition-all duration-300 text-[rgb(var(--color-text-base))] opacity-30 max-h-0 overflow-hidden">Analyze conversation for reusable, non-obvious learnings</div></div></div></div><div class="p-3 rounded-lg border transition-all duration-300 border-[rgb(var(--color-border))] opacity-40"><div class="flex items-start gap-3"><div class="text-xl transition-all duration-300 ">📄</div><div class="flex-1"><div class="font-bold mb-1 transition-colors text-[rgb(var(--color-text-base))]">4<!-- -->. <!-- -->Save to the right doc</div><div class="text-xs transition-all duration-300 text-[rgb(var(--color-text-base))] opacity-30 max-h-0 overflow-hidden">Append to nuxt-content-gotchas.md in /docs folder</div></div></div></div><div class="p-3 rounded-lg border transition-all duration-300 border-[rgb(var(--color-border))] opacity-40"><div class="flex items-start gap-3"><div class="text-xl transition-all duration-300 ">✓</div><div class="flex-1"><div class="font-bold mb-1 transition-colors text-[rgb(var(--color-text-base))]">5<!-- -->. <!-- -->Next session reads doc</div><div class="text-xs transition-all duration-300 text-[rgb(var(--color-text-base))] opacity-30 max-h-0 overflow-hidden">Claude reads gotchas doc before working with content queries</div></div></div></div></div><div class="flex items-center justify-between"><div class="text-xs text-[rgb(var(--color-text-base))] opacity-50">Step <!-- -->1<!-- --> of <!-- -->5</div><button class="px-4 py-2 rounded border border-[rgb(var(--color-accent))]
                         text-[rgb(var(--color-accent))] text-sm
                         hover:bg-[rgb(var(--color-accent))] hover:text-[rgb(var(--color-fill))]
                         transition-all disabled:opacity-30 disabled:cursor-not-allowed">Next Step →</button></div></div></div><p class="text-center mt-4 text-sm text-[rgb(var(--color-text-base))] opacity-50">Click &quot;Next Step&quot; to walk through the feedback loop, or &quot;Auto&quot; for automatic playback.</p><style>
        @keyframes fade-in {
          from { opacity: 0; transform: translateY(-10px); }
          to { opacity: 1; transform: translateY(0); }
        }
        .animate-fade-in {
          animation: fade-in 0.3s ease-out forwards;
        }
      </style></div><!--astro:end--></astro-island>
<p>Over time, my <code>/docs</code> folder becomes a curated knowledge base of <em>exactly the things AI coding tools get wrong</em> in my codebase. It’s like fine-tuning, but under my control.</p>
<p>I got this idea from a pattern for self-improving skills where agents automatically analyze sessions and update themselves.<sup><a href="#user-content-fn-5" id="user-content-fnref-5" data-footnote-ref aria-describedby="footnote-label">7</a></sup> I adapted it to use markdown documentation and a <code>/learn</code> command instead—giving me explicit control over what gets captured and where it goes.</p>
<p>An actual entry from my <code>nuxt-content-gotchas.md</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Page Collection Queries: Use </span><span style="color:#89DDFF;font-weight:bold">`stem`</span><span style="color:#61BDF2;font-weight:bold"> Not </span><span style="color:#89DDFF;font-weight:bold">`slug`</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">The </span><span style="color:#89DDFF">`slug`</span><span style="color:#9AA5CE"> field doesn&#39;t exist in page-type collections.</span></span>
<span class="line"><span style="color:#9AA5CE">Use </span><span style="color:#89DDFF">`stem`</span><span style="color:#9AA5CE"> (file path without extension) instead:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">// ❌ Fails: &quot;no such column: slug&quot;</span></span>
<span class="line"><span style="color:#9AA5CE">queryCollection(&#39;content&#39;).select(&#39;slug&#39;, &#39;title&#39;).all()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">// ✅ Works</span></span>
<span class="line"><span style="color:#9AA5CE">queryCollection(&#39;content&#39;).select(&#39;stem&#39;, &#39;title&#39;).all()</span></span></code><button type="button" class="copy" data-code="## Page Collection Queries: Use `stem` Not `slug`

The `slug` field doesn't exist in page-type collections.
Use `stem` (file path without extension) instead:

// ❌ Fails: &#34;no such column: slug&#34;
queryCollection('content').select('slug', 'title').all()

// ✅ Works
queryCollection('content').select('stem', 'title').all()" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Claude will never make this mistake again in my project. Not because I added it to CLAUDE.md—but because when it’s working with content queries, it reads the gotchas doc first.</p>
<h2 id="my-50-line-claudemd">My 50-Line CLAUDE.md<a class="heading-link" aria-label="Link to section" href="#my-50-line-claudemd"><span class="heading-link-icon">#</span></a></h2>
<p>The structure:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> CLAUDE.md</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Second Brain is a personal knowledge base using</span></span>
<span class="line"><span style="color:#9AA5CE">Zettelkasten-style wiki-links.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Commands</span></span>
<span class="line"><span style="color:#9AA5CE">pnpm dev          # Start dev server</span></span>
<span class="line"><span style="color:#9AA5CE">pnpm lint:fix     # Auto-fix linting issues</span></span>
<span class="line"><span style="color:#9AA5CE">pnpm typecheck    # Verify type safety</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Run </span><span style="color:#89DDFF">`pnpm lint:fix &amp;&amp; pnpm typecheck`</span><span style="color:#9AA5CE"> after code changes.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Stack</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Nuxt 4, @nuxt/content v3, @nuxt/ui v3</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Structure</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `app/`</span><span style="color:#9AA5CE"> - Vue application</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `content/`</span><span style="color:#9AA5CE"> - Markdown files</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `content.config.ts`</span><span style="color:#9AA5CE"> - Collection schemas</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Further Reading</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**IMPORTANT:**</span><span style="color:#9AA5CE"> Read relevant docs below before starting any task.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `docs/nuxt-content-gotchas.md`</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `docs/testing-strategy.md`</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `docs/SYSTEM_KNOWLEDGE_MAP.md`</span></span></code><button type="button" class="copy" data-code="# CLAUDE.md

Second Brain is a personal knowledge base using
Zettelkasten-style wiki-links.

## Commands
pnpm dev          # Start dev server
pnpm lint:fix     # Auto-fix linting issues
pnpm typecheck    # Verify type safety

Run `pnpm lint:fix &#38;&#38; pnpm typecheck` after code changes.

## Stack
- Nuxt 4, @nuxt/content v3, @nuxt/ui v3

## Structure
- `app/` - Vue application
- `content/` - Markdown files
- `content.config.ts` - Collection schemas

## Further Reading

**IMPORTANT:** Read relevant docs below before starting any task.

- `docs/nuxt-content-gotchas.md`
- `docs/testing-strategy.md`
- `docs/SYSTEM_KNOWLEDGE_MAP.md`" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>That’s it. Universal context only. Everything else lives in docs, agents, or tooling.</p>
<h2 id="cross-tool-compatibility">Cross-Tool Compatibility<a class="heading-link" aria-label="Link to section" href="#cross-tool-compatibility"><span class="heading-link-icon">#</span></a></h2>
<p>If you use multiple AI coding tools, you don’t need separate config files. VS Code Copilot and Cursor both support <code>agents.md</code> for project-level instructions. You can symlink it to share the same configuration:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#51597D;font-style:italic"># Create a symlink so all tools read the same file</span></span>
<span class="line"><span style="color:#C0CAF5">ln</span><span style="color:#E0AF68"> -s</span><span style="color:#9ECE6A"> CLAUDE.md</span><span style="color:#9ECE6A"> agents.md</span></span></code><button type="button" class="copy" data-code="# Create a symlink so all tools read the same file
ln -s CLAUDE.md agents.md" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Now your minimal, focused instructions work across Claude Code, Copilot, and Cursor. One source of truth, no drift between tools.</p>
<h2 id="how-this-played-out-last-week">How This Played Out Last Week<a class="heading-link" aria-label="Link to section" href="#how-this-played-out-last-week"><span class="heading-link-icon">#</span></a></h2>
<p>Last week I was implementing semantic search. When Claude started working on content queries, it read <code>nuxt-content-gotchas.md</code> first—as my CLAUDE.md instructs. The stem/slug gotcha was already there.</p>
<p>No mistake. No correction needed.</p>
<p>But during the session, we discovered something new: <code>queryCollectionSearchSections</code> returns IDs with a leading slash. Don’t add another slash when constructing URLs.</p>
<p>I ran <code>/learn</code>. Claude proposed:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Search Section IDs</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Returns IDs with leading slash (</span><span style="color:#89DDFF">`/slug#section`</span><span style="color:#9AA5CE">).</span></span>
<span class="line"><span style="color:#9AA5CE">Don&#39;t add another slash when constructing URLs.</span></span></code><button type="button" class="copy" data-code="## Search Section IDs

Returns IDs with leading slash (`/slug#section`).
Don't add another slash when constructing URLs." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Added. Next time I work on search, Claude will know.</p>
<hr/>
<p>AI tools being stateless isn’t a bug to fight. It’s a design constraint—like limited screen real estate or slow network connections. Accept it, and you can build systems that work with it.</p>
<p><strong>Keep CLAUDE.md minimal. Let tooling enforce what it can. Capture learnings as you go. Load context on demand.</strong></p>
<p>One caveat: you can never be 100% sure agents will read your docs when they face issues. For tricky domains like Nuxt Content—where training data is sparse or outdated—I’ve learned to be explicit in my prompts. When I know I’m working on something with poor training coverage, I’ll add to the plan: “If you encounter issues with Nuxt Content APIs, read <code>docs/nuxt-content-gotchas.md</code> first.” This nudge makes the difference between the agent guessing based on outdated patterns and actually consulting current knowledge.</p>
<p>The AI forgets. Your documentation doesn’t.</p>
<hr/>
<section data-footnotes class="footnotes"><h2 class="sr-only" id="footnote-label">Footnotes<a class="heading-link" aria-label="Link to section" href="#footnote-label"><span class="heading-link-icon">#</span></a></h2>
<ol>
<li id="user-content-fn-1">
<p>LLMs have no memory between sessions—context is just tokens in a sliding window. See Factory’s analysis in <a href="https://factory.ai/news/context-window-problem" rel="noopener noreferrer" target="_blank">The Context Window Problem</a>. <a href="#user-content-fnref-1" data-footnote-backref aria-label="Back to reference 1" class="data-footnote-backref">↩</a></p>
</li>
<li id="user-content-fn-6">
<p>Dex Horthy, <a href="https://www.youtube.com/watch?v=rmvDxxNubIg" rel="noopener noreferrer" target="_blank">No Vibes Allowed: Solving Hard Problems in Complex Codebases</a>. Dex is the founder of HumanLayer and creator of the Ralph technique for autonomous AI coding. His <a href="https://www.humanlayer.dev/blog/12-factor-agents" rel="noopener noreferrer" target="_blank">12 Factor Agents</a> manifesto includes “Make Your Agent a Stateless Reducer” as Factor 12. <a href="#user-content-fnref-6" data-footnote-backref aria-label="Back to reference 2" class="data-footnote-backref">↩</a></p>
</li>
<li id="user-content-fn-2">
<p>HumanLayer’s guide on <a href="https://www.humanlayer.dev/blog/writing-a-good-claude-md" rel="noopener noreferrer" target="_blank">Writing a Good CLAUDE.md</a> recommends keeping files under 60 lines and using progressive disclosure for detailed instructions. <a href="#user-content-fnref-2" data-footnote-backref aria-label="Back to reference 3" class="data-footnote-backref">↩</a> <a href="#user-content-fnref-2-2" data-footnote-backref aria-label="Back to reference 3-2" class="data-footnote-backref">↩<sup>2</sup></a> <a href="#user-content-fnref-2-3" data-footnote-backref aria-label="Back to reference 3-3" class="data-footnote-backref">↩<sup>3</sup></a></p>
</li>
<li id="user-content-fn-7">
<p>Moss, <a href="https://banay.me/dont-waste-your-backpressure" rel="noopener noreferrer" target="_blank">Don’t Waste Your Back Pressure</a>. Backpressure—automated feedback from type systems, linters, and build tools—is what enables agents to work on longer-horizon tasks without constant human intervention. <a href="#user-content-fnref-7" data-footnote-backref aria-label="Back to reference 4" class="data-footnote-backref">↩</a></p>
</li>
<li id="user-content-fn-8">
<p>Geoffrey Huntley, <a href="https://ghuntley.com/ralph/" rel="noopener noreferrer" target="_blank">Ralph</a>. Ralph is a technique for autonomous AI coding where tasks are queued and executed without human intervention, making automated checks on commit essential. <a href="#user-content-fnref-8" data-footnote-backref aria-label="Back to reference 5" class="data-footnote-backref">↩</a></p>
</li>
<li id="user-content-fn-9">
<p>Jude Gao, <a href="https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals" rel="noopener noreferrer" target="_blank">AGENTS.md outperforms skills in our agent evals</a>. Vercel’s evals found that a compressed docs index embedded directly in AGENTS.md achieved 100% pass rate, while skills maxed out at 79% even with explicit instructions—and performed no better than baseline when left to trigger naturally. <a href="#user-content-fnref-9" data-footnote-backref aria-label="Back to reference 6" class="data-footnote-backref">↩</a></p>
</li>
<li id="user-content-fn-5">
<p>Developers Digest, <a href="https://www.youtube.com/watch?v=-4nUCaMNBR8" rel="noopener noreferrer" target="_blank">Self-Improving Skills in Claude Code</a>. A pattern for capturing learnings automatically: skills analyze sessions, extract corrections, and update themselves. <a href="#user-content-fnref-5" data-footnote-backref aria-label="Back to reference 7" class="data-footnote-backref">↩</a></p>
</li>
</ol>
</section> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/claude-code/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">claude-code</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai-tools/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai-tools</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/developer-experience/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">developer-experience</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/productivity/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-5"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">productivity</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools";

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
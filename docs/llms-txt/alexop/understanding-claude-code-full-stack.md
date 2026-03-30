# Source: https://alexop.dev/posts/understanding-claude-code-full-stack

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/understanding-claude-code-full-stack/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Understanding Claude Code&#39;s Full Stack: MCP, Skills, Subagents, and Hooks Explained | alexop.dev</title><meta name="title" content="Understanding Claude Code's Full Stack: MCP, Skills, Subagents, and Hooks Explained | alexop.dev"><meta name="description" content="A practical guide to Claude Code's features — explained in the order they were introduced: MCP (2024), Claude Code core (Feb 2025), Plugins (2025), and Agent Skills (Oct 2025). What each does, how they fit together, and when to use what."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Understanding Claude Code's Full Stack: MCP, Skills, Subagents, and Hooks Explained | alexop.dev"><meta property="og:description" content="A practical guide to Claude Code's features — explained in the order they were introduced: MCP (2024), Claude Code core (Feb 2025), Plugins (2025), and Agent Skills (Oct 2025). What each does, how they fit together, and when to use what."><meta property="og:url" content="https://alexop.dev/posts/understanding-claude-code-full-stack/"><meta property="og:image" content="https://alexop.dev/posts/understanding-claude-codes-full-stack-mcp-skills-subagents-and-hooks-explained/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-11-09T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/understanding-claude-code-full-stack/"><meta property="twitter:title" content="Understanding Claude Code's Full Stack: MCP, Skills, Subagents, and Hooks Explained | alexop.dev"><meta property="twitter:description" content="A practical guide to Claude Code's features — explained in the order they were introduced: MCP (2024), Claude Code core (Feb 2025), Plugins (2025), and Agent Skills (Oct 2025). What each does, how they fit together, and when to use what."><meta property="twitter:image" content="https://alexop.dev/posts/understanding-claude-codes-full-stack-mcp-skills-subagents-and-hooks-explained/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Understanding Claude Code's Full Stack: MCP, Skills, Subagents, and Hooks Explained | alexop.dev","description":"A practical guide to Claude Code's features — explained in the order they were introduced: MCP (2024), Claude Code core (Feb 2025), Plugins (2025), and Agent Skills (Oct 2025). What each does, how they fit together, and when to use what.","image":"https://alexop.dev/posts/understanding-claude-codes-full-stack-mcp-skills-subagents-and-hooks-explained/index.png","datePublished":"2025-11-09T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: understanding-claude-codes-full-stack-mcp-skills-subagents-and-hooks-explained; }@layer astro { ::view-transition-old(understanding-claude-codes-full-stack-mcp-skills-subagents-and-hooks-explained) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(understanding-claude-codes-full-stack-mcp-skills-subagents-and-hooks-explained) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(understanding-claude-codes-full-stack-mcp-skills-subagents-and-hooks-explained) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(understanding-claude-codes-full-stack-mcp-skills-subagents-and-hooks-explained) { 
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
</style><style>.file-tree__item:where(.astro-o25vlg2d){margin:0;padding:0;position:relative}.file-tree__item:where(.astro-o25vlg2d):before{content:"";position:absolute;left:calc(.5rem + (var(--level) * 1.25rem));top:0;bottom:0;width:1px;background:rgba(var(--color-text-base),.15)}.file-tree__item:where(.astro-o25vlg2d):last-child:before{bottom:50%}.file-tree__item:where(.astro-o25vlg2d):after{content:"";position:absolute;left:calc(.5rem + (var(--level) * 1.25rem));top:50%;width:.75rem;height:1px;background:rgba(var(--color-text-base),.15)}.file-tree__folder:where(.astro-o25vlg2d){margin:0;padding:0}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d){list-style:none;cursor:pointer;display:flex;gap:.5rem;align-items:center;padding:.2rem .5rem .2rem calc(1.5rem + (var(--level) * 1.25rem));border-radius:.25rem;transition:background-color .15s ease;line-height:1.6;position:relative}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d):hover{background:rgba(var(--color-text-base),.05)}.file-tree__folder:where(.astro-o25vlg2d)[open]>summary:where(.astro-o25vlg2d) .file-tree__caret:where(.astro-o25vlg2d){transform:rotate(90deg)}.file-tree__folder:where(.astro-o25vlg2d):not([open])>summary:where(.astro-o25vlg2d) .file-tree__caret:where(.astro-o25vlg2d){transform:rotate(0)}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d)::-webkit-details-marker{display:none}.file-tree__list:where(.astro-o25vlg2d){list-style:none;margin:0;padding:0}.file-tree__file:where(.astro-o25vlg2d){display:flex;gap:.5rem;align-items:center;padding:.2rem .5rem .2rem calc(1.5rem + (var(--level) * 1.25rem));border-radius:.25rem;text-decoration:none;color:inherit;transition:background-color .15s ease;line-height:1.6;position:relative}.file-tree__file:where(.astro-o25vlg2d):hover{background:rgba(var(--color-text-base),.05)}a:where(.astro-o25vlg2d).file-tree__file:hover .file-tree__name:where(.astro-o25vlg2d){color:rgb(var(--color-accent))}.file-tree__icon:where(.astro-o25vlg2d){width:1rem;height:1rem;flex-shrink:0;color:rgba(var(--color-text-base),.4);display:inline-flex;align-items:center;justify-content:center}.file-tree__icon--file:where(.astro-o25vlg2d){color:rgba(var(--color-text-base),.4)}.file-tree__icon--colored:where(.astro-o25vlg2d){color:inherit}.file-tree__icon--text:where(.astro-o25vlg2d){font-weight:600;font-size:.875rem;display:inline-flex;align-items:center;justify-content:center;width:1rem;height:1rem}.file-tree__name:where(.astro-o25vlg2d){white-space:nowrap;transition:color .15s ease;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace}.file-tree__comment:where(.astro-o25vlg2d){color:rgba(var(--color-text-base),.5);font-style:italic;margin-left:.5rem;white-space:nowrap;font-size:.9em}.file-tree__caret:where(.astro-o25vlg2d){width:.75rem;height:.75rem;transition:transform .2s ease;flex-shrink:0;color:rgba(var(--color-text-base),.5);font-size:.625rem;display:inline-flex;align-items:center;justify-content:center;transform-origin:center}
</style><style>.file-tree:where(.astro-htwbjus4){font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace;font-size:.8125rem;background:rgb(var(--color-card));color:rgb(var(--color-text-base));border:1px solid rgba(var(--color-border),.5);border-radius:.5rem;padding:.75rem;margin:1.5rem 0;overflow-x:auto}.file-tree__list:where(.astro-htwbjus4){list-style:none;margin:0;padding:0}.file-tree__list:where(.astro-htwbjus4)>li:where(.astro-htwbjus4):first-child:before,.file-tree__list:where(.astro-htwbjus4)>li:where(.astro-htwbjus4):first-child:after{display:none}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar{height:.5rem}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-track{background:rgb(var(--color-fill))}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-thumb{background:rgb(var(--color-border));border-radius:.25rem}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-thumb:hover{background:rgb(var(--color-card-muted))}
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: mcp; }@layer astro { ::view-transition-old(mcp) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(mcp) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(mcp) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(mcp) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-6"] { view-transition-name: tooling; }@layer astro { ::view-transition-old(tooling) { 
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
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-6"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-6"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-6"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-6"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-6"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-6"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-6"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-6"] { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Understanding Claude Code&#39;s Full Stack: MCP, Skills, Subagents, and Hooks Explained</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-11-09T00:00:00.000Z">Nov 9, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="JQunn" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Understanding Claude Code&#39;s Full Stack: MCP, Skills, Subagents, and Hooks Explained&quot;],&quot;content&quot;:[0,&quot;import Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\nimport Aside from \&quot;@features/mdx-components/components/Aside.astro\&quot;;\nimport FileTree from \&quot;@features/filetree/components/FileTree.astro\&quot;;\nimport Figure from \&quot;@features/mdx-components/components/Figure.astro\&quot;;\nimport TLDR from \&quot;@features/mdx-components/components/TLDR.astro\&quot;;\nimport InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\nimport claudeSenpai from \&quot;@assets/images/claude-code/claudesenpai.png\&quot;;\nimport claudeMd from \&quot;@assets/images/claude-code/claudeMd.png\&quot;;\n\nI&#39;ve been using Claude Code for months. Mostly for quick edits and generating boilerplate. The vibe coding tool everyone talks about.\n\nThen I actually explored what it could do. MCP servers. Slash commands. Plugins. Skills. Hooks. Subagents. CLAUDE.md files.\n\nI was blown away. Claude Code isn&#39;t just a coding assistant. It&#39;s a framework for orchestrating AI agents. It speeds up development in ways I&#39;ve never seen before.\n\nMost people use one or two features. They miss how these features stack together. This guide explains each concept **in the order they build on each other** — from external connections to automatic behaviors. (New to using LLMs for development? Start with my &lt;InternalLink slug=\&quot;how-i-use-llms\&quot;&gt;overview of how I use LLMs&lt;/InternalLink&gt; for context.)\n\n&gt; Claude Code is, with hindsight, poorly named. It&#39;s not purely a coding tool: it&#39;s a tool for general computer automation. Anything you can achieve by typing commands into a computer is something that can now be automated by Claude Code. It&#39;s best described as a general agent. Skills make this a whole lot more obvious and explicit.\n&gt;\n&gt; — Simon Willison, [Claude Skills are awesome, maybe a bigger deal than MCP](https://simonwillison.net/2025/Oct/16/claude-skills/)\n\n&lt;TLDR\n  items={[\n    \&quot;CLAUDE.md files give Claude project memory and context\&quot;,\n    \&quot;Slash commands are user-triggered, repeatable workflows\&quot;,\n    \&quot;Subagents handle parallel work in isolated contexts\&quot;,\n    \&quot;Hooks automatically react to lifecycle events\&quot;,\n    \&quot;Plugins bundle commands, hooks, and skills for sharing\&quot;,\n    \&quot;MCP connects external tools through a universal protocol\&quot;,\n    \&quot;Skills activate automatically based on task context\&quot;,\n  ]}\n/&gt;\n\n## The feature stack\n\n1. **Model Context Protocol (MCP)** — the foundation for connecting external tools and data sources\n2. **Claude Code core features** — project memory, slash commands, subagents, and hooks\n3. **Plugins** — shareable packages that bundle commands, hooks, and skills\n4. **Agent Skills** — automatic, model-invoked capabilities that activate based on task context\n\n&lt;Figure\n  src={claudeSenpai}\n  caption=\&quot;Claude Senpai knows all the features!\&quot;\n  alt=\&quot;Robot Claude Senpai with a knowing expression\&quot;\n  size=\&quot;medium\&quot;\n/&gt;\n\n---\n\n## 1) Model Context Protocol (MCP) — connecting external systems\n\n```mermaid\nsequenceDiagram\n    actor User\n    participant Claude\n    participant MCPServer\n\n    User-&gt;&gt;Claude: /mcp connect github\n    Claude-&gt;&gt;MCPServer: Authenticate + request capabilities\n    MCPServer--&gt;&gt;Claude: Return tools/resources/prompts\n    Claude--&gt;&gt;User: Display /mcp__github__* commands\n```\n\n**What it is.** The &lt;InternalLink slug=\&quot;what-is-model-context-protocol-mcp\&quot;&gt;Model Context Protocol&lt;/InternalLink&gt; connects Claude Code to external tools and data sources. Think universal adapter for GitHub, databases, APIs, and other systems.\n\n**How it works.** Connect an MCP server, get access to its tools, resources, and prompts as slash commands:\n\n```bash\n# Install a server\nclaude mcp add playwright npx @playwright/mcp@latest\n\n# Use it\n/mcp__playwright__create-test [args]\n```\n\n&lt;Alert type=\&quot;caution\&quot; title=\&quot;Context Window Management\&quot;&gt;\n  Each MCP server consumes context. Monitor with `/context` and remove unused\n  servers.\n&lt;/Alert&gt;\n\n**The gotcha.** MCP servers expose their own tools — they don&#39;t inherit Claude&#39;s Read, Write, or Bash unless explicitly provided.\n\n**Real-world example.** Want to see MCP in action? Check out how to &lt;InternalLink slug=\&quot;building_ai_qa_engineer_claude_code_playwright\&quot;&gt;build an AI QA engineer with Playwright MCP&lt;/InternalLink&gt; that tests your app like a real user.\n\n---\n\n## 2) Claude Code core features\n\n### 2.1) Project memory with `CLAUDE.md`\n\n**What it is.** Markdown files Claude loads at startup. They give Claude memory about your project&#39;s conventions, architecture, and patterns.\n\n**How it works.** Files merge hierarchically from enterprise → user (`~/.claude/CLAUDE.md`) → project (`./CLAUDE.md`). When you reference `@components/Button.vue`, Claude also reads CLAUDE.md from that directory and its parents.\n\n**Example structure for a Vue app:**\n\n&lt;FileTree\n  tree={[\n    {\n      name: \&quot;my-vue-app\&quot;,\n      open: true,\n      children: [\n        {\n          name: \&quot;CLAUDE.md\&quot;,\n          comment: \&quot;Project-wide conventions, tech stack, build commands\&quot;,\n        },\n        {\n          name: \&quot;src\&quot;,\n          open: true,\n          children: [\n            {\n              name: \&quot;components\&quot;,\n              open: true,\n              children: [\n                {\n                  name: \&quot;CLAUDE.md\&quot;,\n                  comment: \&quot;Component patterns, naming conventions, prop types\&quot;,\n                },\n                { name: \&quot;Button.vue\&quot; },\n                { name: \&quot;Card.vue\&quot; },\n              ],\n            },\n            {\n              name: \&quot;pages\&quot;,\n              open: true,\n              children: [\n                {\n                  name: \&quot;CLAUDE.md\&quot;,\n                  comment: \&quot;Routing patterns, page structure, data fetching\&quot;,\n                },\n                { name: \&quot;Home.vue\&quot; },\n                { name: \&quot;About.vue\&quot; },\n              ],\n            },\n          ],\n        },\n      ],\n    },\n  ]}\n/&gt;\n\nWhen you work on `src/components/Button.vue`, Claude loads context from:\n\n1. Enterprise CLAUDE.md (if configured)\n2. User `~/.claude/CLAUDE.md` (personal preferences)\n3. Project root `CLAUDE.md` (project-wide info)\n4. `src/components/CLAUDE.md` (component-specific patterns)\n\n**What goes in.** Common commands, coding standards, architectural patterns. Keep it concise — reference guide, not documentation. Need help creating your own? Check out this [CLAUDE.md creation guide](/prompts/claude/claude-create-md).\n\nHere&#39;s my blog&#39;s CLAUDE.md:\n\n````markdown\n# CLAUDE.md\n\n## Project Overview\n\nAlexander Opalic&#39;s personal blog built on AstroPaper - Astro-based blog theme with TypeScript, React, TailwindCSS.\n\n**Tech Stack**: Astro 5, TypeScript, React, TailwindCSS, Shiki, FuseJS, Playwright\n\n## Development Commands\n\n```bash\nnpm run dev              # Build + Pagefind + dev server (localhost:4321)\nnpm run build            # Production build\nnpm run lint             # ESLint for .astro, .ts, .tsx\n---\n```\n````\n\n### 2.2) Slash Commands — explicit, reusable prompts\n\n```mermaid\ngraph LR\n    User[/ /my-command args /]\n    PreBash[Pre-execution Bash Steps]\n    Prompt[Markdown prompt]\n    Claude[Claude processes]\n    Output[Result]\n\n    User --&gt; PreBash --&gt; Prompt --&gt; Claude --&gt; Output\n```\n\n**What they are.** Markdown files in `.claude/commands/` you trigger manually by typing `/name [args]`. User-controlled workflows.\n\n**Key features:**\n\n- `$ARGUMENTS` or `$1`, `$2` for argument passing\n- `@file` syntax to inline code\n- `allowed-tools: Bash(...)` for pre-execution scripts\n- &lt;InternalLink slug=\&quot;xml-tagged-prompts-framework-reliable-ai-responses\&quot;&gt;\n    XML-tagged prompts\n  &lt;/InternalLink&gt;\n  for reliable outputs\n\n**When to use.** Repeatable workflows you trigger on demand — code reviews, commit messages, scaffolding. For a complete example of a git workflow built entirely with slash commands, see my &lt;InternalLink slug=\&quot;claude-code-slash-commands-guide\&quot;&gt;Slash Commands Guide&lt;/InternalLink&gt;. Want to create your own? Use this [slash command creation guide](/prompts/claude/claude-create-command).\n\n**Example structure:**\n\n```markdown\n---\ndescription: Create new slash commands\nargument-hint: [name] [purpose]\nallowed-tools: Bash(mkdir:*), Bash(tee:*)\n---\n\n# /create-command\n\nGenerate slash command files with proper structure.\n\n**Inputs:** `$1` = name, `$2` = purpose\n**Outputs:** `STATUS=WROTE PATH=.claude/commands/{name}.md`\n\n[... instructions ...]\n```\n\nCommands can create commands. Meta, but powerful.\n\n---\n\n### 2.3) Subagents — specialized AI personalities for delegation\n\n```mermaid\nsequenceDiagram\n    participant Main\n    participant SubA\n    participant SubB\n\n    Main-&gt;&gt;SubA: task: security analysis\n    Main-&gt;&gt;SubB: task: test generation\n    par Parallel execution\n        SubA--&gt;&gt;Main: results\n        SubB--&gt;&gt;Main: results\n    end\n```\n\n**What they are.** Pre-configured AI personalities with specific expertise areas. Each subagent has its own system prompt, allowed tools, and separate context window. When Claude encounters a task matching a subagent&#39;s expertise, it delegates automatically.\n\n**Why use them.** Keep your main conversation clean while offloading specialized work. Each subagent works independently in its own context window, preventing token bloat. Run multiple subagents in parallel for concurrent analysis.\n\n&lt;Alert type=\&quot;tip\&quot; title=\&quot;Avoiding Context Poisoning\&quot;&gt;\n  Subagents prevent \&quot;context poisoning\&quot; — when detailed implementation work\n  clutters your main conversation. Use subagents for deep dives (security\n  audits, test generation, refactoring) that would otherwise fill your primary\n  context with noise.\n&lt;/Alert&gt;\n\n**Example structure:**\n\n```markdown\n---\nname: security-auditor\ndescription: Analyzes code for security vulnerabilities\ntools: Read, Grep, Bash # Controls what this personality can access\nmodel: sonnet # Optional: sonnet, opus, haiku, inherit\n---\n\nYou are a security-focused code auditor.\n\nIdentify vulnerabilities (XSS, SQL injection, CSRF, etc.)\nCheck dependencies and packages\nVerify auth/authorization\nReview data validation\n\nProvide severity levels: Critical, High, Medium, Low.\nFocus on OWASP Top 10.\n```\n\nThe system prompt shapes the subagent&#39;s behavior. The `description` helps Claude know when to delegate. The `tools` restrict what the personality can access.\n\n**Best practices:** One expertise area per subagent. Grant minimal tool access. Use `haiku` for simple tasks, `sonnet` for complex analysis. Run independent work in parallel. Need a template? Check out this [subagent creation guide](/prompts/claude/claude-create-agent).\n\n---\n\n### 2.4) Hooks — automatic event-driven actions\n\n```mermaid\ngraph TD\n    Event[Lifecycle Event]\n    HookA[Hook 1]\n    HookB[Hook 2]\n    HookC[Hook 3]\n\n    Event --&gt; HookA\n    Event --&gt; HookB\n    Event --&gt; HookC\n```\n\n**What they are.** JSON-configured handlers in `.claude/settings.json` that trigger automatically on lifecycle events. No manual invocation.\n\n**Available events:** `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Notification`, `Stop`, `SubagentStop`, `SessionStart`\n\n**Two modes:**\n\n- **Command:** Run shell commands (fast, predictable)\n- **Prompt:** Let Claude decide with the LLM (flexible, context-aware)\n\n**Example:** Auto-lint after file edits.\n\n```json\n{\n  \&quot;hooks\&quot;: {\n    \&quot;PostToolUse\&quot;: [\n      {\n        \&quot;matcher\&quot;: \&quot;Edit|Write\&quot;,\n        \&quot;hooks\&quot;: [\n          {\n            \&quot;type\&quot;: \&quot;command\&quot;,\n            \&quot;command\&quot;: \&quot;\\\&quot;$CLAUDE_PROJECT_DIR\\\&quot;/.claude/hooks/run-oxlint.sh\&quot;\n          }\n        ]\n      }\n    ]\n  }\n}\n```\n\n```bash\n#!/usr/bin/env bash\nfile_path=\&quot;$(jq -r &#39;.tool_input.file_path // \&quot;\&quot;&#39;)\&quot;\n\nif [[ \&quot;$file_path\&quot; =~ \\.(js|jsx|ts|tsx|vue)$ ]]; then\n  pnpm lint:fast\nfi\n```\n\n**Common uses:** Auto-format after edits, require approval for bash commands, validate writes, initialize sessions. For a practical example, see how to &lt;InternalLink slug=\&quot;claude-code-notification-hooks\&quot;&gt;set up desktop notifications&lt;/InternalLink&gt; when Claude needs your attention. Want to create your own hooks? Use this [hook creation guide](/prompts/claude/claude-create-hook).\n\n---\n\n## 3) Plugins — shareable, packaged configurations\n\n```mermaid\nclassDiagram\n    class Plugin {\n      name\n      version\n      author\n    }\n    Plugin --&gt; Commands\n    Plugin --&gt; Hooks\n    Plugin --&gt; Skills\n```\n\n**What they are.** Distributable bundles of commands, hooks, skills, and metadata. Share your setup with teammates or install pre-built configurations.\n\n**Basic structure:**\n\n&lt;FileTree\n  tree={[\n    {\n      name: \&quot;my-plugin\&quot;,\n      open: true,\n      children: [\n        {\n          name: \&quot;.claude-plugin\&quot;,\n          open: true,\n          children: [\n            { name: \&quot;plugin.json\&quot;, comment: \&quot;Manifest: name, version, author\&quot; },\n          ],\n        },\n        { name: \&quot;commands\&quot;, children: [{ name: \&quot;greet.md\&quot; }] },\n        {\n          name: \&quot;skills\&quot;,\n          children: [{ name: \&quot;my-skill\&quot;, children: [{ name: \&quot;SKILL.md\&quot; }] }],\n        },\n        { name: \&quot;hooks\&quot;, children: [{ name: \&quot;hooks.json\&quot; }] },\n      ],\n    },\n  ]}\n/&gt;\n\n**When to use.** Share team configurations, &lt;InternalLink slug=\&quot;building-my-first-claude-code-plugin\&quot;&gt;package domain workflows&lt;/InternalLink&gt;, distribute opinionated patterns, install community tooling.\n\n**How it works.** Install a plugin, get instant access. Components merge seamlessly — hooks combine, commands appear in autocomplete, skills activate automatically. Ready to build your own? Check out this [plugin creation guide](/prompts/claude/claude-create-plugin).\n\n---\n\n## 4) Agent Skills — automatic, task-driven capabilities\n\n```mermaid\nflowchart TD\n    Ctx[\&quot;Task context\&quot;] --&gt; Match[\&quot;Match SKILL.md&lt;br/&gt;description?\&quot;]\n    Skills[\&quot;Available skills&lt;br/&gt;(personal / project / plugin)\&quot;] --&gt; Match\n    Match --&gt;|yes| Tools[\&quot;Check allowed-tools\&quot;]\n    Tools --&gt;|ok| Exec[\&quot;Run skill\&quot;]\n    Tools --&gt;|blocked| Pass[\&quot;Skip\&quot;]\n    Match --&gt;|no| Pass\n    Exec --&gt; Out[\&quot;Return result\&quot;]\n    Pass --&gt; Out\n```\n\n**What they are.** Folders with `SKILL.md` descriptors plus optional scripts. Unlike slash commands, skills activate **automatically** when their description matches the task context.\n\n**How Claude discovers them.** When you give Claude a task, it reviews available skill descriptions to find relevant ones. If a skill&#39;s `description` field matches the task context, Claude loads the full skill instructions and applies them. This happens transparently — you never explicitly invoke skills.\n\n&lt;Alert type=\&quot;info\&quot; title=\&quot;Official Example Skills\&quot;&gt;\n  Check out the [official Anthropic skills\n  repository](https://github.com/anthropics/skills) for ready-to-use examples.\n&lt;/Alert&gt;\n\n&gt; Claude Skills are awesome, maybe a bigger deal than MCP\n&gt;\n&gt; — Simon Willison, [Claude Skills are awesome, maybe a bigger deal than MCP](https://simonwillison.net/2025/Oct/16/claude-skills/)\n\n&lt;Alert type=\&quot;tip\&quot; title=\&quot;Advanced Skills: Superpowers Library\&quot;&gt;\nWant rigorous, spec-driven development? Check out [obra&#39;s superpowers](https://github.com/obra/superpowers) — a comprehensive skills library that enforces systematic workflows.\n\n**What it provides:** TDD workflows (RED-GREEN-REFACTOR), systematic debugging, code review processes, git worktree management, and brainstorming frameworks. Each skill pushes you toward verification-based development instead of \&quot;trust me, it works.\&quot;\n\n**The philosophy:** Test before implementation. Verify with evidence. Debug systematically through four phases. Plan before coding. No shortcuts.\n\nThese skills work together to prevent common mistakes. The brainstorming skill activates before implementation. The TDD skill enforces writing tests first. The verification skill blocks completion claims without proof.\n\n**Use when:** You want Claude to be more disciplined about development practices, especially for production code.\n\n&lt;/Alert&gt;\n\n**Where to put them:**\n\n- `~/.claude/skills/` — personal, all projects\n- `.claude/skills/` — project-specific\n- Inside plugins — distributable\n\n**What you need:**\n\n- `SKILL.md` with frontmatter (`name`, `description`)\n- Optional `allowed-tools` declaration\n- Optional helper scripts\n\nWant to create your own skill? Use this [skill creation guide](/prompts/claude/claude-create-skill).\n\n**Why they&#39;re powerful.** Skills package expertise Claude applies automatically. Style enforcement, doc updates, test hygiene, framework patterns — all without manual triggering.\n\n**Skills vs CLAUDE.md.** Think of skills as modular chunks of a CLAUDE.md file. Instead of Claude reviewing a massive document every time, skills let Claude access specific expertise only when needed. This improves context efficiency while maintaining automatic behavior.\n\n**Key difference.** Skills are \&quot;always on.\&quot; Claude activates them based on context. Commands require manual invocation.\n\n&lt;Alert type=\&quot;caution\&quot; title=\&quot;Skills vs Commands: The Gray Area\&quot;&gt;\nSome workflows could be either a skill or a command. Example: git worktree management.\n\n**Make it a skill if:** You want Claude to automatically consider git worktrees whenever relevant to the conversation.\n\n**Make it a command if:** You want explicit control over when worktree logic runs (e.g., `/create-worktree feature-branch`).\n\nThe overlap is real — choose based on whether you prefer automatic activation or manual control.\n\n&lt;/Alert&gt;\n\n&lt;Alert type=\&quot;info\&quot; title=\&quot;Automatic vs Manual Triggering\&quot;&gt;\n**Subagents and Skills activate automatically** when Claude determines they&#39;re relevant to the task. You don&#39;t need to invoke them manually — Claude uses them proactively when it thinks they&#39;re useful.\n\n**Slash commands require manual triggering** — you type `/command-name` to run them.\n\nThis is the fundamental difference: automation vs explicit control.\n\n&lt;/Alert&gt;\n\n---\n\n## Putting it all together\n\nHere&#39;s how these features work together in practice:\n\n1. **Memory (`CLAUDE.md`)** — Establish project context and conventions that Claude always knows\n2. **Slash commands** — Create explicit shortcuts for workflows you want to trigger on demand\n3. **Subagents** — Offload parallel or isolated work to specialized agents\n4. **Hooks** — Enforce rules and automate repetitive actions at key lifecycle events\n5. **Plugins** — Package and distribute your entire setup to others\n6. **MCP** — Connect external systems and make their capabilities available as commands\n7. **Skills** — Define automatic behaviors that activate based on task context\n\n### Example: A Task-Based Development Workflow\n\nHere&#39;s a real-world workflow that combines multiple features:\n\n**Setup phase:**\n\n- `CLAUDE.md` contains implementation standards (\&quot;don&#39;t commit until I approve\&quot;, \&quot;write tests first\&quot;)\n- `/load-context` slash command initializes new chats with project state\n- `update-documentation` skill activates automatically after implementations\n- Hook triggers linting after file edits\n\n**Planning phase (Chat 1):**\n\n- Main agent plans bug fix or new feature\n- Outputs detailed task file with approach\n\n**Implementation phase (Chat 2):**\n\n- Start fresh context with `/load-context`\n- Feed in the plan from Chat 1\n- Implementation subagent executes the plan\n- `update-documentation` skill updates docs automatically\n- `/resolve-task` command marks task complete\n\n**Why this works:** Main context stays focused on planning. Heavy implementation work happens in isolated context. Skills handle documentation. Hooks enforce quality standards. No context pollution.\n\n## Decision guide: choosing the right tool\n\n&lt;Alert type=\&quot;info\&quot; title=\&quot;Community Resource: Claude Code Driver Repository\&quot;&gt;\n  🎉 **Huge thanks to [@thewiredbear](https://github.com/thewiredbear)** for creating the [Claude Code Driver](https://github.com/thewiredbear/Claude_Code_Driver/) repository! This community-driven collection includes examples, templates, and resources based on this guide. Perfect for getting started quickly or finding inspiration for your own Claude Code setup. Check it out and contribute your own patterns!\n&lt;/Alert&gt;\n\n&lt;Alert type=\&quot;info\&quot; title=\&quot;Quick Reference Cheat Sheet\&quot;&gt;\n  For a comprehensive visual guide to all Claude Code features, check out the\n  [Awesome Claude Code Cheat Sheet](https://awesomeclaude.ai/code-cheatsheet).\n&lt;/Alert&gt;\n\n\n&lt;Alert type=\&quot;tip\&quot; title=\&quot;Customize Your Terminal\&quot;&gt;\n  Want model name, context usage, and cost displayed in your terminal? See how to &lt;InternalLink slug=\&quot;customize_claude_code_status_line\&quot;&gt;customize your Claude Code status line&lt;/InternalLink&gt;.\n&lt;/Alert&gt;\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;Quick Reference\&quot;&gt;\n\n- **Use `CLAUDE.md`** to define lasting project context — architecture, conventions, and patterns Claude should always remember. Best for: static knowledge that rarely changes.\n- **Use &lt;InternalLink slug=\&quot;claude-code-slash-commands-guide\&quot;&gt;Slash Commands&lt;/InternalLink&gt;** for explicit, repeatable workflows you want to trigger manually. Best for: workflow automation, user-initiated actions.\n- **Use Subagents** when you need parallel execution or want to isolate heavy computational work. Best for: preventing context pollution, specialized deep dives.\n- **Use Hooks** to automatically enforce standards or react to specific events. Best for: quality gates, automatic actions tied to tool usage.\n- **Use Plugins** to package and share complete configurations across teams or projects. Best for: team standardization, distributing opinionated setups.\n- **Use MCP** to integrate external systems and expose their capabilities as native commands. Best for: connecting databases, APIs, third-party tools.\n- **Use Skills** for automatic, context-driven behaviors that should apply without manual invocation. Best for: automated context provision, \&quot;always on\&quot; expertise.\n\n&lt;/Aside&gt;\n\n### Feature comparison\n\n&lt;Alert type=\&quot;info\&quot; title=\&quot;Source\&quot;&gt;\n  This comparison table is adapted from [IndyDevDan&#39;s video \&quot;I finally CRACKED\n  Claude Agent Skills\&quot;](https://www.youtube.com/watch?v=kFpLzCVLA20&amp;t=1027s).\n&lt;/Alert&gt;\n\n| Category            | Skill | MCP     | Subagent | Slash Command |\n| ------------------- | ----- | ------- | -------- | ------------- |\n| Triggered By        | Agent | Both    | Both     | Engineer      |\n| Context Efficiency  | High  | Low     | High     | High          |\n| Context Persistence | ✅    | ✅      | ✅       | ✅            |\n| Parallelizable      | ❌    | ❌      | ❌       | ❌            |\n| Specializable       | ✅    | ✅      | ✅       | ✅            |\n| Sharable            | ✅    | ✅      | ✅       | ✅            |\n| Modularity          | High  | High    | Mid      | Mid           |\n| Tool Permissions    | ✅    | ❌      | ✅       | ✅            |\n| Can Use Prompts     | ✅    | ✅      | ✅       | ✅            |\n| Can Use Skills      | ✅    | Kind of | ✅       | ✅            |\n| Can Use MCP Servers | ✅    | ✅      | ✅       | ✅            |\n| Can Use Subagents   | ✅    | ✅      | ✅       | ❌            |\n\n### Real-world examples\n\n| Use Case                                               | Best Tool     | Why                                                  |\n| ------------------------------------------------------ | ------------- | ---------------------------------------------------- |\n| \&quot;Always use Pinia for state management in Vue apps\&quot;    | `CLAUDE.md`   | Persistent context that applies to all conversations |\n| Generate standardized commit messages                  | Slash Command | Explicit action you trigger when ready to commit     |\n| Check Jira tickets and analyze security simultaneously | Subagents     | Parallel execution with isolated contexts            |\n| Run linter after every file edit                       | Hook          | Automatic reaction to lifecycle event                |\n| Share your team&#39;s Vue testing patterns                 | Plugin        | Distributable package with commands + skills         |\n| Query PostgreSQL database for reports                  | MCP           | External system integration                          |\n| &lt;InternalLink slug=\&quot;how-i-use-claude-code-for-doing-seo-audits\&quot;&gt;Run automated SEO audits with browser testing&lt;/InternalLink&gt; | MCP | External system integration |\n| Detect style guide violations during any edit          | Skill         | Automatic behavior based on task context             |\n| Create React components from templates                 | Slash Command | Manual workflow with repeatable structure            |\n| \&quot;Never use `any` type in TypeScript\&quot;                   | Hook          | Automatic enforcement after code changes             |\n| Auto-format code on save                               | Hook          | Event-driven automation                              |\n| Connect to GitHub for issue management                 | MCP           | External API integration                             |\n| Run comprehensive test suite in parallel               | Subagent      | Isolated, resource-intensive work                    |\n| Deploy to staging environment                          | Slash Command | Manual trigger with safeguards                       |\n| &lt;InternalLink slug=\&quot;custom-tdd-workflow-claude-code-vue\&quot;&gt;Enforce TDD workflow automatically&lt;/InternalLink&gt; | Skill | Context-aware automatic behavior |\n| Initialize new projects with team standards            | Plugin        | Shareable, complete configuration                    |&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>I’ve been using Claude Code for months. Mostly for quick edits and generating boilerplate. The vibe coding tool everyone talks about.</p>
<p>Then I actually explored what it could do. MCP servers. Slash commands. Plugins. Skills. Hooks. Subagents. CLAUDE.md files.</p>
<p>I was blown away. Claude Code isn’t just a coding assistant. It’s a framework for orchestrating AI agents. It speeds up development in ways I’ve never seen before.</p>
<p>Most people use one or two features. They miss how these features stack together. This guide explains each concept <strong>in the order they build on each other</strong> — from external connections to automatic behaviors. (New to using LLMs for development? Start with my <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-i-use-llms/" class="internal-link astro-3tyn5ojg"> overview of how I use LLMs </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How I Use LLMs</span> <span class="preview-description astro-3tyn5ojg">Learn how I use LLMs to improve my productivity and efficiency.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">productivity</span>  </span> <time class="preview-date astro-3tyn5ojg">May 25, 2025</time> </span> </span> </span>  <script>
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
</script> for context.)</p>
<blockquote>
<p>Claude Code is, with hindsight, poorly named. It’s not purely a coding tool: it’s a tool for general computer automation. Anything you can achieve by typing commands into a computer is something that can now be automated by Claude Code. It’s best described as a general agent. Skills make this a whole lot more obvious and explicit.</p>
<p>— Simon Willison, <a href="https://simonwillison.net/2025/Oct/16/claude-skills/" rel="noopener noreferrer" target="_blank">Claude Skills are awesome, maybe a bigger deal than MCP</a></p>
</blockquote>
<div class="from-card to-cardMuted relative my-8 rounded-lg bg-gradient-to-br p-6"> <div class="from-accent/10 absolute inset-0 rounded-lg bg-gradient-to-br to-transparent backdrop-blur-[1px]"></div> <div class="relative z-10"> <h2 class="text-textBase mb-4 flex items-center gap-2 text-xl font-bold"> <span>✨</span> <span>TLDR</span> </h2> <ul class="space-y-2"> <li class="flex items-start"> <span class="text-accent mr-2">→</span> <span class="text-textBase">CLAUDE.md files give Claude project memory and context</span> </li><li class="flex items-start"> <span class="text-accent mr-2">→</span> <span class="text-textBase">Slash commands are user-triggered, repeatable workflows</span> </li><li class="flex items-start"> <span class="text-accent mr-2">→</span> <span class="text-textBase">Subagents handle parallel work in isolated contexts</span> </li><li class="flex items-start"> <span class="text-accent mr-2">→</span> <span class="text-textBase">Hooks automatically react to lifecycle events</span> </li><li class="flex items-start"> <span class="text-accent mr-2">→</span> <span class="text-textBase">Plugins bundle commands, hooks, and skills for sharing</span> </li><li class="flex items-start"> <span class="text-accent mr-2">→</span> <span class="text-textBase">MCP connects external tools through a universal protocol</span> </li><li class="flex items-start"> <span class="text-accent mr-2">→</span> <span class="text-textBase">Skills activate automatically based on task context</span> </li> </ul> </div> <div class="border-border/40 absolute inset-0 rounded-lg border"></div> </div>
<h2 id="the-feature-stack">The feature stack<a class="heading-link" aria-label="Link to section" href="#the-feature-stack"><span class="heading-link-icon">#</span></a></h2>
<ol>
<li><strong>Model Context Protocol (MCP)</strong> — the foundation for connecting external tools and data sources</li>
<li><strong>Claude Code core features</strong> — project memory, slash commands, subagents, and hooks</li>
<li><strong>Plugins</strong> — shareable packages that bundle commands, hooks, and skills</li>
<li><strong>Agent Skills</strong> — automatic, model-invoked capabilities that activate based on task context</li>
</ol>
<figure class="max-w-2xl mx-auto "> <img src="/_astro/claudesenpai.Ju-9Acc1_1HdQq8.webp" alt="Robot Claude Senpai with a knowing expression" loading="lazy" decoding="async" fetchpriority="auto" width="1536" height="1024" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> Claude Senpai knows all the features! </figcaption> </figure>
<hr/>
<h2 id="1-model-context-protocol-mcp--connecting-external-systems">1) Model Context Protocol (MCP) — connecting external systems<a class="heading-link" aria-label="Link to section" href="#1-model-context-protocol-mcp--connecting-external-systems"><span class="heading-link-icon">#</span></a></h2>
<p><svg id="mermaid-0" width="664" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="421.5" viewBox="-50 -10 664 421.5" role="graphics-document document" aria-roledescription="sequence"><g><rect x="414" y="335.5" fill="#eaeaea" stroke="#666" width="150" height="65" name="MCPServer" rx="3" ry="3" class="actor actor-bottom"></rect><text x="489" y="368" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="489" dy="0">MCPServer</tspan></text></g><g><rect x="201" y="335.5" fill="#eaeaea" stroke="#666" width="150" height="65" name="Claude" rx="3" ry="3" class="actor actor-bottom"></rect><text x="276" y="368" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="276" dy="0">Claude</tspan></text></g><g></g><g><line id="actor2" x1="489" y1="65" x2="489" y2="335.5" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="MCPServer"></line><g id="root-2"><rect x="414" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="MCPServer" rx="3" ry="3" class="actor actor-top"></rect><text x="489" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="489" dy="0">MCPServer</tspan></text></g></g><g><line id="actor1" x1="276" y1="65" x2="276" y2="335.5" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="Claude"></line><g id="root-1"><rect x="201" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="Claude" rx="3" ry="3" class="actor actor-top"></rect><text x="276" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="276" dy="0">Claude</tspan></text></g></g><g><line id="actor0" x1="75" y1="80" x2="75" y2="335.5" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="User"></line></g><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .actor{stroke:#ccc;fill:transparent;}#mermaid-0 text.actor>tspan{fill:lightgrey;stroke:none;}#mermaid-0 .actor-line{stroke:#ccc;}#mermaid-0 .innerArc{stroke-width:1.5;stroke-dasharray:none;}#mermaid-0 .messageLine0{stroke-width:1.5;stroke-dasharray:none;stroke:lightgrey;}#mermaid-0 .messageLine1{stroke-width:1.5;stroke-dasharray:2,2;stroke:lightgrey;}#mermaid-0 #arrowhead path{fill:lightgrey;stroke:lightgrey;}#mermaid-0 .sequenceNumber{fill:black;}#mermaid-0 #sequencenumber{fill:lightgrey;}#mermaid-0 #crosshead path{fill:lightgrey;stroke:lightgrey;}#mermaid-0 .messageText{fill:lightgrey;stroke:none;}#mermaid-0 .labelBox{stroke:#ccc;fill:transparent;}#mermaid-0 .labelText,#mermaid-0 .labelText>tspan{fill:lightgrey;stroke:none;}#mermaid-0 .loopText,#mermaid-0 .loopText>tspan{fill:lightgrey;stroke:none;}#mermaid-0 .loopLine{stroke-width:2px;stroke-dasharray:2,2;stroke:#ccc;fill:#ccc;}#mermaid-0 .note{stroke:hsl(180, 0%, 18.3529411765%);fill:hsla(0, 0%, 16%, 0);}#mermaid-0 .noteText,#mermaid-0 .noteText>tspan{fill:rgb(183.8476190475, 181.5523809523, 181.5523809523);stroke:none;}#mermaid-0 .activation0{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-0 .activation1{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-0 .activation2{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-0 .actorPopupMenu{position:absolute;}#mermaid-0 .actorPopupMenuPanel{position:absolute;fill:transparent;box-shadow:0px 8px 16px 0px rgba(0,0,0,0.2);filter:drop-shadow(3px 5px 2px rgb(0 0 0 / 0.4));}#mermaid-0 .actor-man line{stroke:#ccc;fill:transparent;}#mermaid-0 .actor-man circle,#mermaid-0 line{stroke:#ccc;fill:transparent;stroke-width:2px;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g></g><defs><symbol id="computer" width="24" height="24"><path transform="scale(.5)" d="M2 2v13h20v-13h-20zm18 11h-16v-9h16v9zm-10.228 6l.466-1h3.524l.467 1h-4.457zm14.228 3h-24l2-6h2.104l-1.33 4h18.45l-1.297-4h2.073l2 6zm-5-10h-14v-7h14v7z"></path></symbol></defs><defs><symbol id="database" fill-rule="evenodd" clip-rule="evenodd"><path transform="scale(.5)" d="M12.258.001l.256.004.255.005.253.008.251.01.249.012.247.015.246.016.242.019.241.02.239.023.236.024.233.027.231.028.229.031.225.032.223.034.22.036.217.038.214.04.211.041.208.043.205.045.201.046.198.048.194.05.191.051.187.053.183.054.18.056.175.057.172.059.168.06.163.061.16.063.155.064.15.066.074.033.073.033.071.034.07.034.069.035.068.035.067.035.066.035.064.036.064.036.062.036.06.036.06.037.058.037.058.037.055.038.055.038.053.038.052.038.051.039.05.039.048.039.047.039.045.04.044.04.043.04.041.04.04.041.039.041.037.041.036.041.034.041.033.042.032.042.03.042.029.042.027.042.026.043.024.043.023.043.021.043.02.043.018.044.017.043.015.044.013.044.012.044.011.045.009.044.007.045.006.045.004.045.002.045.001.045v17l-.001.045-.002.045-.004.045-.006.045-.007.045-.009.044-.011.045-.012.044-.013.044-.015.044-.017.043-.018.044-.02.043-.021.043-.023.043-.024.043-.026.043-.027.042-.029.042-.03.042-.032.042-.033.042-.034.041-.036.041-.037.041-.039.041-.04.041-.041.04-.043.04-.044.04-.045.04-.047.039-.048.039-.05.039-.051.039-.052.038-.053.038-.055.038-.055.038-.058.037-.058.037-.06.037-.06.036-.062.036-.064.036-.064.036-.066.035-.067.035-.068.035-.069.035-.07.034-.071.034-.073.033-.074.033-.15.066-.155.064-.16.063-.163.061-.168.06-.172.059-.175.057-.18.056-.183.054-.187.053-.191.051-.194.05-.198.048-.201.046-.205.045-.208.043-.211.041-.214.04-.217.038-.22.036-.223.034-.225.032-.229.031-.231.028-.233.027-.236.024-.239.023-.241.02-.242.019-.246.016-.247.015-.249.012-.251.01-.253.008-.255.005-.256.004-.258.001-.258-.001-.256-.004-.255-.005-.253-.008-.251-.01-.249-.012-.247-.015-.245-.016-.243-.019-.241-.02-.238-.023-.236-.024-.234-.027-.231-.028-.228-.031-.226-.032-.223-.034-.22-.036-.217-.038-.214-.04-.211-.041-.208-.043-.204-.045-.201-.046-.198-.048-.195-.05-.19-.051-.187-.053-.184-.054-.179-.056-.176-.057-.172-.059-.167-.06-.164-.061-.159-.063-.155-.064-.151-.066-.074-.033-.072-.033-.072-.034-.07-.034-.069-.035-.068-.035-.067-.035-.066-.035-.064-.036-.063-.036-.062-.036-.061-.036-.06-.037-.058-.037-.057-.037-.056-.038-.055-.038-.053-.038-.052-.038-.051-.039-.049-.039-.049-.039-.046-.039-.046-.04-.044-.04-.043-.04-.041-.04-.04-.041-.039-.041-.037-.041-.036-.041-.034-.041-.033-.042-.032-.042-.03-.042-.029-.042-.027-.042-.026-.043-.024-.043-.023-.043-.021-.043-.02-.043-.018-.044-.017-.043-.015-.044-.013-.044-.012-.044-.011-.045-.009-.044-.007-.045-.006-.045-.004-.045-.002-.045-.001-.045v-17l.001-.045.002-.045.004-.045.006-.045.007-.045.009-.044.011-.045.012-.044.013-.044.015-.044.017-.043.018-.044.02-.043.021-.043.023-.043.024-.043.026-.043.027-.042.029-.042.03-.042.032-.042.033-.042.034-.041.036-.041.037-.041.039-.041.04-.041.041-.04.043-.04.044-.04.046-.04.046-.039.049-.039.049-.039.051-.039.052-.038.053-.038.055-.038.056-.038.057-.037.058-.037.06-.037.061-.036.062-.036.063-.036.064-.036.066-.035.067-.035.068-.035.069-.035.07-.034.072-.034.072-.033.074-.033.151-.066.155-.064.159-.063.164-.061.167-.06.172-.059.176-.057.179-.056.184-.054.187-.053.19-.051.195-.05.198-.048.201-.046.204-.045.208-.043.211-.041.214-.04.217-.038.22-.036.223-.034.226-.032.228-.031.231-.028.234-.027.236-.024.238-.023.241-.02.243-.019.245-.016.247-.015.249-.012.251-.01.253-.008.255-.005.256-.004.258-.001.258.001zm-9.258 20.499v.01l.001.021.003.021.004.022.005.021.006.022.007.022.009.023.01.022.011.023.012.023.013.023.015.023.016.024.017.023.018.024.019.024.021.024.022.025.023.024.024.025.052.049.056.05.061.051.066.051.07.051.075.051.079.052.084.052.088.052.092.052.097.052.102.051.105.052.11.052.114.051.119.051.123.051.127.05.131.05.135.05.139.048.144.049.147.047.152.047.155.047.16.045.163.045.167.043.171.043.176.041.178.041.183.039.187.039.19.037.194.035.197.035.202.033.204.031.209.03.212.029.216.027.219.025.222.024.226.021.23.02.233.018.236.016.24.015.243.012.246.01.249.008.253.005.256.004.259.001.26-.001.257-.004.254-.005.25-.008.247-.011.244-.012.241-.014.237-.016.233-.018.231-.021.226-.021.224-.024.22-.026.216-.027.212-.028.21-.031.205-.031.202-.034.198-.034.194-.036.191-.037.187-.039.183-.04.179-.04.175-.042.172-.043.168-.044.163-.045.16-.046.155-.046.152-.047.148-.048.143-.049.139-.049.136-.05.131-.05.126-.05.123-.051.118-.052.114-.051.11-.052.106-.052.101-.052.096-.052.092-.052.088-.053.083-.051.079-.052.074-.052.07-.051.065-.051.06-.051.056-.05.051-.05.023-.024.023-.025.021-.024.02-.024.019-.024.018-.024.017-.024.015-.023.014-.024.013-.023.012-.023.01-.023.01-.022.008-.022.006-.022.006-.022.004-.022.004-.021.001-.021.001-.021v-4.127l-.077.055-.08.053-.083.054-.085.053-.087.052-.09.052-.093.051-.095.05-.097.05-.1.049-.102.049-.105.048-.106.047-.109.047-.111.046-.114.045-.115.045-.118.044-.12.043-.122.042-.124.042-.126.041-.128.04-.13.04-.132.038-.134.038-.135.037-.138.037-.139.035-.142.035-.143.034-.144.033-.147.032-.148.031-.15.03-.151.03-.153.029-.154.027-.156.027-.158.026-.159.025-.161.024-.162.023-.163.022-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.011-.178.01-.179.008-.179.008-.181.006-.182.005-.182.004-.184.003-.184.002h-.37l-.184-.002-.184-.003-.182-.004-.182-.005-.181-.006-.179-.008-.179-.008-.178-.01-.176-.011-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.022-.162-.023-.161-.024-.159-.025-.157-.026-.156-.027-.155-.027-.153-.029-.151-.03-.15-.03-.148-.031-.146-.032-.145-.033-.143-.034-.141-.035-.14-.035-.137-.037-.136-.037-.134-.038-.132-.038-.13-.04-.128-.04-.126-.041-.124-.042-.122-.042-.12-.044-.117-.043-.116-.045-.113-.045-.112-.046-.109-.047-.106-.047-.105-.048-.102-.049-.1-.049-.097-.05-.095-.05-.093-.052-.09-.051-.087-.052-.085-.053-.083-.054-.08-.054-.077-.054v4.127zm0-5.654v.011l.001.021.003.021.004.021.005.022.006.022.007.022.009.022.01.022.011.023.012.023.013.023.015.024.016.023.017.024.018.024.019.024.021.024.022.024.023.025.024.024.052.05.056.05.061.05.066.051.07.051.075.052.079.051.084.052.088.052.092.052.097.052.102.052.105.052.11.051.114.051.119.052.123.05.127.051.131.05.135.049.139.049.144.048.147.048.152.047.155.046.16.045.163.045.167.044.171.042.176.042.178.04.183.04.187.038.19.037.194.036.197.034.202.033.204.032.209.03.212.028.216.027.219.025.222.024.226.022.23.02.233.018.236.016.24.014.243.012.246.01.249.008.253.006.256.003.259.001.26-.001.257-.003.254-.006.25-.008.247-.01.244-.012.241-.015.237-.016.233-.018.231-.02.226-.022.224-.024.22-.025.216-.027.212-.029.21-.03.205-.032.202-.033.198-.035.194-.036.191-.037.187-.039.183-.039.179-.041.175-.042.172-.043.168-.044.163-.045.16-.045.155-.047.152-.047.148-.048.143-.048.139-.05.136-.049.131-.05.126-.051.123-.051.118-.051.114-.052.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.051.07-.052.065-.051.06-.05.056-.051.051-.049.023-.025.023-.024.021-.025.02-.024.019-.024.018-.024.017-.024.015-.023.014-.023.013-.024.012-.022.01-.023.01-.023.008-.022.006-.022.006-.022.004-.021.004-.022.001-.021.001-.021v-4.139l-.077.054-.08.054-.083.054-.085.052-.087.053-.09.051-.093.051-.095.051-.097.05-.1.049-.102.049-.105.048-.106.047-.109.047-.111.046-.114.045-.115.044-.118.044-.12.044-.122.042-.124.042-.126.041-.128.04-.13.039-.132.039-.134.038-.135.037-.138.036-.139.036-.142.035-.143.033-.144.033-.147.033-.148.031-.15.03-.151.03-.153.028-.154.028-.156.027-.158.026-.159.025-.161.024-.162.023-.163.022-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.011-.178.009-.179.009-.179.007-.181.007-.182.005-.182.004-.184.003-.184.002h-.37l-.184-.002-.184-.003-.182-.004-.182-.005-.181-.007-.179-.007-.179-.009-.178-.009-.176-.011-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.022-.162-.023-.161-.024-.159-.025-.157-.026-.156-.027-.155-.028-.153-.028-.151-.03-.15-.03-.148-.031-.146-.033-.145-.033-.143-.033-.141-.035-.14-.036-.137-.036-.136-.037-.134-.038-.132-.039-.13-.039-.128-.04-.126-.041-.124-.042-.122-.043-.12-.043-.117-.044-.116-.044-.113-.046-.112-.046-.109-.046-.106-.047-.105-.048-.102-.049-.1-.049-.097-.05-.095-.051-.093-.051-.09-.051-.087-.053-.085-.052-.083-.054-.08-.054-.077-.054v4.139zm0-5.666v.011l.001.02.003.022.004.021.005.022.006.021.007.022.009.023.01.022.011.023.012.023.013.023.015.023.016.024.017.024.018.023.019.024.021.025.022.024.023.024.024.025.052.05.056.05.061.05.066.051.07.051.075.052.079.051.084.052.088.052.092.052.097.052.102.052.105.051.11.052.114.051.119.051.123.051.127.05.131.05.135.05.139.049.144.048.147.048.152.047.155.046.16.045.163.045.167.043.171.043.176.042.178.04.183.04.187.038.19.037.194.036.197.034.202.033.204.032.209.03.212.028.216.027.219.025.222.024.226.021.23.02.233.018.236.017.24.014.243.012.246.01.249.008.253.006.256.003.259.001.26-.001.257-.003.254-.006.25-.008.247-.01.244-.013.241-.014.237-.016.233-.018.231-.02.226-.022.224-.024.22-.025.216-.027.212-.029.21-.03.205-.032.202-.033.198-.035.194-.036.191-.037.187-.039.183-.039.179-.041.175-.042.172-.043.168-.044.163-.045.16-.045.155-.047.152-.047.148-.048.143-.049.139-.049.136-.049.131-.051.126-.05.123-.051.118-.052.114-.051.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.052.07-.051.065-.051.06-.051.056-.05.051-.049.023-.025.023-.025.021-.024.02-.024.019-.024.018-.024.017-.024.015-.023.014-.024.013-.023.012-.023.01-.022.01-.023.008-.022.006-.022.006-.022.004-.022.004-.021.001-.021.001-.021v-4.153l-.077.054-.08.054-.083.053-.085.053-.087.053-.09.051-.093.051-.095.051-.097.05-.1.049-.102.048-.105.048-.106.048-.109.046-.111.046-.114.046-.115.044-.118.044-.12.043-.122.043-.124.042-.126.041-.128.04-.13.039-.132.039-.134.038-.135.037-.138.036-.139.036-.142.034-.143.034-.144.033-.147.032-.148.032-.15.03-.151.03-.153.028-.154.028-.156.027-.158.026-.159.024-.161.024-.162.023-.163.023-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.01-.178.01-.179.009-.179.007-.181.006-.182.006-.182.004-.184.003-.184.001-.185.001-.185-.001-.184-.001-.184-.003-.182-.004-.182-.006-.181-.006-.179-.007-.179-.009-.178-.01-.176-.01-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.023-.162-.023-.161-.024-.159-.024-.157-.026-.156-.027-.155-.028-.153-.028-.151-.03-.15-.03-.148-.032-.146-.032-.145-.033-.143-.034-.141-.034-.14-.036-.137-.036-.136-.037-.134-.038-.132-.039-.13-.039-.128-.041-.126-.041-.124-.041-.122-.043-.12-.043-.117-.044-.116-.044-.113-.046-.112-.046-.109-.046-.106-.048-.105-.048-.102-.048-.1-.05-.097-.049-.095-.051-.093-.051-.09-.052-.087-.052-.085-.053-.083-.053-.08-.054-.077-.054v4.153zm8.74-8.179l-.257.004-.254.005-.25.008-.247.011-.244.012-.241.014-.237.016-.233.018-.231.021-.226.022-.224.023-.22.026-.216.027-.212.028-.21.031-.205.032-.202.033-.198.034-.194.036-.191.038-.187.038-.183.04-.179.041-.175.042-.172.043-.168.043-.163.045-.16.046-.155.046-.152.048-.148.048-.143.048-.139.049-.136.05-.131.05-.126.051-.123.051-.118.051-.114.052-.11.052-.106.052-.101.052-.096.052-.092.052-.088.052-.083.052-.079.052-.074.051-.07.052-.065.051-.06.05-.056.05-.051.05-.023.025-.023.024-.021.024-.02.025-.019.024-.018.024-.017.023-.015.024-.014.023-.013.023-.012.023-.01.023-.01.022-.008.022-.006.023-.006.021-.004.022-.004.021-.001.021-.001.021.001.021.001.021.004.021.004.022.006.021.006.023.008.022.01.022.01.023.012.023.013.023.014.023.015.024.017.023.018.024.019.024.02.025.021.024.023.024.023.025.051.05.056.05.06.05.065.051.07.052.074.051.079.052.083.052.088.052.092.052.096.052.101.052.106.052.11.052.114.052.118.051.123.051.126.051.131.05.136.05.139.049.143.048.148.048.152.048.155.046.16.046.163.045.168.043.172.043.175.042.179.041.183.04.187.038.191.038.194.036.198.034.202.033.205.032.21.031.212.028.216.027.22.026.224.023.226.022.231.021.233.018.237.016.241.014.244.012.247.011.25.008.254.005.257.004.26.001.26-.001.257-.004.254-.005.25-.008.247-.011.244-.012.241-.014.237-.016.233-.018.231-.021.226-.022.224-.023.22-.026.216-.027.212-.028.21-.031.205-.032.202-.033.198-.034.194-.036.191-.038.187-.038.183-.04.179-.041.175-.042.172-.043.168-.043.163-.045.16-.046.155-.046.152-.048.148-.048.143-.048.139-.049.136-.05.131-.05.126-.051.123-.051.118-.051.114-.052.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.051.07-.052.065-.051.06-.05.056-.05.051-.05.023-.025.023-.024.021-.024.02-.025.019-.024.018-.024.017-.023.015-.024.014-.023.013-.023.012-.023.01-.023.01-.022.008-.022.006-.023.006-.021.004-.022.004-.021.001-.021.001-.021-.001-.021-.001-.021-.004-.021-.004-.022-.006-.021-.006-.023-.008-.022-.01-.022-.01-.023-.012-.023-.013-.023-.014-.023-.015-.024-.017-.023-.018-.024-.019-.024-.02-.025-.021-.024-.023-.024-.023-.025-.051-.05-.056-.05-.06-.05-.065-.051-.07-.052-.074-.051-.079-.052-.083-.052-.088-.052-.092-.052-.096-.052-.101-.052-.106-.052-.11-.052-.114-.052-.118-.051-.123-.051-.126-.051-.131-.05-.136-.05-.139-.049-.143-.048-.148-.048-.152-.048-.155-.046-.16-.046-.163-.045-.168-.043-.172-.043-.175-.042-.179-.041-.183-.04-.187-.038-.191-.038-.194-.036-.198-.034-.202-.033-.205-.032-.21-.031-.212-.028-.216-.027-.22-.026-.224-.023-.226-.022-.231-.021-.233-.018-.237-.016-.241-.014-.244-.012-.247-.011-.25-.008-.254-.005-.257-.004-.26-.001-.26.001z"></path></symbol></defs><defs><symbol id="clock" width="24" height="24"><path transform="scale(.5)" d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm5.848 12.459c.202.038.202.333.001.372-1.907.361-6.045 1.111-6.547 1.111-.719 0-1.301-.582-1.301-1.301 0-.512.77-5.447 1.125-7.445.034-.192.312-.181.343.014l.985 6.238 5.394 1.011z"></path></symbol></defs><defs><marker id="arrowhead" refX="7.9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M -1 0 L 10 5 L 0 10 z"></path></marker></defs><defs><marker id="crosshead" markerWidth="15" markerHeight="8" orient="auto" refX="4" refY="4.5"><path fill="none" stroke="#000000" stroke-width="1pt" d="M 1,2 L 6,7 M 6,2 L 1,7" style="stroke-dasharray:0, 0"></path></marker></defs><defs><marker id="filled-head" refX="15.5" refY="7" markerWidth="20" markerHeight="28" orient="auto"><path d="M 18,7 L9,13 L14,7 L9,1 Z"></path></marker></defs><defs><marker id="sequencenumber" refX="15" refY="15" markerWidth="60" markerHeight="40" orient="auto"><circle cx="15" cy="15" r="6"></circle></marker></defs><g class="actor-man actor-top" name="User"><line id="actor-man-torso0" x1="75" y1="25" x2="75" y2="45"></line><line id="actor-man-arms0" x1="57" y1="33" x2="93" y2="33"></line><line x1="57" y1="60" x2="75" y2="45"></line><line x1="75" y1="45" x2="91" y2="60"></line><circle cx="75" cy="10" r="15" width="150" height="65"></circle><text x="75" y="67.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-man" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="75" dy="0">User</tspan></text></g><text x="174" y="80" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">/mcp connect github</text><line x1="76" y1="113" x2="272" y2="113" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></line><text x="381" y="128" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Authenticate + request</text><text x="381" y="147" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">capabilities</text><line x1="277" y1="180" x2="485" y2="180" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></line><text x="384" y="195" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Return</text><text x="384" y="214" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">tools/resources/prompts</text><line x1="488" y1="247" x2="280" y2="247" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></line><text x="177" y="262" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Display /mcp__github__*</text><text x="177" y="282" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">commands</text><line x1="275" y1="315.5" x2="79" y2="315.5" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></line><g class="actor-man actor-bottom" name="User"><line id="actor-man-torso2" x1="75" y1="360.5" x2="75" y2="380.5"></line><line id="actor-man-arms2" x1="57" y1="368.5" x2="93" y2="368.5"></line><line x1="57" y1="395.5" x2="75" y2="380.5"></line><line x1="75" y1="380.5" x2="91" y2="395.5"></line><circle cx="75" cy="345.5" r="15" width="150" height="65"></circle><text x="75" y="403" dominant-baseline="central" alignment-baseline="central" class="actor actor-man" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="75" dy="0">User</tspan></text></g></svg></p>
<p><strong>What it is.</strong> The <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/what-is-model-context-protocol-mcp/" class="internal-link astro-3tyn5ojg"> Model Context Protocol </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">What Is the Model Context Protocol (MCP)? How It Works</span> <span class="preview-description astro-3tyn5ojg">Learn how MCP (Model Context Protocol) standardizes AI tool integration, enabling LLMs to interact with external services, databases, and APIs through a universal protocol similar to USB-C for AI applications.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">mcp</span><span class="preview-tag astro-3tyn5ojg">typescript</span><span class="preview-tag astro-3tyn5ojg">ai</span>  </span> <time class="preview-date astro-3tyn5ojg">Aug 10, 2025</time> </span> </span> </span>  <script>
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
</script> connects Claude Code to external tools and data sources. Think universal adapter for GitHub, databases, APIs, and other systems.</p>
<p><strong>How it works.</strong> Connect an MCP server, get access to its tools, resources, and prompts as slash commands:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#51597D;font-style:italic"># Install a server</span></span>
<span class="line"><span style="color:#C0CAF5">claude</span><span style="color:#9ECE6A"> mcp</span><span style="color:#9ECE6A"> add</span><span style="color:#9ECE6A"> playwright</span><span style="color:#9ECE6A"> npx</span><span style="color:#9ECE6A"> @playwright/mcp@latest</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic"># Use it</span></span>
<span class="line"><span style="color:#C0CAF5">/mcp__playwright__create-test</span><span style="color:#A9B1D6"> [args]</span></span></code><button type="button" class="copy" data-code="# Install a server
claude mcp add playwright npx @playwright/mcp@latest

# Use it
/mcp__playwright__create-test [args]" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<div class="alert alert-caution astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">🚨</span> Context Window Management </p> <div class="alert-content astro-7kdbuayl"> <p>Each MCP server consumes context. Monitor with <code>/context</code> and remove unused
servers.</p> </div> </div> 
<p><strong>The gotcha.</strong> MCP servers expose their own tools — they don’t inherit Claude’s Read, Write, or Bash unless explicitly provided.</p>
<p><strong>Real-world example.</strong> Want to see MCP in action? Check out how to <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/building_ai_qa_engineer_claude_code_playwright/" class="internal-link astro-3tyn5ojg"> build an AI QA engineer with Playwright MCP </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Building an AI QA Engineer with Claude Code and Playwright MCP</span> <span class="preview-description astro-3tyn5ojg">Learn how to build an automated QA engineer using Claude Code and Playwright MCP that tests your web app like a real user, runs on every pull request, and writes detailed bug reports.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">testing</span><span class="preview-tag astro-3tyn5ojg">claude-code</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Dec 13, 2025</time> </span> </span> </span>  <script>
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
</script> that tests your app like a real user.</p>
<hr/>
<h2 id="2-claude-code-core-features">2) Claude Code core features<a class="heading-link" aria-label="Link to section" href="#2-claude-code-core-features"><span class="heading-link-icon">#</span></a></h2>
<h3 id="21-project-memory-with-claudemd">2.1) Project memory with <code>CLAUDE.md</code><a class="heading-link" aria-label="Link to section" href="#21-project-memory-with-claudemd"><span class="heading-link-icon">#</span></a></h3>
<p><strong>What it is.</strong> Markdown files Claude loads at startup. They give Claude memory about your project’s conventions, architecture, and patterns.</p>
<p><strong>How it works.</strong> Files merge hierarchically from enterprise → user (<code>~/.claude/CLAUDE.md</code>) → project (<code>./CLAUDE.md</code>). When you reference <code>@components/Button.vue</code>, Claude also reads CLAUDE.md from that directory and its parents.</p>
<p><strong>Example structure for a Vue app:</strong></p>
<nav class="file-tree astro-htwbjus4" aria-label="File tree"> <ul class="file-tree__list astro-htwbjus4"> <li class="file-tree__item astro-o25vlg2d" style="--level: 0;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">my-vue-app</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">CLAUDE.md</span> <span class="file-tree__comment astro-o25vlg2d">Project-wide conventions, tech stack, build commands</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">src</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">components</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">CLAUDE.md</span> <span class="file-tree__comment astro-o25vlg2d">Component patterns, naming conventions, prop types</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#4FC08D" d="M24,1.61H14.06L12,5.16,9.94,1.61H0L12,22.39ZM12,14.08,5.16,2.23H9.59L12,6.41l2.41-4.18h4.43Z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">Button.vue</span>  </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#4FC08D" d="M24,1.61H14.06L12,5.16,9.94,1.61H0L12,22.39ZM12,14.08,5.16,2.23H9.59L12,6.41l2.41-4.18h4.43Z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">Card.vue</span>  </span> </li>  </ul> </details>   </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">pages</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">CLAUDE.md</span> <span class="file-tree__comment astro-o25vlg2d">Routing patterns, page structure, data fetching</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#4FC08D" d="M24,1.61H14.06L12,5.16,9.94,1.61H0L12,22.39ZM12,14.08,5.16,2.23H9.59L12,6.41l2.41-4.18h4.43Z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">Home.vue</span>  </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#4FC08D" d="M24,1.61H14.06L12,5.16,9.94,1.61H0L12,22.39ZM12,14.08,5.16,2.23H9.59L12,6.41l2.41-4.18h4.43Z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">About.vue</span>  </span> </li>  </ul> </details>   </li>  </ul> </details>   </li>  </ul> </details>   </li>  </ul> </nav> 
<p>When you work on <code>src/components/Button.vue</code>, Claude loads context from:</p>
<ol>
<li>Enterprise CLAUDE.md (if configured)</li>
<li>User <code>~/.claude/CLAUDE.md</code> (personal preferences)</li>
<li>Project root <code>CLAUDE.md</code> (project-wide info)</li>
<li><code>src/components/CLAUDE.md</code> (component-specific patterns)</li>
</ol>
<p><strong>What goes in.</strong> Common commands, coding standards, architectural patterns. Keep it concise — reference guide, not documentation. Need help creating your own? Check out this <a href="/prompts/claude/claude-create-md">CLAUDE.md creation guide</a>.</p>
<p>Here’s my blog’s CLAUDE.md:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> CLAUDE.md</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Project Overview</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Alexander Opalic&#39;s personal blog built on AstroPaper - Astro-based blog theme with TypeScript, React, TailwindCSS.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Tech Stack**</span><span style="color:#9AA5CE">: Astro 5, TypeScript, React, TailwindCSS, Shiki, FuseJS, Playwright</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Development Commands</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">```bash</span></span>
<span class="line"><span style="color:#C0CAF5">npm </span><span style="color:#9ECE6A">run</span><span style="color:#9ECE6A"> dev</span><span style="color:#51597D;font-style:italic">              # Build + Pagefind + dev server (localhost:4321)</span></span>
<span class="line"><span style="color:#C0CAF5">npm </span><span style="color:#9ECE6A">run</span><span style="color:#9ECE6A"> build</span><span style="color:#51597D;font-style:italic">            # Production build</span></span>
<span class="line"><span style="color:#C0CAF5">npm </span><span style="color:#9ECE6A">run</span><span style="color:#9ECE6A"> lint</span><span style="color:#51597D;font-style:italic">             # ESLint for .astro, .ts, .tsx</span></span>
<span class="line"><span style="color:#C0CAF5">---</span></span>
<span class="line"><span style="color:#89DDFF">```</span></span></code><button type="button" class="copy" data-code="# CLAUDE.md

## Project Overview

Alexander Opalic's personal blog built on AstroPaper - Astro-based blog theme with TypeScript, React, TailwindCSS.

**Tech Stack**: Astro 5, TypeScript, React, TailwindCSS, Shiki, FuseJS, Playwright

## Development Commands

```bash
npm run dev              # Build + Pagefind + dev server (localhost:4321)
npm run build            # Production build
npm run lint             # ESLint for .astro, .ts, .tsx
---
```" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="22-slash-commands--explicit-reusable-prompts">2.2) Slash Commands — explicit, reusable prompts<a class="heading-link" aria-label="Link to section" href="#22-slash-commands--explicit-reusable-prompts"><span class="heading-link-icon">#</span></a></h3>
<p><svg id="mermaid-1" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:1220.546875px" viewBox="0 0 1220.546875 94" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-1{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1 .error-icon{fill:#a44141;}#mermaid-1 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-1 .edge-thickness-normal{stroke-width:1px;}#mermaid-1 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-1 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-1 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-1 p{margin:0;}#mermaid-1 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-1 .cluster-label text{fill:#F9FFFE;}#mermaid-1 .cluster-label span{color:#F9FFFE;}#mermaid-1 .cluster-label span p{background-color:transparent;}#mermaid-1 .label text,#mermaid-1 span{fill:#ccc;color:#ccc;}#mermaid-1 .node rect,#mermaid-1 .node circle,#mermaid-1 .node ellipse,#mermaid-1 .node polygon,#mermaid-1 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-1 .rough-node .label text,#mermaid-1 .node .label text,#mermaid-1 .image-shape .label,#mermaid-1 .icon-shape .label{text-anchor:middle;}#mermaid-1 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-1 .rough-node .label,#mermaid-1 .node .label,#mermaid-1 .image-shape .label,#mermaid-1 .icon-shape .label{text-align:center;}#mermaid-1 .node.clickable{cursor:pointer;}#mermaid-1 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-1 .arrowheadPath{fill:lightgrey;}#mermaid-1 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-1 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-1 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-1 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-1 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-1 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-1 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-1 .cluster text{fill:#F9FFFE;}#mermaid-1 .cluster span{color:#F9FFFE;}#mermaid-1 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-1 rect.text{fill:none;stroke-width:0;}#mermaid-1 .icon-shape,#mermaid-1 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-1 .icon-shape p,#mermaid-1 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-1 .icon-shape rect,#mermaid-1 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-1 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-1 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-1 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-1_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-1_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-1_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-1_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M206.875,47.5L212.583,47.417C218.292,47.333,229.708,47.167,238.917,47.083C248.125,47,255.125,47,258.625,47L262.125,47" id="L_User_PreBash_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_User_PreBash_0" data-points="W3sieCI6MjA2Ljg3NSwieSI6NDcuNX0seyJ4IjoyNDEuMTI1LCJ5Ijo0N30seyJ4IjoyNjYuMTI1LCJ5Ijo0N31d" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M526.125,47L530.292,47C534.458,47,542.792,47,550.458,47C558.125,47,565.125,47,568.625,47L572.125,47" id="L_PreBash_Prompt_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_PreBash_Prompt_0" data-points="W3sieCI6NTI2LjEyNSwieSI6NDd9LHsieCI6NTUxLjEyNSwieSI6NDd9LHsieCI6NTc2LjEyNSwieSI6NDd9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M780.625,47L784.792,47C788.958,47,797.292,47,804.958,47C812.625,47,819.625,47,823.125,47L826.625,47" id="L_Prompt_Claude_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Prompt_Claude_0" data-points="W3sieCI6NzgwLjYyNSwieSI6NDd9LHsieCI6ODA1LjYyNSwieSI6NDd9LHsieCI6ODMwLjYyNSwieSI6NDd9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path><path d="M1044.75,47L1048.917,47C1053.083,47,1061.417,47,1069.083,47C1076.75,47,1083.75,47,1087.25,47L1090.75,47" id="L_Claude_Output_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Claude_Output_0" data-points="W3sieCI6MTA0NC43NSwieSI6NDd9LHsieCI6MTA2OS43NSwieSI6NDd9LHsieCI6MTA5NC43NSwieSI6NDd9XQ==" marker-end="url(#mermaid-1_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_User_PreBash_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_PreBash_Prompt_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Prompt_Claude_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Claude_Output_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-User-0" transform="translate(112.0625, 47)"><polygon points="-19.5,0 169.125,0 188.625,-39 0,-39" class="label-container" transform="translate(-84.5625,19.5)"></polygon><g class="label" style="" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>/my-command args</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-PreBash-1" transform="translate(396.125, 47)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Pre-execution Bash Steps</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Prompt-2" transform="translate(678.375, 47)"><rect class="basic label-container" style="" x="-102.25" y="-27" width="204.5" height="54"></rect><g class="label" style="" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Markdown prompt</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Claude-3" transform="translate(937.6875, 47)"><rect class="basic label-container" style="" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Claude processes</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Output-4" transform="translate(1153.6484375, 47)"><rect class="basic label-container" style="" x="-58.8984375" y="-27" width="117.796875" height="54"></rect><g class="label" style="" transform="translate(-28.8984375, -12)"><rect></rect><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Result</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<p><strong>What they are.</strong> Markdown files in <code>.claude/commands/</code> you trigger manually by typing <code>/name [args]</code>. User-controlled workflows.</p>
<p><strong>Key features:</strong></p>
<ul>
<li><code>$ARGUMENTS</code> or <code>$1</code>, <code>$2</code> for argument passing</li>
<li><code>@file</code> syntax to inline code</li>
<li><code>allowed-tools: Bash(...)</code> for pre-execution scripts</li>
<li>
<span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/xml-tagged-prompts-framework-reliable-ai-responses/" class="internal-link astro-3tyn5ojg"> <p>XML-tagged prompts</p> </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">XML-Style Tagged Prompts: A Framework for Reliable AI Responses</span> <span class="preview-description astro-3tyn5ojg">Learn how top AI engineers use XML-style prompts to consistently get structured, accurate responses from ChatGPT, Claude, and other LLMs. Step-by-step guide with real examples</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">llm</span><span class="preview-tag astro-3tyn5ojg">prompt-engineering</span>  </span> <time class="preview-date astro-3tyn5ojg">Dec 22, 2024</time> </span> </span> </span>  <script>
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
</script>
for reliable outputs</li>
</ul>
<p><strong>When to use.</strong> Repeatable workflows you trigger on demand — code reviews, commit messages, scaffolding. For a complete example of a git workflow built entirely with slash commands, see my <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/claude-code-slash-commands-guide/" class="internal-link astro-3tyn5ojg"> Slash Commands Guide </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Speed Up Your Claude Code Experience with Slash Commands</span> <span class="preview-description astro-3tyn5ojg">Learn how to transform Claude Code from a chatbot into a deterministic engine using Slash Commands. This guide covers the technical setup and a complete &#39;Full Circle&#39; workflow that automates your entire feature lifecycle.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">claude-code</span>  </span> <time class="preview-date astro-3tyn5ojg">Nov 22, 2025</time> </span> </span> </span>  <script>
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
</script>. Want to create your own? Use this <a href="/prompts/claude/claude-create-command">slash command creation guide</a>.</p>
<p><strong>Example structure:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Create new slash commands</span></span>
<span class="line"><span style="color:#F7768E">argument-hint</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> [</span><span style="color:#9ECE6A">name</span><span style="color:#89DDFF">]</span><span style="color:#89DDFF"> [</span><span style="color:#9ECE6A">purpose</span><span style="color:#89DDFF">]</span></span>
<span class="line"><span style="color:#F7768E">allowed-tools</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Bash(mkdir:*), Bash(tee:*)</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> /create-command</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Generate slash command files with proper structure.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Inputs:**</span><span style="color:#89DDFF"> `$1`</span><span style="color:#9AA5CE"> = name, </span><span style="color:#89DDFF">`$2`</span><span style="color:#9AA5CE"> = purpose</span></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Outputs:**</span><span style="color:#89DDFF"> `STATUS=WROTE PATH=.claude/commands/{name}.md`</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">[... instructions ...]</span></span></code><button type="button" class="copy" data-code="---
description: Create new slash commands
argument-hint: [name] [purpose]
allowed-tools: Bash(mkdir:*), Bash(tee:*)
---

# /create-command

Generate slash command files with proper structure.

**Inputs:** `$1` = name, `$2` = purpose
**Outputs:** `STATUS=WROTE PATH=.claude/commands/{name}.md`

[... instructions ...]" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Commands can create commands. Meta, but powerful.</p>
<hr/>
<h3 id="23-subagents--specialized-ai-personalities-for-delegation">2.3) Subagents — specialized AI personalities for delegation<a class="heading-link" aria-label="Link to section" href="#23-subagents--specialized-ai-personalities-for-delegation"><span class="heading-link-icon">#</span></a></h3>
<p><svg id="mermaid-2" width="650" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="418" viewBox="-50 -10 650 418" role="graphics-document document" aria-roledescription="sequence"><g><rect x="400" y="332" fill="#eaeaea" stroke="#666" width="150" height="65" name="SubB" rx="3" ry="3" class="actor actor-bottom"></rect><text x="475" y="364.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="475" dy="0">SubB</tspan></text></g><g><rect x="200" y="332" fill="#eaeaea" stroke="#666" width="150" height="65" name="SubA" rx="3" ry="3" class="actor actor-bottom"></rect><text x="275" y="364.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="275" dy="0">SubA</tspan></text></g><g><rect x="0" y="332" fill="#eaeaea" stroke="#666" width="150" height="65" name="Main" rx="3" ry="3" class="actor actor-bottom"></rect><text x="75" y="364.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="75" dy="0">Main</tspan></text></g><g><line id="actor5" x1="475" y1="65" x2="475" y2="332" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="SubB"></line><g id="root-5"><rect x="400" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="SubB" rx="3" ry="3" class="actor actor-top"></rect><text x="475" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="475" dy="0">SubB</tspan></text></g></g><g><line id="actor4" x1="275" y1="65" x2="275" y2="332" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="SubA"></line><g id="root-4"><rect x="200" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="SubA" rx="3" ry="3" class="actor actor-top"></rect><text x="275" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="275" dy="0">SubA</tspan></text></g></g><g><line id="actor3" x1="75" y1="65" x2="75" y2="332" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="Main"></line><g id="root-3"><rect x="0" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="Main" rx="3" ry="3" class="actor actor-top"></rect><text x="75" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="75" dy="0">Main</tspan></text></g></g><style>#mermaid-2{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-2 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-2 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-2 .error-icon{fill:#a44141;}#mermaid-2 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-2 .edge-thickness-normal{stroke-width:1px;}#mermaid-2 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-2 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-2 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-2 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-2 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-2 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-2 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-2 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-2 p{margin:0;}#mermaid-2 .actor{stroke:#ccc;fill:transparent;}#mermaid-2 text.actor>tspan{fill:lightgrey;stroke:none;}#mermaid-2 .actor-line{stroke:#ccc;}#mermaid-2 .innerArc{stroke-width:1.5;stroke-dasharray:none;}#mermaid-2 .messageLine0{stroke-width:1.5;stroke-dasharray:none;stroke:lightgrey;}#mermaid-2 .messageLine1{stroke-width:1.5;stroke-dasharray:2,2;stroke:lightgrey;}#mermaid-2 #arrowhead path{fill:lightgrey;stroke:lightgrey;}#mermaid-2 .sequenceNumber{fill:black;}#mermaid-2 #sequencenumber{fill:lightgrey;}#mermaid-2 #crosshead path{fill:lightgrey;stroke:lightgrey;}#mermaid-2 .messageText{fill:lightgrey;stroke:none;}#mermaid-2 .labelBox{stroke:#ccc;fill:transparent;}#mermaid-2 .labelText,#mermaid-2 .labelText>tspan{fill:lightgrey;stroke:none;}#mermaid-2 .loopText,#mermaid-2 .loopText>tspan{fill:lightgrey;stroke:none;}#mermaid-2 .loopLine{stroke-width:2px;stroke-dasharray:2,2;stroke:#ccc;fill:#ccc;}#mermaid-2 .note{stroke:hsl(180, 0%, 18.3529411765%);fill:hsla(0, 0%, 16%, 0);}#mermaid-2 .noteText,#mermaid-2 .noteText>tspan{fill:rgb(183.8476190475, 181.5523809523, 181.5523809523);stroke:none;}#mermaid-2 .activation0{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-2 .activation1{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-2 .activation2{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-2 .actorPopupMenu{position:absolute;}#mermaid-2 .actorPopupMenuPanel{position:absolute;fill:transparent;box-shadow:0px 8px 16px 0px rgba(0,0,0,0.2);filter:drop-shadow(3px 5px 2px rgb(0 0 0 / 0.4));}#mermaid-2 .actor-man line{stroke:#ccc;fill:transparent;}#mermaid-2 .actor-man circle,#mermaid-2 line{stroke:#ccc;fill:transparent;stroke-width:2px;}#mermaid-2 :root{--mermaid-font-family:arial,sans-serif;}</style><g></g><defs><symbol id="computer" width="24" height="24"><path transform="scale(.5)" d="M2 2v13h20v-13h-20zm18 11h-16v-9h16v9zm-10.228 6l.466-1h3.524l.467 1h-4.457zm14.228 3h-24l2-6h2.104l-1.33 4h18.45l-1.297-4h2.073l2 6zm-5-10h-14v-7h14v7z"></path></symbol></defs><defs><symbol id="database" fill-rule="evenodd" clip-rule="evenodd"><path transform="scale(.5)" d="M12.258.001l.256.004.255.005.253.008.251.01.249.012.247.015.246.016.242.019.241.02.239.023.236.024.233.027.231.028.229.031.225.032.223.034.22.036.217.038.214.04.211.041.208.043.205.045.201.046.198.048.194.05.191.051.187.053.183.054.18.056.175.057.172.059.168.06.163.061.16.063.155.064.15.066.074.033.073.033.071.034.07.034.069.035.068.035.067.035.066.035.064.036.064.036.062.036.06.036.06.037.058.037.058.037.055.038.055.038.053.038.052.038.051.039.05.039.048.039.047.039.045.04.044.04.043.04.041.04.04.041.039.041.037.041.036.041.034.041.033.042.032.042.03.042.029.042.027.042.026.043.024.043.023.043.021.043.02.043.018.044.017.043.015.044.013.044.012.044.011.045.009.044.007.045.006.045.004.045.002.045.001.045v17l-.001.045-.002.045-.004.045-.006.045-.007.045-.009.044-.011.045-.012.044-.013.044-.015.044-.017.043-.018.044-.02.043-.021.043-.023.043-.024.043-.026.043-.027.042-.029.042-.03.042-.032.042-.033.042-.034.041-.036.041-.037.041-.039.041-.04.041-.041.04-.043.04-.044.04-.045.04-.047.039-.048.039-.05.039-.051.039-.052.038-.053.038-.055.038-.055.038-.058.037-.058.037-.06.037-.06.036-.062.036-.064.036-.064.036-.066.035-.067.035-.068.035-.069.035-.07.034-.071.034-.073.033-.074.033-.15.066-.155.064-.16.063-.163.061-.168.06-.172.059-.175.057-.18.056-.183.054-.187.053-.191.051-.194.05-.198.048-.201.046-.205.045-.208.043-.211.041-.214.04-.217.038-.22.036-.223.034-.225.032-.229.031-.231.028-.233.027-.236.024-.239.023-.241.02-.242.019-.246.016-.247.015-.249.012-.251.01-.253.008-.255.005-.256.004-.258.001-.258-.001-.256-.004-.255-.005-.253-.008-.251-.01-.249-.012-.247-.015-.245-.016-.243-.019-.241-.02-.238-.023-.236-.024-.234-.027-.231-.028-.228-.031-.226-.032-.223-.034-.22-.036-.217-.038-.214-.04-.211-.041-.208-.043-.204-.045-.201-.046-.198-.048-.195-.05-.19-.051-.187-.053-.184-.054-.179-.056-.176-.057-.172-.059-.167-.06-.164-.061-.159-.063-.155-.064-.151-.066-.074-.033-.072-.033-.072-.034-.07-.034-.069-.035-.068-.035-.067-.035-.066-.035-.064-.036-.063-.036-.062-.036-.061-.036-.06-.037-.058-.037-.057-.037-.056-.038-.055-.038-.053-.038-.052-.038-.051-.039-.049-.039-.049-.039-.046-.039-.046-.04-.044-.04-.043-.04-.041-.04-.04-.041-.039-.041-.037-.041-.036-.041-.034-.041-.033-.042-.032-.042-.03-.042-.029-.042-.027-.042-.026-.043-.024-.043-.023-.043-.021-.043-.02-.043-.018-.044-.017-.043-.015-.044-.013-.044-.012-.044-.011-.045-.009-.044-.007-.045-.006-.045-.004-.045-.002-.045-.001-.045v-17l.001-.045.002-.045.004-.045.006-.045.007-.045.009-.044.011-.045.012-.044.013-.044.015-.044.017-.043.018-.044.02-.043.021-.043.023-.043.024-.043.026-.043.027-.042.029-.042.03-.042.032-.042.033-.042.034-.041.036-.041.037-.041.039-.041.04-.041.041-.04.043-.04.044-.04.046-.04.046-.039.049-.039.049-.039.051-.039.052-.038.053-.038.055-.038.056-.038.057-.037.058-.037.06-.037.061-.036.062-.036.063-.036.064-.036.066-.035.067-.035.068-.035.069-.035.07-.034.072-.034.072-.033.074-.033.151-.066.155-.064.159-.063.164-.061.167-.06.172-.059.176-.057.179-.056.184-.054.187-.053.19-.051.195-.05.198-.048.201-.046.204-.045.208-.043.211-.041.214-.04.217-.038.22-.036.223-.034.226-.032.228-.031.231-.028.234-.027.236-.024.238-.023.241-.02.243-.019.245-.016.247-.015.249-.012.251-.01.253-.008.255-.005.256-.004.258-.001.258.001zm-9.258 20.499v.01l.001.021.003.021.004.022.005.021.006.022.007.022.009.023.01.022.011.023.012.023.013.023.015.023.016.024.017.023.018.024.019.024.021.024.022.025.023.024.024.025.052.049.056.05.061.051.066.051.07.051.075.051.079.052.084.052.088.052.092.052.097.052.102.051.105.052.11.052.114.051.119.051.123.051.127.05.131.05.135.05.139.048.144.049.147.047.152.047.155.047.16.045.163.045.167.043.171.043.176.041.178.041.183.039.187.039.19.037.194.035.197.035.202.033.204.031.209.03.212.029.216.027.219.025.222.024.226.021.23.02.233.018.236.016.24.015.243.012.246.01.249.008.253.005.256.004.259.001.26-.001.257-.004.254-.005.25-.008.247-.011.244-.012.241-.014.237-.016.233-.018.231-.021.226-.021.224-.024.22-.026.216-.027.212-.028.21-.031.205-.031.202-.034.198-.034.194-.036.191-.037.187-.039.183-.04.179-.04.175-.042.172-.043.168-.044.163-.045.16-.046.155-.046.152-.047.148-.048.143-.049.139-.049.136-.05.131-.05.126-.05.123-.051.118-.052.114-.051.11-.052.106-.052.101-.052.096-.052.092-.052.088-.053.083-.051.079-.052.074-.052.07-.051.065-.051.06-.051.056-.05.051-.05.023-.024.023-.025.021-.024.02-.024.019-.024.018-.024.017-.024.015-.023.014-.024.013-.023.012-.023.01-.023.01-.022.008-.022.006-.022.006-.022.004-.022.004-.021.001-.021.001-.021v-4.127l-.077.055-.08.053-.083.054-.085.053-.087.052-.09.052-.093.051-.095.05-.097.05-.1.049-.102.049-.105.048-.106.047-.109.047-.111.046-.114.045-.115.045-.118.044-.12.043-.122.042-.124.042-.126.041-.128.04-.13.04-.132.038-.134.038-.135.037-.138.037-.139.035-.142.035-.143.034-.144.033-.147.032-.148.031-.15.03-.151.03-.153.029-.154.027-.156.027-.158.026-.159.025-.161.024-.162.023-.163.022-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.011-.178.01-.179.008-.179.008-.181.006-.182.005-.182.004-.184.003-.184.002h-.37l-.184-.002-.184-.003-.182-.004-.182-.005-.181-.006-.179-.008-.179-.008-.178-.01-.176-.011-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.022-.162-.023-.161-.024-.159-.025-.157-.026-.156-.027-.155-.027-.153-.029-.151-.03-.15-.03-.148-.031-.146-.032-.145-.033-.143-.034-.141-.035-.14-.035-.137-.037-.136-.037-.134-.038-.132-.038-.13-.04-.128-.04-.126-.041-.124-.042-.122-.042-.12-.044-.117-.043-.116-.045-.113-.045-.112-.046-.109-.047-.106-.047-.105-.048-.102-.049-.1-.049-.097-.05-.095-.05-.093-.052-.09-.051-.087-.052-.085-.053-.083-.054-.08-.054-.077-.054v4.127zm0-5.654v.011l.001.021.003.021.004.021.005.022.006.022.007.022.009.022.01.022.011.023.012.023.013.023.015.024.016.023.017.024.018.024.019.024.021.024.022.024.023.025.024.024.052.05.056.05.061.05.066.051.07.051.075.052.079.051.084.052.088.052.092.052.097.052.102.052.105.052.11.051.114.051.119.052.123.05.127.051.131.05.135.049.139.049.144.048.147.048.152.047.155.046.16.045.163.045.167.044.171.042.176.042.178.04.183.04.187.038.19.037.194.036.197.034.202.033.204.032.209.03.212.028.216.027.219.025.222.024.226.022.23.02.233.018.236.016.24.014.243.012.246.01.249.008.253.006.256.003.259.001.26-.001.257-.003.254-.006.25-.008.247-.01.244-.012.241-.015.237-.016.233-.018.231-.02.226-.022.224-.024.22-.025.216-.027.212-.029.21-.03.205-.032.202-.033.198-.035.194-.036.191-.037.187-.039.183-.039.179-.041.175-.042.172-.043.168-.044.163-.045.16-.045.155-.047.152-.047.148-.048.143-.048.139-.05.136-.049.131-.05.126-.051.123-.051.118-.051.114-.052.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.051.07-.052.065-.051.06-.05.056-.051.051-.049.023-.025.023-.024.021-.025.02-.024.019-.024.018-.024.017-.024.015-.023.014-.023.013-.024.012-.022.01-.023.01-.023.008-.022.006-.022.006-.022.004-.021.004-.022.001-.021.001-.021v-4.139l-.077.054-.08.054-.083.054-.085.052-.087.053-.09.051-.093.051-.095.051-.097.05-.1.049-.102.049-.105.048-.106.047-.109.047-.111.046-.114.045-.115.044-.118.044-.12.044-.122.042-.124.042-.126.041-.128.04-.13.039-.132.039-.134.038-.135.037-.138.036-.139.036-.142.035-.143.033-.144.033-.147.033-.148.031-.15.03-.151.03-.153.028-.154.028-.156.027-.158.026-.159.025-.161.024-.162.023-.163.022-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.011-.178.009-.179.009-.179.007-.181.007-.182.005-.182.004-.184.003-.184.002h-.37l-.184-.002-.184-.003-.182-.004-.182-.005-.181-.007-.179-.007-.179-.009-.178-.009-.176-.011-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.022-.162-.023-.161-.024-.159-.025-.157-.026-.156-.027-.155-.028-.153-.028-.151-.03-.15-.03-.148-.031-.146-.033-.145-.033-.143-.033-.141-.035-.14-.036-.137-.036-.136-.037-.134-.038-.132-.039-.13-.039-.128-.04-.126-.041-.124-.042-.122-.043-.12-.043-.117-.044-.116-.044-.113-.046-.112-.046-.109-.046-.106-.047-.105-.048-.102-.049-.1-.049-.097-.05-.095-.051-.093-.051-.09-.051-.087-.053-.085-.052-.083-.054-.08-.054-.077-.054v4.139zm0-5.666v.011l.001.02.003.022.004.021.005.022.006.021.007.022.009.023.01.022.011.023.012.023.013.023.015.023.016.024.017.024.018.023.019.024.021.025.022.024.023.024.024.025.052.05.056.05.061.05.066.051.07.051.075.052.079.051.084.052.088.052.092.052.097.052.102.052.105.051.11.052.114.051.119.051.123.051.127.05.131.05.135.05.139.049.144.048.147.048.152.047.155.046.16.045.163.045.167.043.171.043.176.042.178.04.183.04.187.038.19.037.194.036.197.034.202.033.204.032.209.03.212.028.216.027.219.025.222.024.226.021.23.02.233.018.236.017.24.014.243.012.246.01.249.008.253.006.256.003.259.001.26-.001.257-.003.254-.006.25-.008.247-.01.244-.013.241-.014.237-.016.233-.018.231-.02.226-.022.224-.024.22-.025.216-.027.212-.029.21-.03.205-.032.202-.033.198-.035.194-.036.191-.037.187-.039.183-.039.179-.041.175-.042.172-.043.168-.044.163-.045.16-.045.155-.047.152-.047.148-.048.143-.049.139-.049.136-.049.131-.051.126-.05.123-.051.118-.052.114-.051.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.052.07-.051.065-.051.06-.051.056-.05.051-.049.023-.025.023-.025.021-.024.02-.024.019-.024.018-.024.017-.024.015-.023.014-.024.013-.023.012-.023.01-.022.01-.023.008-.022.006-.022.006-.022.004-.022.004-.021.001-.021.001-.021v-4.153l-.077.054-.08.054-.083.053-.085.053-.087.053-.09.051-.093.051-.095.051-.097.05-.1.049-.102.048-.105.048-.106.048-.109.046-.111.046-.114.046-.115.044-.118.044-.12.043-.122.043-.124.042-.126.041-.128.04-.13.039-.132.039-.134.038-.135.037-.138.036-.139.036-.142.034-.143.034-.144.033-.147.032-.148.032-.15.03-.151.03-.153.028-.154.028-.156.027-.158.026-.159.024-.161.024-.162.023-.163.023-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.01-.178.01-.179.009-.179.007-.181.006-.182.006-.182.004-.184.003-.184.001-.185.001-.185-.001-.184-.001-.184-.003-.182-.004-.182-.006-.181-.006-.179-.007-.179-.009-.178-.01-.176-.01-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.023-.162-.023-.161-.024-.159-.024-.157-.026-.156-.027-.155-.028-.153-.028-.151-.03-.15-.03-.148-.032-.146-.032-.145-.033-.143-.034-.141-.034-.14-.036-.137-.036-.136-.037-.134-.038-.132-.039-.13-.039-.128-.041-.126-.041-.124-.041-.122-.043-.12-.043-.117-.044-.116-.044-.113-.046-.112-.046-.109-.046-.106-.048-.105-.048-.102-.048-.1-.05-.097-.049-.095-.051-.093-.051-.09-.052-.087-.052-.085-.053-.083-.053-.08-.054-.077-.054v4.153zm8.74-8.179l-.257.004-.254.005-.25.008-.247.011-.244.012-.241.014-.237.016-.233.018-.231.021-.226.022-.224.023-.22.026-.216.027-.212.028-.21.031-.205.032-.202.033-.198.034-.194.036-.191.038-.187.038-.183.04-.179.041-.175.042-.172.043-.168.043-.163.045-.16.046-.155.046-.152.048-.148.048-.143.048-.139.049-.136.05-.131.05-.126.051-.123.051-.118.051-.114.052-.11.052-.106.052-.101.052-.096.052-.092.052-.088.052-.083.052-.079.052-.074.051-.07.052-.065.051-.06.05-.056.05-.051.05-.023.025-.023.024-.021.024-.02.025-.019.024-.018.024-.017.023-.015.024-.014.023-.013.023-.012.023-.01.023-.01.022-.008.022-.006.023-.006.021-.004.022-.004.021-.001.021-.001.021.001.021.001.021.004.021.004.022.006.021.006.023.008.022.01.022.01.023.012.023.013.023.014.023.015.024.017.023.018.024.019.024.02.025.021.024.023.024.023.025.051.05.056.05.06.05.065.051.07.052.074.051.079.052.083.052.088.052.092.052.096.052.101.052.106.052.11.052.114.052.118.051.123.051.126.051.131.05.136.05.139.049.143.048.148.048.152.048.155.046.16.046.163.045.168.043.172.043.175.042.179.041.183.04.187.038.191.038.194.036.198.034.202.033.205.032.21.031.212.028.216.027.22.026.224.023.226.022.231.021.233.018.237.016.241.014.244.012.247.011.25.008.254.005.257.004.26.001.26-.001.257-.004.254-.005.25-.008.247-.011.244-.012.241-.014.237-.016.233-.018.231-.021.226-.022.224-.023.22-.026.216-.027.212-.028.21-.031.205-.032.202-.033.198-.034.194-.036.191-.038.187-.038.183-.04.179-.041.175-.042.172-.043.168-.043.163-.045.16-.046.155-.046.152-.048.148-.048.143-.048.139-.049.136-.05.131-.05.126-.051.123-.051.118-.051.114-.052.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.051.07-.052.065-.051.06-.05.056-.05.051-.05.023-.025.023-.024.021-.024.02-.025.019-.024.018-.024.017-.023.015-.024.014-.023.013-.023.012-.023.01-.023.01-.022.008-.022.006-.023.006-.021.004-.022.004-.021.001-.021.001-.021-.001-.021-.001-.021-.004-.021-.004-.022-.006-.021-.006-.023-.008-.022-.01-.022-.01-.023-.012-.023-.013-.023-.014-.023-.015-.024-.017-.023-.018-.024-.019-.024-.02-.025-.021-.024-.023-.024-.023-.025-.051-.05-.056-.05-.06-.05-.065-.051-.07-.052-.074-.051-.079-.052-.083-.052-.088-.052-.092-.052-.096-.052-.101-.052-.106-.052-.11-.052-.114-.052-.118-.051-.123-.051-.126-.051-.131-.05-.136-.05-.139-.049-.143-.048-.148-.048-.152-.048-.155-.046-.16-.046-.163-.045-.168-.043-.172-.043-.175-.042-.179-.041-.183-.04-.187-.038-.191-.038-.194-.036-.198-.034-.202-.033-.205-.032-.21-.031-.212-.028-.216-.027-.22-.026-.224-.023-.226-.022-.231-.021-.233-.018-.237-.016-.241-.014-.244-.012-.247-.011-.25-.008-.254-.005-.257-.004-.26-.001-.26.001z"></path></symbol></defs><defs><symbol id="clock" width="24" height="24"><path transform="scale(.5)" d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm5.848 12.459c.202.038.202.333.001.372-1.907.361-6.045 1.111-6.547 1.111-.719 0-1.301-.582-1.301-1.301 0-.512.77-5.447 1.125-7.445.034-.192.312-.181.343.014l.985 6.238 5.394 1.011z"></path></symbol></defs><defs><marker id="arrowhead" refX="7.9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M -1 0 L 10 5 L 0 10 z"></path></marker></defs><defs><marker id="crosshead" markerWidth="15" markerHeight="8" orient="auto" refX="4" refY="4.5"><path fill="none" stroke="#000000" stroke-width="1pt" d="M 1,2 L 6,7 M 6,2 L 1,7" style="stroke-dasharray:0, 0"></path></marker></defs><defs><marker id="filled-head" refX="15.5" refY="7" markerWidth="20" markerHeight="28" orient="auto"><path d="M 18,7 L9,13 L14,7 L9,1 Z"></path></marker></defs><defs><marker id="sequencenumber" refX="15" refY="15" markerWidth="60" markerHeight="40" orient="auto"><circle cx="15" cy="15" r="6"></circle></marker></defs><g><line x1="64" y1="171" x2="486" y2="171" class="loopLine"></line><line x1="486" y1="171" x2="486" y2="312" class="loopLine"></line><line x1="64" y1="312" x2="486" y2="312" class="loopLine"></line><line x1="64" y1="171" x2="64" y2="312" class="loopLine"></line><polygon points="64,171 114,171 114,184 105.6,191 64,191" class="labelBox"></polygon><text x="89" y="184" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="labelText" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">par</text><text x="300" y="189" text-anchor="middle" class="loopText" style="font-family:arial, sans-serif;font-size:16px;font-weight:400"><tspan x="300">[Parallel execution]</tspan></text></g><text x="174" y="80" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">task: security analysis</text><line x1="76" y1="113" x2="271" y2="113" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></line><text x="274" y="128" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">task: test generation</text><line x1="76" y1="161" x2="471" y2="161" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></line><text x="177" y="221" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">results</text><line x1="274" y1="254" x2="79" y2="254" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></line><text x="277" y="269" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">results</text><line x1="474" y1="302" x2="79" y2="302" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></line></svg></p>
<p><strong>What they are.</strong> Pre-configured AI personalities with specific expertise areas. Each subagent has its own system prompt, allowed tools, and separate context window. When Claude encounters a task matching a subagent’s expertise, it delegates automatically.</p>
<p><strong>Why use them.</strong> Keep your main conversation clean while offloading specialized work. Each subagent works independently in its own context window, preventing token bloat. Run multiple subagents in parallel for concurrent analysis.</p>
<div class="alert alert-tip astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💪</span> Avoiding Context Poisoning </p> <div class="alert-content astro-7kdbuayl"> <p>Subagents prevent “context poisoning” — when detailed implementation work
clutters your main conversation. Use subagents for deep dives (security
audits, test generation, refactoring) that would otherwise fill your primary
context with noise.</p> </div> </div> 
<p><strong>Example structure:</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> security-auditor</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Analyzes code for security vulnerabilities</span></span>
<span class="line"><span style="color:#F7768E">tools</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Read, Grep, Bash</span><span style="color:#51597D;font-style:italic"> # Controls what this personality can access</span></span>
<span class="line"><span style="color:#F7768E">model</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> sonnet</span><span style="color:#51597D;font-style:italic"> # Optional: sonnet, opus, haiku, inherit</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">You are a security-focused code auditor.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Identify vulnerabilities (XSS, SQL injection, CSRF, etc.)</span></span>
<span class="line"><span style="color:#9AA5CE">Check dependencies and packages</span></span>
<span class="line"><span style="color:#9AA5CE">Verify auth/authorization</span></span>
<span class="line"><span style="color:#9AA5CE">Review data validation</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Provide severity levels: Critical, High, Medium, Low.</span></span>
<span class="line"><span style="color:#9AA5CE">Focus on OWASP Top 10.</span></span></code><button type="button" class="copy" data-code="---
name: security-auditor
description: Analyzes code for security vulnerabilities
tools: Read, Grep, Bash # Controls what this personality can access
model: sonnet # Optional: sonnet, opus, haiku, inherit
---

You are a security-focused code auditor.

Identify vulnerabilities (XSS, SQL injection, CSRF, etc.)
Check dependencies and packages
Verify auth/authorization
Review data validation

Provide severity levels: Critical, High, Medium, Low.
Focus on OWASP Top 10." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The system prompt shapes the subagent’s behavior. The <code>description</code> helps Claude know when to delegate. The <code>tools</code> restrict what the personality can access.</p>
<p><strong>Best practices:</strong> One expertise area per subagent. Grant minimal tool access. Use <code>haiku</code> for simple tasks, <code>sonnet</code> for complex analysis. Run independent work in parallel. Need a template? Check out this <a href="/prompts/claude/claude-create-agent">subagent creation guide</a>.</p>
<hr/>
<h3 id="24-hooks--automatic-event-driven-actions">2.4) Hooks — automatic event-driven actions<a class="heading-link" aria-label="Link to section" href="#24-hooks--automatic-event-driven-actions"><span class="heading-link-icon">#</span></a></h3>
<p><svg id="mermaid-3" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:469.390625px" viewBox="0 0 469.390625 174" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-3{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-3 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-3 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-3 .error-icon{fill:#a44141;}#mermaid-3 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-3 .edge-thickness-normal{stroke-width:1px;}#mermaid-3 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-3 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-3 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-3 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-3 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-3 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-3 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-3 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-3 p{margin:0;}#mermaid-3 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-3 .cluster-label text{fill:#F9FFFE;}#mermaid-3 .cluster-label span{color:#F9FFFE;}#mermaid-3 .cluster-label span p{background-color:transparent;}#mermaid-3 .label text,#mermaid-3 span{fill:#ccc;color:#ccc;}#mermaid-3 .node rect,#mermaid-3 .node circle,#mermaid-3 .node ellipse,#mermaid-3 .node polygon,#mermaid-3 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-3 .rough-node .label text,#mermaid-3 .node .label text,#mermaid-3 .image-shape .label,#mermaid-3 .icon-shape .label{text-anchor:middle;}#mermaid-3 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-3 .rough-node .label,#mermaid-3 .node .label,#mermaid-3 .image-shape .label,#mermaid-3 .icon-shape .label{text-align:center;}#mermaid-3 .node.clickable{cursor:pointer;}#mermaid-3 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-3 .arrowheadPath{fill:lightgrey;}#mermaid-3 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-3 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-3 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-3 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-3 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-3 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-3 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-3 .cluster text{fill:#F9FFFE;}#mermaid-3 .cluster span{color:#F9FFFE;}#mermaid-3 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-3 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-3 rect.text{fill:none;stroke-width:0;}#mermaid-3 .icon-shape,#mermaid-3 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-3 .icon-shape p,#mermaid-3 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-3 .icon-shape rect,#mermaid-3 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-3 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-3 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-3 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-3_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-3_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-3_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-3_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-3_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-3_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M147.57,62L134.125,66.167C120.679,70.333,93.789,78.667,80.344,86.333C66.898,94,66.898,101,66.898,104.5L66.898,108" id="L_Event_HookA_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Event_HookA_0" data-points="W3sieCI6MTQ3LjU3MDAxMjAxOTIzMDc3LCJ5Ijo2Mn0seyJ4Ijo2Ni44OTg0Mzc1LCJ5Ijo4N30seyJ4Ijo2Ni44OTg0Mzc1LCJ5IjoxMTJ9XQ==" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M234.695,62L234.695,66.167C234.695,70.333,234.695,78.667,234.695,86.333C234.695,94,234.695,101,234.695,104.5L234.695,108" id="L_Event_HookB_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Event_HookB_0" data-points="W3sieCI6MjM0LjY5NTMxMjUsInkiOjYyfSx7IngiOjIzNC42OTUzMTI1LCJ5Ijo4N30seyJ4IjoyMzQuNjk1MzEyNSwieSI6MTEyfV0=" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path><path d="M321.821,62L335.266,66.167C348.711,70.333,375.602,78.667,389.047,86.333C402.492,94,402.492,101,402.492,104.5L402.492,108" id="L_Event_HookC_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Event_HookC_0" data-points="W3sieCI6MzIxLjgyMDYxMjk4MDc2OTIsInkiOjYyfSx7IngiOjQwMi40OTIxODc1LCJ5Ijo4N30seyJ4Ijo0MDIuNDkyMTg3NSwieSI6MTEyfV0=" marker-end="url(#mermaid-3_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_Event_HookA_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Event_HookB_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Event_HookC_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-Event-0" transform="translate(234.6953125, 35)"><rect class="basic label-container" style="" x="-102.25" y="-27" width="204.5" height="54"></rect><g class="label" style="" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Lifecycle Event</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-HookA-1" transform="translate(66.8984375, 139)"><rect class="basic label-container" style="" x="-58.8984375" y="-27" width="117.796875" height="54"></rect><g class="label" style="" transform="translate(-28.8984375, -12)"><rect></rect><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Hook 1</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-HookB-2" transform="translate(234.6953125, 139)"><rect class="basic label-container" style="" x="-58.8984375" y="-27" width="117.796875" height="54"></rect><g class="label" style="" transform="translate(-28.8984375, -12)"><rect></rect><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Hook 2</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-HookC-3" transform="translate(402.4921875, 139)"><rect class="basic label-container" style="" x="-58.8984375" y="-27" width="117.796875" height="54"></rect><g class="label" style="" transform="translate(-28.8984375, -12)"><rect></rect><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Hook 3</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<p><strong>What they are.</strong> JSON-configured handlers in <code>.claude/settings.json</code> that trigger automatically on lifecycle events. No manual invocation.</p>
<p><strong>Available events:</strong> <code>PreToolUse</code>, <code>PostToolUse</code>, <code>UserPromptSubmit</code>, <code>Notification</code>, <code>Stop</code>, <code>SubagentStop</code>, <code>SessionStart</code></p>
<p><strong>Two modes:</strong></p>
<ul>
<li><strong>Command:</strong> Run shell commands (fast, predictable)</li>
<li><strong>Prompt:</strong> Let Claude decide with the LLM (flexible, context-aware)</li>
</ul>
<p><strong>Example:</strong> Auto-lint after file edits.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="json"><code><span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#89DDFF">  &quot;</span><span style="color:#7AA2F7">hooks</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#89DDFF">    &quot;</span><span style="color:#0DB9D7">PostToolUse</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">      {</span></span>
<span class="line"><span style="color:#89DDFF">        &quot;</span><span style="color:#7DCFFF">matcher</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Edit|Write</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">        &quot;</span><span style="color:#7DCFFF">hooks</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span></span>
<span class="line"><span style="color:#89DDFF">            &quot;</span><span style="color:#BB9AF7">type</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">command</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">            &quot;</span><span style="color:#BB9AF7">command</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;\&quot;</span><span style="color:#9ECE6A">$CLAUDE_PROJECT_DIR</span><span style="color:#89DDFF">\&quot;</span><span style="color:#9ECE6A">/.claude/hooks/run-oxlint.sh</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span></span>
<span class="line"><span style="color:#9ABDF5">        ]</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span></span>
<span class="line"><span style="color:#9ABDF5">    ]</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="{
  &#34;hooks&#34;: {
    &#34;PostToolUse&#34;: [
      {
        &#34;matcher&#34;: &#34;Edit|Write&#34;,
        &#34;hooks&#34;: [
          {
            &#34;type&#34;: &#34;command&#34;,
            &#34;command&#34;: &#34;\&#34;$CLAUDE_PROJECT_DIR\&#34;/.claude/hooks/run-oxlint.sh&#34;
          }
        ]
      }
    ]
  }
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#51597D;font-style:italic">#!/usr/bin/env bash</span></span>
<span class="line"><span style="color:#C0CAF5">file_path</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;$(</span><span style="color:#C0CAF5">jq</span><span style="color:#E0AF68"> -r</span><span style="color:#89DDFF"> &#39;</span><span style="color:#9ECE6A">.tool_input.file_path // &quot;&quot;</span><span style="color:#89DDFF">&#39;)&quot;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">if</span><span style="color:#89DDFF"> [[</span><span style="color:#89DDFF"> &quot;</span><span style="color:#C0CAF5">$file_path</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> =~</span><span style="color:#89DDFF"> \.</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">js</span><span style="color:#89DDFF">|</span><span style="color:#C0CAF5">jsx</span><span style="color:#89DDFF">|</span><span style="color:#C0CAF5">ts</span><span style="color:#89DDFF">|</span><span style="color:#C0CAF5">tsx</span><span style="color:#89DDFF">|</span><span style="color:#C0CAF5">vue</span><span style="color:#9ABDF5">)</span><span style="color:#A9B1D6">$ </span><span style="color:#89DDFF">]];</span><span style="color:#BB9AF7"> then</span></span>
<span class="line"><span style="color:#C0CAF5">  pnpm</span><span style="color:#9ECE6A"> lint:fast</span></span>
<span class="line"><span style="color:#BB9AF7">fi</span></span></code><button type="button" class="copy" data-code="#!/usr/bin/env bash
file_path=&#34;$(jq -r '.tool_input.file_path // &#34;&#34;')&#34;

if [[ &#34;$file_path&#34; =~ \.(js|jsx|ts|tsx|vue)$ ]]; then
  pnpm lint:fast
fi" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>Common uses:</strong> Auto-format after edits, require approval for bash commands, validate writes, initialize sessions. For a practical example, see how to <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/claude-code-notification-hooks/" class="internal-link astro-3tyn5ojg"> set up desktop notifications </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Claude Code Notifications: Get Alerts When Tasks Finish (Hooks Setup)</span> <span class="preview-description astro-3tyn5ojg">How to set up Claude Code notifications using hooks. Get desktop alerts when Claude finishes a task, needs your input, or requests permission, instead of watching the terminal.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">notifications</span><span class="preview-tag astro-3tyn5ojg">hooks</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 23, 2025</time> </span> </span> </span>  <script>
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
</script> when Claude needs your attention. Want to create your own hooks? Use this <a href="/prompts/claude/claude-create-hook">hook creation guide</a>.</p>
<hr/>
<h2 id="3-plugins--shareable-packaged-configurations">3) Plugins — shareable, packaged configurations<a class="heading-link" aria-label="Link to section" href="#3-plugins--shareable-packaged-configurations"><span class="heading-link-icon">#</span></a></h2>
<p><svg id="mermaid-4" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="classDiagram" style="max-width:371.03125px" viewBox="0 0 371.03125 318" role="graphics-document document" aria-roledescription="class"><style>#mermaid-4{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-4 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-4 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-4 .error-icon{fill:#a44141;}#mermaid-4 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-4 .edge-thickness-normal{stroke-width:1px;}#mermaid-4 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-4 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-4 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-4 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-4 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-4 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-4 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-4 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-4 p{margin:0;}#mermaid-4 g.classGroup text{fill:2px;stroke:none;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:10px;}#mermaid-4 g.classGroup text .title{font-weight:bolder;}#mermaid-4 .nodeLabel,#mermaid-4 .edgeLabel{color:rgb(234, 237, 243);}#mermaid-4 .edgeLabel .label rect{fill:transparent;}#mermaid-4 .label text{fill:rgb(234, 237, 243);}#mermaid-4 .labelBkg{background:transparent;}#mermaid-4 .edgeLabel .label span{background:transparent;}#mermaid-4 .classTitle{font-weight:bolder;}#mermaid-4 .node rect,#mermaid-4 .node circle,#mermaid-4 .node ellipse,#mermaid-4 .node polygon,#mermaid-4 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-4 .divider{stroke:2px;stroke-width:1;}#mermaid-4 g.clickable{cursor:pointer;}#mermaid-4 g.classGroup rect{fill:transparent;stroke:2px;}#mermaid-4 g.classGroup line{stroke:2px;stroke-width:1;}#mermaid-4 .classLabel .box{stroke:none;stroke-width:0;fill:transparent;opacity:0.5;}#mermaid-4 .classLabel .label{fill:2px;font-size:10px;}#mermaid-4 .relation{stroke:rgb(171, 75, 153);stroke-width:1;fill:none;}#mermaid-4 .dashed-line{stroke-dasharray:3;}#mermaid-4 .dotted-line{stroke-dasharray:1 2;}#mermaid-4 #compositionStart,#mermaid-4 .composition{fill:rgb(171, 75, 153)!important;stroke:rgb(171, 75, 153)!important;stroke-width:1;}#mermaid-4 #compositionEnd,#mermaid-4 .composition{fill:rgb(171, 75, 153)!important;stroke:rgb(171, 75, 153)!important;stroke-width:1;}#mermaid-4 #dependencyStart,#mermaid-4 .dependency{fill:rgb(171, 75, 153)!important;stroke:rgb(171, 75, 153)!important;stroke-width:1;}#mermaid-4 #dependencyStart,#mermaid-4 .dependency{fill:rgb(171, 75, 153)!important;stroke:rgb(171, 75, 153)!important;stroke-width:1;}#mermaid-4 #extensionStart,#mermaid-4 .extension{fill:transparent!important;stroke:rgb(171, 75, 153)!important;stroke-width:1;}#mermaid-4 #extensionEnd,#mermaid-4 .extension{fill:transparent!important;stroke:rgb(171, 75, 153)!important;stroke-width:1;}#mermaid-4 #aggregationStart,#mermaid-4 .aggregation{fill:transparent!important;stroke:rgb(171, 75, 153)!important;stroke-width:1;}#mermaid-4 #aggregationEnd,#mermaid-4 .aggregation{fill:transparent!important;stroke:rgb(171, 75, 153)!important;stroke-width:1;}#mermaid-4 #lollipopStart,#mermaid-4 .lollipop{fill:transparent!important;stroke:rgb(171, 75, 153)!important;stroke-width:1;}#mermaid-4 #lollipopEnd,#mermaid-4 .lollipop{fill:transparent!important;stroke:rgb(171, 75, 153)!important;stroke-width:1;}#mermaid-4 .edgeTerminals{font-size:11px;line-height:initial;}#mermaid-4 .classTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-4 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-4 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-4 :root{--mermaid-font-family:arial,sans-serif;}</style><g><defs><marker id="mermaid-4_class-aggregationStart" class="marker aggregation class" refX="18" refY="7" markerWidth="190" markerHeight="240" orient="auto"><path d="M 18,7 L9,13 L1,7 L9,1 Z"></path></marker></defs><defs><marker id="mermaid-4_class-aggregationEnd" class="marker aggregation class" refX="1" refY="7" markerWidth="20" markerHeight="28" orient="auto"><path d="M 18,7 L9,13 L1,7 L9,1 Z"></path></marker></defs><defs><marker id="mermaid-4_class-extensionStart" class="marker extension class" refX="18" refY="7" markerWidth="190" markerHeight="240" orient="auto"><path d="M 1,7 L18,13 V 1 Z"></path></marker></defs><defs><marker id="mermaid-4_class-extensionEnd" class="marker extension class" refX="1" refY="7" markerWidth="20" markerHeight="28" orient="auto"><path d="M 1,1 V 13 L18,7 Z"></path></marker></defs><defs><marker id="mermaid-4_class-compositionStart" class="marker composition class" refX="18" refY="7" markerWidth="190" markerHeight="240" orient="auto"><path d="M 18,7 L9,13 L1,7 L9,1 Z"></path></marker></defs><defs><marker id="mermaid-4_class-compositionEnd" class="marker composition class" refX="1" refY="7" markerWidth="20" markerHeight="28" orient="auto"><path d="M 18,7 L9,13 L1,7 L9,1 Z"></path></marker></defs><defs><marker id="mermaid-4_class-dependencyStart" class="marker dependency class" refX="6" refY="7" markerWidth="190" markerHeight="240" orient="auto"><path d="M 5,7 L9,13 L1,7 L9,1 Z"></path></marker></defs><defs><marker id="mermaid-4_class-dependencyEnd" class="marker dependency class" refX="13" refY="7" markerWidth="20" markerHeight="28" orient="auto"><path d="M 18,7 L9,13 L14,7 L9,1 Z"></path></marker></defs><defs><marker id="mermaid-4_class-lollipopStart" class="marker lollipop class" refX="13" refY="7" markerWidth="190" markerHeight="240" orient="auto"><circle stroke="black" fill="transparent" cx="7" cy="7" r="6"></circle></marker></defs><defs><marker id="mermaid-4_class-lollipopEnd" class="marker lollipop class" refX="1" refY="7" markerWidth="190" markerHeight="240" orient="auto"><circle stroke="black" fill="transparent" cx="7" cy="7" r="6"></circle></marker></defs><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M134.98,140.005L122.239,150.171C109.497,160.337,84.014,180.668,71.273,194.001C58.531,207.333,58.531,213.667,58.531,216.833L58.531,220" id="id_Plugin_Commands_1" class="edge-thickness-normal edge-pattern-solid relation" style="" data-edge="true" data-et="edge" data-id="id_Plugin_Commands_1" data-points="W3sieCI6MTM0Ljk4MDQ2ODc1LCJ5IjoxNDAuMDA1MDAzNzE3MDQ2OTV9LHsieCI6NTguNTMxMjUsInkiOjIwMX0seyJ4Ijo1OC41MzEyNSwieSI6MjI2fV0=" marker-end="url(#mermaid-4_class-dependencyEnd)"></path><path d="M195.148,176L195.148,180.167C195.148,184.333,195.148,192.667,195.148,200C195.148,207.333,195.148,213.667,195.148,216.833L195.148,220" id="id_Plugin_Hooks_2" class="edge-thickness-normal edge-pattern-solid relation" style="" data-edge="true" data-et="edge" data-id="id_Plugin_Hooks_2" data-points="W3sieCI6MTk1LjE0ODQzNzUsInkiOjE3Nn0seyJ4IjoxOTUuMTQ4NDM3NSwieSI6MjAxfSx7IngiOjE5NS4xNDg0Mzc1LCJ5IjoyMjZ9XQ==" marker-end="url(#mermaid-4_class-dependencyEnd)"></path><path d="M255.316,143.647L266.452,153.205C277.589,162.764,299.861,181.882,310.997,194.608C322.133,207.333,322.133,213.667,322.133,216.833L322.133,220" id="id_Plugin_Skills_3" class="edge-thickness-normal edge-pattern-solid relation" style="" data-edge="true" data-et="edge" data-id="id_Plugin_Skills_3" data-points="W3sieCI6MjU1LjMxNjQwNjI1LCJ5IjoxNDMuNjQ2NTc5MzAzNTU2MDV9LHsieCI6MzIyLjEzMjgxMjUsInkiOjIwMX0seyJ4IjozMjIuMTMyODEyNSwieSI6MjI2fV0=" marker-end="url(#mermaid-4_class-dependencyEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="id_Plugin_Commands_1" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="id_Plugin_Hooks_2" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="id_Plugin_Skills_3" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="classId-Plugin-0" transform="translate(195.1484375, 92)"><g class="basic label-container"><path d="M-60.16796875 -84 L60.16796875 -84 L60.16796875 84 L-60.16796875 84" stroke="none" stroke-width="0" fill="transparent" style=""></path><path d="M-60.16796875 -84 C-30.939173930959054 -84, -1.7103791119181082 -84, 60.16796875 -84 M-60.16796875 -84 C-21.95305509792751 -84, 16.26185855414498 -84, 60.16796875 -84 M60.16796875 -84 C60.16796875 -43.29814195856605, 60.16796875 -2.596283917132098, 60.16796875 84 M60.16796875 -84 C60.16796875 -26.62704274991016, 60.16796875 30.74591450017968, 60.16796875 84 M60.16796875 84 C31.72103468979335 84, 3.274100629586698 84, -60.16796875 84 M60.16796875 84 C19.069275349860817 84, -22.029418050278366 84, -60.16796875 84 M-60.16796875 84 C-60.16796875 48.47120478748366, -60.16796875 12.942409574967314, -60.16796875 -84 M-60.16796875 84 C-60.16796875 27.30661327312165, -60.16796875 -29.386773453756703, -60.16796875 -84" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g><g class="annotation-group text" transform="translate(0, -60)"></g><g class="label-group text" transform="translate(-28.8984375, -60)"><g class="label" style="font-weight:bolder" transform="translate(0,-12)"><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:99px;text-align:center"><span class="nodeLabel markdown-node-label" style=""><p>Plugin</p></span></div></foreignObject></g></g><g class="members-group text" transform="translate(-48.16796875, -12)"><g class="label" style="" transform="translate(0,-12)"><foreignObject width="38.53125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:95px;text-align:center"><span class="nodeLabel markdown-node-label" style=""><p>name</p></span></div></foreignObject></g><g class="label" style="" transform="translate(0,12)"><foreignObject width="67.4375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:109px;text-align:center"><span class="nodeLabel markdown-node-label" style=""><p>version</p></span></div></foreignObject></g><g class="label" style="" transform="translate(0,36)"><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:103px;text-align:center"><span class="nodeLabel markdown-node-label" style=""><p>author</p></span></div></foreignObject></g></g><g class="methods-group text" transform="translate(-48.16796875, 84)"></g><g class="divider" style=""><path d="M-60.16796875 -36 C-27.393636571026356 -36, 5.380695607947288 -36, 60.16796875 -36 M-60.16796875 -36 C-13.658023726254221 -36, 32.85192129749156 -36, 60.16796875 -36" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g><g class="divider" style=""><path d="M-60.16796875 60 C-17.513464178143423 60, 25.141040393713155 60, 60.16796875 60 M-60.16796875 60 C-31.197950293628654 60, -2.2279318372573087 60, 60.16796875 60" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g></g><g class="node default" id="classId-Commands-1" transform="translate(58.53125, 268)"><g class="basic label-container"><path d="M-50.53125 -42 L50.53125 -42 L50.53125 42 L-50.53125 42" stroke="none" stroke-width="0" fill="transparent" style=""></path><path d="M-50.53125 -42 C-16.31560272781463 -42, 17.900044544370743 -42, 50.53125 -42 M-50.53125 -42 C-27.033768676748263 -42, -3.536287353496526 -42, 50.53125 -42 M50.53125 -42 C50.53125 -12.629267741733678, 50.53125 16.741464516532645, 50.53125 42 M50.53125 -42 C50.53125 -18.327237331695635, 50.53125 5.3455253366087305, 50.53125 42 M50.53125 42 C25.05842404521229 42, -0.41440190957541745 42, -50.53125 42 M50.53125 42 C15.315466085784664 42, -19.900317828430673 42, -50.53125 42 M-50.53125 42 C-50.53125 19.64604493510159, -50.53125 -2.707910129796822, -50.53125 -42 M-50.53125 42 C-50.53125 16.92191476484124, -50.53125 -8.15617047031752, -50.53125 -42" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g><g class="annotation-group text" transform="translate(0, -18)"></g><g class="label-group text" transform="translate(-38.53125, -18)"><g class="label" style="font-weight:bolder" transform="translate(0,-12)"><foreignObject width="77.0625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:141px;text-align:center"><span class="nodeLabel markdown-node-label" style=""><p>Commands</p></span></div></foreignObject></g></g><g class="members-group text" transform="translate(-38.53125, 30)"></g><g class="methods-group text" transform="translate(-38.53125, 60)"></g><g class="divider" style=""><path d="M-50.53125 6 C-24.452990421951405 6, 1.6252691560971897 6, 50.53125 6 M-50.53125 6 C-10.431680736074973 6, 29.667888527850053 6, 50.53125 6" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g><g class="divider" style=""><path d="M-50.53125 24 C-12.327213349979438 24, 25.876823300041124 24, 50.53125 24 M-50.53125 24 C-23.852172005077907 24, 2.8269059898441853 24, 50.53125 24" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g></g><g class="node default" id="classId-Hooks-2" transform="translate(195.1484375, 268)"><g class="basic label-container"><path d="M-36.0859375 -42 L36.0859375 -42 L36.0859375 42 L-36.0859375 42" stroke="none" stroke-width="0" fill="transparent" style=""></path><path d="M-36.0859375 -42 C-20.847603795513187 -42, -5.609270091026371 -42, 36.0859375 -42 M-36.0859375 -42 C-18.32751271870368 -42, -0.5690879374073603 -42, 36.0859375 -42 M36.0859375 -42 C36.0859375 -14.21051719124555, 36.0859375 13.5789656175089, 36.0859375 42 M36.0859375 -42 C36.0859375 -10.044677731268212, 36.0859375 21.910644537463575, 36.0859375 42 M36.0859375 42 C13.553389994727983 42, -8.979157510544034 42, -36.0859375 42 M36.0859375 42 C14.505841973319825 42, -7.07425355336035 42, -36.0859375 42 M-36.0859375 42 C-36.0859375 22.762457195548393, -36.0859375 3.524914391096786, -36.0859375 -42 M-36.0859375 42 C-36.0859375 11.587593498503292, -36.0859375 -18.824813002993416, -36.0859375 -42" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g><g class="annotation-group text" transform="translate(0, -18)"></g><g class="label-group text" transform="translate(-24.0859375, -18)"><g class="label" style="font-weight:bolder" transform="translate(0,-12)"><foreignObject width="48.171875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:99px;text-align:center"><span class="nodeLabel markdown-node-label" style=""><p>Hooks</p></span></div></foreignObject></g></g><g class="members-group text" transform="translate(-24.0859375, 30)"></g><g class="methods-group text" transform="translate(-24.0859375, 60)"></g><g class="divider" style=""><path d="M-36.0859375 6 C-8.290327784875608 6, 19.505281930248785 6, 36.0859375 6 M-36.0859375 6 C-8.37930217556298 6, 19.32733314887404 6, 36.0859375 6" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g><g class="divider" style=""><path d="M-36.0859375 24 C-21.09827046850114 24, -6.110603437002279 24, 36.0859375 24 M-36.0859375 24 C-14.340961626144992 24, 7.404014247710016 24, 36.0859375 24" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g></g><g class="node default" id="classId-Skills-3" transform="translate(322.1328125, 268)"><g class="basic label-container"><path d="M-40.8984375 -42 L40.8984375 -42 L40.8984375 42 L-40.8984375 42" stroke="none" stroke-width="0" fill="transparent" style=""></path><path d="M-40.8984375 -42 C-12.984170183174754 -42, 14.930097133650492 -42, 40.8984375 -42 M-40.8984375 -42 C-20.48365135863239 -42, -0.06886521726477923 -42, 40.8984375 -42 M40.8984375 -42 C40.8984375 -18.766508622933642, 40.8984375 4.466982754132715, 40.8984375 42 M40.8984375 -42 C40.8984375 -15.046543680918983, 40.8984375 11.906912638162034, 40.8984375 42 M40.8984375 42 C13.975226111368805 42, -12.94798527726239 42, -40.8984375 42 M40.8984375 42 C19.038095200813338 42, -2.8222470983733245 42, -40.8984375 42 M-40.8984375 42 C-40.8984375 16.24203530454736, -40.8984375 -9.515929390905278, -40.8984375 -42 M-40.8984375 42 C-40.8984375 10.802402032843165, -40.8984375 -20.39519593431367, -40.8984375 -42" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g><g class="annotation-group text" transform="translate(0, -18)"></g><g class="label-group text" transform="translate(-28.8984375, -18)"><g class="label" style="font-weight:bolder" transform="translate(0,-12)"><foreignObject width="57.796875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:91px;text-align:center"><span class="nodeLabel markdown-node-label" style=""><p>Skills</p></span></div></foreignObject></g></g><g class="members-group text" transform="translate(-28.8984375, 30)"></g><g class="methods-group text" transform="translate(-28.8984375, 60)"></g><g class="divider" style=""><path d="M-40.8984375 6 C-11.707010905223271 6, 17.484415689553458 6, 40.8984375 6 M-40.8984375 6 C-13.780945121802983 6, 13.336547256394034 6, 40.8984375 6" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g><g class="divider" style=""><path d="M-40.8984375 24 C-16.463487235110918 24, 7.971463029778164 24, 40.8984375 24 M-40.8984375 24 C-19.668759083785876 24, 1.5609193324282487 24, 40.8984375 24" stroke="2px" stroke-width="1.3" fill="none" stroke-dasharray="0 0" style=""></path></g></g></g></g></g></svg></p>
<p><strong>What they are.</strong> Distributable bundles of commands, hooks, skills, and metadata. Share your setup with teammates or install pre-built configurations.</p>
<p><strong>Basic structure:</strong></p>
<nav class="file-tree astro-htwbjus4" aria-label="File tree"> <ul class="file-tree__list astro-htwbjus4"> <li class="file-tree__item astro-o25vlg2d" style="--level: 0;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">my-plugin</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">.claude-plugin</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d"> <span class="file-tree__icon file-tree__icon--text astro-o25vlg2d" style="color: #F59E0B" aria-hidden="true"> {} </span>   <span class="file-tree__name astro-o25vlg2d">plugin.json</span> <span class="file-tree__comment astro-o25vlg2d">Manifest: name, version, author</span> </span> </li>  </ul> </details>   </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d"> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">commands</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">greet.md</span>  </span> </li>  </ul> </details>   </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d"> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">skills</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;"> <details class="file-tree__folder astro-o25vlg2d"> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">my-skill</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">SKILL.md</span>  </span> </li>  </ul> </details>   </li>  </ul> </details>   </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d"> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">hooks</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d"> <span class="file-tree__icon file-tree__icon--text astro-o25vlg2d" style="color: #F59E0B" aria-hidden="true"> {} </span>   <span class="file-tree__name astro-o25vlg2d">hooks.json</span>  </span> </li>  </ul> </details>   </li>  </ul> </details>   </li>  </ul> </nav> 
<p><strong>When to use.</strong> Share team configurations, <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/building-my-first-claude-code-plugin/" class="internal-link astro-3tyn5ojg"> package domain workflows </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Building My First Claude Code Plugin</span> <span class="preview-description astro-3tyn5ojg">How I built a Claude Code plugin to generate skills, agents, commands, and more—and stopped copy-pasting boilerplate.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">tooling</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 8, 2025</time> </span> </span> </span>  <script>
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
</script>, distribute opinionated patterns, install community tooling.</p>
<p><strong>How it works.</strong> Install a plugin, get instant access. Components merge seamlessly — hooks combine, commands appear in autocomplete, skills activate automatically. Ready to build your own? Check out this <a href="/prompts/claude/claude-create-plugin">plugin creation guide</a>.</p>
<hr/>
<h2 id="4-agent-skills--automatic-task-driven-capabilities">4) Agent Skills — automatic, task-driven capabilities<a class="heading-link" aria-label="Link to section" href="#4-agent-skills--automatic-task-driven-capabilities"><span class="heading-link-icon">#</span></a></h2>
<p><svg id="mermaid-5" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:501.59375px" viewBox="0 0 501.59375 606" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-5{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-5 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-5 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-5 .error-icon{fill:#a44141;}#mermaid-5 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-5 .edge-thickness-normal{stroke-width:1px;}#mermaid-5 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-5 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-5 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-5 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-5 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-5 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-5 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-5 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-5 p{margin:0;}#mermaid-5 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-5 .cluster-label text{fill:#F9FFFE;}#mermaid-5 .cluster-label span{color:#F9FFFE;}#mermaid-5 .cluster-label span p{background-color:transparent;}#mermaid-5 .label text,#mermaid-5 span{fill:#ccc;color:#ccc;}#mermaid-5 .node rect,#mermaid-5 .node circle,#mermaid-5 .node ellipse,#mermaid-5 .node polygon,#mermaid-5 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-5 .rough-node .label text,#mermaid-5 .node .label text,#mermaid-5 .image-shape .label,#mermaid-5 .icon-shape .label{text-anchor:middle;}#mermaid-5 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-5 .rough-node .label,#mermaid-5 .node .label,#mermaid-5 .image-shape .label,#mermaid-5 .icon-shape .label{text-align:center;}#mermaid-5 .node.clickable{cursor:pointer;}#mermaid-5 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-5 .arrowheadPath{fill:lightgrey;}#mermaid-5 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-5 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-5 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-5 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-5 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-5 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-5 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-5 .cluster text{fill:#F9FFFE;}#mermaid-5 .cluster span{color:#F9FFFE;}#mermaid-5 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-5 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-5 rect.text{fill:none;stroke-width:0;}#mermaid-5 .icon-shape,#mermaid-5 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-5 .icon-shape p,#mermaid-5 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-5 .icon-shape rect,#mermaid-5 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-5 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-5 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-5 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-5_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-5_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-5_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-5_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-5_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-5_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M95.797,86L95.797,94.167C95.797,102.333,95.797,118.667,103.913,130.713C112.029,142.758,128.26,150.517,136.376,154.396L144.492,158.275" id="L_Ctx_Match_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Ctx_Match_0" data-points="W3sieCI6OTUuNzk2ODc1LCJ5Ijo4Nn0seyJ4Ijo5NS43OTY4NzUsInkiOjEzNX0seyJ4IjoxNDguMTAwOTUyMTQ4NDM3NSwieSI6MTYwfV0=" marker-end="url(#mermaid-5_flowchart-v2-pointEnd)"></path><path d="M363.594,110L363.594,114.167C363.594,118.333,363.594,126.667,355.478,134.713C347.362,142.758,331.13,150.517,323.014,154.396L314.899,158.275" id="L_Skills_Match_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Skills_Match_0" data-points="W3sieCI6MzYzLjU5Mzc1LCJ5IjoxMTB9LHsieCI6MzYzLjU5Mzc1LCJ5IjoxMzV9LHsieCI6MzExLjI4OTY3Mjg1MTU2MjUsInkiOjE2MH1d" marker-end="url(#mermaid-5_flowchart-v2-pointEnd)"></path><path d="M187.065,238L180.324,244.167C173.584,250.333,160.102,262.667,153.362,274.333C146.621,286,146.621,297,146.621,302.5L146.621,308" id="L_Match_Tools_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Match_Tools_0" data-points="W3sieCI6MTg3LjA2NTEyMTI5OTM0MjEsInkiOjIzOH0seyJ4IjoxNDYuNjIxMDkzNzUsInkiOjI3NX0seyJ4IjoxNDYuNjIxMDkzNzUsInkiOjMxMn1d" marker-end="url(#mermaid-5_flowchart-v2-pointEnd)"></path><path d="M133.258,366L130.206,372.167C127.154,378.333,121.049,390.667,117.997,402.333C114.945,414,114.945,425,114.945,430.5L114.945,436" id="L_Tools_Exec_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Tools_Exec_0" data-points="W3sieCI6MTMzLjI1Nzg3MzUzNTE1NjI1LCJ5IjozNjZ9LHsieCI6MTE0Ljk0NTMxMjUsInkiOjQwM30seyJ4IjoxMTQuOTQ1MzEyNSwieSI6NDQwfV0=" marker-end="url(#mermaid-5_flowchart-v2-pointEnd)"></path><path d="M183.033,366L191.349,372.167C199.665,378.333,216.297,390.667,232.09,402.593C247.883,414.52,262.835,426.039,270.312,431.799L277.788,437.559" id="L_Tools_Pass_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Tools_Pass_0" data-points="W3sieCI6MTgzLjAzMjUzMTczODI4MTI1LCJ5IjozNjZ9LHsieCI6MjMyLjkyOTY4NzUsInkiOjQwM30seyJ4IjoyODAuOTU2OTcwMjE0ODQzNzUsInkiOjQ0MH1d" marker-end="url(#mermaid-5_flowchart-v2-pointEnd)"></path><path d="M287.768,238L296.951,244.167C306.133,250.333,324.498,262.667,333.681,279.5C342.863,296.333,342.863,317.667,342.863,339C342.863,360.333,342.863,381.667,340.533,397.885C338.203,414.104,333.543,425.208,331.213,430.76L328.883,436.312" id="L_Match_Pass_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Match_Pass_0" data-points="W3sieCI6Mjg3Ljc2ODM0OTA5NTM5NDc0LCJ5IjoyMzh9LHsieCI6MzQyLjg2MzI4MTI1LCJ5IjoyNzV9LHsieCI6MzQyLjg2MzI4MTI1LCJ5IjozMzl9LHsieCI6MzQyLjg2MzI4MTI1LCJ5Ijo0MDN9LHsieCI6MzI3LjMzNTIwNTA3ODEyNSwieSI6NDQwfV0=" marker-end="url(#mermaid-5_flowchart-v2-pointEnd)"></path><path d="M114.945,494L114.945,498.167C114.945,502.333,114.945,510.667,123.533,518.725C132.12,526.783,149.295,534.566,157.883,538.457L166.47,542.349" id="L_Exec_Out_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Exec_Out_0" data-points="W3sieCI6MTE0Ljk0NTMxMjUsInkiOjQ5NH0seyJ4IjoxMTQuOTQ1MzEyNSwieSI6NTE5fSx7IngiOjE3MC4xMTM1ODE3MzA3NjkyMywieSI6NTQ0fV0=" marker-end="url(#mermaid-5_flowchart-v2-pointEnd)"></path><path d="M316.004,494L316.004,498.167C316.004,502.333,316.004,510.667,309.659,518.656C303.314,526.645,290.625,534.29,284.28,538.113L277.936,541.936" id="L_Pass_Out_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Pass_Out_0" data-points="W3sieCI6MzE2LjAwMzkwNjI1LCJ5Ijo0OTR9LHsieCI6MzE2LjAwMzkwNjI1LCJ5Ijo1MTl9LHsieCI6Mjc0LjUwOTM5MDAyNDAzODQ1LCJ5Ijo1NDR9XQ==" marker-end="url(#mermaid-5_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_Ctx_Match_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Skills_Match_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(146.62109375, 275)"><g class="label" data-id="L_Match_Tools_0" transform="translate(-14.453125, -12)"><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>yes</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(114.9453125, 403)"><g class="label" data-id="L_Tools_Exec_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>ok</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(232.9296875, 403)"><g class="label" data-id="L_Tools_Pass_0" transform="translate(-33.71875, -12)"><foreignObject width="67.4375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>blocked</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(342.86328125, 339)"><g class="label" data-id="L_Match_Pass_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>no</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Exec_Out_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Pass_Out_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-Ctx-0" transform="translate(95.796875, 59)"><rect class="basic label-container" style="" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Task context</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Match-1" transform="translate(229.6953125, 199)"><rect class="basic label-container" style="" x="-97.4296875" y="-39" width="194.859375" height="78"></rect><g class="label" style="" transform="translate(-67.4296875, -24)"><rect></rect><foreignObject width="134.859375" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Match SKILL.md<br/>description?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Skills-2" transform="translate(363.59375, 59)"><rect class="basic label-container" style="" x="-130" y="-51" width="260" height="102"></rect><g class="label" style="" transform="translate(-100, -36)"><rect></rect><foreignObject width="200" height="72"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Available skills<br/>(personal / project / plugin)</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Tools-5" transform="translate(146.62109375, 339)"><rect class="basic label-container" style="" x="-121.515625" y="-27" width="243.03125" height="54"></rect><g class="label" style="" transform="translate(-91.515625, -12)"><rect></rect><foreignObject width="183.03125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Check allowed-tools</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Exec-7" transform="translate(114.9453125, 467)"><rect class="basic label-container" style="" x="-73.3515625" y="-27" width="146.703125" height="54"></rect><g class="label" style="" transform="translate(-43.3515625, -12)"><rect></rect><foreignObject width="86.703125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Run skill</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Pass-9" transform="translate(316.00390625, 467)"><rect class="basic label-container" style="" x="-49.265625" y="-27" width="98.53125" height="54"></rect><g class="label" style="" transform="translate(-19.265625, -12)"><rect></rect><foreignObject width="38.53125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Skip</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Out-13" transform="translate(229.6953125, 571)"><rect class="basic label-container" style="" x="-92.6171875" y="-27" width="185.234375" height="54"></rect><g class="label" style="" transform="translate(-62.6171875, -12)"><rect></rect><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Return result</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<p><strong>What they are.</strong> Folders with <code>SKILL.md</code> descriptors plus optional scripts. Unlike slash commands, skills activate <strong>automatically</strong> when their description matches the task context.</p>
<p><strong>How Claude discovers them.</strong> When you give Claude a task, it reviews available skill descriptions to find relevant ones. If a skill’s <code>description</code> field matches the task context, Claude loads the full skill instructions and applies them. This happens transparently — you never explicitly invoke skills.</p>
<div class="alert alert-info astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl"></span> Official Example Skills </p> <div class="alert-content astro-7kdbuayl"> <p>Check out the <a href="https://github.com/anthropics/skills" rel="noopener noreferrer" target="_blank">official Anthropic skills
repository</a> for ready-to-use examples.</p> </div> </div> 
<blockquote>
<p>Claude Skills are awesome, maybe a bigger deal than MCP</p>
<p>— Simon Willison, <a href="https://simonwillison.net/2025/Oct/16/claude-skills/" rel="noopener noreferrer" target="_blank">Claude Skills are awesome, maybe a bigger deal than MCP</a></p>
</blockquote>
<div class="alert alert-tip astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💪</span> Advanced Skills: Superpowers Library </p> <div class="alert-content astro-7kdbuayl"> <p>Want rigorous, spec-driven development? Check out <a href="https://github.com/obra/superpowers" rel="noopener noreferrer" target="_blank">obra’s superpowers</a> — a comprehensive skills library that enforces systematic workflows.</p><p><strong>What it provides:</strong> TDD workflows (RED-GREEN-REFACTOR), systematic debugging, code review processes, git worktree management, and brainstorming frameworks. Each skill pushes you toward verification-based development instead of “trust me, it works.”</p><p><strong>The philosophy:</strong> Test before implementation. Verify with evidence. Debug systematically through four phases. Plan before coding. No shortcuts.</p><p>These skills work together to prevent common mistakes. The brainstorming skill activates before implementation. The TDD skill enforces writing tests first. The verification skill blocks completion claims without proof.</p><p><strong>Use when:</strong> You want Claude to be more disciplined about development practices, especially for production code.</p> </div> </div> 
<p><strong>Where to put them:</strong></p>
<ul>
<li><code>~/.claude/skills/</code> — personal, all projects</li>
<li><code>.claude/skills/</code> — project-specific</li>
<li>Inside plugins — distributable</li>
</ul>
<p><strong>What you need:</strong></p>
<ul>
<li><code>SKILL.md</code> with frontmatter (<code>name</code>, <code>description</code>)</li>
<li>Optional <code>allowed-tools</code> declaration</li>
<li>Optional helper scripts</li>
</ul>
<p>Want to create your own skill? Use this <a href="/prompts/claude/claude-create-skill">skill creation guide</a>.</p>
<p><strong>Why they’re powerful.</strong> Skills package expertise Claude applies automatically. Style enforcement, doc updates, test hygiene, framework patterns — all without manual triggering.</p>
<p><strong>Skills vs CLAUDE.md.</strong> Think of skills as modular chunks of a CLAUDE.md file. Instead of Claude reviewing a massive document every time, skills let Claude access specific expertise only when needed. This improves context efficiency while maintaining automatic behavior.</p>
<p><strong>Key difference.</strong> Skills are “always on.” Claude activates them based on context. Commands require manual invocation.</p>
<div class="alert alert-caution astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">🚨</span> Skills vs Commands: The Gray Area </p> <div class="alert-content astro-7kdbuayl"> <p>Some workflows could be either a skill or a command. Example: git worktree management.</p><p><strong>Make it a skill if:</strong> You want Claude to automatically consider git worktrees whenever relevant to the conversation.</p><p><strong>Make it a command if:</strong> You want explicit control over when worktree logic runs (e.g., <code>/create-worktree feature-branch</code>).</p><p>The overlap is real — choose based on whether you prefer automatic activation or manual control.</p> </div> </div> 
<div class="alert alert-info astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl"></span> Automatic vs Manual Triggering </p> <div class="alert-content astro-7kdbuayl"> <p><strong>Subagents and Skills activate automatically</strong> when Claude determines they’re relevant to the task. You don’t need to invoke them manually — Claude uses them proactively when it thinks they’re useful.</p><p><strong>Slash commands require manual triggering</strong> — you type <code>/command-name</code> to run them.</p><p>This is the fundamental difference: automation vs explicit control.</p> </div> </div> 
<hr/>
<h2 id="putting-it-all-together">Putting it all together<a class="heading-link" aria-label="Link to section" href="#putting-it-all-together"><span class="heading-link-icon">#</span></a></h2>
<p>Here’s how these features work together in practice:</p>
<ol>
<li><strong>Memory (<code>CLAUDE.md</code>)</strong> — Establish project context and conventions that Claude always knows</li>
<li><strong>Slash commands</strong> — Create explicit shortcuts for workflows you want to trigger on demand</li>
<li><strong>Subagents</strong> — Offload parallel or isolated work to specialized agents</li>
<li><strong>Hooks</strong> — Enforce rules and automate repetitive actions at key lifecycle events</li>
<li><strong>Plugins</strong> — Package and distribute your entire setup to others</li>
<li><strong>MCP</strong> — Connect external systems and make their capabilities available as commands</li>
<li><strong>Skills</strong> — Define automatic behaviors that activate based on task context</li>
</ol>
<h3 id="example-a-task-based-development-workflow">Example: A Task-Based Development Workflow<a class="heading-link" aria-label="Link to section" href="#example-a-task-based-development-workflow"><span class="heading-link-icon">#</span></a></h3>
<p>Here’s a real-world workflow that combines multiple features:</p>
<p><strong>Setup phase:</strong></p>
<ul>
<li><code>CLAUDE.md</code> contains implementation standards (“don’t commit until I approve”, “write tests first”)</li>
<li><code>/load-context</code> slash command initializes new chats with project state</li>
<li><code>update-documentation</code> skill activates automatically after implementations</li>
<li>Hook triggers linting after file edits</li>
</ul>
<p><strong>Planning phase (Chat 1):</strong></p>
<ul>
<li>Main agent plans bug fix or new feature</li>
<li>Outputs detailed task file with approach</li>
</ul>
<p><strong>Implementation phase (Chat 2):</strong></p>
<ul>
<li>Start fresh context with <code>/load-context</code></li>
<li>Feed in the plan from Chat 1</li>
<li>Implementation subagent executes the plan</li>
<li><code>update-documentation</code> skill updates docs automatically</li>
<li><code>/resolve-task</code> command marks task complete</li>
</ul>
<p><strong>Why this works:</strong> Main context stays focused on planning. Heavy implementation work happens in isolated context. Skills handle documentation. Hooks enforce quality standards. No context pollution.</p>
<h2 id="decision-guide-choosing-the-right-tool">Decision guide: choosing the right tool<a class="heading-link" aria-label="Link to section" href="#decision-guide-choosing-the-right-tool"><span class="heading-link-icon">#</span></a></h2>
<div class="alert alert-info astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl"></span> Community Resource: Claude Code Driver Repository </p> <div class="alert-content astro-7kdbuayl"> <p>🎉 <strong>Huge thanks to <a href="https://github.com/thewiredbear" rel="noopener noreferrer" target="_blank">@thewiredbear</a></strong> for creating the <a href="https://github.com/thewiredbear/Claude_Code_Driver/" rel="noopener noreferrer" target="_blank">Claude Code Driver</a> repository! This community-driven collection includes examples, templates, and resources based on this guide. Perfect for getting started quickly or finding inspiration for your own Claude Code setup. Check it out and contribute your own patterns!</p> </div> </div> 
<div class="alert alert-info astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl"></span> Quick Reference Cheat Sheet </p> <div class="alert-content astro-7kdbuayl"> <p>For a comprehensive visual guide to all Claude Code features, check out the
<a href="https://awesomeclaude.ai/code-cheatsheet" rel="noopener noreferrer" target="_blank">Awesome Claude Code Cheat Sheet</a>.</p> </div> </div> 
<div class="alert alert-tip astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💪</span> Customize Your Terminal </p> <div class="alert-content astro-7kdbuayl"> <p>Want model name, context usage, and cost displayed in your terminal? See how to <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/customize_claude_code_status_line/" class="internal-link astro-3tyn5ojg"> customize your Claude Code status line </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Customize Your Claude Code Status Line</span> <span class="preview-description astro-3tyn5ojg">Learn how to display model name, context usage, and cost directly in your terminal while using Claude Code. A step-by-step guide to creating custom status line scripts.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">tooling</span>  </span> <time class="preview-date astro-3tyn5ojg">Dec 14, 2025</time> </span> </span> </span>  <script>
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
</script>.</p> </div> </div> 
<aside aria-label="Quick Reference" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> Quick Reference </p> <section class="aside-body astro-37uy2q7c"> <ul>
<li><strong>Use <code>CLAUDE.md</code></strong> to define lasting project context — architecture, conventions, and patterns Claude should always remember. Best for: static knowledge that rarely changes.</li>
<li><strong>Use <span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/claude-code-slash-commands-guide/" class="internal-link astro-3tyn5ojg"> Slash Commands </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Speed Up Your Claude Code Experience with Slash Commands</span> <span class="preview-description astro-3tyn5ojg">Learn how to transform Claude Code from a chatbot into a deterministic engine using Slash Commands. This guide covers the technical setup and a complete &#39;Full Circle&#39; workflow that automates your entire feature lifecycle.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">claude-code</span>  </span> <time class="preview-date astro-3tyn5ojg">Nov 22, 2025</time> </span> </span> </span>  <script>
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
</script></strong> for explicit, repeatable workflows you want to trigger manually. Best for: workflow automation, user-initiated actions.</li>
<li><strong>Use Subagents</strong> when you need parallel execution or want to isolate heavy computational work. Best for: preventing context pollution, specialized deep dives.</li>
<li><strong>Use Hooks</strong> to automatically enforce standards or react to specific events. Best for: quality gates, automatic actions tied to tool usage.</li>
<li><strong>Use Plugins</strong> to package and share complete configurations across teams or projects. Best for: team standardization, distributing opinionated setups.</li>
<li><strong>Use MCP</strong> to integrate external systems and expose their capabilities as native commands. Best for: connecting databases, APIs, third-party tools.</li>
<li><strong>Use Skills</strong> for automatic, context-driven behaviors that should apply without manual invocation. Best for: automated context provision, “always on” expertise.</li>
</ul> </section> </div> </aside> 
<h3 id="feature-comparison">Feature comparison<a class="heading-link" aria-label="Link to section" href="#feature-comparison"><span class="heading-link-icon">#</span></a></h3>
<div class="alert alert-info astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl"></span> Source </p> <div class="alert-content astro-7kdbuayl"> <p>This comparison table is adapted from <a href="https://www.youtube.com/watch?v=kFpLzCVLA20&t=1027s" rel="noopener noreferrer" target="_blank">IndyDevDan’s video “I finally CRACKED
Claude Agent Skills”</a>.</p> </div> </div> 
































































































<table><thead><tr><th>Category</th><th>Skill</th><th>MCP</th><th>Subagent</th><th>Slash Command</th></tr></thead><tbody><tr><td data-label="Category">Triggered By</td><td data-label="Skill">Agent</td><td data-label="MCP">Both</td><td data-label="Subagent">Both</td><td data-label="Slash Command">Engineer</td></tr><tr><td data-label="Category">Context Efficiency</td><td data-label="Skill">High</td><td data-label="MCP">Low</td><td data-label="Subagent">High</td><td data-label="Slash Command">High</td></tr><tr><td data-label="Category">Context Persistence</td><td data-label="Skill">✅</td><td data-label="MCP">✅</td><td data-label="Subagent">✅</td><td data-label="Slash Command">✅</td></tr><tr><td data-label="Category">Parallelizable</td><td data-label="Skill">❌</td><td data-label="MCP">❌</td><td data-label="Subagent">❌</td><td data-label="Slash Command">❌</td></tr><tr><td data-label="Category">Specializable</td><td data-label="Skill">✅</td><td data-label="MCP">✅</td><td data-label="Subagent">✅</td><td data-label="Slash Command">✅</td></tr><tr><td data-label="Category">Sharable</td><td data-label="Skill">✅</td><td data-label="MCP">✅</td><td data-label="Subagent">✅</td><td data-label="Slash Command">✅</td></tr><tr><td data-label="Category">Modularity</td><td data-label="Skill">High</td><td data-label="MCP">High</td><td data-label="Subagent">Mid</td><td data-label="Slash Command">Mid</td></tr><tr><td data-label="Category">Tool Permissions</td><td data-label="Skill">✅</td><td data-label="MCP">❌</td><td data-label="Subagent">✅</td><td data-label="Slash Command">✅</td></tr><tr><td data-label="Category">Can Use Prompts</td><td data-label="Skill">✅</td><td data-label="MCP">✅</td><td data-label="Subagent">✅</td><td data-label="Slash Command">✅</td></tr><tr><td data-label="Category">Can Use Skills</td><td data-label="Skill">✅</td><td data-label="MCP">Kind of</td><td data-label="Subagent">✅</td><td data-label="Slash Command">✅</td></tr><tr><td data-label="Category">Can Use MCP Servers</td><td data-label="Skill">✅</td><td data-label="MCP">✅</td><td data-label="Subagent">✅</td><td data-label="Slash Command">✅</td></tr><tr><td data-label="Category">Can Use Subagents</td><td data-label="Skill">✅</td><td data-label="MCP">✅</td><td data-label="Subagent">✅</td><td data-label="Slash Command">❌</td></tr></tbody></table>
<h3 id="real-world-examples">Real-world examples<a class="heading-link" aria-label="Link to section" href="#real-world-examples"><span class="heading-link-icon">#</span></a></h3>


























































































<table><thead><tr><th>Use Case</th><th>Best Tool</th><th>Why</th></tr></thead><tbody><tr><td data-label="Use Case">”Always use Pinia for state management in Vue apps”</td><td data-label="Best Tool"><code>CLAUDE.md</code></td><td data-label="Why">Persistent context that applies to all conversations</td></tr><tr><td data-label="Use Case">Generate standardized commit messages</td><td data-label="Best Tool">Slash Command</td><td data-label="Why">Explicit action you trigger when ready to commit</td></tr><tr><td data-label="Use Case">Check Jira tickets and analyze security simultaneously</td><td data-label="Best Tool">Subagents</td><td data-label="Why">Parallel execution with isolated contexts</td></tr><tr><td data-label="Use Case">Run linter after every file edit</td><td data-label="Best Tool">Hook</td><td data-label="Why">Automatic reaction to lifecycle event</td></tr><tr><td data-label="Use Case">Share your team’s Vue testing patterns</td><td data-label="Best Tool">Plugin</td><td data-label="Why">Distributable package with commands + skills</td></tr><tr><td data-label="Use Case">Query PostgreSQL database for reports</td><td data-label="Best Tool">MCP</td><td data-label="Why">External system integration</td></tr><tr><td data-label="Use Case"><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-i-use-claude-code-for-doing-seo-audits/" class="internal-link astro-3tyn5ojg"> Run automated SEO audits with browser testing </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How I Use Claude Code for Doing SEO Audits</span> <span class="preview-description astro-3tyn5ojg">Learn how to leverage Claude Code with Puppeteer MCP to perform comprehensive SEO audits in minutes, complete with automated analysis and actionable reports.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">seo</span>  </span> <time class="preview-date astro-3tyn5ojg">Jun 26, 2025</time> </span> </span> </span>  <script>
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
</script></td><td data-label="Best Tool">MCP</td><td data-label="Why">External system integration</td></tr><tr><td data-label="Use Case">Detect style guide violations during any edit</td><td data-label="Best Tool">Skill</td><td data-label="Why">Automatic behavior based on task context</td></tr><tr><td data-label="Use Case">Create React components from templates</td><td data-label="Best Tool">Slash Command</td><td data-label="Why">Manual workflow with repeatable structure</td></tr><tr><td data-label="Use Case">”Never use <code>any</code> type in TypeScript”</td><td data-label="Best Tool">Hook</td><td data-label="Why">Automatic enforcement after code changes</td></tr><tr><td data-label="Use Case">Auto-format code on save</td><td data-label="Best Tool">Hook</td><td data-label="Why">Event-driven automation</td></tr><tr><td data-label="Use Case">Connect to GitHub for issue management</td><td data-label="Best Tool">MCP</td><td data-label="Why">External API integration</td></tr><tr><td data-label="Use Case">Run comprehensive test suite in parallel</td><td data-label="Best Tool">Subagent</td><td data-label="Why">Isolated, resource-intensive work</td></tr><tr><td data-label="Use Case">Deploy to staging environment</td><td data-label="Best Tool">Slash Command</td><td data-label="Why">Manual trigger with safeguards</td></tr><tr><td data-label="Use Case"><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/custom-tdd-workflow-claude-code-vue/" class="internal-link astro-3tyn5ojg"> Enforce TDD workflow automatically </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Forcing Claude Code to TDD: An Agentic Red-Green-Refactor Loop</span> <span class="preview-description astro-3tyn5ojg">Build a custom TDD workflow with Claude Code using skills and subagents that enforce Red-Green-Refactor discipline for your Vue projects.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 30, 2025</time> </span> </span> </span>  <script>
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
</script></td><td data-label="Best Tool">Skill</td><td data-label="Why">Context-aware automatic behavior</td></tr><tr><td data-label="Use Case">Initialize new projects with team standards</td><td data-label="Best Tool">Plugin</td><td data-label="Why">Shareable, complete configuration</td></tr></tbody></table> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_understanding-claude-code-full-stack" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="understanding-claude-code-full-stack" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/claude-code/" class="
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
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/mcp/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">mcp</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/productivity/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-5"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">productivity</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/tooling/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-6"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">tooling</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/understanding-claude-code-full-stack/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/understanding-claude-code-full-stack/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/understanding-claude-code-full-stack/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/understanding-claude-code-full-stack/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/understanding-claude-code-full-stack/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/understanding-claude-code-full-stack/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/understanding-claude-code-full-stack/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/how-i-use-claude-code-for-doing-seo-audits/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How I Use Claude Code for Doing SEO Audits</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to leverage Claude Code with Puppeteer MCP to perform comprehensive SEO audits in minutes, complete with automated analysis and actionable reports. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-06-26T00:00:00.000Z">Jun 26, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> ai </span> </div> </div> </a><a href="/posts/what-is-model-context-protocol-mcp/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">What Is the Model Context Protocol (MCP)? How It Works</h3> <p class="related-post-description astro-vj4tpspi"> Learn how MCP (Model Context Protocol) standardizes AI tool integration, enabling LLMs to interact with external services, databases, and APIs through a universal protocol similar to USB-C for AI applications. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-08-10T00:00:00.000Z">Aug 10, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> mcp </span> </div> </div> </a><a href="/posts/building-my-first-claude-code-plugin/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Building My First Claude Code Plugin</h3> <p class="related-post-description astro-vj4tpspi"> How I built a Claude Code plugin to generate skills, agents, commands, and more—and stopped copy-pasting boilerplate. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-11-08T00:00:00.000Z">Nov 8, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> claude-code </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "understanding-claude-code-full-stack";

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
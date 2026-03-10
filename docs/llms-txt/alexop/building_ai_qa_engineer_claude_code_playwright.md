# Source: https://alexop.dev/posts/building_ai_qa_engineer_claude_code_playwright

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/building_ai_qa_engineer_claude_code_playwright/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Building an AI QA Engineer with Claude Code and Playwright MCP | alexop.dev</title><meta name="title" content="Building an AI QA Engineer with Claude Code and Playwright MCP | alexop.dev"><meta name="description" content="Learn how to build an automated QA engineer using Claude Code and Playwright MCP that tests your web app like a real user, runs on every pull request, and writes detailed bug reports."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Building an AI QA Engineer with Claude Code and Playwright MCP | alexop.dev"><meta property="og:description" content="Learn how to build an automated QA engineer using Claude Code and Playwright MCP that tests your web app like a real user, runs on every pull request, and writes detailed bug reports."><meta property="og:url" content="https://alexop.dev/posts/building_ai_qa_engineer_claude_code_playwright/"><meta property="og:image" content="https://alexop.dev/posts/building-an-ai-qa-engineer-with-claude-code-and-playwright-mcp/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-12-13T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/building_ai_qa_engineer_claude_code_playwright/"><meta property="twitter:title" content="Building an AI QA Engineer with Claude Code and Playwright MCP | alexop.dev"><meta property="twitter:description" content="Learn how to build an automated QA engineer using Claude Code and Playwright MCP that tests your web app like a real user, runs on every pull request, and writes detailed bug reports."><meta property="twitter:image" content="https://alexop.dev/posts/building-an-ai-qa-engineer-with-claude-code-and-playwright-mcp/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Building an AI QA Engineer with Claude Code and Playwright MCP | alexop.dev","description":"Learn how to build an automated QA engineer using Claude Code and Playwright MCP that tests your web app like a real user, runs on every pull request, and writes detailed bug reports.","image":"https://alexop.dev/posts/building-an-ai-qa-engineer-with-claude-code-and-playwright-mcp/index.png","datePublished":"2025-12-13T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: building-an-ai-qa-engineer-with-claude-code-and-playwright-mcp; }@layer astro { ::view-transition-old(building-an-ai-qa-engineer-with-claude-code-and-playwright-mcp) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(building-an-ai-qa-engineer-with-claude-code-and-playwright-mcp) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(building-an-ai-qa-engineer-with-claude-code-and-playwright-mcp) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(building-an-ai-qa-engineer-with-claude-code-and-playwright-mcp) { 
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
</style><style>.internal-link-wrapper:where(.astro-3tyn5ojg){position:relative;display:inline-block}.internal-link:where(.astro-3tyn5ojg){--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));text-decoration-line:underline;text-decoration-style:dashed;text-decoration-thickness:1px;text-underline-offset:4px;transition-property:all;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.15s}.internal-link:where(.astro-3tyn5ojg):hover{text-decoration-style:solid}.internal-link:where(.astro-3tyn5ojg){cursor:pointer;display:inline}.preview-card:where(.astro-3tyn5ojg){display:block;position:absolute;bottom:calc(100% + 8px);left:50%;transform:translate(-50%);z-index:9999;width:320px;max-width:90vw;border-radius:.5rem;border-width:1px;--tw-border-opacity: 1;border-color:rgba(var(--color-border),var(--tw-border-opacity, 1));--tw-bg-opacity: 1;background-color:rgba(var(--color-card),var(--tw-bg-opacity, 1));--tw-shadow: 0 10px 15px -3px rgb(0 0 0 / .1), 0 4px 6px -4px rgb(0 0 0 / .1);--tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000),var(--tw-ring-shadow, 0 0 #0000),var(--tw-shadow);opacity:0;visibility:hidden;transition:opacity .2s ease-in-out,visibility .2s ease-in-out}.preview-card:where(.astro-3tyn5ojg).is-fixed{position:fixed!important;bottom:auto!important;top:var(--pc-top, 0px)!important;left:var(--pc-left, 0px)!important;transform:none!important}.preview-content:where(.astro-3tyn5ojg){display:block;padding:1rem}.preview-title:where(.astro-3tyn5ojg){display:block;margin-bottom:.5rem;font-size:1rem;line-height:1.5rem;font-weight:600;--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1));line-height:1.3}.preview-title:where(.astro-3tyn5ojg) .heading-link:where(.astro-3tyn5ojg){display:none!important}.preview-description:where(.astro-3tyn5ojg){display:block;margin-bottom:.75rem;font-size:.875rem;line-height:1.25rem;color:rgba(var(--color-text-base),.8);line-height:1.4;overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical}.preview-tags:where(.astro-3tyn5ojg){margin-bottom:.5rem;display:flex;flex-wrap:wrap;gap:.375rem}.preview-tag:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;background-color:rgba(var(--color-accent),.1);--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));font-weight:500}.preview-tag-more:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;--tw-bg-opacity: 1;background-color:rgba(var(--color-fill),var(--tw-bg-opacity, 1));color:rgba(var(--color-text-base),.6);font-weight:500}.preview-date:where(.astro-3tyn5ojg){font-size:.75rem;line-height:1rem;color:rgba(var(--color-text-base),.6);display:block;margin-top:8px;font-style:italic}.preview-card:where(.astro-3tyn5ojg):after{content:"";position:absolute;top:100%;left:50%;transform:translate(-50%);border:6px solid transparent;border-top-color:var(--color-card)}.preview-card:where(.astro-3tyn5ojg).is-fixed:after{display:none}
</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: ai; }@layer astro { ::view-transition-old(ai) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: claude-code; }@layer astro { ::view-transition-old(claude-code) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-5"] { view-transition-name: automation; }@layer astro { ::view-transition-old(automation) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(automation) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(automation) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(automation) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Building an AI QA Engineer with Claude Code and Playwright MCP</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-12-13T00:00:00.000Z">Dec 13, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="1e0UA6" prefix="r3" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Building an AI QA Engineer with Claude Code and Playwright MCP&quot;],&quot;content&quot;:[0,&quot;import Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\nimport Aside from \&quot;@features/mdx-components/components/Aside.astro\&quot;;\nimport InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\nimport Figure from \&quot;@features/mdx-components/components/Figure.astro\&quot;;\nimport claudeAiImage from \&quot;@assets/images/claude/CLAUDEAI.png\&quot;;\nimport claudeQaWorkflow from \&quot;@assets/images/claude/claudeQaWorkflow.png\&quot;;\n\n&lt;Figure src={claudeAiImage} alt=\&quot;AI QA Engineer with Claude Code and Playwright\&quot; size=\&quot;large\&quot; /&gt;\n\n## Quick Summary\n\n- Build an AI-powered QA engineer that tests your app through the browser like a real user\n- Use Claude Code with Playwright MCP to automate browser interactions\n- Run automated QA on every pull request via GitHub Actions\n- Get detailed bug reports with screenshots posted directly to your PRs\n\n## Table of Contents\n\n## Introduction\n\nManual testing gets old fast. Clicking through your app after every change, checking if forms still work, making sure nothing breaks on mobile—it&#39;s tedious work that most developers avoid.\n\nSo I built an AI that does it for me.\n\nMeet **Quinn**, my automated QA engineer. Quinn tests my app like a real person would. It clicks buttons. It fills forms with weird inputs. It resizes the browser to check mobile layouts. And it writes detailed bug reports.\n\nThe best part? Quinn runs automatically every time I open a pull request.\n\n&lt;Figure src={claudeQaWorkflow} alt=\&quot;Claude QA workflow: Developer opens PR, GitHub Actions triggers workflow, Claude Code tests via Playwright, QA report posted back to PR\&quot; caption=\&quot;The automated QA workflow\&quot; size=\&quot;large\&quot; /&gt;\n\n## The secret sauce: Claude Code + Playwright\n\nTwo tools make this possible:\n\n**Claude Code** is Anthropic&#39;s coding assistant. It can run commands, create files, and—here&#39;s the magic—control a web browser.\n\n**Playwright** is a browser automation tool. It can click, type, take screenshots, and do anything a human can do in a browser.\n\nWhen you combine them through the &lt;InternalLink slug=\&quot;what-is-model-context-protocol-mcp\&quot;&gt;Model Context Protocol (MCP)&lt;/InternalLink&gt;, Claude can literally browse your app like a real user.\n\n&lt;Aside type=\&quot;info\&quot; title=\&quot;What is MCP?\&quot;&gt;\n  MCP (Model Context Protocol) standardizes how AI tools connect to external services. Think of it as USB-C for AI—one universal way to connect tools like Playwright, databases, or APIs to any LLM. Learn more in my &lt;InternalLink slug=\&quot;what-is-model-context-protocol-mcp\&quot;&gt;MCP deep dive&lt;/InternalLink&gt;.\n&lt;/Aside&gt;\n\n## Step 1: Give Claude a personality\n\nI didn&#39;t want a boring test robot. I wanted a QA engineer with opinions.\n\nSo I created a prompt file that gives Claude a backstory:\n\n```markdown\n# QA Engineer Identity\n\nYou are **Quinn**, a veteran QA engineer with 12 years\nof experience breaking software. You&#39;ve seen it all -\napps that crash on empty input, forms that lose data,\nbuttons that do nothing.\n\n## Your Philosophy\n\n- **Trust nothing.** Developers say it works? Prove it.\n- **Users are creative.** They&#39;ll do things no one anticipated.\n- **Edge cases are where bugs hide.** The happy path is boring.\n```\n\nThis isn&#39;t just for fun. The personality makes Claude test more thoroughly. Quinn doesn&#39;t just check if buttons work—Quinn tries to *break* things.\n\nI also gave Quinn strict rules:\n\n```markdown\n## Non-Negotiable Rules\n\n1. **UI ONLY.** You interact through the browser like a\n   real user. You cannot read source code.\n\n2. **SCREENSHOT BUGS.** Every bug gets a screenshot.\n\n3. **CONTINUE AFTER BUGS.** Finding a bug is not the end.\n   Document it, then KEEP TESTING.\n\n4. **MOBILE MATTERS.** Always test mobile viewport (375x667).\n```\n\n## Step 2: Create the GitHub Action\n\nGitHub Actions are like little robots that run tasks for you. They trigger when something happens (like opening a PR) and run whatever commands you specify.\n\nHere&#39;s the core of the workflow:\n\n```yaml\nname: Claude QA\n\non:\n  pull_request:\n    types: [labeled]\n\njobs:\n  qa:\n    runs-on: ubuntu-latest\n\n    steps:\n      - name: Checkout code\n        uses: actions/checkout@v4\n\n      - name: Start my app\n        run: |\n          pnpm dev &amp;\n          # Wait for server to be ready\n          sleep 10\n\n      - name: Run Claude QA\n        uses: anthropics/claude-code-action@v1\n        with:\n          prompt: ${{ steps.load-prompts.outputs.prompt }}\n          claude_args: |\n            --mcp-config &#39;{\&quot;mcpServers\&quot;:{\&quot;playwright\&quot;:{\n              \&quot;command\&quot;:\&quot;npx\&quot;,\n              \&quot;args\&quot;:[\&quot;@playwright/mcp@latest\&quot;,\&quot;--headless\&quot;]\n            }}}&#39;\n```\n\nLet me break this down:\n\n1. **Trigger**: The workflow runs when you add a label to a PR (like `qa-verify`)\n2. **Start the app**: Launch your dev server so Claude has something to test\n3. **Run Claude**: Use Anthropic&#39;s official GitHub Action with Playwright MCP connected\n\n&lt;Alert type=\&quot;tip\&quot; title=\&quot;Headless mode\&quot;&gt;\n  The `--headless` flag runs the browser without a visible window. This is required for CI environments like GitHub Actions where there&#39;s no display.\n&lt;/Alert&gt;\n\n## Step 3: Tell Claude what to test\n\nFor each PR, I want Claude to verify the actual changes. So I pass in the PR description:\n\n```markdown\n# PR Verification Testing\n\n**PR #32**: Improve set editing and fix playlist overflow\n\n## Your Mission\n\nThis PR claims to implement something. Your job is to:\n1. **Verify** the claimed changes actually work\n2. **Break** them with edge cases\n3. **Ensure** no regressions in related features\n\n## Test This PR\n\n- Can users edit ANY set during active workout?\n- Do completed sets stay editable?\n- Do long exercise names truncate properly?\n```\n\nClaude reads this, understands what changed, and tests specifically for those features.\n\n## What Quinn actually does\n\nHere&#39;s a real example from my workout tracker. I opened a PR that said \&quot;allow editing any set during a workout.\&quot;\n\n&lt;Aside type=\&quot;info\&quot; title=\&quot;See it in action\&quot;&gt;\n  You can view the [actual GitHub Actions run](https://github.com/alexanderop/workoutTracker/actions/runs/20197464088) for this PR. The workflow completed in about 7 minutes and generated a QA report artifact.\n&lt;/Aside&gt;\n\nQuinn went to work:\n\n```mermaid\ngraph TD\n    A[Start Workout] --&gt; B[Add Exercise]\n    B --&gt; C[Fill Set Data]\n    C --&gt; D[Mark Complete]\n    D --&gt; E{Test Edit Feature}\n    E --&gt;|Happy Path| F[Change Weight ✓]\n    E --&gt;|Edge Case| G[Enter -50]\n    E --&gt;|Edge Case| H[Enter 999999]\n    F --&gt; I[Mobile Test]\n    G --&gt; I\n    H --&gt; I\n    I --&gt; J[Long Name Test]\n    J --&gt; K[Generate Report]\n```\n\n## The report\n\nQuinn generates a full QA report in Markdown:\n\n```markdown\n# QA Verification Report\n\n**PR**: #32 - Improve set editing\n**Tester**: Quinn (Claude QA)\n\n## Executive Summary\n\n**APPROVED** - All claimed features work as described.\n\n## Requirements Verification\n\n| Requirement | Status | How Tested |\n|-------------|--------|------------|\n| Edit any set | PASS | Changed weight after marking complete |\n| Long names truncate | PASS | Added 27-character exercise name |\n| Mobile layout | PASS | Tested at 375x667 viewport |\n\n## Bugs Found\n\nNone\n\n## Verdict\n\n**APPROVED** - Ready to merge.\n```\n\nThis report gets posted automatically as a comment on your PR. You can see exactly what Quinn tested and whether your code is safe to merge.\n\n## The toolbox\n\nQuinn only gets access to browser tools—no code access:\n\n```yaml\n--allowedTools \&quot;\n  mcp__playwright__browser_navigate,\n  mcp__playwright__browser_click,\n  mcp__playwright__browser_type,\n  mcp__playwright__browser_take_screenshot,\n  mcp__playwright__browser_resize,\n  Write\n\&quot;\n```\n\nThis keeps things realistic. A real QA engineer tests through the UI, not by reading code. Quinn does the same.\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;Why restrict tools?\&quot;&gt;\n  Limiting Claude to browser-only tools prevents it from \&quot;cheating\&quot; by reading your source code. This forces truly &lt;InternalLink slug=\&quot;stop-white-box-testing-vue\&quot;&gt;black-box testing&lt;/InternalLink&gt;—the same way real users experience your app.\n&lt;/Aside&gt;\n\n## Why this works\n\nThree reasons this approach beats traditional testing:\n\n### It tests like a human\n\nUnit tests check if functions return the right values. Quinn checks if users can actually accomplish their goals.\n\n### It&#39;s flexible\n\nYou don&#39;t write test scripts that break when you change a button&#39;s text. Quinn understands intent and adapts.\n\n### It finds unexpected bugs\n\nQuinn tries things you wouldn&#39;t think to try. Negative numbers? Extremely long inputs? Clicking the same button five times fast? Quinn tests all of it.\n\n## Comparison: AI QA vs traditional testing\n\n| Aspect | Unit Tests | E2E Scripts | AI QA (Quinn) |\n|--------|-----------|-------------|---------------|\n| Tests user flows | ❌ | ✅ | ✅ |\n| Handles UI changes | ❌ | ❌ | ✅ |\n| Finds edge cases | Manual | Manual | ✅ Automatic |\n| Setup complexity | Low | High | Medium |\n| Maintenance | Low | High | Low |\n\n## Getting started\n\nWant to build your own AI QA engineer? Here&#39;s what you need:\n\n1. **Get Claude Code access** — Sign up at Anthropic and get an API token\n\n2. **Create your QA prompt** — Give Claude a personality and testing philosophy\n\n3. **Set up the GitHub Action** — Use `anthropics/claude-code-action` with Playwright MCP\n\n4. **Write a verification template** — Tell Claude what to test for each PR\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;Full workflow available\&quot;&gt;\n  The complete GitHub Actions workflow with explore/verify modes, focus areas, and automatic PR comments is available as a [GitHub Gist](https://gist.github.com/alexanderop/464a7a228653e4df27179b9c806b2065). Use it as a starting point for your own QA automation.\n&lt;/Aside&gt;\n\n&lt;Alert type=\&quot;note\&quot; title=\&quot;Learn more about Claude Code\&quot;&gt;\n  If you&#39;re new to Claude Code, check out my &lt;InternalLink slug=\&quot;understanding-claude-code-full-stack\&quot;&gt;comprehensive guide to Claude Code features&lt;/InternalLink&gt; covering MCP, Skills, Hooks, and more. You can also set up &lt;InternalLink slug=\&quot;claude-code-notification-hooks\&quot;&gt;desktop notifications via hooks&lt;/InternalLink&gt; so you know the moment Claude finishes a task locally.\n&lt;/Alert&gt;\n\n## A word of caution\n\nThis approach is experimental. AI-driven QA is exciting, but it&#39;s not a replacement for deterministic testing.\n\nA solid testing foundation still matters more:\n\n- **Unit tests** catch regressions instantly\n- **Integration tests** verify your components work together\n- **E2E tests** with Playwright or Cypress give you reproducible, reliable checks\n\nAI QA works best as a *complement* to these, not a replacement. Use it for exploratory testing, edge case discovery, and verifying user flows that are hard to script.\n\n&lt;Alert type=\&quot;tip\&quot; title=\&quot;Beyond QA\&quot;&gt;\n  Claude Code in GitHub Actions isn&#39;t limited to QA. The same pattern works for:\n  - **SEO audits** — Check meta tags, heading structure, Core Web Vitals\n  - **&lt;InternalLink slug=\&quot;how-to-improve-accessibility-with-testing-library-and-jest-axe-for-your-vue-application\&quot;&gt;Accessibility testing&lt;/InternalLink&gt;** — Verify ARIA labels, keyboard navigation, color contrast\n  - **Content review** — Validate links, check for broken images, lint prose\n  - **&lt;InternalLink slug=\&quot;visual-regression-testing-with-vue-and-vitest-browser\&quot;&gt;Visual regression&lt;/InternalLink&gt;** — Compare screenshots across deployments\n\n  Any task where you&#39;d open a browser and manually check something can be automated this way.\n&lt;/Alert&gt;\n\n## Conclusion\n\nBuilding an AI QA engineer combines two powerful tools: Claude Code for intelligence and Playwright MCP for browser control. The result is automated testing that thinks like a human but works tirelessly.\n\nIt&#39;s still early days for this approach. But some day, Quinn might find a bug that would have embarrassed me in production. On that day, this whole experiment will have paid for itself.\n\n## Additional resources\n\n- [Full GitHub Actions Workflow](https://gist.github.com/alexanderop/464a7a228653e4df27179b9c806b2065) — Complete QA workflow with explore/verify modes\n- [Anthropic Claude Code Action](https://github.com/anthropics/claude-code-action) — Official GitHub Action\n- [Playwright MCP](https://github.com/microsoft/playwright-mcp) — Browser automation for Claude\n- [GitHub Actions Documentation](https://docs.github.com/en/actions) — Workflow automation basics&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <figure class="max-w-4xl mx-auto "> <img src="/_astro/CLAUDEAI.B5_3DuFq_w6Is9.webp" alt="AI QA Engineer with Claude Code and Playwright" loading="lazy" decoding="async" fetchpriority="auto" width="1024" height="559" class="w-full">  </figure>
<h2 id="quick-summary">Quick Summary<a class="heading-link" aria-label="Link to section" href="#quick-summary"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li>Build an AI-powered QA engineer that tests your app through the browser like a real user</li>
<li>Use Claude Code with Playwright MCP to automate browser interactions</li>
<li>Run automated QA on every pull request via GitHub Actions</li>
<li>Get detailed bug reports with screenshots posted directly to your PRs</li>
</ul>
<h2 id="table-of-contents">Table of Contents<a class="heading-link" aria-label="Link to section" href="#table-of-contents"><span class="heading-link-icon">#</span></a></h2>
<p></p><details><summary>Open Table of Contents</summary><p></p>
<ul>
<li><a href="#introduction">Introduction</a></li>
<li><a href="#the-secret-sauce-claude-code--playwright">The secret sauce: Claude Code + Playwright</a></li>
<li><a href="#step-1-give-claude-a-personality">Step 1: Give Claude a personality</a></li>
<li><a href="#step-2-create-the-github-action">Step 2: Create the GitHub Action</a></li>
<li><a href="#step-3-tell-claude-what-to-test">Step 3: Tell Claude what to test</a></li>
<li><a href="#what-quinn-actually-does">What Quinn actually does</a></li>
<li><a href="#the-report">The report</a></li>
<li><a href="#the-toolbox">The toolbox</a></li>
<li><a href="#why-this-works">Why this works</a>
<ul>
<li><a href="#it-tests-like-a-human">It tests like a human</a></li>
<li><a href="#its-flexible">It’s flexible</a></li>
<li><a href="#it-finds-unexpected-bugs">It finds unexpected bugs</a></li>
</ul>
</li>
<li><a href="#comparison-ai-qa-vs-traditional-testing">Comparison: AI QA vs traditional testing</a></li>
<li><a href="#getting-started">Getting started</a></li>
<li><a href="#a-word-of-caution">A word of caution</a></li>
<li><a href="#conclusion">Conclusion</a></li>
<li><a href="#additional-resources">Additional resources</a></li>
</ul>
<p></p></details><p></p>
<h2 id="introduction">Introduction<a class="heading-link" aria-label="Link to section" href="#introduction"><span class="heading-link-icon">#</span></a></h2>
<p>Manual testing gets old fast. Clicking through your app after every change, checking if forms still work, making sure nothing breaks on mobile—it’s tedious work that most developers avoid.</p>
<p>So I built an AI that does it for me.</p>
<p>Meet <strong>Quinn</strong>, my automated QA engineer. Quinn tests my app like a real person would. It clicks buttons. It fills forms with weird inputs. It resizes the browser to check mobile layouts. And it writes detailed bug reports.</p>
<p>The best part? Quinn runs automatically every time I open a pull request.</p>
<figure class="max-w-4xl mx-auto "> <img src="/_astro/claudeQaWorkflow.CDF1PwEd_ZnuVju.webp" alt="Claude QA workflow: Developer opens PR, GitHub Actions triggers workflow, Claude Code tests via Playwright, QA report posted back to PR" loading="lazy" decoding="async" fetchpriority="auto" width="1024" height="590" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> The automated QA workflow </figcaption> </figure>
<h2 id="the-secret-sauce-claude-code--playwright">The secret sauce: Claude Code + Playwright<a class="heading-link" aria-label="Link to section" href="#the-secret-sauce-claude-code--playwright"><span class="heading-link-icon">#</span></a></h2>
<p>Two tools make this possible:</p>
<p><strong>Claude Code</strong> is Anthropic’s coding assistant. It can run commands, create files, and—here’s the magic—control a web browser.</p>
<p><strong>Playwright</strong> is a browser automation tool. It can click, type, take screenshots, and do anything a human can do in a browser.</p>
<p>When you combine them through the <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/what-is-model-context-protocol-mcp/" class="internal-link astro-3tyn5ojg"> Model Context Protocol (MCP) </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">What Is the Model Context Protocol (MCP)? How It Works</span> <span class="preview-description astro-3tyn5ojg">Learn how MCP (Model Context Protocol) standardizes AI tool integration, enabling LLMs to interact with external services, databases, and APIs through a universal protocol similar to USB-C for AI applications.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">mcp</span><span class="preview-tag astro-3tyn5ojg">typescript</span><span class="preview-tag astro-3tyn5ojg">ai</span>  </span> <time class="preview-date astro-3tyn5ojg">Aug 10, 2025</time> </span> </span> </span>  <script>
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
</script>, Claude can literally browse your app like a real user.</p>
<aside aria-label="What is MCP?" class="aside aside-info astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">ℹ️</span> What is MCP? </p> <section class="aside-body astro-37uy2q7c"> <p>MCP (Model Context Protocol) standardizes how AI tools connect to external services. Think of it as USB-C for AI—one universal way to connect tools like Playwright, databases, or APIs to any LLM. Learn more in my <span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/what-is-model-context-protocol-mcp/" class="internal-link astro-3tyn5ojg"> MCP deep dive </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">What Is the Model Context Protocol (MCP)? How It Works</span> <span class="preview-description astro-3tyn5ojg">Learn how MCP (Model Context Protocol) standardizes AI tool integration, enabling LLMs to interact with external services, databases, and APIs through a universal protocol similar to USB-C for AI applications.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">mcp</span><span class="preview-tag astro-3tyn5ojg">typescript</span><span class="preview-tag astro-3tyn5ojg">ai</span>  </span> <time class="preview-date astro-3tyn5ojg">Aug 10, 2025</time> </span> </span> </span>  <script>
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
</script>.</p> </section> </div> </aside> 
<h2 id="step-1-give-claude-a-personality">Step 1: Give Claude a personality<a class="heading-link" aria-label="Link to section" href="#step-1-give-claude-a-personality"><span class="heading-link-icon">#</span></a></h2>
<p>I didn’t want a boring test robot. I wanted a QA engineer with opinions.</p>
<p>So I created a prompt file that gives Claude a backstory:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> QA Engineer Identity</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">You are </span><span style="color:#C0CAF5;font-weight:bold">**Quinn**</span><span style="color:#9AA5CE">, a veteran QA engineer with 12 years</span></span>
<span class="line"><span style="color:#9AA5CE">of experience breaking software. You&#39;ve seen it all -</span></span>
<span class="line"><span style="color:#9AA5CE">apps that crash on empty input, forms that lose data,</span></span>
<span class="line"><span style="color:#9AA5CE">buttons that do nothing.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Your Philosophy</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Trust nothing.**</span><span style="color:#9AA5CE"> Developers say it works? Prove it.</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Users are creative.**</span><span style="color:#9AA5CE"> They&#39;ll do things no one anticipated.</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Edge cases are where bugs hide.**</span><span style="color:#9AA5CE"> The happy path is boring.</span></span></code><button type="button" class="copy" data-code="# QA Engineer Identity

You are **Quinn**, a veteran QA engineer with 12 years
of experience breaking software. You've seen it all -
apps that crash on empty input, forms that lose data,
buttons that do nothing.

## Your Philosophy

- **Trust nothing.** Developers say it works? Prove it.
- **Users are creative.** They'll do things no one anticipated.
- **Edge cases are where bugs hide.** The happy path is boring." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This isn’t just for fun. The personality makes Claude test more thoroughly. Quinn doesn’t just check if buttons work—Quinn tries to <em>break</em> things.</p>
<p>I also gave Quinn strict rules:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Non-Negotiable Rules</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#C0CAF5;font-weight:bold"> **UI ONLY.**</span><span style="color:#9AA5CE"> You interact through the browser like a</span></span>
<span class="line"><span style="color:#9AA5CE">   real user. You cannot read source code.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#C0CAF5;font-weight:bold"> **SCREENSHOT BUGS.**</span><span style="color:#9AA5CE"> Every bug gets a screenshot.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#C0CAF5;font-weight:bold"> **CONTINUE AFTER BUGS.**</span><span style="color:#9AA5CE"> Finding a bug is not the end.</span></span>
<span class="line"><span style="color:#9AA5CE">   Document it, then KEEP TESTING.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#C0CAF5;font-weight:bold"> **MOBILE MATTERS.**</span><span style="color:#9AA5CE"> Always test mobile viewport (375x667).</span></span></code><button type="button" class="copy" data-code="## Non-Negotiable Rules

1. **UI ONLY.** You interact through the browser like a
   real user. You cannot read source code.

2. **SCREENSHOT BUGS.** Every bug gets a screenshot.

3. **CONTINUE AFTER BUGS.** Finding a bug is not the end.
   Document it, then KEEP TESTING.

4. **MOBILE MATTERS.** Always test mobile viewport (375x667)." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="step-2-create-the-github-action">Step 2: Create the GitHub Action<a class="heading-link" aria-label="Link to section" href="#step-2-create-the-github-action"><span class="heading-link-icon">#</span></a></h2>
<p>GitHub Actions are like little robots that run tasks for you. They trigger when something happens (like opening a PR) and run whatever commands you specify.</p>
<p>Here’s the core of the workflow:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="yaml"><code><span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Claude QA</span></span>
<span class="line"></span>
<span class="line"><span style="color:#FF9E64">on</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#F7768E">  pull_request</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#F7768E">    types</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> [</span><span style="color:#9ECE6A">labeled</span><span style="color:#89DDFF">]</span></span>
<span class="line"></span>
<span class="line"><span style="color:#F7768E">jobs</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#F7768E">  qa</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#F7768E">    runs-on</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> ubuntu-latest</span></span>
<span class="line"></span>
<span class="line"><span style="color:#F7768E">    steps</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#9ABDF5">      -</span><span style="color:#F7768E"> name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Checkout code</span></span>
<span class="line"><span style="color:#F7768E">        uses</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> actions/checkout@v4</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ABDF5">      -</span><span style="color:#F7768E"> name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Start my app</span></span>
<span class="line"><span style="color:#F7768E">        run</span><span style="color:#89DDFF">:</span><span style="color:#BB9AF7"> |</span></span>
<span class="line"><span style="color:#9ECE6A">          pnpm dev &amp;</span></span>
<span class="line"><span style="color:#9ECE6A">          # Wait for server to be ready</span></span>
<span class="line"><span style="color:#9ECE6A">          sleep 10</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9ABDF5">      -</span><span style="color:#F7768E"> name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Run Claude QA</span></span>
<span class="line"><span style="color:#F7768E">        uses</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> anthropics/claude-code-action@v1</span></span>
<span class="line"><span style="color:#F7768E">        with</span><span style="color:#89DDFF">:</span></span>
<span class="line"><span style="color:#F7768E">          prompt</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> ${{ steps.load-prompts.outputs.prompt }}</span></span>
<span class="line"><span style="color:#F7768E">          claude_args</span><span style="color:#89DDFF">:</span><span style="color:#BB9AF7"> |</span></span>
<span class="line"><span style="color:#9ECE6A">            --mcp-config &#39;{&quot;mcpServers&quot;:{&quot;playwright&quot;:{</span></span>
<span class="line"><span style="color:#9ECE6A">              &quot;command&quot;:&quot;npx&quot;,</span></span>
<span class="line"><span style="color:#9ECE6A">              &quot;args&quot;:[&quot;@playwright/mcp@latest&quot;,&quot;--headless&quot;]</span></span>
<span class="line"><span style="color:#9ECE6A">            }}}&#39;</span></span></code><button type="button" class="copy" data-code="name: Claude QA

on:
  pull_request:
    types: [labeled]

jobs:
  qa:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Start my app
        run: |
          pnpm dev &#38;
          # Wait for server to be ready
          sleep 10

      - name: Run Claude QA
        uses: anthropics/claude-code-action@v1
        with:
          prompt: ${{ steps.load-prompts.outputs.prompt }}
          claude_args: |
            --mcp-config '{&#34;mcpServers&#34;:{&#34;playwright&#34;:{
              &#34;command&#34;:&#34;npx&#34;,
              &#34;args&#34;:[&#34;@playwright/mcp@latest&#34;,&#34;--headless&#34;]
            }}}'" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Let me break this down:</p>
<ol>
<li><strong>Trigger</strong>: The workflow runs when you add a label to a PR (like <code>qa-verify</code>)</li>
<li><strong>Start the app</strong>: Launch your dev server so Claude has something to test</li>
<li><strong>Run Claude</strong>: Use Anthropic’s official GitHub Action with Playwright MCP connected</li>
</ol>
<div class="alert alert-tip astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💪</span> Headless mode </p> <div class="alert-content astro-7kdbuayl"> <p>The <code>--headless</code> flag runs the browser without a visible window. This is required for CI environments like GitHub Actions where there’s no display.</p> </div> </div> 
<h2 id="step-3-tell-claude-what-to-test">Step 3: Tell Claude what to test<a class="heading-link" aria-label="Link to section" href="#step-3-tell-claude-what-to-test"><span class="heading-link-icon">#</span></a></h2>
<p>For each PR, I want Claude to verify the actual changes. So I pass in the PR description:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> PR Verification Testing</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**PR #32**</span><span style="color:#9AA5CE">: Improve set editing and fix playlist overflow</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Your Mission</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">This PR claims to implement something. Your job is to:</span></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#C0CAF5;font-weight:bold"> **Verify**</span><span style="color:#9AA5CE"> the claimed changes actually work</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#C0CAF5;font-weight:bold"> **Break**</span><span style="color:#9AA5CE"> them with edge cases</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#C0CAF5;font-weight:bold"> **Ensure**</span><span style="color:#9AA5CE"> no regressions in related features</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Test This PR</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Can users edit ANY set during active workout?</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Do completed sets stay editable?</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Do long exercise names truncate properly?</span></span></code><button type="button" class="copy" data-code="# PR Verification Testing

**PR #32**: Improve set editing and fix playlist overflow

## Your Mission

This PR claims to implement something. Your job is to:
1. **Verify** the claimed changes actually work
2. **Break** them with edge cases
3. **Ensure** no regressions in related features

## Test This PR

- Can users edit ANY set during active workout?
- Do completed sets stay editable?
- Do long exercise names truncate properly?" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Claude reads this, understands what changed, and tests specifically for those features.</p>
<h2 id="what-quinn-actually-does">What Quinn actually does<a class="heading-link" aria-label="Link to section" href="#what-quinn-actually-does"><span class="heading-link-icon">#</span></a></h2>
<p>Here’s a real example from my workout tracker. I opened a PR that said “allow editing any set during a workout.”</p>
<aside aria-label="See it in action" class="aside aside-info astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">ℹ️</span> See it in action </p> <section class="aside-body astro-37uy2q7c"> <p>You can view the <a target="_blank" rel="noopener noreferrer" href="https://github.com/alexanderop/workoutTracker/actions/runs/20197464088" rel="noopener noreferrer" target="_blank">actual GitHub Actions run</a> for this PR. The workflow completed in about 7 minutes and generated a QA report artifact.</p> </section> </div> </aside> 
<p>Quinn went to work:</p>
<p><svg id="mermaid-0" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:642.796875px" viewBox="0 0 642.796875 1089.765625" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-0 .cluster-label text{fill:#F9FFFE;}#mermaid-0 .cluster-label span{color:#F9FFFE;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#ccc;color:#ccc;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-0 .arrowheadPath{fill:lightgrey;}#mermaid-0 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-0 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-0 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-0 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-0 .cluster text{fill:#F9FFFE;}#mermaid-0 .cluster span{color:#F9FFFE;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-0 .icon-shape rect,#mermaid-0 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-0_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M335.852,62L335.852,66.167C335.852,70.333,335.852,78.667,335.852,86.333C335.852,94,335.852,101,335.852,104.5L335.852,108" id="L_A_B_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_B_0" data-points="W3sieCI6MzM1Ljg1MTU2MjUsInkiOjYyfSx7IngiOjMzNS44NTE1NjI1LCJ5Ijo4N30seyJ4IjozMzUuODUxNTYyNSwieSI6MTEyfV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M335.852,166L335.852,170.167C335.852,174.333,335.852,182.667,335.852,190.333C335.852,198,335.852,205,335.852,208.5L335.852,212" id="L_B_C_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_C_0" data-points="W3sieCI6MzM1Ljg1MTU2MjUsInkiOjE2Nn0seyJ4IjozMzUuODUxNTYyNSwieSI6MTkxfSx7IngiOjMzNS44NTE1NjI1LCJ5IjoyMTZ9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M335.852,270L335.852,274.167C335.852,278.333,335.852,286.667,335.852,294.333C335.852,302,335.852,309,335.852,312.5L335.852,316" id="L_C_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_D_0" data-points="W3sieCI6MzM1Ljg1MTU2MjUsInkiOjI3MH0seyJ4IjozMzUuODUxNTYyNSwieSI6Mjk1fSx7IngiOjMzNS44NTE1NjI1LCJ5IjozMjB9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M335.852,374L335.852,378.167C335.852,382.333,335.852,390.667,335.852,398.333C335.852,406,335.852,413,335.852,416.5L335.852,420" id="L_D_E_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_E_0" data-points="W3sieCI6MzM1Ljg1MTU2MjUsInkiOjM3NH0seyJ4IjozMzUuODUxNTYyNSwieSI6Mzk5fSx7IngiOjMzNS44NTE1NjI1LCJ5Ijo0MjR9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M269.727,575.641L243.148,592.829C216.568,610.016,163.409,644.391,136.83,667.078C110.25,689.766,110.25,700.766,110.25,706.266L110.25,711.766" id="L_E_F_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_E_F_0" data-points="W3sieCI6MjY5LjcyNzI5MzgwMjU3NjI0LCJ5Ijo1NzUuNjQxMzU2MzAyNTc2Mn0seyJ4IjoxMTAuMjUsInkiOjY3OC43NjU2MjV9LHsieCI6MTEwLjI1LCJ5Ijo3MTUuNzY1NjI1fV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M335.852,641.766L335.852,647.932C335.852,654.099,335.852,666.432,335.852,678.099C335.852,689.766,335.852,700.766,335.852,706.266L335.852,711.766" id="L_E_G_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_E_G_0" data-points="W3sieCI6MzM1Ljg1MTU2MjUsInkiOjY0MS43NjU2MjV9LHsieCI6MzM1Ljg1MTU2MjUsInkiOjY3OC43NjU2MjV9LHsieCI6MzM1Ljg1MTU2MjUsInkiOjcxNS43NjU2MjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M400.245,577.372L424.704,594.271C449.163,611.17,498.082,644.968,522.541,667.367C547,689.766,547,700.766,547,706.266L547,711.766" id="L_E_H_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_E_H_0" data-points="W3sieCI6NDAwLjI0NDkwNTQ2MzYyMTQsInkiOjU3Ny4zNzIyODIwMzYzNzg2fSx7IngiOjU0NywieSI6Njc4Ljc2NTYyNX0seyJ4Ijo1NDcsInkiOjcxNS43NjU2MjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M110.25,769.766L110.25,773.932C110.25,778.099,110.25,786.432,133.37,795.928C156.49,805.424,202.73,816.082,225.849,821.411L248.969,826.74" id="L_F_I_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_F_I_0" data-points="W3sieCI6MTEwLjI1LCJ5Ijo3NjkuNzY1NjI1fSx7IngiOjExMC4yNSwieSI6Nzk0Ljc2NTYyNX0seyJ4IjoyNTIuODY3MTg3NSwieSI6ODI3LjYzODE1MzMwOTcyNzV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M335.852,769.766L335.852,773.932C335.852,778.099,335.852,786.432,335.852,794.099C335.852,801.766,335.852,808.766,335.852,812.266L335.852,815.766" id="L_G_I_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_G_I_0" data-points="W3sieCI6MzM1Ljg1MTU2MjUsInkiOjc2OS43NjU2MjV9LHsieCI6MzM1Ljg1MTU2MjUsInkiOjc5NC43NjU2MjV9LHsieCI6MzM1Ljg1MTU2MjUsInkiOjgxOS43NjU2MjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M547,769.766L547,773.932C547,778.099,547,786.432,526.287,795.7C505.573,804.968,464.147,815.17,443.433,820.271L422.72,825.372" id="L_H_I_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_H_I_0" data-points="W3sieCI6NTQ3LCJ5Ijo3NjkuNzY1NjI1fSx7IngiOjU0NywieSI6Nzk0Ljc2NTYyNX0seyJ4Ijo0MTguODM1OTM3NSwieSI6ODI2LjMyODg3NjU2MzI1MTZ9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M335.852,873.766L335.852,877.932C335.852,882.099,335.852,890.432,335.852,898.099C335.852,905.766,335.852,912.766,335.852,916.266L335.852,919.766" id="L_I_J_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_I_J_0" data-points="W3sieCI6MzM1Ljg1MTU2MjUsInkiOjg3My43NjU2MjV9LHsieCI6MzM1Ljg1MTU2MjUsInkiOjg5OC43NjU2MjV9LHsieCI6MzM1Ljg1MTU2MjUsInkiOjkyMy43NjU2MjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M335.852,977.766L335.852,981.932C335.852,986.099,335.852,994.432,335.852,1002.099C335.852,1009.766,335.852,1016.766,335.852,1020.266L335.852,1023.766" id="L_J_K_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_J_K_0" data-points="W3sieCI6MzM1Ljg1MTU2MjUsInkiOjk3Ny43NjU2MjV9LHsieCI6MzM1Ljg1MTU2MjUsInkiOjEwMDIuNzY1NjI1fSx7IngiOjMzNS44NTE1NjI1LCJ5IjoxMDI3Ljc2NTYyNX1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_A_B_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B_C_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C_D_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_D_E_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(110.25, 678.765625)"><g class="label" data-id="L_E_F_0" transform="translate(-48.1640625, -12)"><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Happy Path</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(335.8515625, 678.765625)"><g class="label" data-id="L_E_G_0" transform="translate(-43.3515625, -12)"><foreignObject width="86.703125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Edge Case</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(547, 678.765625)"><g class="label" data-id="L_E_H_0" transform="translate(-43.3515625, -12)"><foreignObject width="86.703125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Edge Case</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_F_I_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_G_I_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_H_I_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_I_J_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_J_K_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-0" transform="translate(335.8515625, 35)"><rect class="basic label-container" style="" x="-92.6171875" y="-27" width="185.234375" height="54"></rect><g class="label" style="" transform="translate(-62.6171875, -12)"><rect></rect><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Start Workout</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B-1" transform="translate(335.8515625, 139)"><rect class="basic label-container" style="" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Add Exercise</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C-3" transform="translate(335.8515625, 243)"><rect class="basic label-container" style="" x="-92.6171875" y="-27" width="185.234375" height="54"></rect><g class="label" style="" transform="translate(-62.6171875, -12)"><rect></rect><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Fill Set Data</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-D-5" transform="translate(335.8515625, 347)"><rect class="basic label-container" style="" x="-92.6171875" y="-27" width="185.234375" height="54"></rect><g class="label" style="" transform="translate(-62.6171875, -12)"><rect></rect><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Mark Complete</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-E-7" transform="translate(335.8515625, 532.8828125)"><polygon points="108.8828125,0 217.765625,-108.8828125 108.8828125,-217.765625 0,-108.8828125" class="label-container" transform="translate(-108.3828125, 108.8828125)"></polygon><g class="label" style="" transform="translate(-81.8828125, -12)"><rect></rect><foreignObject width="163.765625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Test Edit Feature</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-F-9" transform="translate(110.25, 742.765625)"><rect class="basic label-container" style="" x="-102.25" y="-27" width="204.5" height="54"></rect><g class="label" style="" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Change Weight ✓</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-G-11" transform="translate(335.8515625, 742.765625)"><rect class="basic label-container" style="" x="-73.3515625" y="-27" width="146.703125" height="54"></rect><g class="label" style="" transform="translate(-43.3515625, -12)"><rect></rect><foreignObject width="86.703125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Enter -50</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-H-13" transform="translate(547, 742.765625)"><rect class="basic label-container" style="" x="-87.796875" y="-27" width="175.59375" height="54"></rect><g class="label" style="" transform="translate(-57.796875, -12)"><rect></rect><foreignObject width="115.59375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Enter 999999</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-I-15" transform="translate(335.8515625, 846.765625)"><rect class="basic label-container" style="" x="-82.984375" y="-27" width="165.96875" height="54"></rect><g class="label" style="" transform="translate(-52.984375, -12)"><rect></rect><foreignObject width="105.96875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Mobile Test</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-J-21" transform="translate(335.8515625, 950.765625)"><rect class="basic label-container" style="" x="-97.4296875" y="-27" width="194.859375" height="54"></rect><g class="label" style="" transform="translate(-67.4296875, -12)"><rect></rect><foreignObject width="134.859375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Long Name Test</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-K-23" transform="translate(335.8515625, 1054.765625)"><rect class="basic label-container" style="" x="-102.25" y="-27" width="204.5" height="54"></rect><g class="label" style="" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Generate Report</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<h2 id="the-report">The report<a class="heading-link" aria-label="Link to section" href="#the-report"><span class="heading-link-icon">#</span></a></h2>
<p>Quinn generates a full QA report in Markdown:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> QA Verification Report</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**PR**</span><span style="color:#9AA5CE">: #32 - Improve set editing</span></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Tester**</span><span style="color:#9AA5CE">: Quinn (Claude QA)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Executive Summary</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**APPROVED**</span><span style="color:#9AA5CE"> - All claimed features work as described.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Requirements Verification</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Requirement </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Status </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> How Tested </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|-------------|--------|------------|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Edit any set </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> PASS </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Changed weight after marking complete </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Long names truncate </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> PASS </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Added 27-character exercise name </span><span style="color:#89DDFF">|</span></span>
<span class="line"><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Mobile layout </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> PASS </span><span style="color:#89DDFF">|</span><span style="color:#C0CEFC"> Tested at 375x667 viewport </span><span style="color:#89DDFF">|</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Bugs Found</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">None</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Verdict</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**APPROVED**</span><span style="color:#9AA5CE"> - Ready to merge.</span></span></code><button type="button" class="copy" data-code="# QA Verification Report

**PR**: #32 - Improve set editing
**Tester**: Quinn (Claude QA)

## Executive Summary

**APPROVED** - All claimed features work as described.

## Requirements Verification

| Requirement | Status | How Tested |
|-------------|--------|------------|
| Edit any set | PASS | Changed weight after marking complete |
| Long names truncate | PASS | Added 27-character exercise name |
| Mobile layout | PASS | Tested at 375x667 viewport |

## Bugs Found

None

## Verdict

**APPROVED** - Ready to merge." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This report gets posted automatically as a comment on your PR. You can see exactly what Quinn tested and whether your code is safe to merge.</p>
<h2 id="the-toolbox">The toolbox<a class="heading-link" aria-label="Link to section" href="#the-toolbox"><span class="heading-link-icon">#</span></a></h2>
<p>Quinn only gets access to browser tools—no code access:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="yaml"><code><span class="line"><span style="color:#9ECE6A">--allowedTools &quot;</span></span>
<span class="line"><span style="color:#9ECE6A">  mcp__playwright__browser_navigate,</span></span>
<span class="line"><span style="color:#9ECE6A">  mcp__playwright__browser_click,</span></span>
<span class="line"><span style="color:#9ECE6A">  mcp__playwright__browser_type,</span></span>
<span class="line"><span style="color:#9ECE6A">  mcp__playwright__browser_take_screenshot,</span></span>
<span class="line"><span style="color:#9ECE6A">  mcp__playwright__browser_resize,</span></span>
<span class="line"><span style="color:#9ECE6A">  Write</span></span>
<span class="line"><span style="color:#89DDFF">&quot;</span></span></code><button type="button" class="copy" data-code="--allowedTools &#34;
  mcp__playwright__browser_navigate,
  mcp__playwright__browser_click,
  mcp__playwright__browser_type,
  mcp__playwright__browser_take_screenshot,
  mcp__playwright__browser_resize,
  Write
&#34;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This keeps things realistic. A real QA engineer tests through the UI, not by reading code. Quinn does the same.</p>
<aside aria-label="Why restrict tools?" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> Why restrict tools? </p> <section class="aside-body astro-37uy2q7c"> <p>Limiting Claude to browser-only tools prevents it from “cheating” by reading your source code. This forces truly <span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/stop-white-box-testing-vue/" class="internal-link astro-3tyn5ojg"> black-box testing </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Stop White Box Testing Vue Components Use Testing Library Instead</span> <span class="preview-description astro-3tyn5ojg">White Box testing makes your Vue tests fragile and misleading. In this post, I’ll show you how Testing Library helps you write Black Box tests that are resilient, realistic, and focused on actual user behavior</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span>  </span> <time class="preview-date astro-3tyn5ojg">Apr 19, 2025</time> </span> </span> </span>  <script>
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
</script>—the same way real users experience your app.</p> </section> </div> </aside> 
<h2 id="why-this-works">Why this works<a class="heading-link" aria-label="Link to section" href="#why-this-works"><span class="heading-link-icon">#</span></a></h2>
<p>Three reasons this approach beats traditional testing:</p>
<h3 id="it-tests-like-a-human">It tests like a human<a class="heading-link" aria-label="Link to section" href="#it-tests-like-a-human"><span class="heading-link-icon">#</span></a></h3>
<p>Unit tests check if functions return the right values. Quinn checks if users can actually accomplish their goals.</p>
<h3 id="its-flexible">It’s flexible<a class="heading-link" aria-label="Link to section" href="#its-flexible"><span class="heading-link-icon">#</span></a></h3>
<p>You don’t write test scripts that break when you change a button’s text. Quinn understands intent and adapts.</p>
<h3 id="it-finds-unexpected-bugs">It finds unexpected bugs<a class="heading-link" aria-label="Link to section" href="#it-finds-unexpected-bugs"><span class="heading-link-icon">#</span></a></h3>
<p>Quinn tries things you wouldn’t think to try. Negative numbers? Extremely long inputs? Clicking the same button five times fast? Quinn tests all of it.</p>
<h2 id="comparison-ai-qa-vs-traditional-testing">Comparison: AI QA vs traditional testing<a class="heading-link" aria-label="Link to section" href="#comparison-ai-qa-vs-traditional-testing"><span class="heading-link-icon">#</span></a></h2>









































<table><thead><tr><th>Aspect</th><th>Unit Tests</th><th>E2E Scripts</th><th>AI QA (Quinn)</th></tr></thead><tbody><tr><td data-label="Aspect">Tests user flows</td><td data-label="Unit Tests">❌</td><td data-label="E2E Scripts">✅</td><td data-label="AI QA (Quinn)">✅</td></tr><tr><td data-label="Aspect">Handles UI changes</td><td data-label="Unit Tests">❌</td><td data-label="E2E Scripts">❌</td><td data-label="AI QA (Quinn)">✅</td></tr><tr><td data-label="Aspect">Finds edge cases</td><td data-label="Unit Tests">Manual</td><td data-label="E2E Scripts">Manual</td><td data-label="AI QA (Quinn)">✅ Automatic</td></tr><tr><td data-label="Aspect">Setup complexity</td><td data-label="Unit Tests">Low</td><td data-label="E2E Scripts">High</td><td data-label="AI QA (Quinn)">Medium</td></tr><tr><td data-label="Aspect">Maintenance</td><td data-label="Unit Tests">Low</td><td data-label="E2E Scripts">High</td><td data-label="AI QA (Quinn)">Low</td></tr></tbody></table>
<h2 id="getting-started">Getting started<a class="heading-link" aria-label="Link to section" href="#getting-started"><span class="heading-link-icon">#</span></a></h2>
<p>Want to build your own AI QA engineer? Here’s what you need:</p>
<ol>
<li>
<p><strong>Get Claude Code access</strong> — Sign up at Anthropic and get an API token</p>
</li>
<li>
<p><strong>Create your QA prompt</strong> — Give Claude a personality and testing philosophy</p>
</li>
<li>
<p><strong>Set up the GitHub Action</strong> — Use <code>anthropics/claude-code-action</code> with Playwright MCP</p>
</li>
<li>
<p><strong>Write a verification template</strong> — Tell Claude what to test for each PR</p>
</li>
</ol>
<aside aria-label="Full workflow available" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> Full workflow available </p> <section class="aside-body astro-37uy2q7c"> <p>The complete GitHub Actions workflow with explore/verify modes, focus areas, and automatic PR comments is available as a <a target="_blank" rel="noopener noreferrer" href="https://gist.github.com/alexanderop/464a7a228653e4df27179b9c806b2065" rel="noopener noreferrer" target="_blank">GitHub Gist</a>. Use it as a starting point for your own QA automation.</p> </section> </div> </aside> 
<div class="alert alert-note astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💡</span> Learn more about Claude Code </p> <div class="alert-content astro-7kdbuayl"> <p>If you’re new to Claude Code, check out my <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/understanding-claude-code-full-stack/" class="internal-link astro-3tyn5ojg"> comprehensive guide to Claude Code features </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Understanding Claude Code&#39;s Full Stack: MCP, Skills, Subagents, and Hooks Explained</span> <span class="preview-description astro-3tyn5ojg">A practical guide to Claude Code&#39;s features — explained in the order they were introduced: MCP (2024), Claude Code core (Feb 2025), Plugins (2025), and Agent Skills (Oct 2025). What each does, how they fit together, and when to use what.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">mcp</span> <span class="preview-tag-more astro-3tyn5ojg">+2</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 9, 2025</time> </span> </span> </span>  <script>
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
</script> covering MCP, Skills, Hooks, and more. You can also set up <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/claude-code-notification-hooks/" class="internal-link astro-3tyn5ojg"> desktop notifications via hooks </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Claude Code Notifications: Get Alerts When Tasks Finish (Hooks Setup)</span> <span class="preview-description astro-3tyn5ojg">How to set up Claude Code notifications using hooks. Get desktop alerts when Claude finishes a task, needs your input, or requests permission, instead of watching the terminal.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">notifications</span><span class="preview-tag astro-3tyn5ojg">hooks</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 23, 2025</time> </span> </span> </span>  <script>
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
</script> so you know the moment Claude finishes a task locally.</p> </div> </div> 
<h2 id="a-word-of-caution">A word of caution<a class="heading-link" aria-label="Link to section" href="#a-word-of-caution"><span class="heading-link-icon">#</span></a></h2>
<p>This approach is experimental. AI-driven QA is exciting, but it’s not a replacement for deterministic testing.</p>
<p>A solid testing foundation still matters more:</p>
<ul>
<li><strong>Unit tests</strong> catch regressions instantly</li>
<li><strong>Integration tests</strong> verify your components work together</li>
<li><strong>E2E tests</strong> with Playwright or Cypress give you reproducible, reliable checks</li>
</ul>
<p>AI QA works best as a <em>complement</em> to these, not a replacement. Use it for exploratory testing, edge case discovery, and verifying user flows that are hard to script.</p>
<div class="alert alert-tip astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💪</span> Beyond QA </p> <div class="alert-content astro-7kdbuayl"> <p>Claude Code in GitHub Actions isn’t limited to QA. The same pattern works for:</p><ul>
<li><strong>SEO audits</strong> — Check meta tags, heading structure, Core Web Vitals</li>
<li><strong><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/how-to-improve-accessibility-with-testing-library-and-jest-axe-for-your-vue-application/" class="internal-link astro-3tyn5ojg"> Accessibility testing </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Improve Accessibility with Testing Library and jest-axe for Your Vue Application</span> <span class="preview-description astro-3tyn5ojg">Use Jest axe to have automatic tests for your vue application</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">accessibility</span>  </span> <time class="preview-date astro-3tyn5ojg">Apr 12, 2023</time> </span> </span> </span>  <script>
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
</script></strong> — Verify ARIA labels, keyboard navigation, color contrast</li>
<li><strong>Content review</strong> — Validate links, check for broken images, lint prose</li>
<li><strong><span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/visual-regression-testing-with-vue-and-vitest-browser/" class="internal-link astro-3tyn5ojg"> Visual regression </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Do Visual Regression Testing in Vue with Vitest?</span> <span class="preview-description astro-3tyn5ojg">Learn how to implement visual regression testing in Vue.js using Vitest&#39;s browser mode. This comprehensive guide covers setting up screenshot-based testing, creating component stories, and integrating with CI/CD pipelines for automated visual testing.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">vue</span><span class="preview-tag astro-3tyn5ojg">testing</span><span class="preview-tag astro-3tyn5ojg">vitest</span>  </span> <time class="preview-date astro-3tyn5ojg">Feb 22, 2025</time> </span> </span> </span>  <script>
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
</script></strong> — Compare screenshots across deployments</li>
</ul><p>Any task where you’d open a browser and manually check something can be automated this way.</p> </div> </div> 
<h2 id="conclusion">Conclusion<a class="heading-link" aria-label="Link to section" href="#conclusion"><span class="heading-link-icon">#</span></a></h2>
<p>Building an AI QA engineer combines two powerful tools: Claude Code for intelligence and Playwright MCP for browser control. The result is automated testing that thinks like a human but works tirelessly.</p>
<p>It’s still early days for this approach. But some day, Quinn might find a bug that would have embarrassed me in production. On that day, this whole experiment will have paid for itself.</p>
<h2 id="additional-resources">Additional resources<a class="heading-link" aria-label="Link to section" href="#additional-resources"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li><a href="https://gist.github.com/alexanderop/464a7a228653e4df27179b9c806b2065" rel="noopener noreferrer" target="_blank">Full GitHub Actions Workflow</a> — Complete QA workflow with explore/verify modes</li>
<li><a href="https://github.com/anthropics/claude-code-action" rel="noopener noreferrer" target="_blank">Anthropic Claude Code Action</a> — Official GitHub Action</li>
<li><a href="https://github.com/microsoft/playwright-mcp" rel="noopener noreferrer" target="_blank">Playwright MCP</a> — Browser automation for Claude</li>
<li><a href="https://docs.github.com/en/actions" rel="noopener noreferrer" target="_blank">GitHub Actions Documentation</a> — Workflow automation basics</li>
</ul> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_building_ai_qa_engineer_claude_code_playwright" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="building_ai_qa_engineer_claude_code_playwright" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/testing/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">testing</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/claude-code/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">claude-code</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/automation/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-5"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">automation</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/building_ai_qa_engineer_claude_code_playwright/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/building_ai_qa_engineer_claude_code_playwright/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/building_ai_qa_engineer_claude_code_playwright/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/building_ai_qa_engineer_claude_code_playwright/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/building_ai_qa_engineer_claude_code_playwright/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/building_ai_qa_engineer_claude_code_playwright/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/building_ai_qa_engineer_claude_code_playwright/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "building_ai_qa_engineer_claude_code_playwright";

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
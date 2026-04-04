# Source: https://docs.trackjs.com/browser-agent/tips-and-tricks/monitor-memory/

Title: Monitoring JavaScript Memory

URL Source: https://docs.trackjs.com/browser-agent/tips-and-tricks/monitor-memory/

Markdown Content:
JavaScript memory leaks can severely impact application performance and user experience, but they’re notoriously difficult to catch in production. While browser memory APIs are limited and deprecated, you can still implement basic memory monitoring to catch critical issues before they affect your users.

For a detailed guide on JavaScript memory leak patterns and prevention strategies, see our blog post: [How to Monitor JavaScript Memory Leaks in Production](https://trackjs.com/blog/monitoring-javascript-memory-leaks-production/).

[Basic Memory Usage Monitoring](https://docs.trackjs.com/browser-agent/tips-and-tricks/monitor-memory/#basic-memory-usage-monitoring "Permalink Here")
------------------------------------------------------------------------------------------------------------------------------------------------------

Add this snippet to monitor memory usage and track an error when heap usage exceeds 90%:

if ("performance" in window && performance.memory) { const memoryCheckInterval = setInterval(() => { const errorThresholdPct = 0.90; if (performance.memory.usedJSHeapSize >= (performance.memory.jsHeapSizeLimit * errorThresholdPct)) { console.warn(`{"totalJSHeapSize":${performance.memory.totalJSHeapSize},"usedJSHeapSize":${performance.memory.usedJSHeapSize},"jsHeapSizeLimit":${performance.memory.jsHeapSizeLimit}}`); if (window.TrackJS && TrackJS.track) { TrackJS.track("Approaching maximum memory"); } // Stop checking after alert clearInterval(memoryCheckInterval); } }, 5000); // Check every 5 seconds}

[Memory Usage Monitor](https://docs.trackjs.com/browser-agent/tips-and-tricks/monitor-memory/#code-memory-usage-monitor)

**Note:** The `performance.memory` API is deprecated and only works in Chromium-based browsers. The values may not be perfectly accurate, but they can still help identify severe memory issues in production.

[Adding Memory Usage to Telemetry](https://docs.trackjs.com/browser-agent/tips-and-tricks/monitor-memory/#adding-memory-usage-to-telemetry "Permalink Here")
------------------------------------------------------------------------------------------------------------------------------------------------------------

To correlate memory usage with user actions and errors, log memory information to the console. TrackJS will automatically capture these console logs as telemetry:

function logMemoryUsage(action) { if ("performance" in window && performance.memory) { const memoryMB = Math.round(performance.memory.usedJSHeapSize / 1048576); console.info(`${action} - Memory: ${memoryMB}MB`); }}// Use throughout your application logMemoryUsage("Page loaded"); logMemoryUsage("Modal opened"); logMemoryUsage("Data fetched");

[Memory Telemetry Logger](https://docs.trackjs.com/browser-agent/tips-and-tricks/monitor-memory/#code-memory-telemetry-logger)

This telemetry will appear in your TrackJS error reports, helping you understand memory usage patterns leading up to errors.

[Monitoring DOM Growth](https://docs.trackjs.com/browser-agent/tips-and-tricks/monitor-memory/#monitoring-dom-growth "Permalink Here")
--------------------------------------------------------------------------------------------------------------------------------------

Memory leaks often manifest as DOM nodes that never get cleaned up. Monitor DOM size to catch these issues:

let lastNodeCount = 0; setInterval(() => { const currentNodes = document.getElementsByTagName("*").length; // Alert if DOM has grown by 50% and exceeds 1000 nodes if (currentNodes > lastNodeCount * 1.5 && currentNodes > 1000) { console.warn(`DOM growth detected: ${currentNodes} nodes`); if (window.TrackJS && TrackJS.track) { TrackJS.track(`Excessive DOM growth: ${currentNodes} nodes`); } } lastNodeCount = currentNodes;}, 30000); // Check every 30 seconds

[DOM Growth Monitor](https://docs.trackjs.com/browser-agent/tips-and-tricks/monitor-memory/#code-dom-growth-monitor)

[Best Practices](https://docs.trackjs.com/browser-agent/tips-and-tricks/monitor-memory/#best-practices "Permalink Here")
------------------------------------------------------------------------------------------------------------------------

1.   **Don’t over-monitor**: Check memory every 5-10 seconds at most to avoid performance impact
2.   **Set reasonable thresholds**: 90% heap usage is critical, but normal usage patterns vary by application
3.   **Combine with other metrics**: Memory issues often correlate with slow performance or increased errors
4.   **Test in production-like environments**: Memory behavior differs significantly between development and production

[Limitations](https://docs.trackjs.com/browser-agent/tips-and-tricks/monitor-memory/#limitations "Permalink Here")
------------------------------------------------------------------------------------------------------------------

*   Only works in Chromium-based browsers (Chrome, Edge, Opera)
*   Memory values are estimates and may not reflect actual memory pressure
*   Cannot prevent memory leaks, only detect them
*   No standardized cross-browser alternative currently exists

Despite these limitations, basic memory monitoring can help you catch severe issues and improve application reliability. Combined with TrackJS error tracking and telemetry, you’ll have better visibility into memory-related problems affecting your users.

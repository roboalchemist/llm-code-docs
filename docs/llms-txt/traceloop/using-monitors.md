# Source: https://www.traceloop.com/docs/monitoring/using-monitors.md

# Using Monitors

> Learn how to view, analyze, and act on monitor results in your LLM applications

Once you've created monitors, Traceloop continuously evaluates your LLM outputs and provides insights into their performance. This guide explains how to interpret and act on monitor results.

## Monitor Dashboard

The Monitor Dashboard provides an overview of all active monitors and their current status.
It shows each monitor’s health, the number of times it has run, and the most recent execution time.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-light.png?fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=30a73ea21acf37932c555562f725543d" data-og-width="2464" width="2464" data-og-height="640" height="640" data-path="img/monitor/monitor-list-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-light.png?w=280&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=85fda1e47b38bc90c2648e1a0acc8446 280w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-light.png?w=560&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=52b421f78ec768b573a8a0b69035fc41 560w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-light.png?w=840&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=75a062bf0645a72a4cfeb37e9a366994 840w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-light.png?w=1100&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=f23bdd12b8455e6982b5938387af235e 1100w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-light.png?w=1650&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=ea458a1e2d79db8e234dba522de90778 1650w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-light.png?w=2500&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=feea6bdf4053cac87e91c6297c9b0953 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-dark.png?fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=d3856b465eaf0a313f8d68c015f3b11b" data-og-width="2456" width="2456" data-og-height="650" height="650" data-path="img/monitor/monitor-list-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-dark.png?w=280&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=86feeb8f3346c34c5e61e758e6505414 280w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-dark.png?w=560&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=0716483ddec0796643c43948daa07301 560w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-dark.png?w=840&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=eea8087dab9cf76768b945144a6de930 840w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-dark.png?w=1100&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=f5caa6a5549ff434693e5167f6e42ec2 1100w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-dark.png?w=1650&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=345a0850f093beff67b9fe9100e940f6 1650w, https://mintcdn.com/enrolla/f92M4jgLiPyzhzrI/img/monitor/monitor-list-dark.png?w=2500&fit=max&auto=format&n=f92M4jgLiPyzhzrI&q=85&s=7df3a76d26001cf279a67517da5675d5 2500w" />
</Frame>

## Viewing Monitor Results

### Real-time Monitoring

Monitor results are displayed in real-time as your LLM applications generate new spans. You can view:

* **Run Details**: The span value that was evaluated and its result
* **Trend Analysis**: Performance over time
* **Volume Metrics**: Number of evaluations performed
* **Evaluator Output Rates**: Such as success rates for threshold-based evaluators

### Monitor Results Page

Click on any monitor to access its detailed results page. The monitor page provides comprehensive analytics and span-level details.

#### Chart Visualizations

The Monitor page includes multiple chart views to help you analyze your data, and you can switch between chart types using the selector in the top-right corner.

**Line Chart View** - Shows evaluation trends over time:

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-light.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=bcacca5096e53a569970c17fcecf0d8a" data-og-width="3538" width="3538" data-og-height="2018" height="2018" data-path="img/monitor/monitor-page-line-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-light.png?w=280&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=bd714ec4bcb3f7cc7aa2566a130f9665 280w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-light.png?w=560&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=0a7238c51f943c3855485184a503e267 560w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-light.png?w=840&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=03a39499add955563caac24467885e01 840w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-light.png?w=1100&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=28654624a3c50e73afc7aa0b2d1484e6 1100w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-light.png?w=1650&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=bcd53e20a3a3941a26e106cb1523c4e8 1650w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-light.png?w=2500&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=93c2dc25c9b2b5bbb1772de73b225198 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-dark.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=c9249577d43a7098883e30cb505abbde" data-og-width="3532" width="3532" data-og-height="2018" height="2018" data-path="img/monitor/monitor-page-line-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-dark.png?w=280&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=1d35692ad9a4641fe021771f68890b93 280w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-dark.png?w=560&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=8989d4e802521bed189cc77a19f9011c 560w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-dark.png?w=840&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=191cd29eb139a4033d08b84c35e7f3d8 840w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-dark.png?w=1100&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=ad7495ada812b635791516f649f3199e 1100w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-dark.png?w=1650&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=494a16c63220cda58bcd4a5444ee6ee0 1650w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-line-dark.png?w=2500&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=7810fbed1f9d5c362bf368fc36da6f8a 2500w" />
</Frame>

**Bar Chart View** - Displays evaluation results in time buckets:

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-light.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=faf09c414909355ea856ae7f44328d90" data-og-width="3550" width="3550" data-og-height="2020" height="2020" data-path="img/monitor/monitor-page-buckets-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-light.png?w=280&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=f473490a880a24be706fdae1f292c0cb 280w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-light.png?w=560&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=b59e90f300026cb440d9d9f7e2dafa8f 560w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-light.png?w=840&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=07feb355059f7860f85116318976d972 840w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-light.png?w=1100&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=a825bef37af8404cf1a98850bd4f95e8 1100w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-light.png?w=1650&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=b1b110dcc12dade0e5eb0cb9c92ab90c 1650w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-light.png?w=2500&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=59972434ef6c867f1e72ff4be698ccd8 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-dark.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=1ecf640aff45d206120ff6282eec02b3" data-og-width="3550" width="3550" data-og-height="1882" height="1882" data-path="img/monitor/monitor-page-buckets-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-dark.png?w=280&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=21c337525fc8679f830ebf68251e73d9 280w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-dark.png?w=560&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=587a3d4c9ab6c4551e66907922ecdc7a 560w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-dark.png?w=840&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=88aebd07c2449e0c7611381c840be524 840w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-dark.png?w=1100&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=f6650d10f4c6a7de3fee70b7ecb936cc 1100w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-dark.png?w=1650&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=f7ca68ae5966604d70e3aa12dd88150c 1650w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/monitor/monitor-page-buckets-dark.png?w=2500&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=96d2a28c7b279418be36ec0006099df0 2500w" />
</Frame>

#### Filtering and Time Controls

The top toolbar provides filtering options:

* **Environment**: Filter by production, staging, etc.
* **Time Range**: 24h, 7d, 14d, or custom ranges
* **Metric**: Select which evaluator output property to measure
* **Bucket Size**: 6h, Hourly, Daily, etc.
* **Aggregation**: Choose average, median, sum, min, max, or count

#### Matching Spans Table

The bottom section shows all spans that matched your monitor's filter criteria:

* **Timestamp**: When the evaluation occurred
* **Input**: The actual content that was mapped to be evaluated
* **Output**: The evaluation result/score
* **Completed Runs**: Total successful/error evaluations
* **Error Runs**: Failed evaluation attempts

Each row includes a link icon to view the full span details in the trace explorer:

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=2733424bcb797188846417e2516e50fe" data-og-width="3014" width="3014" data-og-height="1798" height="1798" data-path="img/trace/trace-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?w=280&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=c024b621caac98fb924006c3e2fdf3e2 280w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?w=560&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=ab9ba8134ba04bdfefb6a56c44f03256 560w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?w=840&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=637f82f9dd748f77b39a80591f34ab9d 840w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?w=1100&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=b47f4145aad5d3ac1f78646d6b000b05 1100w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?w=1650&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=176db5b65b57b786248777ac9660de8f 1650w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?w=2500&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=fac61fd5dc7f341881afe09c4a25cc67 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=740795f397c532c9080a91ea521a3a7e" data-og-width="3024" width="3024" data-og-height="1806" height="1806" data-path="img/trace/trace-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?w=280&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=2146004180f5dce3c59c73da4e4445f1 280w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?w=560&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=277eb56b1e83c16a15de79612b490935 560w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?w=840&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=d64bec8d366115d0070c6ac5fdf34855 840w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?w=1100&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=c892fe1ad02e8b04c94171ebf5b7fbad 1100w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?w=1650&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=8625ee39f6877740038d00c9ca5d97a4 1650w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?w=2500&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=966a935d28281d3b9e1944e97e8ea6c6 2500w" />
</Frame>

For further information on tracing refer to [OpenLLMetry](/openllmetry/introduction).

<Tip>
  Ready to set up an evaluator for your monitor? Learn more about creating and configuring evaluators in the [Evaluators](/evaluators/intro) section.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt
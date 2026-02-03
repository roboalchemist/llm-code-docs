# Source: https://docs.intelligems.io/developer-resources/external-api/automations-and-guides/build-a-multi-client-test-overview-dashboard.md

# Build a Multi-Client Test Overview Dashboard

## Overview:

This guide provides a walkthrough for building a centralized, multi-client testing dashboard using the Intelligems External API. By consolidating data from multiple accounts into a single interface, your agency can monitor experiment performance, track key metrics like Conversion Rate and Revenue per Visitor (RPV), and identify winning tests without the friction of constant account switching.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FCXsmguKVCyi7B0e3M00T%2FScreenshot%202026-01-16%20at%2011.19.23%E2%80%AFAM.png?alt=media&#x26;token=3f426027-34c2-4a5b-b41a-b00a9cf64e03" alt=""><figcaption></figcaption></figure>

### Tools Used:

This guide uses the following tools:

* The Terminal: You will use the command line to initialize your project and execute deployment commands.
* Netlify: This platform will host the dashboard and manage the Serverless Functions (Node.js) used to securely fetch and process data from the Intelligems External API.

{% hint style="info" %}
Want to use your own softwares? Give Claude/Gemini/ChatGPT this article and ask how to recreate this but with X software instead so that your report uses existing company tools.
{% endhint %}

### Prerequisite <a href="#prerequisite" id="prerequisite"></a>

* Requires a [Netlify](https://app.netlify.com/) account (free plan available!)

## Step 1: Create desktop folder structure

On your desktop, create a new file titled *intelligems-dashboard*.

Inside it, create the following folder structure:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FVNLX0TMmjlTyKWzsYNLT%2FScreenshot%202026-01-15%20at%2012.32.33%E2%80%AFPM.png?alt=media&#x26;token=f3d6beeb-55c7-406a-98c2-f81818915854" alt=""><figcaption></figcaption></figure>

## Step 2: Add an api.js file to the functions folder

If you're using a Mac, you can create an .js document by:

1. Open **TextEdit** (in your Applications folder)
2. In the top menu bar, Go to **TextEdit** → **Settings**
3. Click **"Plain Text"** (very important - NOT Rich Text)
4. Close Settings
5. Create new document: **File** → **New**
6. Paste your code (shown below!)
7. **File** → **Save As**
   * Uncheck "If no extension is provided, use .txt"
   * Name it: `api.js`
   * Location: Navigate to `intelligems-dashboard/netlify/functions/`
   * Click **Save**

Here's the code to put in your api.js file:

```
exports.handler = async (event) => {
  try {
    const rawKeys = process.env.INTELLIGEMS_KEYS || "[]";
    const clients = JSON.parse(rawKeys);

    const allResults = await Promise.all(clients.map(async (client) => {
      try {
        const listRes = await fetch('https://api.intelligems.io/v25-10-beta/experiences-list?status=started', {
          headers: { 'intelligems-access-token': client.key }
        });
        const listData = await listRes.json();
        const experiences = listData.experiencesList || [];

        return await Promise.all(experiences.map(async (exp) => {
          try {
            const analyticsRes = await fetch(`https://api.intelligems.io/v25-10-beta/analytics/resource/${exp.id}`, {
              headers: { 'intelligems-access-token': client.key }
            });
            const analyticsData = await analyticsRes.json();

            const testVariant = analyticsData.variations?.find(v => v.isControl === false);
            const testVariantId = testVariant?.id;
            const vM = analyticsData.metrics?.find(m => m.variation_id === testVariantId) || {};

            const getUpliftPct = (metric) => {
              const val = metric?.uplift?.value;
              return val !== undefined ? (val * 100).toFixed(2) : "0.00";
            };

            return {
              id: exp.id,
              clientName: client.name,
              name: analyticsData.experienceName || exp.name || "Unnamed Test",
              status: exp.status,
              // Only keeping the requested columns
              conversion: getUpliftPct(vM.conversion_rate), 
              rpv: getUpliftPct(vM.net_revenue_per_visitor),
              gpv: getUpliftPct(vM.gross_profit_per_visitor),
              aov: getUpliftPct(vM.net_product_revenue_per_order), 
              url: `https://app.intelligems.io/experiment/${exp.id}`
            };
          } catch (err) {
            console.error(`Error fetching analytics for ${exp.id}:`, err);
            return null;
          }
        }));
      } catch (err) {
        console.error(`Error fetching experience list for ${client.name}:`, err);
        return [];
      }
    }));

    const finalData = allResults.flat().filter(item => item !== null);

    return {
      statusCode: 200,
      headers: { 
        "Content-Type": "application/json", 
        "Access-Control-Allow-Origin": "*" 
      },
      body: JSON.stringify(finalData),
    };
  } catch (error) {
    return { 
      statusCode: 500, 
      body: JSON.stringify({ error: error.message }) 
    };
  }
};
```

## Step 3: Add an netlify.toml file to the intelligems-dashboard folder&#x20;

If you're using a Mac, you can create an .toml document by:

1. Open **TextEdit** (in your Applications folder)
2. In the top menu bar, Go to **TextEdit** → **Settings** (you should have already done this is Step 2)
   1. Click **"Plain Text"** (very important - NOT Rich Text)
   2. Close Settings
3. Create new document: **File** → **New**
4. Paste your code (shown below!)
5. **File** → **Save As**
   * Uncheck "If no extension is provided, use .txt"
   * Name it: `netlify.toml`
   * Location: Navigate to `intelligems-dashboard/`
   * Click **Save**

Here's the code to put in your netlify.toml file:

```
[build]
  publish = "."
  functions = "netlify/functions"

[functions]
  node_bundler = "esbuild"
  external_node_modules = ["node-fetch"]
```

## Step 4: Add an index.html file to the intelligems-dashboard folder&#x20;

If you're using a Mac, you can create an .html document by:

1. Open **TextEdit** (in your Applications folder)
2. In the top menu bar, Go to **TextEdit** → **Settings** (you should have already done this is Step 2)
   1. Click **"Plain Text"** (very important - NOT Rich Text)
   2. Close Settings
3. Create new document: **File** → **New**
4. Paste your code (shown below!)
5. **File** → **Save As**
   * Uncheck "If no extension is provided, use .txt"
   * Name it: `index.html`
   * Location: Navigate to `intelligems-dashboard/`
   * Click **Save**

Here's the code to put in your index.html file (Callout: In the code below, update "intelligems2026" with your own desired password for this page):

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Marketing Agency Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-slate-100 p-6">
    <div class="max-w-[1600px] mx-auto">
        <div class="flex justify-between items-center mb-6">
            <h1 class="text-xl font-bold border-l-4 border-blue-500 pl-4">Client Performance Monitor</h1>
            <button onclick="loadData()" class="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded text-xs font-bold transition">REFRESH ALL CLIENTS</button>
        </div>
        
        <div class="bg-slate-800 rounded-xl shadow-2xl overflow-x-auto border border-slate-700">
            <table class="w-full text-left border-collapse">
                <thead class="bg-slate-700/50 text-[10px] uppercase tracking-widest text-slate-400">
                    <tr>
                        <th class="p-4 cursor-pointer hover:text-white" onclick="sortTable('clientName')">Client ↕</th>
                        <th class="p-4 cursor-pointer hover:text-white" onclick="sortTable('name')">Test Name ↕</th>
                        <th class="p-4 text-center">Conv Rate</th>
                        <th class="p-4 text-center">RPV Uplift</th>
                        <th class="p-4 text-center">GPV Uplift</th>
                        <th class="p-4 text-center">AOV Uplift</th>
                        <th class="p-4 text-right">Link</th>
                    </tr>
                </thead>
                <tbody id="dashboard-body" class="divide-y divide-slate-700">
                    <tr><td colspan="7" class="p-10 text-center text-slate-500">Connecting to Intelligems...</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <script>
        // Simple password protection
        (function() {
            const DASHBOARD_PASSWORD = 'intelligems2026';
            const hasAccess = sessionStorage.getItem('dashboard_access');
            
            if (!hasAccess) {
                const password = prompt('Enter dashboard password:');
                if (password !== DASHBOARD_PASSWORD) {
                    document.body.innerHTML = '<div style="display:flex;align-items:center;justify-content:center;height:100vh;font-family:sans-serif;"><h1 style="color:#ef4444;font-size:32px;font-weight:bold;">Access Denied</h1></div>';
                    throw new Error('Access denied');
                }
                sessionStorage.setItem('dashboard_access', 'true');
            }
        })();

        let testData = [];

        async function loadData() {
            const body = document.getElementById('dashboard-body');
            body.innerHTML = `<tr><td colspan="7" class="p-10 text-center text-blue-400 animate-pulse font-bold text-sm tracking-widest">FETCHING DETAILED ANALYTICS...</td></tr>`;
            try {
                const res = await fetch('/.netlify/functions/api?t=' + Date.now());
                testData = await res.json();
                renderTable(testData);
            } catch (err) {
                body.innerHTML = `<tr><td colspan="7" class="p-10 text-center text-red-400 font-bold">Error: Connection Failed</td></tr>`;
            }
        }

        function renderTable(data) {
            const body = document.getElementById('dashboard-body');
            if (!data || data.length === 0) {
                body.innerHTML = `<tr><td colspan="7" class="p-10 text-center text-slate-500">No active tests found.</td></tr>`;
                return;
            }

            body.innerHTML = data.map(test => {
                // Formatting helper: now consistently uses % as requested
                const format = (val) => {
                    const num = parseFloat(val) || 0;
                    const color = num > 0 ? 'text-emerald-400' : (num < 0 ? 'text-rose-400' : 'text-slate-500');
                    // All values are treated as percentages
                    return `<span class="font-mono font-bold ${color}">${num.toFixed(2)}%</span>`;
                };

                return `
                <tr class="hover:bg-slate-700/40 transition-colors">
                    <td class="p-4 font-bold text-blue-400 text-sm">${test.clientName}</td>
                    <td class="p-4 text-xs font-medium text-slate-300 max-w-[200px] truncate">${test.name}</td>
                    <td class="p-4 text-center">${format(test.conversion)}</td>
                    <td class="p-4 text-center">${format(test.rpv)}</td>
                    <td class="p-4 text-center">${format(test.gpv)}</td>
                    <td class="p-4 text-center">${format(test.aov)}</td>
                    <td class="p-4 text-right">
                        <a href="${test.url}" target="_blank" class="text-[10px] bg-slate-700 hover:bg-slate-600 px-3 py-1.5 rounded font-black text-slate-200 uppercase">View ↗</a>
                    </td>
                </tr>
            `}).join('');
        }

        function sortTable(key) {
            testData.sort((a, b) => {
                const valA = a[key] ? String(a[key]) : "";
                const valB = b[key] ? String(b[key]) : "";
                return valA.localeCompare(valB);
            });
            renderTable(testData);
        }

        loadData();
    </script>
</body>
</html>
```

## Step 5: Add a package.json file to the intelligems-dashboard folder&#x20;

If you're using a Mac, you can create an .html document by:

1. Open **TextEdit** (in your Applications folder)
2. In the top menu bar, Go to **TextEdit** → **Settings** (you should have already done this is Step 2)
   1. Click **"Plain Text"** (very important - NOT Rich Text)
   2. Close Settings
3. Create new document: **File** → **New**
4. Paste your code (shown below!)
5. **File** → **Save As**
   * Uncheck "If no extension is provided, use .txt"
   * Name it: `package.json`
   * Location: Navigate to `intelligems-dashboard/`
   * Click **Save**

Here's the code to put in your index.html file:

```
{
  "name": "intelligems-dashboard",
  "version": "1.0.0",
  "description": "Dashboard for Intelligems test results",
  "dependencies": {
    "node-fetch": "^2.6.7"
  }
}
```

## Step 6: Deploy to Netlify

Go to [app.netlify.com](https://app.netlify.com) and sign up (free).

Find & open the Terminal Application on your computer.

![](https://docs.intelligems.io/~gitbook/image?url=https%3A%2F%2F2052204893-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2SvefuMLsJyJPAcVXeWc%252Fuploads%252FDjdWSpcTHZm3VdZitzGs%252FScreenshot%25202026-01-13%2520at%25201.20.50%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D23af913e-e0db-4173-a835-0a4d1f83e9b4\&width=768\&dpr=4\&quality=100\&sign=165e3efc\&sv=2)

Install Netlify CLI by pasting the following code into Terminal and hitting enter:

```
npm install -g netlify-cli
```

Navigate to your project folder in terminal by pasting the following code into Terminal and hitting enter:

```
cd ~/Desktop/intelligems-dashboard
```

Login to Netlify by pasting the following code into Terminal and hitting enter (this will open your browser - click "Authorize" when it does):

```
netlify login
```

Deploy to your site by pasting the following code into Terminal and hitting enter:

```
netlify deploy
```

In terminal, you'll be prompted with a few questions. Answer them the following way (navigate with arrow keys & hit enter to select the highlighted answer):

* Choose to "Create & configure a new project"
* Choose your team
* Write in a site name like "YOURCOMPANY-intelligems-dashboard"

Now deploy this to production by pasting the below code into your Terminal and pressing enter:

```
netlify deploy --prod
```

## Step 7: Add your API keys

In your browser, go to your [Netlify dashboard](https://app.netlify.com/).

Click on your YOURCOMPANY-intelligems-dashboard project.

Navigate to project configuration > Environment variables > Add a variable > Add a single variable

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FNQHwCJzUOg0gtSq9Klfh%2FScreenshot%202026-01-15%20at%204.14.38%E2%80%AFPM.png?alt=media&#x26;token=9ef89c1e-8e68-4f7c-a554-0b21109738e1" alt=""><figcaption></figcaption></figure>

Set the key value to INTELLIGEMS\_KEY&#x53;*.*

Set the value to your Intelligems API Key(s). \[[How to get Intelligems API Key](https://docs.intelligems.io/developer-resources/external-api#getting-started)] Follow this format:

```
[{"name":"Client One", "key":"ig_live_1111"}, {"name":"Client Two", "key":"ig_live_2222"}]
```

Replace "Client One" with yourself or if you're an agency, replace this with the name of the client associated with the API Key.

Select Create Variable.

Redeploy by pasting the below code into Terminal and hitting enter:

```
netlify deploy --prod
```

## Step 8: Visit your dashboard

In terminal, it will display your production URL. It'll be formatting like <https://INSERT.netlify.app>

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FLMKeWzcEMeQ8kXTZFRww%2FScreenshot%202026-01-16%20at%2010.41.25%E2%80%AFAM.png?alt=media&#x26;token=44d84b6a-61e4-4e30-81f2-834ec28d627c" alt=""><figcaption></figcaption></figure>

When you visit this URL, it'll prompt you for a password (unless you changed it in the code above it'll be intelligems2026). Once you enter your password, you'll see your new Multi-Client Dashboard!:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F4iPxd2U6iSlrXZWpDB7L%2FScreenshot%202026-01-16%20at%2011.19.23%E2%80%AFAM.png?alt=media&#x26;token=7cda918f-c639-4620-bff8-52ee28dd0b99" alt=""><figcaption></figcaption></figure>

## Bonus: Enhancements

You can customize this dashboard with specific metrics you are looking for! Here are a few ideas of metrics you can include & their mapping for the API:

* Total visitors per variant
  * API: GET `/v25-10-beta/analytics/resource/{experienceId}`
  * Metric: `metrics[].n_visitors.value` (where `variation_id == [ID]`)
* Total orders per variant
  * API: GET `/v25-10-beta/analytics/resource/{experienceId}`
  * Metric: `metrics[].n_orders.value` (where `variation_id == [ID]`)
* Total revenue per variant
  * API: GET `/v25-10-beta/analytics/resource/{experienceId}`
  * Metric: `metrics[].net_revenue.value` (where `variation_id == [ID]`)
* Launch date
  * API: GET `/v25-10-beta/experiences-list`
  * Metrics: `experiencesList[0].startedAtTs`
* Total tests launched within the last 30 days
  * API: GET `/v25-10-beta/experiences-list`
  * Metric: Filter the `experiencesList` for objects where `startedAtTs` is less than or equal to 30 days ago.
* List of tests in draft
  * API: GET `/v25-10-beta/experiences-list`
  * Metric: use `experiencesList[].status` (where the status is `pending`)

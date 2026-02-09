# Source: https://docs.pinata.cloud/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Start uploading and retrieving content in no time

<img style={{ width:"100%",borderRadius:"0.5rem" }} src="https://mintcdn.com/pinata/09jphG_rC0WCVTMW/assets/hero.png?fit=max&auto=format&n=09jphG_rC0WCVTMW&q=85&s=95297a18fcd1c80bef2f0e46d8ea85b0" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="assets/hero.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinata/09jphG_rC0WCVTMW/assets/hero.png?w=280&fit=max&auto=format&n=09jphG_rC0WCVTMW&q=85&s=5c1566e77a2caece80509dc03928cef3 280w, https://mintcdn.com/pinata/09jphG_rC0WCVTMW/assets/hero.png?w=560&fit=max&auto=format&n=09jphG_rC0WCVTMW&q=85&s=204381c67d5efab5c5f7c3cb9be37ada 560w, https://mintcdn.com/pinata/09jphG_rC0WCVTMW/assets/hero.png?w=840&fit=max&auto=format&n=09jphG_rC0WCVTMW&q=85&s=65fd318eeb23036c1c28122b5d3f894f 840w, https://mintcdn.com/pinata/09jphG_rC0WCVTMW/assets/hero.png?w=1100&fit=max&auto=format&n=09jphG_rC0WCVTMW&q=85&s=8955b68fd16e765a25b3a5b3ef84ee97 1100w, https://mintcdn.com/pinata/09jphG_rC0WCVTMW/assets/hero.png?w=1650&fit=max&auto=format&n=09jphG_rC0WCVTMW&q=85&s=cf457d49ca6e7cd2ef3651630f1362bb 1650w, https://mintcdn.com/pinata/09jphG_rC0WCVTMW/assets/hero.png?w=2500&fit=max&auto=format&n=09jphG_rC0WCVTMW&q=85&s=2d72ab84231016d3ec2dcf704cea91ea 2500w" />

## Getting Started with Pinata

Whether you're brand new or a seasoned developer, Pinata makes it simple to store and retrieve content with speed and security. All you need to kick off your journey is a [free Pinata account](https://app.pinata.cloud/register)!

<CardGroup cols={3}>
  <Card title="Next.Js" icon="https://mintlify.s3.us-west-1.amazonaws.com/pinata/%3Csvg%20width=%22800px%22%20height=%22800px%22%20class=%22h-6%20w-6%22%20viewBox=%220%200%20256%20256%22%20version=%221.1%22%20xmlns=%22http:/www.w3.org/2000/svg%22%20xmlns:xlink=%22http:/www.w3.org/1999/xlink%22%20preserveAspectRatio=%22xMidYMid%22%3E%3Cg%3E%3Cpath%20d=%22M119.616813,0.0688905149%20C119.066276,0.118932037%20117.314565,0.294077364%20115.738025,0.419181169%20C79.3775171,3.69690087%2045.3192571,23.3131775%2023.7481916,53.4631946%20C11.7364614,70.2271045%204.05395894,89.2428829%201.15112414,109.384595%20C0.12512219,116.415429%200,118.492153%200,128.025062%20C0,137.557972%200.12512219,139.634696%201.15112414,146.665529%20C8.10791789,194.730411%2042.3163245,235.11392%2088.7116325,250.076335%20C97.0197458,252.753556%20105.778299,254.580072%20115.738025,255.680985%20C119.616813,256.106338%20136.383187,256.106338%20140.261975,255.680985%20C157.453763,253.779407%20172.017986,249.525878%20186.382014,242.194795%20C188.584164,241.068861%20189.00958,240.768612%20188.709286,240.518404%20C188.509091,240.36828%20179.124927,227.782837%20167.86393,212.570214%20L147.393939,184.922273%20L121.743891,146.965779%20C107.630108,126.098464%2096.0187683,109.034305%2095.9186706,109.034305%20C95.8185728,109.009284%2095.7184751,125.873277%2095.6684262,146.465363%20C95.5933529,182.52028%2095.5683284,183.971484%2095.1178886,184.82219%20C94.4672532,186.048207%2093.9667644,186.548623%2092.915738,187.099079%20C92.114956,187.499411%2091.4142717,187.574474%2087.6355816,187.574474%20L83.3063539,187.574474%20L82.1552297,186.848872%20C81.4044966,186.373477%2080.8539589,185.747958%2080.4785924,185.022356%20L79.9530792,183.896422%20L80.0031281,133.729796%20L80.0782014,83.5381493%20L80.8539589,82.5623397%20C81.25435,82.0369037%2082.1051808,81.3613431%2082.7057674,81.0360732%20C83.7317693,80.535658%2084.1321603,80.4856165%2088.4613881,80.4856165%20C93.5663734,80.4856165%2094.4172043,80.6857826%2095.7434995,82.1369867%20C96.1188661,82.5373189%20110.007429,103.454675%20126.623656,128.650581%20C143.239883,153.846488%20165.962072,188.250034%20177.122972,205.139048%20L197.392766,235.839522%20L198.418768,235.163961%20C207.502639,229.259062%20217.112023,220.852086%20224.719453,212.09482%20C240.910264,193.504394%20251.345455,170.835585%20254.848876,146.665529%20C255.874878,139.634696%20256,137.557972%20256,128.025062%20C256,118.492153%20255.874878,116.415429%20254.848876,109.384595%20C247.892082,61.3197135%20213.683675,20.9362052%20167.288368,5.97379012%20C159.105376,3.32158945%20150.396872,1.49507389%20140.637341,0.394160408%20C138.234995,0.143952798%20121.693842,-0.131275573%20119.616813,0.0688905149%20L119.616813,0.0688905149%20Z%20M172.017986,77.4831252%20C173.219159,78.0836234%20174.195112,79.2345784%20174.545455,80.435575%20C174.74565,81.0861148%20174.795699,94.9976579%20174.74565,126.348671%20L174.670577,171.336%20L166.73783,159.17591%20L158.780059,147.01582%20L158.780059,114.313685%20C158.780059,93.1711423%20158.880156,81.2862808%20159.030303,80.7108033%20C159.430694,79.3096407%20160.306549,78.2087272%20161.507722,77.5581875%20C162.533724,77.0327515%20162.909091,76.98271%20166.837928,76.98271%20C170.541544,76.98271%20171.19218,77.0327515%20172.017986,77.4831252%20Z%22%3E%3C/path%3E%3C/g%3E%3C/svg%3E" horizontal href="/frameworks/next-js">
    Quickstart
  </Card>

  <Card title="Hono" icon="https://mintlify.s3.us-west-1.amazonaws.com/pinata/%3Csvg%20xmlns=%22http:/www.w3.org/2000/svg%22%20class=%22h-6%20w-6%22%20width=%2224.83%22%20height=%2232%22%20viewBox=%220%200%20256%20330%22%3E%3Cpath%20fill=%22%23FF5B11%22%20d=%22M134.129.029q1.315-.17%202.319.662a1256%201256%200%200%201%2069.573%2093.427q24.141%2036.346%2041.082%2076.862q27.055%2072.162-28.16%20125.564q-48.313%2040.83-111.318%2031.805q-75.312-15.355-102.373-87.133Q-1.796%20217.85.614%20193.51q4.014-41.896%2019.878-80.838q6.61-15.888%2017.228-29.154a382%20382%200%200%201%2016.565%2021.203q3.66%203.825%207.62%207.289Q92.138%2052.013%20134.13.029%22%20opacity=%22.993%22/%3E%3Cpath%20fill=%22%23FF9758%22%20d=%22M129.49%2053.7q36.47%2042.3%2065.93%2090.114a187.3%20187.3%200%200%201%2015.24%2033.13q12.507%2049.206-26.836%2081.169q-38.05%2026.774-83.488%2015.902q-48.999-15.205-56.653-65.929q-1.857-15.993%203.314-31.142a225.4%20225.4%200%200%201%2017.89-35.78l19.878-29.155a5510%205510%200%200%200%2044.726-58.31%22/%3E%3C/svg%3E" horizontal href="/frameworks/hono">
    Quickstart
  </Card>

  <Card title="React" icon="https://mintlify.s3.us-west-1.amazonaws.com/pinata/%3Csvg%20xmlns=%22http:/www.w3.org/2000/svg%22%20class=%22h-6%20w-6%22%20width=%2228%22%20height=%2232%22%20viewBox=%220%200%20256%20256%22%3E%3Cpath%20fill=%22%2300D8FF%22%20d=%22M210.483%2073.824a172%20172%200%200%200-8.24-2.597c.465-1.9.893-3.777%201.273-5.621c6.238-30.281%202.16-54.676-11.769-62.708c-13.355-7.7-35.196.329-57.254%2019.526a171%20171%200%200%200-6.375%205.848a156%20156%200%200%200-4.241-3.917C100.759%203.829%2077.587-4.822%2063.673%203.233C50.33%2010.957%2046.379%2033.89%2051.995%2062.588a171%20171%200%200%200%201.892%208.48c-3.28.932-6.445%201.924-9.474%202.98C17.309%2083.498%200%2098.307%200%20113.668c0%2015.865%2018.582%2031.778%2046.812%2041.427a146%20146%200%200%200%206.921%202.165a168%20168%200%200%200-2.01%209.138c-5.354%2028.2-1.173%2050.591%2012.134%2058.266c13.744%207.926%2036.812-.22%2059.273-19.855a146%20146%200%200%200%205.342-4.923a168%20168%200%200%200%206.92%206.314c21.758%2018.722%2043.246%2026.282%2056.54%2018.586c13.731-7.949%2018.194-32.003%2012.4-61.268a145%20145%200%200%200-1.535-6.842c1.62-.48%203.21-.974%204.76-1.488c29.348-9.723%2048.443-25.443%2048.443-41.52c0-15.417-17.868-30.326-45.517-39.844m-6.365%2070.984q-2.102.694-4.3%201.345c-3.24-10.257-7.612-21.163-12.963-32.432c5.106-11%209.31-21.767%2012.459-31.957c2.619.758%205.16%201.557%207.61%202.4c23.69%208.156%2038.14%2020.213%2038.14%2029.504c0%209.896-15.606%2022.743-40.946%2031.14m-10.514%2020.834c2.562%2012.94%202.927%2024.64%201.23%2033.787c-1.524%208.219-4.59%2013.698-8.382%2015.893c-8.067%204.67-25.32-1.4-43.927-17.412a157%20157%200%200%201-6.437-5.87c7.214-7.889%2014.423-17.06%2021.459-27.246c12.376-1.098%2024.068-2.894%2034.671-5.345q.785%203.162%201.386%206.193M87.276%20214.515c-7.882%202.783-14.16%202.863-17.955.675c-8.075-4.657-11.432-22.636-6.853-46.752a157%20157%200%200%201%201.869-8.499c10.486%202.32%2022.093%203.988%2034.498%204.994c7.084%209.967%2014.501%2019.128%2021.976%2027.15a135%20135%200%200%201-4.877%204.492c-9.933%208.682-19.886%2014.842-28.658%2017.94M50.35%20144.747c-12.483-4.267-22.792-9.812-29.858-15.863c-6.35-5.437-9.555-10.836-9.555-15.216c0-9.322%2013.897-21.212%2037.076-29.293c2.813-.98%205.757-1.905%208.812-2.773c3.204%2010.42%207.406%2021.315%2012.477%2032.332c-5.137%2011.18-9.399%2022.249-12.634%2032.792a135%20135%200%200%201-6.318-1.979m12.378-84.26c-4.811-24.587-1.616-43.134%206.425-47.789c8.564-4.958%2027.502%202.111%2047.463%2019.835a144%20144%200%200%201%203.841%203.545c-7.438%207.987-14.787%2017.08-21.808%2026.988c-12.04%201.116-23.565%202.908-34.161%205.309a160%20160%200%200%201-1.76-7.887m110.427%2027.268a348%20348%200%200%200-7.785-12.803c8.168%201.033%2015.994%202.404%2023.343%204.08c-2.206%207.072-4.956%2014.465-8.193%2022.045a381%20381%200%200%200-7.365-13.322m-45.032-43.861c5.044%205.465%2010.096%2011.566%2015.065%2018.186a322%20322%200%200%200-30.257-.006c4.974-6.559%2010.069-12.652%2015.192-18.18M82.802%2087.83a323%20323%200%200%200-7.227%2013.238c-3.184-7.553-5.909-14.98-8.134-22.152c7.304-1.634%2015.093-2.97%2023.209-3.984a322%20322%200%200%200-7.848%2012.897m8.081%2065.352c-8.385-.936-16.291-2.203-23.593-3.793c2.26-7.3%205.045-14.885%208.298-22.6a321%20321%200%200%200%207.257%2013.246c2.594%204.48%205.28%208.868%208.038%2013.147m37.542%2031.03c-5.184-5.592-10.354-11.779-15.403-18.433c4.902.192%209.899.29%2014.978.29c5.218%200%2010.376-.117%2015.453-.343c-4.985%206.774-10.018%2012.97-15.028%2018.486m52.198-57.817c3.422%207.8%206.306%2015.345%208.596%2022.52c-7.422%201.694-15.436%203.058-23.88%204.071a382%20382%200%200%200%207.859-13.026a347%20347%200%200%200%207.425-13.565m-16.898%208.101a359%20359%200%200%201-12.281%2019.815a329%20329%200%200%201-23.444.823c-7.967%200-15.716-.248-23.178-.732a310%20310%200%200%201-12.513-19.846h.001a307%20307%200%200%201-10.923-20.627a310%20310%200%200%201%2010.89-20.637l-.001.001a307%20307%200%200%201%2012.413-19.761c7.613-.576%2015.42-.876%2023.31-.876H128c7.926%200%2015.743.303%2023.354.883a329%20329%200%200%201%2012.335%2019.695a359%20359%200%200%201%2011.036%2020.54a330%20330%200%200%201-11%2020.722m22.56-122.124c8.572%204.944%2011.906%2024.881%206.52%2051.026q-.518%202.504-1.15%205.09c-10.622-2.452-22.155-4.275-34.23-5.408c-7.034-10.017-14.323-19.124-21.64-27.008a161%20161%200%200%201%205.888-5.4c18.9-16.447%2036.564-22.941%2044.612-18.3M128%2090.808c12.625%200%2022.86%2010.235%2022.86%2022.86s-10.235%2022.86-22.86%2022.86s-22.86-10.235-22.86-22.86s10.235-22.86%2022.86-22.86%22/%3E%3C/svg%3E" horizontal href="/frameworks/react">
    Quickstart
  </Card>

  <Card title="Svelte" icon="https://mintlify.s3.us-west-1.amazonaws.com/pinata/%3Csvg%20class=%22h-6%20w-6%22%20xmlns=%22http:/www.w3.org/2000/svg%22%20width=%2226.6%22%20height=%2232%22%20viewBox=%220%200%20256%20308%22%3E%3Cpath%20fill=%22%23FF3E00%22%20d=%22M239.682%2040.707C211.113-.182%20154.69-12.301%20113.895%2013.69L42.247%2059.356a82.2%2082.2%200%200%200-37.135%2055.056a86.57%2086.57%200%200%200%208.536%2055.576a82.4%2082.4%200%200%200-12.296%2030.719a87.6%2087.6%200%200%200%2014.964%2066.244c28.574%2040.893%2084.997%2053.007%20125.787%2027.016l71.648-45.664a82.18%2082.18%200%200%200%2037.135-55.057a86.6%2086.6%200%200%200-8.53-55.577a82.4%2082.4%200%200%200%2012.29-30.718a87.57%2087.57%200%200%200-14.963-66.244%22/%3E%3Cpath%20fill=%22%23FFF%22%20d=%22M106.889%20270.841c-23.102%206.007-47.497-3.036-61.103-22.648a52.7%2052.7%200%200%201-9.003-39.85a50%2050%200%200%201%201.713-6.693l1.35-4.115l3.671%202.697a92.5%2092.5%200%200%200%2028.036%2014.007l2.663.808l-.245%202.659a16.07%2016.07%200%200%200%202.89%2010.656a17.14%2017.14%200%200%200%2018.397%206.828a15.8%2015.8%200%200%200%204.403-1.935l71.67-45.672a14.92%2014.92%200%200%200%206.734-9.977a15.92%2015.92%200%200%200-2.713-12.011a17.16%2017.16%200%200%200-18.404-6.832a15.8%2015.8%200%200%200-4.396%201.933l-27.35%2017.434a52.3%2052.3%200%200%201-14.553%206.391c-23.101%206.007-47.497-3.036-61.101-22.649a52.68%2052.68%200%200%201-9.004-39.849a49.43%2049.43%200%200%201%2022.34-33.114l71.664-45.677a52.2%2052.2%200%200%201%2014.563-6.398c23.101-6.007%2047.497%203.036%2061.101%2022.648a52.7%2052.7%200%200%201%209.004%2039.85a51%2051%200%200%201-1.713%206.692l-1.35%204.116l-3.67-2.693a92.4%2092.4%200%200%200-28.037-14.013l-2.664-.809l.246-2.658a16.1%2016.1%200%200%200-2.89-10.656a17.14%2017.14%200%200%200-18.398-6.828a15.8%2015.8%200%200%200-4.402%201.935l-71.67%2045.674a14.9%2014.9%200%200%200-6.73%209.975a15.9%2015.9%200%200%200%202.709%2012.012a17.16%2017.16%200%200%200%2018.404%206.832a15.8%2015.8%200%200%200%204.402-1.935l27.345-17.427a52.2%2052.2%200%200%201%2014.552-6.397c23.101-6.006%2047.497%203.037%2061.102%2022.65a52.68%2052.68%200%200%201%209.003%2039.848a49.45%2049.45%200%200%201-22.34%2033.12l-71.664%2045.673a52.2%2052.2%200%200%201-14.563%206.398%22/%3E%3C/svg%3E" horizontal href="/frameworks/sveltekit">
    Quickstart
  </Card>

  <Card title="Astro" icon="https://mintlify.s3.us-west-1.amazonaws.com/pinata/%3Csvg%20class=%22h-7%20w-7%22%20xmlns=%22http:/www.w3.org/2000/svg%22%20width=%2232%22%20height=%2232%22%20viewBox=%220%200%2032%2032%22%3E%3Cpath%20fill=%22url(%23vscodeIconsFileTypeAstro0)%22%20d=%22M11.025%2020.499c-.532%201.75-.154%204.184%201.105%205.331v-.042l.042-.112c.154-.741.756-1.203%201.526-1.175c.713.014%201.12.392%201.217%201.217c.042.308.042.616.056.938v.098c0%20.7.196%201.371.588%201.959c.35.56.84.993%201.497%201.287l-.028-.056l-.028-.112c-.49-1.469-.14-2.49%201.147-3.358l.392-.266l.868-.573a4.25%204.25%200%200%200%201.791-3.037c.07-.532%200-1.05-.154-1.553l-.21.14c-1.945%201.035-4.17%201.4-6.325.98c-1.301-.197-2.56-.56-3.498-1.652z%22/%3E%3Cpath%20fill=%22%23fff%22%20d=%22M4.925%2020.191s3.736-1.82%207.486-1.82l2.84-8.759c.098-.42.406-.7.756-.7s.644.28.756.714l2.826%208.746c4.45%200%207.487%201.82%207.487%201.82L20.709%202.84c-.168-.518-.49-.84-.896-.84h-7.612c-.406%200-.7.322-.896.84z%22/%3E%3Cdefs%3E%3ClinearGradient%20id=%22vscodeIconsFileTypeAstro0%22%20x1=%228.19%22%20x2=%2216.91%22%20y1=%2223%22%20y2=%2218.89%22%20gradientTransform=%22translate(-.673%20-2.198)scale(1.3993)%22%20gradientUnits=%22userSpaceOnUse%22%3E%3Cstop%20offset=%220%22%20stop-color=%22%23D83333%22/%3E%3Cstop%20offset=%221%22%20stop-color=%22%23F041FF%22/%3E%3C/linearGradient%3E%3C/defs%3E%3C/svg%3E" horizontal href="/frameworks/astro">
    Quickstart
  </Card>

  <Card title="Remix" icon="https://mintlify.s3.us-west-1.amazonaws.com/pinata/%3Csvg%20class=%22h-6%20w-6%22%20xmlns=%22http:/www.w3.org/2000/svg%22%20width=%2232%22%20height=%2232%22%20viewBox=%220%200%2024%2024%22%3E%3Cpath%20fill=%22%23888888%22%20d=%22M21.511%2018.508c.216%202.773.216%204.073.216%205.492H15.31c0-.309.006-.592.011-.878c.018-.892.036-1.821-.109-3.698c-.19-2.747-1.374-3.358-3.55-3.358H1.574v-5H11.97c2.748%200%204.122-.835%204.122-3.049c0-1.946-1.374-3.125-4.122-3.125H1.573V0h11.541c6.221%200%209.313%202.938%209.313%207.632c0%203.511-2.176%205.8-5.114%206.182c2.48.497%203.93%201.909%204.198%204.694M1.573%2024v-3.727h6.784c1.133%200%201.379.84%201.379%201.342V24Z%22/%3E%3C/svg%3E" horizontal href="/frameworks/remix">
    Quickstart
  </Card>
</CardGroup>

### 1. Get API key and Gateway URL

<img style={{ width:"100%",borderRadius:"0.5rem" }} src="https://docs.mypinata.cloud/ipfs/bafybeignh2yy7bp7qpts5vi46prbjd6lbz23lmtbfcgvpcwc5rjkudrfta" />

Inside the [Pinata App](https://app.pinata.cloud) select "API Keys" from the sidebar, then click "New Key" in the top right. We would recommend starting with Admin privileges and unlimited uses to start. You will receive a `pinata_api_key`, `pinata_api_secret`, and a `JWT`. The JWT is the most common authentication method and what we'll be using below.

Next you will want to grab your Gateway domain by clicking the Gateways tab in the sidebar. You should see it listed in the format `fun-llama-300.mypinata.cloud` and you will want to copy it exactly like that.

### 2. Install and Setup SDK

In the root of your project run the install command with your package manager of choice.

<CodeGroup>
  ```bash npm theme={null}
  npm i pinata
  ```

  ```bash pnpm theme={null}
  pnpm i pinata
  ```

  ```bash yarn theme={null}
  yarn add pinata
  ```

  ```bash bun theme={null}
  bun i pinata
  ```
</CodeGroup>

Import and initialize the SDK in your codebase with the API key and Gateway from the previous step

```typescript  theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: "PINATA_JWT",
  pinataGateway: "example-gateway.mypinata.cloud",
});
```

<Note>
  The `PINATA_JWT` is a secret key, be sure to initialize the SDK in a secure environment and practice basic variable security practices. If you need to upload from a client environment, consider using signed JWTs
</Note>

### 3. Upload a File

Use the `upload` method to upload a File object.

<CodeGroup>
  ```typescript SDK theme={null}
  import { PinataSDK } from "pinata";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  async function main() {
    try {
      const file = new File(["hello world!"], "hello.txt", { type: "text/plain" });
      const upload = await pinata.upload.public.file(file);
      console.log(upload);
    } catch (error) {
      console.log(error);
    }
  }

  await main();
  ```

  ```typescript API theme={null}
  const JWT = "PINATA_JWT";

  async function uploadFile() {
    try {
      const text = "hello world!";
      const blob = new Blob([text], { type: "text/plain" });
      const file = new File([blob], "hello.txt");
      const data = new FormData();
      data.append("file", file);
      data.append("network", "public")

      const request = await fetch(
        "https://uploads.pinata.cloud/v3/files",
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${JWT}`,
          },
          body: data,
        }
      );
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

You should get a response object like the one below

<CodeGroup>
  ```typescript SDK theme={null}
  {
    id: "0195f815-5c5e-716d-9240-d3ae380e2002",
    group_id: null,
    name: "hello.txt",
    cid: "bafkreidvbhs33ighmljlvr7zbv2ywwzcmp5adtf4kqvlly67cy56bdtmve",
    created_at: "2025-04-02T19:58:24.616Z",
    size: 12,
    number_of_files: 1,
    mime_type: "text/plain",
    vectorized: false,
    network: "public",
  }
  ```

  ```typescript API theme={null}
  {
    data: {
      id: "0195f815-5c5e-716d-9240-d3ae380e2002",
      group_id: null,
      name: "hello.txt",
      cid: "bafkreidvbhs33ighmljlvr7zbv2ywwzcmp5adtf4kqvlly67cy56bdtmve",
      created_at: "2025-04-02T19:58:24.616Z",
      size: 12,
      number_of_files: 1,
      mime_type: "text/plain",
      vectorized: false,
      network: "public",
    }
  }
  ```
</CodeGroup>

### 4. Retrieve a File through a Gateway

Use the `cid` of a file to fetch it through a Gateway directly or create a URL

<CodeGroup>
  ```typescript SDK theme={null}
  import { PinataSDK } from "pinata";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  async function main() {
    try {
      const data = await pinata.gateways.public.get("bafkreibm6jg3ux5qumhcn2b3flc3tyu6dmlb4xa7u5bf44yegnrjhc4yeq");
      console.log(data)

      const url = await pinata.gateways.convert(
        "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq"
      )
      console.log(url)
    } catch (error) {
      console.log(error);
    }
  }

  main();
  ```

  ```typescript API theme={null}
  const gatewayDomain = "example-llama-3000.mypinata.cloud"
  const cid = "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"
  const url = `https://${gatewayDomain}/ipfs/${cid}`
  ```
</CodeGroup>

## What's Next?

Ready to see more of what Pinata has to offer? Here are some additional features and concepts to help you get the most out of our platform:

<CardGroup cols={2}>
  <Card title="Groups" icon="cabinet-filing" color="#00cc92" href="https://docs.pinata.cloud/files/groups">
    With Groups, you can organize your files via the Pinata API or the web app. Create a Group, store your IPFS content, and fetch content quickly and easily.
  </Card>

  <Card title="Workspaces" icon="people-group" color="#00cc92" href="https://docs.pinata.cloud/account-management/workspaces">
    Workspaces allow you to add multiple team members to your Pinata account and collaborate seamlessly. Even if your team members don’t have a Pinata account, you can invite them easily. This feature is essential for efficient project collaboration and management.
  </Card>
</CardGroup>

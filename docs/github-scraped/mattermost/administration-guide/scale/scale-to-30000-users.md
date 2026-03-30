# Scale Mattermost up to 30000 users

This page describes the Mattermost reference architecture designed for
the load of up to 30000 concurrent users. Unsure which reference
architecture to use? See the
`scaling for enterprise </administration-guide/scale/scaling-for-enterprise>`{.interpreted-text
role="doc"} documentation for details.

- **High Availability**: Required
- **Database Configuration**: writer, multiple readers

:::: note
::: title
Note
:::

- Usage of CPU, RAM, and storage space can vary significantly based on
  user behavior. These hardware recommendations are based on traditional
  deployments and may grow or shrink depending on how active your users
  are.
- While the following Elasticsearch specifications may be more than
  sufficient for some use cases, we have not extensively tested
  configurations with lower resource allocations for this user scale. If
  cost optimization is a priority, admins may choose to experiment with
  smaller configurations, but we recommend starting with the tested
  specifications to ensure system stability and performance. Keep in
  mind that under-provisioning can lead to degraded user experience and
  additional troubleshooting effort.
::::

## Requirements

<style>
.scale-requirements-table {
  width: 100% !important;
  table-layout: fixed !important;
  border-collapse: collapse;
  font-size: 0.9em;
  overflow-wrap: break-word !important;
  word-wrap: break-word !important;
}
.scale-requirements-table th, .scale-requirements-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
  vertical-align: top;
  word-wrap: break-word;
  overflow-wrap: break-word;
}
.scale-requirements-table th {
  background-color: #f8f9fa;
  font-weight: bold;
}
.scale-requirements-table col:nth-child(1) { width: 25%; }
.scale-requirements-table col:nth-child(2) { width: 10%; }
.scale-requirements-table col:nth-child(3) { width: 18%; }
.scale-requirements-table col:nth-child(4) { width: 23%; }
.scale-requirements-table col:nth-child(5) { width: 24%; }
</style>

<table class="scale-requirements-table">
<colgroup>
<col style="width: 25%">
<col style="width: 10%">
<col style="width: 18%">
<col style="width: 23%">
<col style="width: 24%">
</colgroup>
<thead>
<tr>
<th>Resource Type</th>
<th>Nodes</th>
<th>vCPU/Memory (GiB)</th>
<th>AWS Instance</th>
<th>Azure Instance</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mattermost Application</td>
<td>2</td>
<td>8/16</td>
<td>c7i.2xlarge</td>
<td>F8s v2</td>
</tr>
<tr>
<td>RDS Writer</td>
<td>1</td>
<td>8/64</td>
<td>db.r7g.2xlarge</td>
<td>E8as v6</td>
</tr>
<tr>
<td>RDS Reader</td>
<td>1</td>
<td>8/64</td>
<td>db.r7g.2xlarge</td>
<td>E8as v6</td>
</tr>
<tr>
<td>Elasticsearch cluster</td>
<td>4</td>
<td>8/64</td>
<td>r6g.2xlarge.search</td>
<td>E8ads v6</td>
</tr>
<tr>
<td>Proxy</td>
<td>1</td>
<td>16/64</td>
<td>m7i.4xlarge</td>
<td>D16s v6</td>
</tr>
</tbody>
</table>

## Lifetime storage

.. This page intentionally not accessible via the LHS navigation pane
because it\'s included in other pages

To forecast your own storage usage, begin with a Mattermost server
approximately 600 MB to 800 MB in size including operating system and
database, then add the multiplied product of:

- Estimated storage per user per month (see below), multiplied by 12
  months in a year
- Estimated mean average number of users in a year
- A 1-2x safety factor

### Estimated storage per user, per month

.. This page intentionally not accessible via the LHS navigation pane
because it\'s included in other pages

File usage per user varies significantly across industries. The below
benchmarks are recommended:

- **Low usage teams** (1-5 MB/user/month)

> - Primarily using text messages and links to communicate. Examples
>   would include software development teams that heavily use web-based
>   document creation and management tools, and therefore rarely upload
>   files to the server.

- **Medium usage teams** (5-25 MB/user/month)

> - Using a mix of text messages as well as shared documents and images
>   to communicate. Examples might include business teams that may
>   commonly drag and drop screenshots, PDFs and Microsoft Office
>   documents into Mattermost for sharing and review.

- **High usage teams** (25-100 MB/user/month)

> - Heaviest utilization comes from teams uploading a high number of
>   large files into Mattermost on a regular basis. Examples include
>   creative teams who share and store artwork and media with tags and
>   commentary in a pipeline production process.

### Example

A 30000-person team with medium usage (with a safety factor of 2x) would
require between 3TB ^1^ and 15TB ^2^ of free space per annum.

^1^ 30000 users \* 5 MB \* 12 months \* 2x safety factor

^2^ 30000 users \* 25 MB \* 12 months \* 2x safety factor

We strongly recommend that you review storage utilization at least
quarterly to ensure adequate free space is available.

## Additional considerations

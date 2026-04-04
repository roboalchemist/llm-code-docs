# Source: https://buildkite.com/docs/apis/rest-api/test-engine/flaky-tests.md

# Flaky tests API

> 🚧 This section documents a deprecated Buildkite API endpoint
> Flaky tests should be accessed via the [list tests endpoint](/docs/apis/rest-api/test-engine/tests#list-tests) using the `label=flaky` query parameter.

The flaky test API endpoint provides information about tests detected as flaky in a test suite.

## List all flaky tests

Returns a [paginated list](/docs/rest-api#pagination) of the flaky tests detected in a test suite. Please note that the `last_resolved_at` field represents a deprecated feature in Test Engine and should not be relied upon.

```bash
curl -H "Authorization: Bearer $TOKEN" \
  -X GET "https://api.buildkite.com/v2/analytics/organizations/{org.slug}/suites/{suite.slug}/flaky-tests"
```

```json
[
  {
    "id": "01867216-8478-7fde-a55a-0300f88bb49b",
    "web_url": "https://buildkite.com/organizations/my_great_org/analytics/suites/my_suite_name/tests/01867216-8478-7fde-a55a-0300f88bb49b",
    "scope": "User#email",
    "name": "is correctly formatted",
    "location": "./spec/models/user_spec.rb:42",
    "file_name": "./spec/models/user_spec.rb",
    "instances": 1,
    "latest_occurrence_at": "2024-07-15T00:07:02.547Z",
    "most_recent_instance_at": "2024-07-15T00:07:02.547Z",
    "last_resolved_at": null,
    "ownership_team_ids": ["4c15a4c7-6674-4585-b592-4adcc8630383", "d30fd7ba-82d8-487f-9d98-6e1a057bcca8"]
  }
]
```

Optional [query string parameters](/docs/api#query-string-parameters):

<table>
<tbody>
  <tr>
    <th>
      <code>search</code>
    </th>
    <td>
      <span>Returns flaky tests with a <code>name</code> or <code>scope</code> that contains the search string. Users with the <a href="/docs/test-engine/test-collection/ruby-collectors">Ruby test collector</a> installed can also filter results by <code>location</code>.</span>
      <p class="Docs__api-param-eg"><em>Example:</em> <code>?search="User#find_email"</code>, <code>?search="/billing_spec"</code></p>
    </td>
  </tr>
  <tr>
    <th>
      <code>branch</code>
    </th>
    <td>
      <span>Returns flaky tests for flakes detected one or more times on the branch whose name is specified by the <code>branch</code> value.</span>
      <p class="Docs__api-param-eg"><em>Example:</em> <code>?branch=main</code></p>
    </td>
  </tr>
  <tr>
    <th>
      <code>period</code>
    </th>
    <td>
      <span>Filters the results by the given time <code>period</code>. Valid values are <code>1hour</code>, <code>4hours</code>, <code>1day</code>, <code>7days</code>, <code>14days</code>, and <code>28days</code>. The default period when no <code>period</code> value is specified is <code>7days</code>.</span>
      <p class="Docs__api-param-eg"><em>Example:</em> <code>?period=28days</code></p>
    </td>
  </tr>
</tbody>
</table>

Required scope: `read_suites`

Success response: `200 OK`

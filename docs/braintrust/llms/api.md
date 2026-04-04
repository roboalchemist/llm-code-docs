# Source: https://braintrust.dev/docs/guides/api.md

# API walkthrough

The Braintrust REST API is available via an OpenAPI spec published at
[https://github.com/braintrustdata/braintrust-openapi](https://github.com/braintrustdata/braintrust-openapi).
This guide walks through a few common use cases, and should help you get started
with using the API. Each example is implemented in a particular language, for
legibility, but the API itself is language-agnostic.

To learn more about the API, see the full [API spec](https://www.braintrust.dev/docs/api-reference). If you are
looking for a language-specific wrapper over the bare REST API, we support
several different [languages](https://www.braintrust.dev/docs/reference/api#api-wrappers).

## Run an experiment

<CodeGroup dropdown>
  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from uuid import uuid4

  import requests

  API_URL = "https://api.braintrust.dev/v1"
  headers = {"Authorization": "Bearer " + os.environ["BRAINTRUST_API_KEY"]}

  if __name__ == "__main__":
      # Create a project, if it does not already exist
      project = requests.post(f"{API_URL}/project", headers=headers, json={"name": "rest_test"}).json()
      print(project)

      # Create an experiment. This should always be new
      experiment = requests.post(
          f"{API_URL}/experiment", headers=headers, json={"name": "rest_test", "project_id": project["id"]}
      ).json()
      print(experiment)

      # Log some stuff
      for i in range(10):
          resp = requests.post(
              f"{API_URL}/experiment/{experiment['id']}/insert",
              headers=headers,
              json={"events": [{"id": uuid4().hex, "input": 1, "output": 2, "scores": {"accuracy": 0.5}}]},
          )
          if not resp.ok:
              raise Exception(f"Error: {resp.status_code} {resp.text}: {resp.content}")
  ```
</CodeGroup>

## Fetch experiment results

To fetch experiment results, use a SQL query to retrieve traces that match the
criteria you are interested in.

For example, the script below fetches traces based on whether or not a review
score is present:

<CodeGroup dropdown>
  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  import requests

  API_URL = "https://api.braintrust.dev/"
  headers = {"Authorization": "Bearer " + os.environ["BRAINTRUST_API_KEY"]}

  def make_query(experiment_id: str) -> str:
      # Replace "response quality" with the name of your review score column.
      # Using SQL syntax:
      return f"""
      SELECT
        sum(CASE WHEN scores."response quality" IS NOT NULL THEN 1 ELSE 0 END) AS reviewed,
        sum(CASE WHEN is_root THEN 1 ELSE 0 END) AS total
      FROM experiment('{experiment_id}')
      """

      # Using BTQL syntax:
      # return f"""
      # from: experiment('<experiment_id>')
      # measures: sum(scores."response quality" IS NOT NULL) AS reviewed, count(1) AS total
      # filter: is_root -- Only count traces, not spans
      # """

  def fetch_experiment_review_status(experiment_id: str) -> dict:
      return requests.post(
          f"{API_URL}/btql",
          headers=headers,
          json={"query": make_query(experiment_id), "fmt": "json"},
      ).json()

  EXPERIMENT_ID = "bdec1c5e-8c00-4033-84f0-4e3aa522ecaf"  # Replace with your experiment ID
  print(fetch_experiment_review_status(EXPERIMENT_ID))
  ```
</CodeGroup>

## Fetch specific child spans based on trace-level metadata

To retrieve child spans based on trace-level metadata, use a SQL query
to filter spans by the `metadata` you are interested in.

For example, the script below calculates how long child spans took to run
that are in traces having a metadata key of "orgName" set to "qawolf".

<CodeGroup dropdown>
  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import argparse
  import os

  import requests
  from dotenv import load_dotenv

  load_dotenv(override=True)

  # Make sure to replace this with your stack's Universal API URL if you are self-hosting
  API_URL = "https://api.braintrust.dev/"
  headers = {"Authorization": "Bearer " + os.environ["BRAINTRUST_API_KEY"]}

  if __name__ == "__main__":
      parser = argparse.ArgumentParser()
      parser.add_argument("--project-id", type=str, required=True)
      parser.add_argument("--span-name", type=str, default="root")
      args = parser.parse_args()

      # Find all rows matching a certain metadata value.
      # Using SQL syntax:
      query = f"""
      SELECT span_attributes, metrics
      FROM project_logs('{args.project_id}', shape => 'traces')
      WHERE metadata.orgName = 'qawolf'
      LIMIT 10
      """
      # Using BTQL syntax:
      # query = f"""
      # select: span_attributes, metrics
      # from: project_logs('{args.project_id}') traces
      # filter: metadata.orgName = 'qawolf'
      # limit:10
      # """

      response = requests.post(f"{API_URL}/btql", headers=headers, json={"query": query}).json()

      durations = []
      for trace in response["data"]:
          # print(trace)

          if trace["span_attributes"]["name"] == args.span_name:
              metrics = trace["metrics"]
              if metrics.get("end") and metrics.get("start"):
                  duration = metrics["end"] - metrics["start"]
                  durations.append(duration)
                  print(f"Duration: {duration}ms")
                  print("-" * 100)

              else:
                  print("Start or end not found for this span")
                  print("-" * 100)

      print(f"\nAverage duration: {sum(durations) / len(durations)}ms\n")
  ```
</CodeGroup>

## Paginate a large dataset

<Note>
  If you're using the Python or TypeScript SDK, pagination is handled automatically. Only use this code if you're developing with other tools.
</Note>

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  // If you're self-hosting Braintrust, then use your stack's Universal API URL, e.g.
  //   https://dfwhllz61x709.cloudfront.net
  export const BRAINTRUST_API_URL = "https://api.braintrust.dev";
  export const API_KEY = process.env.BRAINTRUST_API_KEY;

  export async function* paginateDataset(args: {
    project: string;
    dataset: string;
    version?: string;
    // Number of rows to fetch per request. You can adjust this to be a lower number
    // if your rows are very large (e.g. several MB each).
    perRequestLimit?: number;
  }) {
    const { project, dataset, version, perRequestLimit } = args;
    const headers = {
      Accept: "application/json",
      "Accept-Encoding": "gzip",
      Authorization: `Bearer ${API_KEY}`,
    };
    const fullURL = `${BRAINTRUST_API_URL}/v1/dataset?project_name=${encodeURIComponent(
      project,
    )}&dataset_name=${encodeURIComponent(dataset)}`;
    const ds = await fetch(fullURL, {
      method: "GET",
      headers,
    });
    if (!ds.ok) {
      throw new Error(
        `Error fetching dataset metadata: ${ds.status}: ${await ds.text()}`,
      );
    }
    const dsJSON = await ds.json();
    const dsMetadata = dsJSON.objects[0];
    if (!dsMetadata?.id) {
      throw new Error(`Dataset not found: ${project}/${dataset}`);
    }

    let cursor: string | null = null;
    while (true) {
      const body: string = JSON.stringify({
        query: {
          from: {
            op: "function",
            name: { op: "ident", name: ["dataset"] },
            args: [{ op: "literal", value: dsMetadata.id }],
          },
          select: [{ op: "star" }],
          limit: perRequestLimit,
          cursor,
        },
        fmt: "jsonl",
        version,
      });
      const response = await fetch(`${BRAINTRUST_API_URL}/btql`, {
        method: "POST",
        headers,
        body,
      });
      if (!response.ok) {
        throw new Error(
          `Error fetching rows for ${dataset}: ${
            response.status
          }: ${await response.text()}`,
        );
      }

      cursor =
        response.headers.get("x-bt-cursor") ??
        response.headers.get("x-amz-meta-bt_cursor");

      // Parse jsonl line-by-line
      const allRows = await response.text();
      const rows = allRows.split("\n");
      let rowCount = 0;
      for (const row of rows) {
        if (!row.trim()) {
          continue;
        }
        yield JSON.parse(row);
        rowCount++;
      }

      if (rowCount === 0) {
        break;
      }
    }
  }

  async function main() {
    for await (const row of paginateDataset({
      project: "Your project name", // Replace with your project name
      dataset: "Your dataset name", // Replace with your dataset name
      perRequestLimit: 100,
    })) {
      console.log(row);
    }
  }

  main();
  ```
</CodeGroup>

## Delete logs

To delete logs, issue log requests with the `_object_delete` flag set to `true`.

For example, the following script uses a SQL query to find all logs matching a
specific criteria and then deletes them:

<CodeGroup dropdown>
  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import argparse
  import os
  from uuid import uuid4

  import requests

  # Make sure to replace this with your stack's Universal API URL if you are self-hosting
  API_URL = "https://api.braintrust.dev/"
  headers = {"Authorization": "Bearer " + os.environ["BRAINTRUST_API_KEY"]}

  if __name__ == "__main__":
      parser = argparse.ArgumentParser()
      parser.add_argument("--project-id", type=str, required=True)
      # Update this logic to match the rows you'd like to delete
      parser.add_argument("--user-id", type=str, required=True)
      args = parser.parse_args()

      # Find all rows matching a certain metadata value.
      # Using SQL syntax:
      query = f"""
      SELECT id
      FROM project_logs('{args.project_id}', shape => 'traces')
      WHERE metadata.user_id = '{args.user_id}'
      """

      # Using BTQL syntax:
      # query = f"""
      # select: id
      # from: project_logs('{args.project_id}') traces
      # filter: metadata.user_id = '{args.user_id}'
      # """

      response = requests.post(f"{API_URL}/btql", headers=headers, json={"query": query}).json()
      ids = [x["id"] for x in response["data"]]
      print("Deleting", len(ids), "rows")

      delete_requests = [{"id": id, "_object_delete": True} for id in ids]
      response = requests.post(
          f"{API_URL}/v1/project_logs/{args.project_id}/insert", headers=headers, json={"events": delete_requests}
      ).json()
      row_ids = response["row_ids"]
      print("Deleted", len(row_ids), "rows")
  ```
</CodeGroup>

## Impersonate a user for a request

User impersonation allows a privileged user to perform an operation on behalf of
another user, using the impersonated user's identity and permissions. For
example, a proxy service may wish to forward requests coming in from individual
users to Braintrust without requiring each user to directly specify Braintrust
credentials. The privileged service can initiate the request with its own
credentials and impersonate the user so that Braintrust runs the operation with
the user's permissions.

To this end, all API requests accept a header `x-bt-impersonate-user`, which you
can set to the ID or email of the user to impersonate. Currently impersonating
another user requires that the requesting user has specifically been granted the
`Owner` role over all organizations that the impersonated user belongs to. This
check guarantees the requesting user has at least the set of permissions that
the impersonated user has.

Consider the following code example for configuring ACLs and running a request
with user impersonation.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  // If you're self-hosting Braintrust, then use your stack's Universal API URL, e.g.
  //   https://dfwhllz61x709.cloudfront.net
  export const BRAINTRUST_API_URL = "https://api.braintrust.dev";
  export const API_KEY = process.env.BRAINTRUST_API_KEY;

  async function getOwnerRoleId() {
    const roleResp = await fetch(
      `${BRAINTRUST_API_URL}/v1/role?${new URLSearchParams({ role_name: "Owner" })}`,
      {
        method: "GET",
        headers: {
          Authorization: `Bearer ${API_KEY}`,
        },
      },
    );
    if (!roleResp.ok) {
      throw new Error(await roleResp.text());
    }
    const roles = await roleResp.json();
    return roles.objects[0].id;
  }

  async function getUserOrgInfo(orgName: string): Promise<{
    user_id: string;
    org_id: string;
  }> {
    const meResp = await fetch(`${BRAINTRUST_API_URL}/api/self/me`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${API_KEY}`,
      },
    });
    if (!meResp.ok) {
      throw new Error(await meResp.text());
    }
    const meInfo = await meResp.json();
    const orgInfo = meInfo.organizations.find(
      (x: { name: string }) => x.name === orgName,
    );
    if (!orgInfo) {
      throw new Error(`No organization found with name ${orgName}`);
    }
    return { user_id: meInfo.id, org_id: orgInfo.id };
  }

  async function grantOwnershipRole(orgName: string) {
    const ownerRoleId = await getOwnerRoleId();
    const { user_id, org_id } = await getUserOrgInfo(orgName);

    // Grant an 'Owner' ACL to the requesting user on the organization. Granting
    // this ACL requires the user to have `create_acls` permission on the org, which
    // means they must already be an owner of the org indirectly.
    const aclResp = await fetch(`${BRAINTRUST_API_URL}/v1/acl`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        object_type: "organization",
        object_id: org_id,
        user_id,
        role_id: ownerRoleId,
      }),
    });
    if (!aclResp.ok) {
      throw new Error(await aclResp.text());
    }
  }

  async function main() {
    if (!process.env.ORG_NAME || !process.env.USER_EMAIL) {
      throw new Error("Must specify ORG_NAME and USER_EMAIL");
    }

    // This only needs to be done once.
    await grantOwnershipRole(process.env.ORG_NAME);

    // This will only succeed if the user being impersonated has permissions to
    // create a project within the org.
    const projectResp = await fetch(`${BRAINTRUST_API_URL}/v1/project`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${API_KEY}`,
        "Content-Type": "application/json",
        "x-bt-impersonate-user": process.env.USER_EMAIL,
      },
      body: JSON.stringify({
        name: "my-project",
        org_name: process.env.ORG_NAME,
      }),
    });
    if (!projectResp.ok) {
      throw new Error(await projectResp.text());
    }
    console.log(await projectResp.json());
  }

  main();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  import requests

  # If you're self-hosting Braintrust, then use your stack's Universal API URL, e.g.
  # https://dfwhllz61x709.cloudfront.net
  BRAINTRUST_API_URL = "https://api.braintrust.dev"
  API_KEY = os.environ["BRAINTRUST_API_KEY"]

  def get_owner_role_id():
      resp = requests.get(
          f"{BRAINTRUST_API_URL}/v1/role",
          headers={"Authorization": f"Bearer {API_KEY}"},
          params=dict(role_name="Owner"),
      )
      resp.raise_for_status()
      return resp.json()["objects"][0]["id"]

  def get_user_org_info(org_name):
      resp = requests.post(
          f"{BRAINTRUST_API_URL}/api/self/me",
          headers={"Authorization": f"Bearer {API_KEY}"},
      )
      resp.raise_for_status()
      me_info = resp.json()
      org_info = [x for x in me_info["organizations"] if x["name"] == org_name]
      if not org_info:
          raise Exception(f"No organization found with name {org_name}")
      return dict(user_id=me_info["id"], org_id=org_info["id"])

  def grant_ownership_role(org_name):
      owner_role_id = get_owner_role_id()
      user_org_info = get_user_org_info(org_name)

      # Grant an 'Owner' ACL to the requesting user on the organization. Granting
      # this ACL requires the user to have `create_acls` permission on the org,
      # which means they must already be an owner of the org indirectly.
      resp = requests.post(
          f"{BRAINTRUST_API_URL}/v1/acl",
          headers={"Authorization": f"Bearer {API_KEY}"},
          body=dict(
              object_type="organization",
              object_id=user_org_info["org_id"],
              user_id=user_org_info["user_id"],
              role_id=owner_role_id,
          ),
      )
      resp.raise_for_status()

  def main():
      # This only needs to be done once.
      grant_ownership_role(os.environ["ORG_NAME"])

      # This will only succeed if the user being impersonated has permissions to
      # create a project within the org.
      resp = requests.post(
          f"{BRAINTRUST_API_URL}/v1/project",
          headers={
              "Authorization": f"Bearer {API_KEY}",
              "x-bt-impersonate-user": os.environ["USER_EMAIL"],
          },
          json=dict(
              name="my-project",
              org_name=os.environ["ORG_NAME"],
          ),
      )
      resp.raise_for_status()
      print(resp.json())
  ```
</CodeGroup>

## Postman

[Postman](https://www.postman.com/) is a popular tool for interacting with HTTP APIs. You can
load Braintrust's API spec into Postman by importing the OpenAPI spec's URL.

```
https://raw.githubusercontent.com/braintrustdata/braintrust-openapi/main/openapi/spec.json
```

<img src="https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/api/postman.gif?s=e07eb9bbc9488fb638f6019fd63da47a" alt="Postman" data-og-width="960" width="960" data-og-height="790" height="790" data-path="images/guides/api/postman.gif" data-optimize="true" data-opv="3" />

## Trace with the REST API SDKs

In this section, we demonstrate the basics of logging with tracing using the
language-specific REST API SDKs. The end result of running each example should
be a single log entry in a project called `tracing_test`, which looks like the
following:

<img src="https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=0d1b7607bdf5536b75e97be19278a912" alt="Tracing Test Screenshot" data-og-width="4146" width="4146" data-og-height="3054" height="3054" data-path="images/guides/traces/trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?w=280&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=19f4c1bd01265dc56b53044a069eea28 280w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?w=560&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=27a3148ed8c298bbd7323cb6cf7c1930 560w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?w=840&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=ac9e22c98152cada01437f56b06e5233 840w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?w=1100&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=2ee489a6dc1f282d4d164e1af27fc9de 1100w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?w=1650&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=95429ed64c90e811151c3fe7d70f37d1 1650w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?w=2500&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=73c4e519960e3d829406acff196ff0a5 2500w" />

This example shows how to trace with the Go SDK.

<CodeGroup dropdown>
  ```go  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  package main

  import (
  	"context"
  	"time"

  	"go.opentelemetry.io/otel"
  	"go.opentelemetry.io/otel/attribute"
  	"go.opentelemetry.io/otel/sdk/trace"

  	"github.com/braintrustdata/braintrust-sdk-go"
  )

  type LLMInteraction struct {
  	input  interface{}
  	output interface{}
  }

  func runInteraction0(input interface{}) LLMInteraction {
  	return LLMInteraction{
  		input:  input,
  		output: "output0",
  	}
  }

  func runInteraction1(input interface{}) LLMInteraction {
  	return LLMInteraction{
  		input:  input,
  		output: "output1",
  	}
  }

  func getCurrentTime() float64 {
  	return float64(time.Now().UnixMilli()) / 1000.
  }

  func main() {
  	ctx := context.Background()

  	// Create TracerProvider
  	tp := trace.NewTracerProvider()
  	defer tp.Shutdown(ctx)
  	otel.SetTracerProvider(tp)

  	// Initialize Braintrust client with project name
  	_, err := braintrust.New(tp,
  		braintrust.WithProject("tracing_test"),
  		braintrust.WithBlockingLogin(true),
  	)
  	if err != nil {
  		panic(err)
  	}

  	// Get a tracer
  	tracer := otel.Tracer("user-interaction")

  	// Create root span
  	rootCtx, rootSpan := tracer.Start(ctx, "User Interaction")
  	rootSpan.SetAttributes(
  		attribute.String("user_id", "user123"),
  	)
  	startTime := getCurrentTime()

  	// Create child span for Interaction 0
  	_, interaction0Span := tracer.Start(rootCtx, "Interaction 0")
  	interaction0 := runInteraction0("hello world")
  	interaction0Span.SetAttributes(
  		attribute.String("input", interaction0.input.(string)),
  		attribute.String("output", interaction0.output.(string)),
  	)
  	interaction0Span.End()

  	// Create child span for Interaction 1
  	_, interaction1Span := tracer.Start(rootCtx, "Interaction 1")
  	interaction1 := runInteraction1(interaction0.output)
  	interaction1Span.SetAttributes(
  		attribute.String("input", interaction1.input.(string)),
  		attribute.String("output", interaction1.output.(string)),
  	)
  	interaction1Span.End()

  	// End root span
  	rootSpan.End()
  	_ = startTime // Used for timing if needed
  }
  ```
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt
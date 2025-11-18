# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/rolling-releases.md

# Rolling Releases Management

> Learn how to use the Vercel SDK to manage Rolling Releases through real-life examples.

## Updating your project's rolling release configuration

In this example, you configure rolling releases for your project with multiple stages. This allows you to gradually roll out deployments to production, starting with a small percentage of traffic and progressively increasing it.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function setRollingReleaseConfig() {
  const result = await vercel.rollingRelease.updateRollingReleaseConfig({
    idOrName: "your-project-id", // Can be project ID or URL-encoded project name
    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional - required if your token is scoped to multiple teams
    slug: "my-team-url-slug", // Optional - alternative to teamId
    requestBody: {
      target: "production",
      stages: [
        {
          targetPercentage: 5,     // Start with 5% of traffic
          duration: 300           // Wait 5 minutes before next stage
        },
        {
          targetPercentage: 25,    // Then 25% of traffic
          duration: 600           // Wait 10 minutes
        },
        {
          targetPercentage: 50,    // Then 50% of traffic
          duration: 900           // Wait 15 minutes if approved
        },
        {
          targetPercentage: 100,   // Finally, 100% of traffic
        }
      ]
    }
  });

  console.log("Rolling Release Configuration Updated:", result.rollingRelease);
}

setRollingReleaseConfig();
```

## Approve the next stage of a rolling release

In this example, you manually approve advancing a rolling release to the next stage. This is useful when you have stages configured with `requireApproval: true` and want to control the rollout progression.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function approveNextStage() {
  const projectId = "your-project-id";

  try {
    // First, get the current rolling release status to understand the current state
    const currentStatus = await vercel.rollingRelease.getActiveRollingRelease({
      idOrName: projectId,
      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional
    });

    if (!currentStatus.rollingRelease || currentStatus.rollingRelease.state !== "ACTIVE") {
      console.log("No active rolling release found for this project");
      return;
    }

    const { rollingRelease } = currentStatus;

    console.log(`Current stage: ${rollingRelease.activeStage?.index} (${rollingRelease.activeStage?.targetPercentage}% traffic)`);
    console.log(`Next stage: ${rollingRelease.nextStage?.index} (${rollingRelease.nextStage?.targetPercentage}% traffic)`);

    if (!rollingRelease.nextStage) {
      console.log("Rolling release is already at the final stage");
      return;
    }

    if (!rollingRelease.nextStage.requireApproval) {
      console.log("Next stage does not require manual approval");
      return;
    }

    // Approve advancing to the next stage
    const approvalResult = await vercel.rollingRelease.approveRollingReleaseStage({
      idOrName: projectId,
      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional
      requestBody: {
        nextStageIndex: rollingRelease.nextStage.index,
        canaryDeploymentId: rollingRelease.canaryDeployment?.id || "",
      },
    });

    console.log("✓ Rolling release stage approved successfully!");
    console.log(`Advanced to stage ${approvalResult.rollingRelease?.activeStage?.index} (${approvalResult.rollingRelease?.activeStage?.targetPercentage}% traffic)`);

    // Display updated rollout information
    if (approvalResult.rollingRelease?.nextStage) {
      console.log(`Next stage will be: ${approvalResult.rollingRelease.nextStage.index} (${approvalResult.rollingRelease.nextStage.targetPercentage}% traffic)`);
    } else {
      console.log("This was the final stage - rolling release will complete automatically");
    }

  } catch (error) {
    console.error("Failed to approve rolling release stage:", error);
  }
}

approveNextStage();
```

## Force completion of a rolling release

In this example, you force-complete an active rolling release, immediately promoting the canary deployment to serve 100% of traffic. This is useful for emergency situations or when you want to skip remaining stages.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function forceCompleteRollingRelease() {
  const projectId = "your-project-id";

  try {
    // First, get the current rolling release status
    const currentStatus = await vercel.rollingRelease.getActiveRollingRelease({
      idOrName: projectId,
      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional
    });

    if (!currentStatus.rollingRelease || currentStatus.rollingRelease.state !== "ACTIVE") {
      console.log("No active rolling release found for this project");
      return;
    }

    const { rollingRelease } = currentStatus;

    console.log(`Current rolling release state: ${rollingRelease.state}`);
    console.log(`Current stage: ${rollingRelease.activeStage?.index} (${rollingRelease.activeStage?.targetPercentage}% traffic)`);
    console.log(`Canary deployment: ${rollingRelease.canaryDeployment?.name} (${rollingRelease.canaryDeployment?.id})`);

    if (!rollingRelease.canaryDeployment?.id) {
      console.error("No canary deployment found to complete");
      return;
    }

    // Confirm the action (in a real scenario, you might want additional checks)
    console.log("⚠️  WARNING: This will immediately promote the canary deployment to 100% traffic");
    console.log(`   Skipping ${rollingRelease.stages?.length - (rollingRelease.activeStage?.index || 0) - 1} remaining stages`);

    // Force complete the rolling release
    const completionResult = await vercel.rollingRelease.completeRollingRelease({
      idOrName: projectId,
      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional
      requestBody: {
        canaryDeploymentId: rollingRelease.canaryDeployment.id,
      },
    });

    console.log("✓ Rolling release completed successfully!");
    console.log(`Final state: ${completionResult.rollingRelease?.state}`);

    // The canary deployment is now the current deployment serving 100% traffic
    if (completionResult.rollingRelease?.currentDeployment) {
      console.log(`New production deployment: ${completionResult.rollingRelease.currentDeployment.name}`);
      console.log(`Production URL: ${completionResult.rollingRelease.currentDeployment.url}`);
    }

    // Log completion time
    if (completionResult.rollingRelease?.updatedAt) {
      const completedAt = new Date(completionResult.rollingRelease.updatedAt);
      console.log(`Completed at: ${completedAt.toISOString()}`);
    }

  } catch (error) {
    console.error("Failed to complete rolling release:", error);

    // Handle specific error cases
    if (error.response?.status === 404) {
      console.error("Project not found or no rolling release configuration exists");
    } else if (error.response?.status === 400) {
      console.error("Invalid request - check the canary deployment ID");
    } else if (error.response?.status === 403) {
      console.error("Insufficient permissions to complete rolling release");
    }
  }
}

forceCompleteRollingRelease();
```

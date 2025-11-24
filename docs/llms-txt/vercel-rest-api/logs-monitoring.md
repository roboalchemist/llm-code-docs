# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/logs-monitoring.md

# Logs and Monitoring

> Learn how to use the Vercel SDK through real-life examples.

## Get deployment logs and check status

In this example, you retrieve the deployment logs and check the deployment status.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function getLogsAndStatus() {
  try {
    // Get deployment logs
    const logsResponse = await vercel.deployments.getDeploymentEvents({
      idOrUrl: 'project-name-uniqueid.vercel.app',
    });
    if (Array.isArray(logsResponse)) {
      if ('deploymentId' in logsResponse[0]) {
        const deploymentID = logsResponse[0].deploymentId;
        const deploymentStatus = await vercel.deployments.getDeployment({
          idOrUrl: deploymentID,
        });
        console.log(
          `Deployment with id, ${deploymentID} status is ${deploymentStatus.status}`,
        );
      }
      //Display logs with log type, timestamp and text
      for (const item of result) {
        if ('text' in item) {
          console.log(
            `${item.type} at ${new Date(item.created).toLocaleTimeString()}: ${
              item.text
            }`,
          );
        }
      }
    }
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

getLogsAndStatus();
```

## Aggregate logs and send alerts

Create a custom monitoring system that aggregates logs from multiple deployments, analyzes them for errors, and sends alerts if certain thresholds are exceeded.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';
import * as nodemailer from 'nodemailer';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});
const ALERT_EMAIL = 'alerts@example.com';

interface Log {
  type: string;
  created: number;
  text: string;
}

async function monitorDeployments() {
  try {
    // Get recent deployments
    const deploymentsResponse = await vercel.deployments.getDeployments({
      limit: 5,
      projectId: 'my-project', //The project name used in the deployment URL
    });

    let totalErrors = 0;
    let totalWarnings = 0;

    for (const deployment of deploymentsResponse.deployments) {
      console.log(`Analyzing deployment: ${deployment.uid}`);
      const logsResponse = await vercel.deployments.getDeploymentEvents({
        idOrUrl: deployment.uid,
      });

      if (Array.isArray(logsResponse)) {
        const logs = logsResponse as Log[];
        const errors = logs.filter((log) => log.type === 'error');
        const warnings = logs.filter((log) => log.type === 'warning');
        totalErrors += errors.length;
        totalWarnings += warnings.length;
        console.log(`Errors: ${errors.length}, Warnings: ${warnings.length}`);
        errors.forEach((error) => console.log(`Error: ${error.text}`));
      }
    }

    console.log(
      `Total Errors: ${totalErrors}, Total Warnings: ${totalWarnings}`,
    );

    // Send alert if thresholds are exceeded
    if (totalErrors > 10 || totalWarnings > 20) {
      const transporter = nodemailer.createTransport({
        host: 'smtp.example.com',
        port: 587,
        secure: false,
        auth: {
          user: 'your_email@example.com',
          pass: process.env.email_pwd,
        },
      });

      await transporter.sendMail({
        from: '"Vercel Monitor" <monitor@example.com>',
        to: ALERT_EMAIL,
        subject: 'Deployment Alert: High number of errors or warnings',
        text: `Alert: ${totalErrors} errors and ${totalWarnings} warnings detected in recent deployments.`,
      });

      console.log('Alert email sent');
    }
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

monitorDeployments();
```

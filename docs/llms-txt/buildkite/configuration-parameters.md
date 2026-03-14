# Source: https://buildkite.com/docs/agent/self-hosted/gcp/elastic-ci-stack/configuration-parameters.md

# Source: https://buildkite.com/docs/agent/self-hosted/aws/elastic-ci-stack/ec2-linux-and-windows/configuration-parameters.md

# Configuration parameters

The Elastic CI Stack for AWS can be configured using parameters in AWS CloudFormation or variables in Terraform. This page provides a complete reference of all available configuration options.

> 📘 Deployment method
> If you're using AWS CloudFormation, see the [AWS CloudFormation setup guide](/docs/agent/self-hosted/aws/elastic-ci-stack/ec2-linux-and-windows/setup). If you're using Terraform, see the [Terraform deployment guide](/docs/agent/self-hosted/aws/elastic-ci-stack/ec2-linux-and-windows/terraform).

The following tables list all of the available configuration parameters. For CloudFormation deployments, these are parameters in the [`aws-stack.yml` template](https://github.com/buildkite/elastic-ci-stack-for-aws/blob/-/templates/aws-stack.yml). For Terraform deployments, these are variables in the [Terraform module](https://github.com/buildkite/terraform-buildkite-elastic-ci-stack-for-aws).

Note that you must provide a value for the Buildkite agent token (CloudFormation: [`BuildkiteAgentTokenParameterStorePath`](#BuildkiteAgentTokenParameterStorePath) or [`BuildkiteAgentToken`](#BuildkiteAgentToken); Terraform: `agent_token_parameter_store_path` or `agent_token`) to use the stack. All other parameters are optional.

<h2>Base Configuration</h2>

<table>
 <tbody>
  <tr>
   <th>CloudFormation parameter</th>
   <th>Terraform variable</th>
   <th>Description</th>
  </tr>

   <tr id="BuildkiteAgentToken">
    <td>
     <code>BuildkiteAgentToken</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_token</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Buildkite agent registration token. Or, preload it into SSM Parameter Store and use BuildkiteAgentTokenParameterStorePath for secure environments.

    </td>
   </tr>

   <tr id="BuildkiteAgentTokenParameterStorePath">
    <td>
     <code>BuildkiteAgentTokenParameterStorePath</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_token_parameter_store_path</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Path to Buildkite agent token stored in AWS Systems Manager Parameter Store. Supports both parameter paths (e.g., '/buildkite/agent-token') and cross-account SSM parameter ARNs (e.g., 'arn:aws:ssm:us-east-1:123456789012:parameter/buildkite/shared-token'). If provided, this overrides the BuildkiteAgentToken field. Recommended for better security instead of hardcoding tokens in the template. Use cross-account ARNs to access SSM parameters shared via AWS RAM.

      <br/><strong>Allowed Pattern:</strong> <code>^$|^/$|^/[a-zA-Z0-9_.\-/]+$|^arn\:aws\:ssm\:[a-z0-9-]+\:[0-9]{12}:parameter/[a-zA-Z0-9_.\-/]+$</code>

    </td>
   </tr>

   <tr id="BuildkiteAgentTokenParameterStoreKMSKey">
    <td>
     <code>BuildkiteAgentTokenParameterStoreKMSKey</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_token_parameter_store_kms_key</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - AWS KMS key ID used to encrypt the SSM parameter.

    </td>
   </tr>

   <tr id="BuildkiteQueue">
    <td>
     <code>BuildkiteQueue</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_queue</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Queue name that agents will use, targeted in pipeline steps using 'queue={value}'.

      <br/><strong>Default Value:</strong> <code>default</code>

      <br/><strong>Minimum Length:</strong> 1

    </td>
   </tr>

   <tr id="AgentEndpoint">
    <td>
     <code>AgentEndpoint</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>agent_endpoint</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     API endpoint URL for Buildkite agent communication. Most customers shouldn't need to change this unless using a custom endpoint agreed with the Buildkite team.

      <br/><strong>Default Value:</strong> <code>https://agent.buildkite.com/v3</code>

    </td>
   </tr>
  
 </tbody>
</table>

<h2>Signed Pipelines Configuration</h2>

<table>
 <tbody>
  <tr>
   <th>CloudFormation parameter</th>
   <th>Terraform variable</th>
   <th>Description</th>
  </tr>

   <tr id="PipelineSigningKMSKeyId">
    <td>
     <code>PipelineSigningKMSKeyId</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>pipeline_signing_kms_key_id</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Identifier or ARN of existing KMS key for pipeline signing. Leave blank to create a new key when PipelineSigningKMSKeySpec is specified.

    </td>
   </tr>

   <tr id="PipelineSigningKMSKeySpec">
    <td>
     <code>PipelineSigningKMSKeySpec</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>pipeline_signing_kms_key_spec</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Key specification for pipeline signing KMS key. Set to 'none' to disable pipeline signing, or 'ECC_NIST_P256' to enable with automatic key creation.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>ECC_NIST_P256</code></li>
        
         <li><code>none</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>none</code>

    </td>
   </tr>

   <tr id="PipelineSigningKMSAccess">
    <td>
     <code>PipelineSigningKMSAccess</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>pipeline_signing_kms_access</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Access permissions for pipeline signing. 'sign-and-verify' allows both operations, 'verify' restricts to verification only.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>sign-and-verify</code></li>
        
         <li><code>verify</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>sign-and-verify</code>

    </td>
   </tr>

   <tr id="PipelineSigningVerificationFailureBehavior">
    <td>
     <code>PipelineSigningVerificationFailureBehavior</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>pipeline_signing_verification_failure_behavior</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     The behavior when a job is received without a valid verifiable signature (without a signature, with an invalid signature, or with a signature that fails verification).

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>block</code></li>
        
         <li><code>warn</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>block</code>

    </td>
   </tr>

   <tr id="BuildkiteAgentSigningKeySSMParameter">
    <td>
     <code>BuildkiteAgentSigningKeySSMParameter</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>pipeline_signing_jwks_parameter_store_path</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Existing SSM Parameter Store path to a JSON Web Key Set (JWKS) containing a key to sign jobs with.

      <br/><strong>Allowed Pattern:</strong> <code>^$|^/[a-zA-Z0-9_.\-/]+$</code>

    </td>
   </tr>

   <tr id="BuildkiteAgentSigningKeyID">
    <td>
     <code>BuildkiteAgentSigningKeyID</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>pipeline_signing_jwks_key_id</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     The ID of the key in the JWKS to use for signing jobs. If not specified, and the JWKS contains only one key, that key will be used.

    </td>
   </tr>

   <tr id="BuildkiteAgentVerificationKeySSMParameter">
    <td>
     <code>BuildkiteAgentVerificationKeySSMParameter</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>pipeline_verification_jwks_parameter_store_path</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Existing SSM Parameter Store path to a JSON Web Key Set (JWKS) containing keys with which to verify jobs.

      <br/><strong>Allowed Pattern:</strong> <code>^$|^/[a-zA-Z0-9_.\-/]+$</code>

    </td>
   </tr>
  
 </tbody>
</table>

<h2>Advanced Configuration</h2>

<table>
 <tbody>
  <tr>
   <th>CloudFormation parameter</th>
   <th>Terraform variable</th>
   <th>Description</th>
  </tr>

   <tr id="BuildkiteAgentRelease">
    <td>
     <code>BuildkiteAgentRelease</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_release</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Buildkite agent release channel to install. 'stable' = production-ready (recommended), 'beta' = pre-release with latest features, 'edge' = bleeding-edge development builds. Use 'stable' unless specific new features are required.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>stable</code></li>
        
         <li><code>beta</code></li>
        
         <li><code>edge</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>stable</code>

    </td>
   </tr>

   <tr id="BuildkiteAgentTags">
    <td>
     <code>BuildkiteAgentTags</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_tags</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Additional tags to help target specific Buildkite agents in pipeline steps (comma-separated). Example: 'environment=production,docker=enabled,size=large'. Use these tags in pipeline steps with 'agents: { environment: production }'.

    </td>
   </tr>

   <tr id="BuildkiteAgentTimestampLines">
    <td>
     <code>BuildkiteAgentTimestampLines</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_timestamp_lines</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Set to true to prepend timestamps to every line of output.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="BuildkiteAgentExperiments">
    <td>
     <code>BuildkiteAgentExperiments</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_experiments</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Agent experiments to enable, comma delimited. See https://github.com/buildkite/agent/blob/-/EXPERIMENTS.md.

    </td>
   </tr>

   <tr id="BuildkiteAgentEnableGitMirrors">
    <td>
     <code>BuildkiteAgentEnableGitMirrors</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_enable_git_mirrors</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Enables Git mirrors in the agent.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="BuildkiteAgentTracingBackend">
    <td>
     <code>BuildkiteAgentTracingBackend</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_tracing_backend</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - The tracing backend to use for CI tracing. See https://buildkite.com/docs/agent/v3/tracing.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code></code></li>
        
         <li><code>datadog</code></li>
        
         <li><code>opentelemetry</code></li>
        
       </ul>

    </td>
   </tr>

   <tr id="BuildkiteAgentCancelGracePeriod">
    <td>
     <code>BuildkiteAgentCancelGracePeriod</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_cancel_grace_period</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     The number of seconds a canceled or timed out job is given to gracefully terminate and upload its artifacts.

      <br/><strong>Default Value:</strong> <code>60</code>

      <br/><strong>Minimum Value:</strong> 1

    </td>
   </tr>

   <tr id="BuildkiteAgentSignalGracePeriod">
    <td>
     <code>BuildkiteAgentSignalGracePeriod</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_signal_grace_period</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     The number of seconds given to a subprocess to handle being sent `cancel-signal`. After this period has elapsed, SIGKILL will be sent.

      <br/><strong>Default Value:</strong> <code>-1</code>

      <br/><strong>Minimum Value:</strong> -1

    </td>
   </tr>

   <tr id="BuildkiteTerminateInstanceAfterJob">
    <td>
     <code>BuildkiteTerminateInstanceAfterJob</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_terminate_instance_after_job</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Set to 'true' to terminate the instance after a job has completed.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="BuildkiteAgentDisconnectAfterUptime">
    <td>
     <code>BuildkiteAgentDisconnectAfterUptime</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_disconnect_after_uptime</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     The maximum uptime in seconds before the Buildkite agent stops accepting new jobs and shuts down after any running jobs complete. Set to 0 to disable uptime-based termination. This helps regularly cycle out machines and prevent resource accumulation issues.

      <br/><strong>Default Value:</strong> <code>0</code>

      <br/><strong>Minimum Value:</strong> 0

    </td>
   </tr>

   <tr id="BuildkiteTerminateInstanceOnDiskFull">
    <td>
     <code>BuildkiteTerminateInstanceOnDiskFull</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_terminate_instance_on_disk_full</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Set to 'true' to terminate the instance when disk space is critically low (default is to exit job with code 1).

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="BuildkitePurgeBuildsOnDiskFull">
    <td>
     <code>BuildkitePurgeBuildsOnDiskFull</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_purge_builds_on_disk_full</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Set to 'true' to purge build directories as a last resort when disk space is critically low.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="BuildkiteAdditionalSudoPermissions">
    <td>
     <code>BuildkiteAdditionalSudoPermissions</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_additional_sudo_permissions</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Comma-separated list of specific commands (full paths) that build jobs can run with sudo privileges. Include only commands essential for builds. Leave blank unless builds require specific system-level operations.

    </td>
   </tr>

   <tr id="BuildkiteWindowsAdministrator">
    <td>
     <code>BuildkiteWindowsAdministrator</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_windows_administrator</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Add buildkite-agent user to Windows Administrators group. This provides full system access for build jobs. Set to 'false' if builds don't require administrator privileges for additional security isolation.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>true</code>

    </td>
   </tr>

   <tr id="BuildkiteAgentScalerServerlessARN">
    <td>
     <code>BuildkiteAgentScalerServerlessARN</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_scaler_serverless_arn</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     (Deprecated - no longer used) ARN of the Serverless Application Repository that hosts the buildkite-agent-scaler Lambda function. The ARN is now automatically selected based on the LambdaArchitecture parameter. To use a custom scaler deployment, modify the AgentScalerARN mapping in the template.

      <br/><strong>Default Value:</strong> <code>arn\:aws\:serverlessrepo\:us-east-1\:172840064832:applications/buildkite-agent-scaler</code>

    </td>
   </tr>

   <tr id="EnableEC2LogRetentionPolicy">
    <td>
     <code>EnableEC2LogRetentionPolicy</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>enable_ec2_log_retention_policy</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Enable automatic deletion of old EC2 logs to reduce CloudWatch storage costs. Disabled by default to preserve all logs. When enabled, EC2 logs older than EC2LogRetentionDays will be automatically deleted. This only affects EC2 instance logs (agents, system logs), not Lambda logs. WARNING: Enabling this on existing stacks will delete historical logs older than the retention period - this cannot be undone.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="EC2LogRetentionDays">
    <td>
     <code>EC2LogRetentionDays</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>ec2_log_retention_days</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     The number of days to retain CloudWatch Logs for EC2 instances managed by the CloudWatch agent (Buildkite agents, system logs, etc).

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>1</code></li>
        
         <li><code>3</code></li>
        
         <li><code>5</code></li>
        
         <li><code>7</code></li>
        
         <li><code>14</code></li>
        
         <li><code>30</code></li>
        
         <li><code>60</code></li>
        
         <li><code>90</code></li>
        
         <li><code>120</code></li>
        
         <li><code>150</code></li>
        
         <li><code>180</code></li>
        
         <li><code>365</code></li>
        
         <li><code>400</code></li>
        
         <li><code>545</code></li>
        
         <li><code>731</code></li>
        
         <li><code>1827</code></li>
        
         <li><code>3653</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>7</code>

    </td>
   </tr>

   <tr id="LogRetentionDays">
    <td>
     <code>LogRetentionDays</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>ec2_log_retention_days</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     The number of days to retain CloudWatch Logs for Lambda functions in the stack.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>1</code></li>
        
         <li><code>3</code></li>
        
         <li><code>5</code></li>
        
         <li><code>7</code></li>
        
         <li><code>14</code></li>
        
         <li><code>30</code></li>
        
         <li><code>60</code></li>
        
         <li><code>90</code></li>
        
         <li><code>120</code></li>
        
         <li><code>150</code></li>
        
         <li><code>180</code></li>
        
         <li><code>365</code></li>
        
         <li><code>400</code></li>
        
         <li><code>545</code></li>
        
         <li><code>731</code></li>
        
         <li><code>1827</code></li>
        
         <li><code>3653</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>1</code>

    </td>
   </tr>

   <tr id="BuildkiteAgentEnableGracefulShutdown">
    <td>
     <code>BuildkiteAgentEnableGracefulShutdown</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>buildkite_agent_enable_graceful_shutdown</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Set to true to enable graceful shutdown of Buildkite agents when the ASG is updated with replacement. This allows ASGs to be removed in a timely manner during an in-place update of the Elastic CI Stack for AWS, and allows remaining Buildkite agents to finish jobs without interruptions.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="LambdaArchitecture">
    <td>
     <code>LambdaArchitecture</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>lambda_architecture</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     CPU architecture for Lambda functions (x86_64 or arm64). arm64 provides better price-performance but requires compatible dependencies.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>x86_64</code></li>
        
         <li><code>arm64</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>x86_64</code>

    </td>
   </tr>
  
 </tbody>
</table>

<h2>Network Configuration</h2>

<table>
 <tbody>
  <tr>
   <th>CloudFormation parameter</th>
   <th>Terraform variable</th>
   <th>Description</th>
  </tr>

   <tr id="VpcId">
    <td>
     <code>VpcId</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>vpc_id</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Id of an existing VPC to launch instances into. Leave blank to have a new VPC created.

    </td>
   </tr>

   <tr id="Subnets">
    <td>
     <code>Subnets</code>
     <br><code>(CommaDelimitedList)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>subnets</code>
      <br><code>(list(string))</code>
     
    </td>
    <td>
     Optional - Comma separated list of two existing VPC subnet ids where EC2 instances will run. Required if setting VpcId.

    </td>
   </tr>

   <tr id="AvailabilityZones">
    <td>
     <code>AvailabilityZones</code>
     <br><code>(CommaDelimitedList)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>availability_zones</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Comma separated list of AZs that subnets are created in (if Subnets parameter is not specified).

    </td>
   </tr>

   <tr id="SecurityGroupIds">
    <td>
     <code>SecurityGroupIds</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>security_group_ids</code>
      <br><code>(list(string))</code>
     
    </td>
    <td>
     Optional - Comma separated list of security group ids to assign to instances.

    </td>
   </tr>

   <tr id="AssociatePublicIpAddress">
    <td>
     <code>AssociatePublicIpAddress</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>associate_public_ip_address</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Give instances public IP addresses for direct internet access. Set to 'false' for a more isolated environment if the VPC has alternative outbound internet access configured.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>true</code>

    </td>
   </tr>

   <tr id="EnableVpcEndpoints">
    <td>
     <code>EnableVpcEndpoints</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <em>N/A</em>
     
    </td>
    <td>
     Enable VPC endpoints for AWS services (S3, ECR, SSM, Secrets Manager, KMS). Only available when the stack creates a new VPC (VpcId parameter is empty). Interface endpoints incur hourly charges per availability zone. S3 uses a gateway endpoint which is free. Reduces internet traffic, improves security, and lowers data transfer costs for AWS service communication.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>
  
 </tbody>
</table>

<h2>Instance Configuration</h2>

<table>
 <tbody>
  <tr>
   <th>CloudFormation parameter</th>
   <th>Terraform variable</th>
   <th>Description</th>
  </tr>

   <tr id="ImageId">
    <td>
     <code>ImageId</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>image_id</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Custom AMI to use for instances (must be based on the stack's AMI).

    </td>
   </tr>

   <tr id="ImageIdParameter">
    <td>
     <code>ImageIdParameter</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>image_id_parameter</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Custom AMI SSM Parameter to use for instances (must be based on the stack's AMI).

    </td>
   </tr>

   <tr id="InstanceOperatingSystem">
    <td>
     <code>InstanceOperatingSystem</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>instance_operating_system</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     The operating system to run on the instances.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>linux</code></li>
        
         <li><code>windows</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>linux</code>

    </td>
   </tr>

   <tr id="InstanceTypes">
    <td>
     <code>InstanceTypes</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>instance_types</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     EC2 instance types to use (comma-separated, up to 25). The first type listed is preferred for OnDemand instances. Additional types improve Spot instance availability but make costs less predictable. Examples: 't3.large' for light workloads, 'm5.xlarge,m5a.xlarge' for CPU-intensive builds, 'c5.2xlarge,c5.4xlarge' for compute-heavy tasks.

      <br/><strong>Default Value:</strong> <code>t3.large</code>

      <br/><strong>Allowed Pattern:</strong> <code>^[\w-\.]+(,[\w-\.]*){0,24}$</code>

      <br/><strong>Minimum Length:</strong> 1

    </td>
   </tr>

   <tr id="CpuCredits">
    <td>
     <code>CpuCredits</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>cpu_credits</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Credit option for CPU usage of burstable instances. Sets the CreditSpecification.CpuCredits property in the LaunchTemplate for T-class instance types (t2, t3, t3a, t4g).

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>standard</code></li>
        
         <li><code>unlimited</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>unlimited</code>

    </td>
   </tr>

   <tr id="EnableInstanceStorage">
    <td>
     <code>EnableInstanceStorage</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>enable_instance_storage</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Mount available NVMe Instance Storage at /mnt/ephemeral, and use it to store docker images and containers, and the build working directory. You must ensure that the instance types have instance storage available for this to have any effect. See https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-volumes.html

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="MountTmpfsAtTmp">
    <td>
     <code>MountTmpfsAtTmp</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>mount_tmpfs_at_tmp</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Controls the filesystem mounted at /tmp. By default, /tmp is a tmpfs (memory-backed filesystem). Disabling this causes /tmp to be stored in the root filesystem.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>true</code>

    </td>
   </tr>

   <tr id="AgentsPerInstance">
    <td>
     <code>AgentsPerInstance</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>agents_per_instance</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     Number of Buildkite agents to start on each EC2 instance. NOTE: If an agent crashes or is terminated, it won't be automatically restarted, leaving fewer active agents on that instance. The ScaleInIdlePeriod parameter controls when the entire instance terminates (when all agents are idle), not individual agent restarts. Consider enabling ScalerEnableExperimentalElasticCIMode for better agent management, or use fewer agents per instance with more instances for high availability.

      <br/><strong>Default Value:</strong> <code>1</code>

      <br/><strong>Minimum Value:</strong> 1

    </td>
   </tr>

   <tr id="KeyName">
    <td>
     <code>KeyName</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>key_name</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - SSH keypair used to access the Buildkite instances via ec2-user, setting this will enable SSH ingress.

    </td>
   </tr>

   <tr id="SecretsBucket">
    <td>
     <code>SecretsBucket</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>secrets_bucket</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Name of an existing S3 bucket containing pipeline secrets (Created if left blank).

    </td>
   </tr>

   <tr id="SecretsBucketRegion">
    <td>
     <code>SecretsBucketRegion</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>secrets_bucket_region</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Region for the SecretsBucket. If blank the bucket's region is dynamically discovered.

    </td>
   </tr>

   <tr id="SecretsBucketEncryption">
    <td>
     <code>SecretsBucketEncryption</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>secrets_bucket_encryption</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Indicates whether the SecretsBucket should enforce encryption at rest and in transit.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="SecretsPluginSkipSSHKeyNotFoundWarning">
    <td>
     <code>SecretsPluginSkipSSHKeyNotFoundWarning</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>secrets_plugin_skip_ssh_key_not_found_warning</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Optional - Skip warning when SSH key is not found in the secrets bucket.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="ArtifactsBucket">
    <td>
     <code>ArtifactsBucket</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>artifacts_bucket</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Name of an existing S3 bucket for build artifact storage.

    </td>
   </tr>

   <tr id="ArtifactsBucketRegion">
    <td>
     <code>ArtifactsBucketRegion</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>artifacts_bucket_region</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Region for the ArtifactsBucket. If blank the bucket's region is dynamically discovered.

    </td>
   </tr>

   <tr id="ArtifactsS3ACL">
    <td>
     <code>ArtifactsS3ACL</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>artifacts_s3_acl</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - ACL to use for S3 artifact uploads.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>private</code></li>
        
         <li><code>public-read</code></li>
        
         <li><code>public-read-write</code></li>
        
         <li><code>authenticated-read</code></li>
        
         <li><code>aws-exec-read</code></li>
        
         <li><code>bucket-owner-read</code></li>
        
         <li><code>bucket-owner-full-control</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>private</code>

    </td>
   </tr>

   <tr id="AuthorizedUsersUrl">
    <td>
     <code>AuthorizedUsersUrl</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>authorized_users_url</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - HTTPS or S3 URL to periodically download SSH authorized_keys from, setting this will enable SSH ingress. authorized_keys are applied to ec2-user.

    </td>
   </tr>

   <tr id="BootstrapScriptUrl">
    <td>
     <code>BootstrapScriptUrl</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>bootstrap_script_url</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - URI for a script to run on each instance during boot. Supported URI schemes: S3 object URI (s3://bucket/key), HTTPS URL (https://example.com/script.sh), or local file path (file:///path/to/script).

    </td>
   </tr>

   <tr id="AgentEnvFileUrl">
    <td>
     <code>AgentEnvFileUrl</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>agent_env_file_url</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - URI containing environment variables for the Buildkite agent process itself (not for builds). Supported URI schemes: S3 object URI (s3://bucket/key), SSM parameter path (ssm:/path/to/param), HTTPS URL (https://example.com/script.sh), or local file path (file:///path/to/script). These variables configure agent behavior like proxy settings or debugging options. For build environment variables, use pipeline 'env' configuration instead.

    </td>
   </tr>

   <tr id="RootVolumeSize">
    <td>
     <code>RootVolumeSize</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>root_volume_size</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     Size of each instance's root EBS volume (in GB).

      <br/><strong>Default Value:</strong> <code>250</code>

      <br/><strong>Minimum Value:</strong> 10

    </td>
   </tr>

   <tr id="RootVolumeName">
    <td>
     <code>RootVolumeName</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>root_volume_name</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Name of the root block device for the AMI.

    </td>
   </tr>

   <tr id="RootVolumeType">
    <td>
     <code>RootVolumeType</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>root_volume_type</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Type of root volume to use. If specifying `io1` or `io2`, specify `RootVolumeIOPS` as well for optimal performance. See https://docs.aws.amazon.com/ebs/latest/userguide/provisioned-iops.html for more details.

      <br/><strong>Default Value:</strong> <code>gp3</code>

    </td>
   </tr>

   <tr id="RootVolumeEncrypted">
    <td>
     <code>RootVolumeEncrypted</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>root_volume_encrypted</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Indicates whether the EBS volume is encrypted.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="RootVolumeIops">
    <td>
     <code>RootVolumeIops</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>root_volume_iops</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     If the `RootVolumeType` is gp3, io1, or io2, the number of IOPS to provision for the root volume.

      <br/><strong>Default Value:</strong> <code>1000</code>

    </td>
   </tr>

   <tr id="RootVolumeThroughput">
    <td>
     <code>RootVolumeThroughput</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>root_volume_throughput</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     If the `RootVolumeType` is gp3, the throughput (MB/s data transfer rate) to provision for the root volume.

      <br/><strong>Default Value:</strong> <code>125</code>

    </td>
   </tr>

   <tr id="ManagedPolicyARNs">
    <td>
     <code>ManagedPolicyARNs</code>
     <br><code>(CommaDelimitedList)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>managed_policy_arns</code>
      <br><code>(list(string))</code>
     
    </td>
    <td>
     Optional - Comma separated list of managed IAM policy ARNs to attach to the instance role.

    </td>
   </tr>

   <tr id="ScalerManagedPolicyARNs">
    <td>
     <code>ScalerManagedPolicyARNs</code>
     <br><code>(CommaDelimitedList)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <em>N/A</em>
     
    </td>
    <td>
     Optional - Comma separated list of managed IAM policy ARNs to attach to the autoscaling Lambda execution role.

    </td>
   </tr>

   <tr id="InstanceRoleARN">
    <td>
     <code>InstanceRoleARN</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>instance_role_arn</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - ARN of an existing IAM role to attach to instances instead of creating a new role. When specified, the stack will not create any IAM roles or policies, and will use this role instead. The role must have all necessary permissions for Buildkite agents to function correctly. This is useful when you want to share a single IAM role across multiple queues/stacks. Supports roles with custom paths up to 10 levels deep. See https://buildkite.com/docs/agent/v3/aws/elastic-ci-stack/ec2-linux-and-windows/managing-elastic-ci-stack#using-custom-iam-roles for required permissions and configuration examples.

      <br/><strong>Allowed Pattern:</strong> <code>^$|^arn\:aws\:iam\::[0-9]+\:role/.*$</code>

    </td>
   </tr>

   <tr id="InstanceRoleName">
    <td>
     <code>InstanceRoleName</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>instance_role_name</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - A name for the IAM Role attached to the Instance Profile when creating a new role. Ignored when InstanceRoleARN is provided.

    </td>
   </tr>

   <tr id="InstanceRolePermissionsBoundaryARN">
    <td>
     <code>InstanceRolePermissionsBoundaryARN</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>instance_role_permissions_boundary_arn</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - The ARN of the policy used to set the permissions boundary for the role when creating a new role. Ignored when InstanceRoleARN is provided.

    </td>
   </tr>

   <tr id="InstanceRoleTags">
    <td>
     <code>InstanceRoleTags</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>instance_role_tags</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Comma-separated key=value pairs for instance IAM role tags (up to 5 tags). Example: 'Environment=production,Team=platform,Purpose=ci'. Note: Keys and values cannot contain '=' characters. Only applied when creating a new role, ignored when InstanceRoleARN is provided.

      <br/><strong>Allowed Pattern:</strong> <code>^$|^[\w\s_.\:/+\-@]+=[\w\s_.\:/+\-@]*(,[\w\s_.\:/+\-@]+=[\w\s_.\:/+\-@]*){0,4}$</code>

    </td>
   </tr>

   <tr id="IMDSv2Tokens">
    <td>
     <code>IMDSv2Tokens</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>imdsv2_tokens</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Security setting for EC2 instance metadata access. 'Required' enforces secure token-based access (recommended for security), 'Optional' allows both secure and legacy access methods. Use 'Required' unless legacy applications require the older metadata service.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>optional</code></li>
        
         <li><code>required</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>optional</code>

    </td>
   </tr>

   <tr id="EnableDetailedMonitoring">
    <td>
     <code>EnableDetailedMonitoring</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>enable_detailed_monitoring</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Enable detailed EC2 monitoring.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="InstanceName">
    <td>
     <code>InstanceName</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>instance_name</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Customize the EC2 instance Name tag.

    </td>
   </tr>

   <tr id="ExperimentalEnableResourceLimits">
    <td>
     <code>ExperimentalEnableResourceLimits</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>experimental_enable_resource_limits</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Experimental - If true, enables systemd resource limits for the Buildkite agent. This helps prevent resource exhaustion by limiting CPU, memory, and I/O usage. Useful for shared instances running multiple agents or resource-intensive builds.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="ResourceLimitsMemoryHigh">
    <td>
     <code>ResourceLimitsMemoryHigh</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>resource_limits_memory_high</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Experimental - Sets the MemoryHigh limit for the Buildkite agent slice. The value can be a percentage (e.g., '90%') or an absolute value (e.g., '4G').

      <br/><strong>Default Value:</strong> <code>90%</code>

      <br/><strong>Allowed Pattern:</strong> <code>^(\d+([KkMmGgTt])?|(?:[1-9][0-9]?|100)%|infinity)$</code>

    </td>
   </tr>

   <tr id="ResourceLimitsMemoryMax">
    <td>
     <code>ResourceLimitsMemoryMax</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>resource_limits_memory_max</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Experimental - Sets the MemoryMax limit for the Buildkite agent slice. The value can be a percentage (e.g., '90%') or an absolute value (e.g., '4G').

      <br/><strong>Default Value:</strong> <code>90%</code>

      <br/><strong>Allowed Pattern:</strong> <code>^(\d+([KkMmGgTt])?|(?:[1-9][0-9]?|100)%|infinity)$</code>

    </td>
   </tr>

   <tr id="ResourceLimitsMemorySwapMax">
    <td>
     <code>ResourceLimitsMemorySwapMax</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>resource_limits_memory_swap_max</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Experimental - Sets the MemorySwapMax limit for the Buildkite agent slice. The value can be a percentage (e.g., '90%') or an absolute value (e.g., '4G').

      <br/><strong>Default Value:</strong> <code>90%</code>

      <br/><strong>Allowed Pattern:</strong> <code>^(\d+([KkMmGgTt])?|(?:[1-9][0-9]?|100)%|infinity)$</code>

    </td>
   </tr>

   <tr id="ResourceLimitsCPUWeight">
    <td>
     <code>ResourceLimitsCPUWeight</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>resource_limits_cpu_weight</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     Experimental - Sets the CPU weight for the Buildkite agent slice (1-10000, default 100). Higher values give more CPU time to the agent.

      <br/><strong>Default Value:</strong> <code>100</code>

      <br/><strong>Minimum Value:</strong> 1

      <br/><strong>Maximum Value:</strong> 10000

    </td>
   </tr>

   <tr id="ResourceLimitsCPUQuota">
    <td>
     <code>ResourceLimitsCPUQuota</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>resource_limits_cpu_quota</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Experimental - Sets the CPU quota for the Buildkite agent slice. Takes a percentage value, suffixed with "%".

      <br/><strong>Default Value:</strong> <code>90%</code>

      <br/><strong>Allowed Pattern:</strong> <code>^\d+%$</code>

    </td>
   </tr>

   <tr id="ResourceLimitsIOWeight">
    <td>
     <code>ResourceLimitsIOWeight</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>resource_limits_io_weight</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     Experimental - Sets the I/O weight for the Buildkite agent slice (1-10000, default 80). Higher values give more I/O bandwidth to the agent.

      <br/><strong>Default Value:</strong> <code>80</code>

      <br/><strong>Minimum Value:</strong> 1

      <br/><strong>Maximum Value:</strong> 10000

    </td>
   </tr>
  
 </tbody>
</table>

<h2>Auto-scaling Configuration</h2>

<table>
 <tbody>
  <tr>
   <th>CloudFormation parameter</th>
   <th>Terraform variable</th>
   <th>Description</th>
  </tr>

   <tr id="MinSize">
    <td>
     <code>MinSize</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>min_size</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     Minimum number of instances. Ensures baseline capacity for immediate job execution.

      <br/><strong>Default Value:</strong> <code>0</code>

      <br/><strong>Minimum Value:</strong> 0

    </td>
   </tr>

   <tr id="MaxSize">
    <td>
     <code>MaxSize</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>max_size</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     Maximum number of instances. Controls cost ceiling and prevents runaway scaling.

      <br/><strong>Default Value:</strong> <code>10</code>

      <br/><strong>Minimum Value:</strong> 0

    </td>
   </tr>

   <tr id="InstanceBuffer">
    <td>
     <code>InstanceBuffer</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>instance_buffer</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     Number of idle instances to keep running. Lower values save costs, higher values reduce wait times for new jobs.

      <br/><strong>Default Value:</strong> <code>0</code>

    </td>
   </tr>

   <tr id="DisableScaleIn">
    <td>
     <code>DisableScaleIn</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>disable_scale_in</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Whether the desired count should ever be decreased on the Auto Scaling group. When set to "true" (default), the scaler will not reduce the Auto Scaling group's desired capacity, and instances are expected to self-terminate when idle.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>true</code>

    </td>
   </tr>

   <tr id="InstanceScaleInProtection">
    <td>
     <code>InstanceScaleInProtection</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <em>N/A</em>
     
    </td>
    <td>
     Whether new instances launched by the Auto Scaling group should have scale-in protection enabled. When set to "true" (default), instances cannot be terminated by scale-in actions and must self-terminate when idle. Set to "false" to allow CloudFormation and the ASG to terminate instances directly.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>true</code>

    </td>
   </tr>

   <tr id="OnDemandBaseCapacity">
    <td>
     <code>OnDemandBaseCapacity</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>on_demand_base_capacity</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     Specify how much On-Demand capacity the Auto Scaling group should have for its base portion before scaling by percentages. The maximum group size will be increased (but not decreased) to this value.

      <br/><strong>Default Value:</strong> <code>0</code>

      <br/><strong>Minimum Value:</strong> 0

    </td>
   </tr>

   <tr id="OnDemandPercentage">
    <td>
     <code>OnDemandPercentage</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>on_demand_percentage</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     Percentage of instances to launch as OnDemand vs Spot instances. OnDemand instances provide guaranteed availability at higher cost. Spot instances offer 60-90% cost savings but may be interrupted by AWS. Use 100% for critical workloads, lower values when jobs can handle unexpected instance interruptions.

      <br/><strong>Default Value:</strong> <code>100</code>

      <br/><strong>Minimum Value:</strong> 0

      <br/><strong>Maximum Value:</strong> 100

    </td>
   </tr>

   <tr id="SpotAllocationStrategy">
    <td>
     <code>SpotAllocationStrategy</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>spot_allocation_strategy</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Strategy for selecting Spot instance types to minimize interruptions and costs. 'capacity-optimized' (recommended) chooses types with the most available capacity. 'price-capacity-optimized' balances low prices with availability. 'lowest-price' prioritizes cost savings. 'capacity-optimized-prioritized' follows InstanceTypes order while optimizing for capacity.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>price-capacity-optimized</code></li>
        
         <li><code>capacity-optimized</code></li>
        
         <li><code>lowest-price</code></li>
        
         <li><code>capacity-optimized-prioritized</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>capacity-optimized</code>

    </td>
   </tr>

   <tr id="ScaleOutFactor">
    <td>
     <code>ScaleOutFactor</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>scale_out_factor</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     Multiplier for scale-out speed. Values higher than 1.0 create instances more aggressively, values lower than 1.0 more conservatively. Use higher values for time-sensitive workloads, lower values to control costs.

      <br/><strong>Default Value:</strong> <code>1.0</code>

    </td>
   </tr>

   <tr id="ScaleOutCooldownPeriod">
    <td>
     <code>ScaleOutCooldownPeriod</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>scale_out_cooldown_period</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     Cooldown period in seconds before allowing another scale-out event. Prevents rapid scaling and reduces costs from frequent instance launches.

      <br/><strong>Default Value:</strong> <code>300</code>

    </td>
   </tr>

   <tr id="ScaleInIdlePeriod">
    <td>
     <code>ScaleInIdlePeriod</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>scale_in_idle_period</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     Number of seconds ALL agents on an instance must be idle before the instance is terminated. When all AgentsPerInstance agents are idle for this duration, the entire instance is terminated, not individual agents. This parameter controls instance-level scaling behavior.

      <br/><strong>Default Value:</strong> <code>600</code>

    </td>
   </tr>

   <tr id="ScaleInCooldownPeriod">
    <td>
     <code>ScaleInCooldownPeriod</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>scale_in_cooldown_period</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     Cooldown period in seconds before allowing another scale-in event. Longer periods prevent premature termination when job queues fluctuate.

      <br/><strong>Default Value:</strong> <code>3600</code>

    </td>
   </tr>

   <tr id="ScaleOutForWaitingJobs">
    <td>
     <code>ScaleOutForWaitingJobs</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>scale_out_for_waiting_jobs</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Scale up instances for pipeline steps queued behind manual approval or wait steps. When enabled, the scaler will provision instances even when jobs can't start immediately due to pipeline waits. Ensure ScaleInIdlePeriod is long enough to keep instances running during wait periods.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="InstanceCreationTimeout">
    <td>
     <code>InstanceCreationTimeout</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>instance_creation_timeout</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional - Timeout period for Auto Scaling Group Creation Policy.

    </td>
   </tr>

   <tr id="ScalerEventSchedulePeriod">
    <td>
     <code>ScalerEventSchedulePeriod</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>scaler_event_schedule_period</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     How often the Event Schedule for buildkite-agent-scaler is triggered. Should be an expression with units. Example: '30 seconds', '1 minute', '5 minutes'.

      <br/><strong>Default Value:</strong> <code>1 minute</code>

    </td>
   </tr>

   <tr id="ScalerMinPollInterval">
    <td>
     <code>ScalerMinPollInterval</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>scaler_min_poll_interval</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Minimum time between auto-scaler checks for new build jobs (e.g., '30s', '1m').

      <br/><strong>Default Value:</strong> <code>10s</code>

    </td>
   </tr>

   <tr id="ScalerEnableExperimentalElasticCIMode">
    <td>
     <code>ScalerEnableExperimentalElasticCIMode</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>scaler_enable_elastic_ci_mode</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Experimental - Enable the Elastic CI Mode with enhanced features like graceful termination and dangling instance detection.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="EnableScheduledScaling">
    <td>
     <code>EnableScheduledScaling</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>enable_scheduled_scaling</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Enable scheduled scaling to automatically adjust MinSize based on time-based schedules

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="ScheduleTimezone">
    <td>
     <code>ScheduleTimezone</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>schedule_timezone</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Timezone for scheduled scaling actions (only used when EnableScheduledScaling is true). See AWS documentation for supported formats: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html#scheduled-scaling-timezone (America/New_York, UTC, Europe/London, etc.)

      <br/><strong>Default Value:</strong> <code>UTC</code>

    </td>
   </tr>

   <tr id="ScaleUpSchedule">
    <td>
     <code>ScaleUpSchedule</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>scale_up_schedule</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Cron expression for when to scale up (only used when EnableScheduledScaling is true). See AWS documentation for format details: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html#scheduled-scaling-cron ("0 8 * * MON-FRI" for 8 AM weekdays)

      <br/><strong>Default Value:</strong> <code>0 8 * * MON-FRI</code>

      <br/><strong>Allowed Pattern:</strong> <code>^[0-9*,-/]+ [0-9*,-/]+ [0-9*,-/]+ [0-9*,-/]+ [0-9A-Za-z*,-/]+$</code>

    </td>
   </tr>

   <tr id="ScaleUpMinSize">
    <td>
     <code>ScaleUpMinSize</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>scale_up_min_size</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     MinSize to set when the ScaleUpSchedule is triggered (applied at the time specified in ScaleUpSchedule, only used when EnableScheduledScaling is true). Cannot exceed MaxSize.

      <br/><strong>Default Value:</strong> <code>1</code>

      <br/><strong>Minimum Value:</strong> 0

    </td>
   </tr>

   <tr id="ScaleDownSchedule">
    <td>
     <code>ScaleDownSchedule</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>scale_down_schedule</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Cron expression for when to scale down (only used when EnableScheduledScaling is true). See AWS documentation for format details: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html#scheduled-scaling-cron ("0 18 * * MON-FRI" for 6 PM weekdays)

      <br/><strong>Default Value:</strong> <code>0 18 * * MON-FRI</code>

      <br/><strong>Allowed Pattern:</strong> <code>^[0-9*,-/]+ [0-9*,-/]+ [0-9*,-/]+ [0-9*,-/]+ [0-9A-Za-z*,-/]+$</code>

    </td>
   </tr>

   <tr id="ScaleDownMinSize">
    <td>
     <code>ScaleDownMinSize</code>
     <br><code>(Number)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>scale_down_min_size</code>
      <br><code>(number)</code>
     
    </td>
    <td>
     MinSize to set when the ScaleDownSchedule is triggered (applied at the time specified in ScaleDownSchedule, only used when EnableScheduledScaling is true)

      <br/><strong>Default Value:</strong> <code>0</code>

      <br/><strong>Minimum Value:</strong> 0

    </td>
   </tr>
  
 </tbody>
</table>

<h2>Cost Allocation Configuration</h2>

<table>
 <tbody>
  <tr>
   <th>CloudFormation parameter</th>
   <th>Terraform variable</th>
   <th>Description</th>
  </tr>

   <tr id="EnableCostAllocationTags">
    <td>
     <code>EnableCostAllocationTags</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>enable_cost_allocation_tags</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Enables AWS Cost Allocation tags for all resources in the stack. See https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="CostAllocationTagName">
    <td>
     <code>CostAllocationTagName</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>cost_allocation_tag_name</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     The name of the Cost Allocation Tag used for billing purposes.

      <br/><strong>Default Value:</strong> <code>CreatedBy</code>

    </td>
   </tr>

   <tr id="CostAllocationTagValue">
    <td>
     <code>CostAllocationTagValue</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>cost_allocation_tag_value</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     The value of the Cost Allocation Tag used for billing purposes.

      <br/><strong>Default Value:</strong> <code>buildkite-elastic-ci-stack-for-aws</code>

    </td>
   </tr>
  
 </tbody>
</table>

<h2>Docker Daemon Configuration</h2>

<table>
 <tbody>
  <tr>
   <th>CloudFormation parameter</th>
   <th>Terraform variable</th>
   <th>Description</th>
  </tr>

   <tr id="EnableDockerUserNamespaceRemap">
    <td>
     <code>EnableDockerUserNamespaceRemap</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>enable_docker_user_namespace_remap</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Enables Docker user namespace remapping so docker runs as buildkite-agent.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>true</code>

    </td>
   </tr>

   <tr id="EnableDockerExperimental">
    <td>
     <code>EnableDockerExperimental</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>enable_docker_experimental</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Enables Docker experimental features.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>
  
 </tbody>
</table>

<h2>Docker Networking Configuration</h2>

<table>
 <tbody>
  <tr>
   <th>CloudFormation parameter</th>
   <th>Terraform variable</th>
   <th>Description</th>
  </tr>

   <tr id="DockerNetworkingProtocol">
    <td>
     <code>DockerNetworkingProtocol</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>docker_networking_protocol</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Which IP version to enable for docker containers and building docker images. Only applies to Linux instances, not Windows.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>ipv4</code></li>
        
         <li><code>dualstack</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>ipv4</code>

    </td>
   </tr>

   <tr id="DockerIPv4AddressPool1">
    <td>
     <code>DockerIPv4AddressPool1</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>docker_ipv4_address_pool_1</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Primary IPv4 CIDR block for Docker default address pools. Must not conflict with host network or VPC CIDR. Only applies to Linux instances, not Windows.

      <br/><strong>Default Value:</strong> <code>172.17.0.0/12</code>

      <br/><strong>Allowed Pattern:</strong> <code>^(?\:(?\:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?\:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\/(?\:[0-9]|[12][0-9]|3[0-2])$</code>

    </td>
   </tr>

   <tr id="DockerIPv4AddressPool2">
    <td>
     <code>DockerIPv4AddressPool2</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>docker_ipv4_address_pool_2</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Secondary IPv4 CIDR block for Docker default address pools. Only applies to Linux instances, not Windows.

      <br/><strong>Default Value:</strong> <code>192.168.0.0/16</code>

      <br/><strong>Allowed Pattern:</strong> <code>^(?\:(?\:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?\:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\/(?\:[0-9]|[12][0-9]|3[0-2])$</code>

    </td>
   </tr>

   <tr id="DockerIPv6AddressPool">
    <td>
     <code>DockerIPv6AddressPool</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>docker_ipv6_address_pool</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     IPv6 CIDR block for Docker default address pools in dualstack mode. Only applies to Linux instances, not Windows.

      <br/><strong>Default Value:</strong> <code>2001\:db8\:2::/104</code>

      <br/><strong>Allowed Pattern:</strong> <code>^(?\:(?\:[0-9a-fA-F]{1,4}\:){7}[0-9a-fA-F]{1,4}|(?\:[0-9a-fA-F]{1,4}\:){1,7}\:|(?\:[0-9a-fA-F]{1,4}\:){1,6}\:[0-9a-fA-F]{1,4}|(?\:[0-9a-fA-F]{1,4}\:){1,5}(?\:\:[0-9a-fA-F]{1,4}){1,2}|(?\:[0-9a-fA-F]{1,4}\:){1,4}(?\:\:[0-9a-fA-F]{1,4}){1,3}|(?\:[0-9a-fA-F]{1,4}\:){1,3}(?\:\:[0-9a-fA-F]{1,4}){1,4}|(?\:[0-9a-fA-F]{1,4}\:){1,2}(?\:\:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}\:(?\::[0-9a-fA-F]{1,4}){1,6}|\:(?\:(?\:\:[0-9a-fA-F]{1,4}){1,7}|\:))\/(?:[0-9]|[1-9][0-9]|1[01][0-9]|12[0-8])$</code>

    </td>
   </tr>

   <tr id="DockerFixedCidrV4">
    <td>
     <code>DockerFixedCidrV4</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>docker_fixed_cidr_v4</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Optional IPv4 CIDR block for Docker's fixed-cidr option. Restricts the IP range Docker uses for container networking on the default bridge. Must be a subset of the first pool in DockerIPv4AddressPool1 (Docker allocates docker0 from the first pool). Leave empty to disable. Useful to prevent conflicts with external services like databases. Only applies to Linux instances, not Windows.

      <br/><strong>Allowed Pattern:</strong> <code>^$|^(?\:(?\:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?\:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\/(?\:[0-9]|[12][0-9]|3[0-2])$</code>

    </td>
   </tr>

   <tr id="DockerFixedCidrV6">
    <td>
     <code>DockerFixedCidrV6</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>docker_fixed_cidr_v6</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     IPv6 CIDR block for Docker's fixed-cidr-v6 option in dualstack mode. Restricts the IP range Docker uses for IPv6 container networking. Only applies to Linux instances in dualstack mode, not Windows.

      <br/><strong>Default Value:</strong> <code>2001\:db8\:1::/64</code>

      <br/><strong>Allowed Pattern:</strong> <code>^(?\:(?\:[0-9a-fA-F]{1,4}\:){7}[0-9a-fA-F]{1,4}|(?\:[0-9a-fA-F]{1,4}\:){1,7}\:|(?\:[0-9a-fA-F]{1,4}\:){1,6}\:[0-9a-fA-F]{1,4}|(?\:[0-9a-fA-F]{1,4}\:){1,5}(?\:\:[0-9a-fA-F]{1,4}){1,2}|(?\:[0-9a-fA-F]{1,4}\:){1,4}(?\:\:[0-9a-fA-F]{1,4}){1,3}|(?\:[0-9a-fA-F]{1,4}\:){1,3}(?\:\:[0-9a-fA-F]{1,4}){1,4}|(?\:[0-9a-fA-F]{1,4}\:){1,2}(?\:\:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}\:(?\::[0-9a-fA-F]{1,4}){1,6}|\:(?\:(?\:\:[0-9a-fA-F]{1,4}){1,7}|\:))\/(?:[0-9]|[1-9][0-9]|1[01][0-9]|12[0-8])$</code>

    </td>
   </tr>
  
 </tbody>
</table>

<h2>Docker Registry Configuration</h2>

<table>
 <tbody>
  <tr>
   <th>CloudFormation parameter</th>
   <th>Terraform variable</th>
   <th>Description</th>
  </tr>

   <tr id="ECRAccessPolicy">
    <td>
     <code>ECRAccessPolicy</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>ecr_access_policy</code>
      <br><code>(string)</code>
     
    </td>
    <td>
     Docker image registry permissions for agents. 'none' = no access, 'readonly' = pull images only, 'poweruser' = pull/push images, 'full' = complete ECR access. The '-pullthrough' variants (e.g., 'readonly-pullthrough') add permissions to enable automatic caching of public Docker images, reducing pull times and bandwidth costs.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>none</code></li>
        
         <li><code>readonly</code></li>
        
         <li><code>readonly-pullthrough</code></li>
        
         <li><code>poweruser</code></li>
        
         <li><code>poweruser-pullthrough</code></li>
        
         <li><code>full</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>none</code>

    </td>
   </tr>
  
 </tbody>
</table>

<h2>Plugin Configuration</h2>

<table>
 <tbody>
  <tr>
   <th>CloudFormation parameter</th>
   <th>Terraform variable</th>
   <th>Description</th>
  </tr>

   <tr id="EnableSecretsPlugin">
    <td>
     <code>EnableSecretsPlugin</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>enable_secrets_plugin</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Enables S3 Secrets plugin for all pipelines.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>true</code>

    </td>
   </tr>

   <tr id="EnableECRPlugin">
    <td>
     <code>EnableECRPlugin</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>enable_ecr_plugin</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Enables ECR plugin for all pipelines.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>true</code>

    </td>
   </tr>

   <tr id="EnableECRCredentialHelper">
    <td>
     <code>EnableECRCredentialHelper</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>enable_ecr_credential_helper</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Enable Amazon ECR Credential Helper in ECR plugin for Docker authentication.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>false</code>

    </td>
   </tr>

   <tr id="EnableDockerLoginPlugin">
    <td>
     <code>EnableDockerLoginPlugin</code>
     <br><code>(String)</code>
    </td>
    <td style="white-space: nowrap;">
     
      <code>enable_docker_login_plugin</code>
      <br><code>(bool)</code>
     
    </td>
    <td>
     Enables docker-login plugin for all pipelines.

      <br/><strong>Allowed Values</strong>:
       <ul>
        
         <li><code>true</code></li>
        
         <li><code>false</code></li>
        
       </ul>

      <br/><strong>Default Value:</strong> <code>true</code>

    </td>
   </tr>
  
 </tbody>
</table>

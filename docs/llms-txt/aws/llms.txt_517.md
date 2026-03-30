# Source: https://docs.aws.amazon.com/launchwizard/latest/APIReference/llms.txt

# AWS Launch Wizard Welcome

> AWS Launch Wizard offers a guided way of sizing, configuring, and deploying AWS resources for third party applications, such as Microsoft SQL Server Always On and HANA based SAP systems, without the need to manually identify and provision individual AWS resources.

- [Welcome](https://docs.aws.amazon.com/launchwizard/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/launchwizard/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/launchwizard/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_Operations.html)

- [CreateDeployment](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_CreateDeployment.html): Creates a deployment for the given workload.
- [DeleteDeployment](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeleteDeployment.html): Deletes a deployment.
- [GetDeployment](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetDeployment.html): Returns information about the deployment.
- [GetDeploymentPatternVersion](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetDeploymentPatternVersion.html): Returns information about a deployment pattern version.
- [GetWorkload](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkload.html): Returns information about a workload.
- [GetWorkloadDeploymentPattern](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html): Returns details for a given workload and deployment pattern, including the available specifications.
- [ListDeploymentEvents](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListDeploymentEvents.html): Lists the events of a deployment.
- [ListDeploymentPatternVersions](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListDeploymentPatternVersions.html): Lists the deployment pattern versions.
- [ListDeployments](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListDeployments.html): Lists the deployments that have been created.
- [ListTagsForResource](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListTagsForResource.html): Lists the tags associated with a specified resource.
- [ListWorkloadDeploymentPatterns](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html): Lists the workload deployment patterns for a given workload name.
- [ListWorkloads](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html): Lists the available workload names.
- [TagResource](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_TagResource.html): Adds the specified tags to the given resource.
- [UntagResource](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_UntagResource.html): Removes the specified tags from the given resource.
- [UpdateDeployment](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_UpdateDeployment.html): Updates a deployment.


## [Data Types](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_Types.html)

- [DeploymentConditionalField](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeploymentConditionalField.html): A field that details a condition of the specifications for a deployment.
- [DeploymentData](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeploymentData.html): The data associated with a deployment.
- [DeploymentDataSummary](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeploymentDataSummary.html): A summary of the deployment data.
- [DeploymentEventDataSummary](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeploymentEventDataSummary.html): A summary of the deployment event data.
- [DeploymentFilter](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeploymentFilter.html): A filter name and value pair that is used to return more specific results from a describe operation.
- [DeploymentPatternVersionDataSummary](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeploymentPatternVersionDataSummary.html): Describes a deployment pattern version summary.
- [DeploymentPatternVersionFilter](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeploymentPatternVersionFilter.html): A filter for deployment pattern versions.
- [DeploymentSpecificationsField](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeploymentSpecificationsField.html): A field that details a specification of a deployment pattern.
- [WorkloadData](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_WorkloadData.html): Describes a workload.
- [WorkloadDataSummary](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_WorkloadDataSummary.html): Describes workload data.
- [WorkloadDeploymentPatternData](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_WorkloadDeploymentPatternData.html): The data that details a workload deployment pattern.
- [WorkloadDeploymentPatternDataSummary](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_WorkloadDeploymentPatternDataSummary.html): Describes a workload deployment pattern.


## [SAP deployment specifications](https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html)

- [SapHanaHA](https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap-hana-ha.html): The following is an example of the specifications required to create a SAP HANA high-availability deployment with HANA database software installed:
- [SapHanaMulti](https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap-hana-multi.html): The following is an example of the specifications required to create a SAP HANA deployment with multiple nodes and HANA database software installed:
- [SapHanaSingle](https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap-hana-single.html): The following is an example of the specifications required to create a SAP HANA single-node deployment with HANA database software installed:
- [SapNWOnHanaHA](https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap-netweaver-ha.html): The following are examples of the specifications required to create high-availability deployments with SAP software installed.
- [SapNWOnHanaMulti](https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap-netweaver-multi.html): The following are examples of the specifications required to create multi-node deployments.
- [SapNWOnHanaSingle](https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap-netweaver-single.html): The following are examples of the specifications required to create single-node deployments.
- [SapNWOnAseSingle](https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap-netweaver-ase-single.html): The following is an example of the specifications required to create a single-node deployment with SAP software installed:
- [SapNWOnAseMulti](https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap-netweaver-ase-multi.html): The following are examples of the specifications required to create multi-node deployments.

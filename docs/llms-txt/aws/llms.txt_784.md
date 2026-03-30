# Source: https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/llms.txt

# AWS SimSpace Weaver API Reference

> AWS SimSpace Weaver (SimSpace Weaver) is a service that you can use to build and run large-scale spatial simulations in the AWS Cloud. For example, you can create crowd simulations, large real-world environments, and immersive and interactive experiences. For more information about SimSpace Weaver, see the AWS SimSpace Weaver User Guide .

- [Welcome](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_Operations.html)

- [CreateSnapshot](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_CreateSnapshot.html)
- [DeleteApp](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_DeleteApp.html)
- [DeleteSimulation](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_DeleteSimulation.html)
- [DescribeApp](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_DescribeApp.html)
- [DescribeSimulation](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_DescribeSimulation.html)
- [ListApps](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_ListApps.html)
- [ListSimulations](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_ListSimulations.html)
- [ListTagsForResource](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_ListTagsForResource.html)
- [StartApp](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_StartApp.html)
- [StartClock](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_StartClock.html)
- [StartSimulation](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_StartSimulation.html)
- [StopApp](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_StopApp.html)
- [StopClock](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_StopClock.html)
- [StopSimulation](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_StopSimulation.html)
- [TagResource](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_TagResource.html)
- [UntagResource](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_UntagResource.html)


## [Data Types](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_Types.html)

- [CloudWatchLogsLogGroup](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_CloudWatchLogsLogGroup.html): The Amazon CloudWatch Logs log group for the simulation.
- [Domain](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_Domain.html): A collection of app instances that run the same executable app code and have the same launch options and commands.
- [LaunchOverrides](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_LaunchOverrides.html): Options that apply when the app starts.
- [LiveSimulationState](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_LiveSimulationState.html): A collection of additional state information, such as domain and clock configuration.
- [LogDestination](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_LogDestination.html): The location where SimSpace Weaver sends simulation log data.
- [LoggingConfiguration](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_LoggingConfiguration.html): The logging configuration for a simulation.
- [S3Destination](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_S3Destination.html): An Amazon S3 bucket and optional folder (object key prefix) where SimSpace Weaver creates a file.
- [S3Location](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_S3Location.html): A location in Amazon Simple Storage Service (Amazon S3) where SimSpace Weaver stores simulation data, such as your app .zip files and schema file.
- [SimulationAppEndpointInfo](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_SimulationAppEndpointInfo.html): Information about the network endpoint that you can use to connect to your custom or service app.
- [SimulationAppMetadata](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_SimulationAppMetadata.html): A collection of metadata about the app.
- [SimulationAppPortMapping](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_SimulationAppPortMapping.html): A collection of TCP/UDP ports for a custom or service app.
- [SimulationClock](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_SimulationClock.html): Status information about the simulation clock.
- [SimulationMetadata](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_SimulationMetadata.html): A collection of data about the simulation.

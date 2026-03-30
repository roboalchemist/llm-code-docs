# Source: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/llms.txt

# AWS Migration Hub Refactor Spaces API Reference

> Explains how to use AWS Migration Hub Refactor Spaces (Refactor Spaces).

- [Welcome](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_Operations.html)

- [CreateApplication](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateApplication.html)
- [CreateEnvironment](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html)
- [CreateRoute](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateRoute.html)
- [CreateService](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateService.html)
- [DeleteApplication](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DeleteApplication.html)
- [DeleteEnvironment](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DeleteEnvironment.html)
- [DeleteResourcePolicy](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DeleteResourcePolicy.html)
- [DeleteRoute](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DeleteRoute.html)
- [DeleteService](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DeleteService.html)
- [GetApplication](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetApplication.html)
- [GetEnvironment](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetEnvironment.html)
- [GetResourcePolicy](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetResourcePolicy.html)
- [GetRoute](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetRoute.html)
- [GetService](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetService.html)
- [ListApplications](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListApplications.html)
- [ListEnvironments](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListEnvironments.html)
- [ListEnvironmentVpcs](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListEnvironmentVpcs.html)
- [ListRoutes](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListRoutes.html)
- [ListServices](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListServices.html)
- [ListTagsForResource](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListTagsForResource.html)
- [PutResourcePolicy](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_PutResourcePolicy.html)
- [TagResource](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_TagResource.html)
- [UntagResource](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_UntagResource.html)
- [UpdateRoute](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_UpdateRoute.html)


## [Data Types](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_Types.html)

- [ApiGatewayProxyConfig](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ApiGatewayProxyConfig.html): A wrapper object holding the Amazon API Gateway proxy configuration.
- [ApiGatewayProxyInput](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ApiGatewayProxyInput.html): A wrapper object holding the Amazon API Gateway endpoint input.
- [ApiGatewayProxySummary](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ApiGatewayProxySummary.html): A wrapper object holding the Amazon API Gateway proxy summary.
- [ApplicationSummary](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ApplicationSummary.html): The list of ApplicationSummary objects.
- [DefaultRouteInput](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DefaultRouteInput.html): The configuration for the default route type.
- [EnvironmentSummary](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_EnvironmentSummary.html): The summary information for environments as a response to ListEnvironments.
- [EnvironmentVpc](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_EnvironmentVpc.html): Provides summary information for the EnvironmentVpc resource as a response to ListEnvironmentVpc.
- [ErrorResponse](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ErrorResponse.html): Error associated with a resource returned for a Get or List resource response.
- [LambdaEndpointConfig](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_LambdaEndpointConfig.html): The configuration for the AWS Lambda endpoint type.
- [LambdaEndpointInput](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_LambdaEndpointInput.html): The input for the AWS Lambda endpoint type.
- [LambdaEndpointSummary](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_LambdaEndpointSummary.html): The summary for the AWS Lambda endpoint type.
- [RouteSummary](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_RouteSummary.html): The summary information for the routes as a response to ListRoutes.
- [ServiceSummary](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ServiceSummary.html): A summary for the service as a response to ListServices.
- [UriPathRouteInput](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_UriPathRouteInput.html): The configuration for the URI path route type.
- [UrlEndpointConfig](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_UrlEndpointConfig.html): The configuration for the URL endpoint type.
- [UrlEndpointInput](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_UrlEndpointInput.html): The configuration for the URL endpoint type.
- [UrlEndpointSummary](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_UrlEndpointSummary.html): The summary of the configuration for the URL endpoint type.

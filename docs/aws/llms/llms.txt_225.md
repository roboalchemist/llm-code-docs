# Source: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/llms.txt

# Amazon CodeGuru Reviewer API Reference

> This section provides documentation for the Amazon CodeGuru Reviewer API operations. CodeGuru Reviewer is a service that uses program analysis and machine learning to detect potential defects that are difficult for developers to find and recommends fixes in your Java and Python code.

- [Welcome](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_Operations.html)

- [AssociateRepository](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_AssociateRepository.html)
- [CreateCodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateCodeReview.html)
- [CreateCodeReviewInternal](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateCodeReviewInternal.html)
- [CreateConnectionToken](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateConnectionToken.html)
- [DescribeCodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_DescribeCodeReview.html)
- [DescribeRecommendationFeedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_DescribeRecommendationFeedback.html)
- [DescribeRepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_DescribeRepositoryAssociation.html)
- [DisassociateRepository](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_DisassociateRepository.html)
- [GetMetricsData](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_GetMetricsData.html)
- [ListCodeReviews](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListCodeReviews.html)
- [ListRecommendationFeedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRecommendationFeedback.html)
- [ListRecommendations](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRecommendations.html)
- [ListRepositoryAssociations](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html)
- [ListTagsForResource](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListTagsForResource.html)
- [ListThirdPartyRepositories](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListThirdPartyRepositories.html)
- [PutRecommendationFeedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_PutRecommendationFeedback.html)
- [TagResource](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_TagResource.html)
- [UntagResource](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_UntagResource.html)


## [Data Types](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_Types.html)

- [AuthorizationToken](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_AuthorizationToken.html): Contains authorization information for accessing third-party repositories.
- [BranchDiffSourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_BranchDiffSourceCodeType.html): A type of SourceCodeType that specifies a code diff between a source and destination branch in an associated repository.
- [CodeArtifacts](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeArtifacts.html): Code artifacts are source code artifacts and build artifacts used in a repository analysis or a pull request review.
- [CodeCommitRepository](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeCommitRepository.html): Information about an AWS CodeCommit repository.
- [CodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html): Information about a code review.
- [CodeReviewSummary](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReviewSummary.html): Information about the summary of the code review.
- [CodeReviewType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReviewType.html): The type of a code review.
- [CommitDiffSourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CommitDiffSourceCodeType.html): A type of SourceCodeType that specifies the commit diff for a pull request on an associated repository.
- [EventInfo](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_EventInfo.html): Information about an event.
- [FindingsMetricsData](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_FindingsMetricsData.html): Contains metrics data about code analysis findings and statistics.
- [GitHubRepository](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_GitHubRepository.html): Information about a GitHub repository for code analysis.
- [KMSKeyDetails](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_KMSKeyDetails.html): An object that contains:
- [Metrics](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_Metrics.html): Information about the statistics from the code review.
- [MetricsSummary](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_MetricsSummary.html): Information about metrics summaries.
- [RecommendationFeedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RecommendationFeedback.html): Information about the recommendation feedback.
- [RecommendationFeedbackSummary](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RecommendationFeedbackSummary.html): Information about recommendation feedback summaries.
- [RecommendationSummary](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RecommendationSummary.html): Information about recommendations.
- [Repository](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_Repository.html): Information about an associated AWS CodeCommit repository or an associated repository that is managed by AWS CodeStar Connections (for example, Bitbucket).
- [RepositoryAnalysis](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAnalysis.html): A code review type that analyzes all code under a specified branch in an associated repository.
- [RepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html): Information about a repository association.
- [RepositoryAssociationSummary](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html): Summary information about a repository association.
- [RepositoryHeadSourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryHeadSourceCodeType.html): A SourceCodeType that specifies the tip of a branch in an associated repository.
- [RequestMetadata](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RequestMetadata.html): Metadata that is associated with a code review.
- [RuleMetadata](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RuleMetadata.html): Metadata about a rule.
- [S3BucketRepository](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_S3BucketRepository.html): Information about an associated repository in an S3 bucket.
- [S3Repository](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_S3Repository.html): Information about a repository in an S3 bucket.
- [S3RepositoryDetails](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_S3RepositoryDetails.html): Specifies the name of an S3 bucket and a CodeArtifacts object that contains the S3 object keys for a source code .zip file and for a build artifacts .zip file that contains .jar or .class files.
- [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType.html): Specifies the source code that is analyzed in a code review.
- [ThirdPartyRepository](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ThirdPartyRepository.html): Information about a third-party repository that can be connected to CodeGuru Reviewer.
- [ThirdPartySourceRepository](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ThirdPartySourceRepository.html): Information about a third-party source repository connected to CodeGuru Reviewer.

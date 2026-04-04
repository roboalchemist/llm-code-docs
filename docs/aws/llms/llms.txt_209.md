# Source: https://docs.aws.amazon.com/codeartifact/latest/APIReference/llms.txt

# AWS CodeArtifact Welcome

> AWS CodeArtifact is a fully managed artifact repository compatible with language-native package managers and build tools such as npm, Apache Maven, pip, and dotnet. You can use CodeArtifact to share packages with development teams and pull packages. Packages can be pulled from both public and CodeArtifact repositories. You can also create an upstream relationship between a CodeArtifact repository and another repository, which effectively merges their contents from the point of view of a package manager client.

- [Welcome](https://docs.aws.amazon.com/codeartifact/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/codeartifact/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/codeartifact/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_Operations.html)

- [AssociateExternalConnection](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssociateExternalConnection.html): Adds an existing external connection to a repository.
- [CopyPackageVersions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CopyPackageVersions.html): Copies package versions from one repository to another repository in the same domain.
- [CreateDomain](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreateDomain.html): Creates a domain.
- [CreatePackageGroup](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreatePackageGroup.html): Creates a package group.
- [CreateRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreateRepository.html): Creates a repository.
- [DeleteDomain](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeleteDomain.html): Deletes a domain.
- [DeleteDomainPermissionsPolicy](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeleteDomainPermissionsPolicy.html): Deletes the resource policy set on a domain.
- [DeletePackage](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackage.html): Deletes a package and all associated package versions.
- [DeletePackageGroup](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageGroup.html): Deletes a package group.
- [DeletePackageVersions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageVersions.html): Deletes one or more versions of a package.
- [DeleteRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeleteRepository.html): Deletes a repository.
- [DeleteRepositoryPermissionsPolicy](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeleteRepositoryPermissionsPolicy.html): Deletes the resource policy that is set on a repository.
- [DescribeDomain](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribeDomain.html): Returns a DomainDescription object that contains information about the requested domain.
- [DescribePackage](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackage.html): Returns a PackageDescription object that contains information about the requested package.
- [DescribePackageGroup](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageGroup.html): Returns a PackageGroupDescription object that contains information about the requested package group.
- [DescribePackageVersion](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html): Returns a PackageVersionDescription object that contains information about the requested package version.
- [DescribeRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribeRepository.html): Returns a RepositoryDescription object that contains detailed information about the requested repository.
- [DisassociateExternalConnection](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisassociateExternalConnection.html): Removes an existing external connection from a repository.
- [DisposePackageVersions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisposePackageVersions.html): Deletes the assets in package versions and sets the package versions' status to Disposed.
- [GetAssociatedPackageGroup](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetAssociatedPackageGroup.html): Returns the most closely associated package group to the specified package.
- [GetAuthorizationToken](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetAuthorizationToken.html): Generates a temporary authorization token for accessing repositories in the domain.
- [GetDomainPermissionsPolicy](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetDomainPermissionsPolicy.html): Returns the resource policy attached to the specified domain.
- [GetPackageVersionAsset](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetPackageVersionAsset.html): Returns an asset (or file) that is in a package.
- [GetPackageVersionReadme](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetPackageVersionReadme.html): Gets the readme file or descriptive text for a package version.
- [GetRepositoryEndpoint](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetRepositoryEndpoint.html): Returns the endpoint of a repository for a specific package format.
- [GetRepositoryPermissionsPolicy](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetRepositoryPermissionsPolicy.html): Returns the resource policy that is set on a repository.
- [ListAllowedRepositoriesForGroup](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListAllowedRepositoriesForGroup.html): Lists the repositories in the added repositories list of the specified restriction type for a package group.
- [ListAssociatedPackages](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListAssociatedPackages.html): Returns a list of packages associated with the requested package group.
- [ListDomains](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListDomains.html): Returns a list of DomainSummary objects for all domains owned by the AWS account that makes this call.
- [ListPackageGroups](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageGroups.html): Returns a list of package groups in the requested domain.
- [ListPackages](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackages.html): Returns a list of PackageSummary objects for packages in a repository that match the request parameters.
- [ListPackageVersionAssets](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersionAssets.html): Returns a list of AssetSummary objects for assets in a package version.
- [ListPackageVersionDependencies](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersionDependencies.html): Returns the direct dependencies for a package version.
- [ListPackageVersions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html): Returns a list of PackageVersionSummary objects for package versions in a repository that match the request parameters.
- [ListRepositories](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositories.html): Returns a list of RepositorySummary objects.
- [ListRepositoriesInDomain](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositoriesInDomain.html): Returns a list of RepositorySummary objects.
- [ListSubPackageGroups](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListSubPackageGroups.html): Returns a list of direct children of the specified package group.
- [ListTagsForResource](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListTagsForResource.html): Gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS CodeArtifact.
- [PublishPackageVersion](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PublishPackageVersion.html): Creates a new package version containing one or more assets (or files).
- [PutDomainPermissionsPolicy](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PutDomainPermissionsPolicy.html): Sets a resource policy on a domain that specifies permissions to access it.
- [PutPackageOriginConfiguration](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PutPackageOriginConfiguration.html): Sets the package origin configuration for a package.
- [PutRepositoryPermissionsPolicy](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PutRepositoryPermissionsPolicy.html): Sets the resource policy on a repository that specifies permissions to access it.
- [TagResource](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_TagResource.html): Adds or updates tags for a resource in AWS CodeArtifact.
- [UntagResource](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UntagResource.html): Removes tags from a resource in AWS CodeArtifact.
- [UpdatePackageGroup](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageGroup.html): Updates a package group.
- [UpdatePackageGroupOriginConfiguration](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageGroupOriginConfiguration.html): Updates the package origin configuration for a package group.
- [UpdatePackageVersionsStatus](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html): Updates the status of one or more versions of a package.
- [UpdateRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdateRepository.html): Update the properties of a repository.


## [Data Types](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_Types.html)

- [AssetSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html): Contains details about a package version asset.
- [AssociatedPackage](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssociatedPackage.html): A package associated with a package group.
- [DomainDescription](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainDescription.html): Information about a domain.
- [DomainEntryPoint](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainEntryPoint.html): Information about how a package originally entered the CodeArtifact domain.
- [DomainSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainSummary.html): Information about a domain, including its name, Amazon Resource Name (ARN), and status.
- [LicenseInfo](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_LicenseInfo.html): Details of the license data.
- [PackageDependency](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html): Details about a package dependency.
- [PackageDescription](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html): Details about a package.
- [PackageGroupAllowedRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupAllowedRepository.html): Details about an allowed repository for a package group, including its name and origin configuration.
- [PackageGroupDescription](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupDescription.html): The description of the package group.
- [PackageGroupOriginConfiguration](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupOriginConfiguration.html): The package group origin configuration that determines how package versions can enter repositories.
- [PackageGroupOriginRestriction](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupOriginRestriction.html): Contains information about the configured restrictions of the origin controls of a package group.
- [PackageGroupReference](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupReference.html): Information about the identifiers of a package group.
- [PackageGroupSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupSummary.html): Details about a package group.
- [PackageOriginConfiguration](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginConfiguration.html): Details about the package origin configuration of a package.
- [PackageOriginRestrictions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html): Details about the origin restrictions set on the package.
- [PackageSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html): Details about a package, including its format, namespace, and name.
- [PackageVersionDescription](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html): Details about a package version.
- [PackageVersionError](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionError.html): l An error associated with package.
- [PackageVersionOrigin](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionOrigin.html): Information about how a package version was added to a repository.
- [PackageVersionSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html): Details about a package version, including its status, version, and revision.
- [RepositoryDescription](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositoryDescription.html): The details of a repository stored in AWS CodeArtifact.
- [RepositoryExternalConnectionInfo](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositoryExternalConnectionInfo.html): Contains information about the external connection of a repository.
- [RepositorySummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html): Details about a repository, including its Amazon Resource Name (ARN), description, and domain information.
- [ResourcePolicy](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ResourcePolicy.html): An AWS CodeArtifact resource policy that contains a resource ARN, document details, and a revision.
- [SuccessfulPackageVersionInfo](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_SuccessfulPackageVersionInfo.html): Contains the revision and status of a package version.
- [Tag](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_Tag.html): A tag is a key-value pair that can be used to manage, search for, or filter resources in AWS CodeArtifact.
- [UpstreamRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpstreamRepository.html): Information about an upstream repository.
- [UpstreamRepositoryInfo](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpstreamRepositoryInfo.html): Information about an upstream repository.

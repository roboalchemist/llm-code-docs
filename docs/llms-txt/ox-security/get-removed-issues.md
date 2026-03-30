# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-removed-issues.md

# getRemovedIssues

Retrieves a list of security issues that have been removed from recent scans.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetRemovedIssues($getRemovedIssuesInput: DisappearedIssuesInput) {
  getRemovedIssues(getRemovedIssuesInput: $getRemovedIssuesInput) {
    disappearedIssues {
      importantSeverityBreakdown
      overrideSeverityReason
      highestOXCVESeverity
      latestCommit {
        originalSeverity
        oxSeverity
        callBranch
        linkToExternalProduct
        stars
        forks
        downloads
        vulBySeverity
        nameAndVer
        sourceRepoName
        sourceRepoLink
        sourceCreationDate
        sourceLastModifyDate
        destinationRepoName
        destinationRepoLink
        destinationCreationDate
        destinationLastModifyDate
        destinationRepoVisibility
        reasons
        _id
        url
        additionalToolData
        events
        allEvents
        pushType
        sha
        title
        link
        mergedBy
        date
        fileCount
        diffInDays
        reviewers
        user
        userLink
        userAvatar
        devOperation
        devOperationDate
        adminOperation
        adminOperationDate
        reviewOperation
        reviewOperationDate
        orgRole
        earliestActivityDate
        repoPermissions
        adminLocation
        email
        pullRequestsCount
        diffFromNowToCreatedAtInDays
        username
        accessLevel
        createdAt
        lastAccess
        fileName
        fileUri
        startLine
        endLine
        match
        snippet
        commitLink
        commitBy
        mergeDate
        dateCommitPushed
        pullRequestNumber
        pullRequestLink
        codeOwners
        region
        eduVideoLink
        resource
        service
        accountName
        cloudEnv
        secret
        secretType
        secretTypeDescription
        secretStatus
        image
        imageCreatedAt
        pkgCount
        dockerVer
        os
        binariesCount
        tag
        reputation
        sha256
        size
        pushedAt
        source
        sourceLink
        ruleId
        realMatch
        excludedByAlert
        filePath
        lockfile
        accountId
        snippetLineNumber
        language
        daysOpen
        isFixAvailable
        aggId
        pkgName
        installedVersion
        fixedVersion
        triggerPkgName
        triggerPkgVersion
        triggerPkgUpgradeVersion
        dependencyType
        branch
        hashAggId
        repo
        repoCreator
        lastCodeDate
        lastAdminOperation
        exclusionId
        numberOfReposDomainAppear
        layer
        baseImage
        imageLink
        registryName
        project
        resourceGroup
        cloudResourceTags
        location
        locationLink
        parameter
        test
        cvss
        evidence
        request
        response
        dastUrl
        method
        parameterType
        value
        cluster
        type
        cloudType
        k8sType
        consoleLink
        name
        subscriptionId
        stringifiedClusters
        aggStatus
        falsePositive {
          isFalsePositive
          comment
          reportedBy
          reportedAt
          isCanceled
          cancelComment
          canceledBy
          canceledAt
          commentWhenCanceled
        }
        cbomId
        prDeatils {
          sourceControlType
          issueId
          appId
          repo
          prId
          prURL
          prBranchName
          commitMessage
          commiter
          comment
          date
          prTitle
          prBody
          prStatus
          prApprover
          prReviewer
          prMergeTime
        }
        triage {
          triageStatus
          createdBy
          createdAt
        }
      }
      additionalTabs {
        type
        aggItems {
          originalSeverity
          oxSeverity
          callBranch
          linkToExternalProduct
          stars
          forks
          downloads
          vulBySeverity
          nameAndVer
          sourceRepoName
          sourceRepoLink
          sourceCreationDate
          sourceLastModifyDate
          destinationRepoName
          destinationRepoLink
          destinationCreationDate
          destinationLastModifyDate
          destinationRepoVisibility
          reasons
          _id
          url
          additionalToolData
          events
          allEvents
          pushType
          sha
          title
          link
          mergedBy
          date
          fileCount
          diffInDays
          reviewers
          user
          userLink
          userAvatar
          devOperation
          devOperationDate
          adminOperation
          adminOperationDate
          reviewOperation
          reviewOperationDate
          orgRole
          earliestActivityDate
          repoPermissions
          adminLocation
          email
          pullRequestsCount
          diffFromNowToCreatedAtInDays
          username
          accessLevel
          createdAt
          lastAccess
          fileName
          fileUri
          startLine
          endLine
          match
          snippet
          commitLink
          commitBy
          mergeDate
          dateCommitPushed
          pullRequestNumber
          pullRequestLink
          codeOwners
          region
          eduVideoLink
          resource
          service
          accountName
          cloudEnv
          secret
          secretType
          secretTypeDescription
          secretStatus
          image
          imageCreatedAt
          pkgCount
          dockerVer
          os
          binariesCount
          tag
          reputation
          sha256
          size
          pushedAt
          source
          sourceLink
          ruleId
          realMatch
          excludedByAlert
          filePath
          lockfile
          accountId
          snippetLineNumber
          language
          daysOpen
          isFixAvailable
          aggId
          pkgName
          installedVersion
          fixedVersion
          triggerPkgName
          triggerPkgVersion
          triggerPkgUpgradeVersion
          dependencyType
          branch
          hashAggId
          repo
          repoCreator
          lastCodeDate
          lastAdminOperation
          exclusionId
          numberOfReposDomainAppear
          layer
          baseImage
          imageLink
          registryName
          project
          resourceGroup
          cloudResourceTags
          location
          locationLink
          parameter
          test
          cvss
          evidence
          request
          response
          dastUrl
          method
          parameterType
          value
          cluster
          type
          cloudType
          k8sType
          consoleLink
          name
          subscriptionId
          stringifiedClusters
          aggStatus
          falsePositive {
            isFalsePositive
            comment
            reportedBy
            reportedAt
            isCanceled
            cancelComment
            canceledBy
            canceledAt
            commentWhenCanceled
          }
          cbomId
          prDeatils {
            sourceControlType
            issueId
            appId
            repo
            prId
            prURL
            prBranchName
            commitMessage
            commiter
            comment
            date
            prTitle
            prBody
            prStatus
            prApprover
            prReviewer
            prMergeTime
          }
          triage {
            triageStatus
            createdBy
            createdAt
          }
        }
      }
      issueDetailsHeaders {
        id
        label
        featureFlag
      }
      compliance {
        standard
        standardLink
        control
        category
        description
        categoryLink
        controlLink
      }
      sbom {
        id
        references {
          triggerPackage
          location
          locationLink
          dependencyType
          dependencyLevel
          commit {
            commitedAt
            committerName
            committerEmail
          }
          fileName
        }
        language
        libraryName
        libraryVersion
        license
        appName
        location
        dependencyType
        source
        appId
        locationLink
        appLink
        pkgName
        copyWriteInfo
        copyWriteInfoLink
        libLink
        vulnerabilityCounts {
          appox
          critical
          high
          medium
          low
          info
        }
        triggerPackage
        vulnerabilities {
          issueId
          oxSeverity
          severityNumberFromTool
          severityFromTool
          cve
          cveLink
          cvsVer
          cvssVersion
          epss
          percentile
          libName
          dependencyChain
          runtimeStatus
          libVersion
          chainDepth
          exploitInTheWild
          exploitInTheWildLink
          description
          dateDiscovered
          minorVerWithFix
          majorVerWithFix
          exploitRequirement
          exploitCode
          originalSeverity
        }
        latestVersion
        latestVersionDate
        stars
        forks
        openIssues
        packageManager
        packageManagerLink
        maintainers
        contributors
        downloads
        sourceLink
        notPopular
        licenseIssue
        malicious
        malwareType
        osVname
        notMaintained
        isDeprecated
        notImported
        notUpdated
        dependencyLevel
        requestId
        licenseLink
        artifactInSbomLibs {
          image
          imageLink
          imageCreatedAt
          sha
          os
          osVersion
          baseImage
          baseImageVersion
          tag
          layer
          registryName
          source
        }
        sha
        maintainersList {
          name
          email
        }
        runtimeStatus
        usedVersionReleaseDate
        projectDescription
      }
      dependencyGraph {
        nodes {
          id
          name
          width
          height
          vulnerable
        }
        allNodes {
          id
          name
          width
          height
          vulnerable
        }
        edges {
          v
          w
        }
        allEdges {
          v
          w
        }
      }
      groupId
      name
      mainTitle
      secondTitle
      scanId
      sla {
        daysPastSLA
        status
      }
      issueUpdatedAt
      scanDate
      description
      impact
      exposure
      severity
      owners
      ownerEmails
      occurrences
      score {
        value
        comments
      }
      orgConScore
      connector
      learnMore
      extraInfo {
        key
        val
        value
        snippet {
          detectionType
          fileName
          snippetLineNumber
          language
          text
        }
        link
        callBranch
        iconLink
        tags
      }
      resource {
        id
        type
      }
      appName
      app {
        id
        name
        businessPriority
        riskScore
        secPosture
        type
        typeComments
        applicationFlows {
          artifacts {
            type
            name
            hashType
            system
            subType
            hash
            size
            date
            location {
              runBy
              foundBy
              foundIn
              link
            }
            linkName
            k8sType
            cluster
            region
          }
          cloudDeployments {
            type
            subType
            name
            hash
            hashType
            link
            location {
              runBy
              foundBy
              foundIn
              link
            }
            k8sType
            imageName
            date
            cluster
            region
          }
          cicdInfo {
            type
            system
            latestDate
            lastMonthJobCount
            location {
              runBy
              foundBy
              foundIn
              link
            }
          }
          orchestrators {
            type
            name
            hashType
            system
            hash
            size
            date
            location {
              runBy
              foundBy
              foundIn
              link
            }
          }
          kubernetes {
            type
            name
            hashType
            system
            hash
            subType
            size
            date
            location {
              runBy
              foundBy
              foundIn
              link
            }
          }
          repository {
            type
            system
            date
            location {
              runBy
              foundBy
              foundIn
              link
            }
          }
        }
        fakeApp
        originBranchName
        repoId
        organization
        repoName
        owners {
          name
          email
          roles
        }
        credentialsId
        lastCodeChange
        createdAt
        publicVisibility
        branch
      }
      policy {
        id
        name
        detailedDescription
      }
      issueId
      category {
        name
        categoryId
        subCategoryName
        subCategoryComment
      }
      aggregations {
        type
        columns {
          columns {
            header
            key
            tooltip
            href
            type
          }
          comment
        }
        items {
          originalSeverity
          oxSeverity
          callBranch
          linkToExternalProduct
          stars
          forks
          downloads
          vulBySeverity
          nameAndVer
          sourceRepoName
          sourceRepoLink
          sourceCreationDate
          sourceLastModifyDate
          destinationRepoName
          destinationRepoLink
          destinationCreationDate
          destinationLastModifyDate
          destinationRepoVisibility
          reasons
          _id
          url
          additionalToolData
          events
          allEvents
          pushType
          sha
          title
          link
          mergedBy
          date
          fileCount
          diffInDays
          reviewers
          user
          userLink
          userAvatar
          devOperation
          devOperationDate
          adminOperation
          adminOperationDate
          reviewOperation
          reviewOperationDate
          orgRole
          earliestActivityDate
          repoPermissions
          adminLocation
          email
          pullRequestsCount
          diffFromNowToCreatedAtInDays
          username
          accessLevel
          createdAt
          lastAccess
          fileName
          fileUri
          startLine
          endLine
          match
          snippet
          commitLink
          commitBy
          mergeDate
          dateCommitPushed
          pullRequestNumber
          pullRequestLink
          codeOwners
          region
          eduVideoLink
          resource
          service
          accountName
          cloudEnv
          secret
          secretType
          secretTypeDescription
          secretStatus
          image
          imageCreatedAt
          pkgCount
          dockerVer
          os
          binariesCount
          tag
          reputation
          sha256
          size
          pushedAt
          source
          sourceLink
          ruleId
          realMatch
          excludedByAlert
          filePath
          lockfile
          accountId
          snippetLineNumber
          language
          daysOpen
          isFixAvailable
          aggId
          pkgName
          installedVersion
          fixedVersion
          triggerPkgName
          triggerPkgVersion
          triggerPkgUpgradeVersion
          dependencyType
          branch
          hashAggId
          repo
          repoCreator
          lastCodeDate
          lastAdminOperation
          exclusionId
          numberOfReposDomainAppear
          layer
          baseImage
          imageLink
          registryName
          project
          resourceGroup
          cloudResourceTags
          location
          locationLink
          parameter
          test
          cvss
          evidence
          request
          response
          dastUrl
          method
          parameterType
          value
          cluster
          type
          cloudType
          k8sType
          consoleLink
          name
          subscriptionId
          stringifiedClusters
          aggStatus
          falsePositive {
            isFalsePositive
            comment
            reportedBy
            reportedAt
            isCanceled
            cancelComment
            canceledBy
            canceledAt
            commentWhenCanceled
          }
          cbomId
          prDeatils {
            sourceControlType
            issueId
            appId
            repo
            prId
            prURL
            prBranchName
            commitMessage
            commiter
            comment
            date
            prTitle
            prBody
            prStatus
            prApprover
            prReviewer
            prMergeTime
          }
          triage {
            triageStatus
            createdBy
            createdAt
          }
        }
      }
      recommendation
      sourceTools
      ruleId
      fixes {
        settingType
        tooltip
        description
        warning
        confirmation
        inputs {
          type
          name
          options {
            name
            selected
            metadata
            info
            displayName
            isDisabled
          }
          multiSelect
          maxSelect
          minSelect
          displayName
        }
      }
      fixAppliedDeatils {
        appliedBy
        appliedDate
      }
      cwe
      fixLink
      cweList {
        name
        description
        url
      }
      dependencyChain
      publicExploitLink
      createdAt
      tickets {
        provider
        ticketId
        createdBy
        issueId
        issueName
        appName
        appId
        category
        assignee
        reporter
        link
        project
        issueType
        key
      }
      slackNotification {
        channelName
        timestamp
      }
      messages {
        messagingVendor
        recipients {
          name
          id
          type
        }
        createdAt
      }
      fixIssue {
        fixType
        fixTitle
        fixDescription
        isFixApplied
        fixAppliedBy
        sourceControlType
        fixDate
      }
      requestContent
      responseContent
      autoFix {
        fixType
        fixTitle
        fixDescription
        isFixApplied
        fixAppliedBy
        sourceControlType
        fixDate
      }
      lowerSeverityReason
      severityChange
      originalToolSeverity
      scaVulnerabilities {
        issueId
        oxSeverity
        severityNumberFromTool
        severityFromTool
        cve
        cveLink
        cvsVer
        cvssVersion
        epss
        percentile
        libName
        dependencyChain
        runtimeStatus
        libVersion
        chainDepth
        exploitInTheWild
        exploitInTheWildLink
        description
        dateDiscovered
        minorVerWithFix
        majorVerWithFix
        exploitRequirement
        exploitCode
        originalSeverity
      }
      dependencyGraphNodes {
        id
        name
        width
        height
        vulnerable
      }
      dependencyGraphEdges {
        v
        w
      }
      scaTriggerPkg
      scaTriggerPkgs {
        scaTriggerPkg
        fileName
      }
      pkgSemanticVersion
      severityChangeReason
      severityChangedReason {
        changeNumber
        withoutAutoNumbering
        evidenceLabel
        reason
        shortName
        changeCategory
        extraInfo {
          key
          value
          link
          snippet {
            snippetLineNumber
            language
            text
            fileName
          }
          iconLink
          callBranch
        }
        extraInfoContainer {
          layerSha
          layerNum
          artifactName
          sha
          registryName
        }
        order
      }
      aggSeverityExplanation
      aggSFsForCalcDisplay {
        changeNumber
        withoutAutoNumbering
        evidenceLabel
        reason
        shortName
        changeCategory
        extraInfo {
          key
          value
          link
          snippet {
            snippetLineNumber
            language
            text
            fileName
          }
          iconLink
          callBranch
        }
        extraInfoContainer {
          layerSha
          layerNum
          artifactName
          sha
          registryName
        }
        order
      }
      resolvedIssueDate
      isPRAvailable
      cicdFields {
        issueStatus
        sourceBranch
        targetBranch
        jobId
        jobTriggeredAt
        jobTriggeredAtDate
        jobTriggeredBy
        jobTriggeredReason
        jobUrl
        pullRequestId
        pullRequestUrl
        enforcement
        excludedByAlert
        cicdEventType
        workflows {
          id
          name
        }
      }
      comment
      excludedByAlert
      excludedByPolicy
      excludedByApp
      countRule
      exclusionId
      languageInfo {
        name
        version
      }
      isMonoRepoChild
      monoRepoParent
      isFixAvailable
      isFixApplied
      isGPTFixAvailable
      oscarData {
        name
        description
        url
        id
      }
      gptInfo {
        gptResponse
        user
        createdAt
      }
      prDeatils {
        sourceControlType
        issueId
        appId
        repo
        prId
        prURL
        prBranchName
        commitMessage
        commiter
        comment
        date
        prTitle
        prBody
        prStatus
        prApprover
        prReviewer
        prMergeTime
      }
      tags {
        tagId
        name
        email
        displayName
        tagType
        createdBy
        purpose
        deploymentModel
        tagCategory
      }
      originalSeverity
      overrideSeverity
      isFalsePositive
      falsePositiveComment
      isCanceledFalsePositive
      cancelFalsePositiveComment
      falsePositiveDetails {
        canceledBy
        reportedBy
        commentWhenCanceled
        aggregationsStatus
      }
      issueStatus
      scanIssueStatus
      resolvedReason
      resolvedDetails
      resolvedReasonDetails {
        description
      }
      disappearedReason
      disappearedDetails
      disappearedReasonDetails {
        description
      }
      disappearedDate
      correlatedIssueId
      correlatedRegistry
      scaFixType
      previousSeverity {
        severity
        severityChangedDate
      }
      version
      severityFactorsDiff {
        shortName
        change
        status
      }
      exposedByApiItems {
        apiId
        codeLocations {
          link
          callBranch
        }
      }
      originBranchName
      exclusionComment
      exclusionExpiredAt
      problematicPkg
      serverlessDeploymentOperation {
        userIdentity {
          type
          principalId
          arn
          accountId
          accessKeyId
          sessionContext {
            sessionIssuer {
              type
              principalId
              arn
              accountId
              userName
            }
            attributes {
              creationDate
              mfaAuthenticated
            }
          }
        }
        deploymentTime
        sourceIPAddress
        userAgent
        connectedFromConsole
        location
        linkToCode
        functionName
        functionArn
        internalFunctionName
        cloudRegion
        version
        revisionId
        codeSha256
        entryPoint
        codeSize
        memorySize
        timeout
        runtime
        runtimeVersionConfig {
          runtimeVersionArn
        }
        architectures
        role
        recipientAccountId
        description
      }
      eventFromExternalTool
      issueOwners {
        name
        email
      }
      overrideIssueOwner
      originalIssueOwners {
        name
        email
      }
      cveExclusions {
        label
        recommended
        tooltip
        type
        id
        oxRuleId
        level
        excludeBy
        uidOnly
        isDefault
        ffKey
        exclusionScope
      }
    }
    totalDisappearedIssues
    totalFilteredDisappearedIssues
    totalResolvedIssues
    offset
    topOffset
    selectedPosition
    totalActiveIssues
    cursorValue
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getRemovedIssuesInput": {
    "scanID": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
    "limit": 100,
    "offset": 0,
    "sort": {
      "fields": ["Category"],
      "order": ["ASC"]
    },
    "owners": ["example"],
    "tagIds": ["example"],
    "inventoryFilters": ["New"],
    "dateRange": {
      "from": 1749000000000,
      "to": 1749900000000
    },
    "search": [
      {
        "fieldName": "example",
        "value": ["example"]
      }
    ],
    "openItems": ["digest"],
    "conditionalFilters": [
      {
        "condition": "AND",
        "fieldName": "digest",
        "values": ["example"],
        "greaterThan": 13.37,
        "lessThan": 13.37
      }
    ],
    "exportsOptions": {
      "flattenAgg": true,
      "isDemoEnabled": true,
      "name": "SomeName",
      "columns": [
        {
          "key": "Severity",
          "name": "SomeName"
        }
      ],
      "rowsLimit": 42
    },
    "restrictToCategories": [42],
    "topLevelSearch": "example",
    "topOffset": 42,
    "issueId": "30966426-oxPolicy_securityCloudScan_100-example",
    "scrollDirection": "example",
    "cursorValue": "example"
  }
}
```

{% endtab %}

{% tab title="cURL" %}

```shell
curl -X POST \
https://api.cloud.ox.security/api/apollo-gateway \
-H 'Content-Type: application/json' \
-H 'Authorization: YOUR_API_TOKEN' \
-d '{
 "query": "query GetRemovedIssues($getRemovedIssuesInput: DisappearedIssuesInput) { getRemovedIssues(getRemovedIssuesInput: $getRemovedIssuesInput) { disappearedIssues { importantSeverityBreakdown overrideSeverityReason highestOXCVESeverity latestCommit { originalSeverity oxSeverity callBranch linkToExternalProduct stars forks downloads vulBySeverity nameAndVer sourceRepoName sourceRepoLink sourceCreationDate sourceLastModifyDate destinationRepoName destinationRepoLink destinationCreationDate destinationLastModifyDate destinationRepoVisibility reasons _id url additionalToolData events allEvents pushType sha title link mergedBy date fileCount diffInDays reviewers user userLink userAvatar devOperation devOperationDate adminOperation adminOperationDate reviewOperation reviewOperationDate orgRole earliestActivityDate repoPermissions adminLocation email pullRequestsCount diffFromNowToCreatedAtInDays username accessLevel createdAt lastAccess fileName fileUri startLine endLine match snippet commitLink commitBy mergeDate dateCommitPushed pullRequestNumber pullRequestLink codeOwners region eduVideoLink resource service accountName cloudEnv secret secretType secretTypeDescription secretStatus image imageCreatedAt pkgCount dockerVer os binariesCount tag reputation sha256 size pushedAt source sourceLink ruleId realMatch excludedByAlert filePath lockfile accountId snippetLineNumber language daysOpen isFixAvailable aggId pkgName installedVersion fixedVersion triggerPkgName triggerPkgVersion triggerPkgUpgradeVersion dependencyType branch hashAggId repo repoCreator lastCodeDate lastAdminOperation exclusionId numberOfReposDomainAppear layer baseImage imageLink registryName project resourceGroup cloudResourceTags location locationLink parameter test cvss evidence request response dastUrl method parameterType value cluster type cloudType k8sType consoleLink name subscriptionId stringifiedClusters aggStatus falsePositive { isFalsePositive comment reportedBy reportedAt isCanceled cancelComment canceledBy canceledAt commentWhenCanceled } cbomId prDeatils { sourceControlType issueId appId repo prId prURL prBranchName commitMessage commiter comment date prTitle prBody prStatus prApprover prReviewer prMergeTime } triage { triageStatus createdBy createdAt } } additionalTabs { type aggItems { originalSeverity oxSeverity callBranch linkToExternalProduct stars forks downloads vulBySeverity nameAndVer sourceRepoName sourceRepoLink sourceCreationDate sourceLastModifyDate destinationRepoName destinationRepoLink destinationCreationDate destinationLastModifyDate destinationRepoVisibility reasons _id url additionalToolData events allEvents pushType sha title link mergedBy date fileCount diffInDays reviewers user userLink userAvatar devOperation devOperationDate adminOperation adminOperationDate reviewOperation reviewOperationDate orgRole earliestActivityDate repoPermissions adminLocation email pullRequestsCount diffFromNowToCreatedAtInDays username accessLevel createdAt lastAccess fileName fileUri startLine endLine match snippet commitLink commitBy mergeDate dateCommitPushed pullRequestNumber pullRequestLink codeOwners region eduVideoLink resource service accountName cloudEnv secret secretType secretTypeDescription secretStatus image imageCreatedAt pkgCount dockerVer os binariesCount tag reputation sha256 size pushedAt source sourceLink ruleId realMatch excludedByAlert filePath lockfile accountId snippetLineNumber language daysOpen isFixAvailable aggId pkgName installedVersion fixedVersion triggerPkgName triggerPkgVersion triggerPkgUpgradeVersion dependencyType branch hashAggId repo repoCreator lastCodeDate lastAdminOperation exclusionId numberOfReposDomainAppear layer baseImage imageLink registryName project resourceGroup cloudResourceTags location locationLink parameter test cvss evidence request response dastUrl method parameterType value cluster type cloudType k8sType consoleLink name subscriptionId stringifiedClusters aggStatus falsePositive { isFalsePositive comment reportedBy reportedAt isCanceled cancelComment canceledBy canceledAt commentWhenCanceled } cbomId prDeatils { sourceControlType issueId appId repo prId prURL prBranchName commitMessage commiter comment date prTitle prBody prStatus prApprover prReviewer prMergeTime } triage { triageStatus createdBy createdAt } } } issueDetailsHeaders { id label featureFlag } compliance { standard standardLink control category description categoryLink controlLink } sbom { id references { triggerPackage location locationLink dependencyType dependencyLevel commit { commitedAt committerName committerEmail } fileName } language libraryName libraryVersion license appName location dependencyType source appId locationLink appLink pkgName copyWriteInfo copyWriteInfoLink libLink vulnerabilityCounts { appox critical high medium low info } triggerPackage vulnerabilities { issueId oxSeverity severityNumberFromTool severityFromTool cve cveLink cvsVer cvssVersion epss percentile libName dependencyChain runtimeStatus libVersion chainDepth exploitInTheWild exploitInTheWildLink description dateDiscovered minorVerWithFix majorVerWithFix exploitRequirement exploitCode originalSeverity } latestVersion latestVersionDate stars forks openIssues packageManager packageManagerLink maintainers contributors downloads sourceLink notPopular licenseIssue malicious malwareType osVname notMaintained isDeprecated notImported notUpdated dependencyLevel requestId licenseLink artifactInSbomLibs { image imageLink imageCreatedAt sha os osVersion baseImage baseImageVersion tag layer registryName source } sha maintainersList { name email } runtimeStatus usedVersionReleaseDate projectDescription } dependencyGraph { nodes { id name width height vulnerable } allNodes { id name width height vulnerable } edges { v w } allEdges { v w } } groupId name mainTitle secondTitle scanId sla { daysPastSLA status } issueUpdatedAt scanDate description impact exposure severity owners ownerEmails occurrences score { value comments } orgConScore connector learnMore extraInfo { key val value snippet { detectionType fileName snippetLineNumber language text } link callBranch iconLink tags } resource { id type } appName app { id name businessPriority riskScore secPosture type typeComments applicationFlows { artifacts { type name hashType system subType hash size date location { runBy foundBy foundIn link } linkName k8sType cluster region } cloudDeployments { type subType name hash hashType link location { runBy foundBy foundIn link } k8sType imageName date cluster region } cicdInfo { type system latestDate lastMonthJobCount location { runBy foundBy foundIn link } } orchestrators { type name hashType system hash size date location { runBy foundBy foundIn link } } kubernetes { type name hashType system hash subType size date location { runBy foundBy foundIn link } } repository { type system date location { runBy foundBy foundIn link } } } fakeApp originBranchName repoId organization repoName owners { name email roles } credentialsId lastCodeChange createdAt publicVisibility branch } policy { id name detailedDescription } issueId category { name categoryId subCategoryName subCategoryComment } aggregations { type columns { columns { header key tooltip href type } comment } items { originalSeverity oxSeverity callBranch linkToExternalProduct stars forks downloads vulBySeverity nameAndVer sourceRepoName sourceRepoLink sourceCreationDate sourceLastModifyDate destinationRepoName destinationRepoLink destinationCreationDate destinationLastModifyDate destinationRepoVisibility reasons _id url additionalToolData events allEvents pushType sha title link mergedBy date fileCount diffInDays reviewers user userLink userAvatar devOperation devOperationDate adminOperation adminOperationDate reviewOperation reviewOperationDate orgRole earliestActivityDate repoPermissions adminLocation email pullRequestsCount diffFromNowToCreatedAtInDays username accessLevel createdAt lastAccess fileName fileUri startLine endLine match snippet commitLink commitBy mergeDate dateCommitPushed pullRequestNumber pullRequestLink codeOwners region eduVideoLink resource service accountName cloudEnv secret secretType secretTypeDescription secretStatus image imageCreatedAt pkgCount dockerVer os binariesCount tag reputation sha256 size pushedAt source sourceLink ruleId realMatch excludedByAlert filePath lockfile accountId snippetLineNumber language daysOpen isFixAvailable aggId pkgName installedVersion fixedVersion triggerPkgName triggerPkgVersion triggerPkgUpgradeVersion dependencyType branch hashAggId repo repoCreator lastCodeDate lastAdminOperation exclusionId numberOfReposDomainAppear layer baseImage imageLink registryName project resourceGroup cloudResourceTags location locationLink parameter test cvss evidence request response dastUrl method parameterType value cluster type cloudType k8sType consoleLink name subscriptionId stringifiedClusters aggStatus falsePositive { isFalsePositive comment reportedBy reportedAt isCanceled cancelComment canceledBy canceledAt commentWhenCanceled } cbomId prDeatils { sourceControlType issueId appId repo prId prURL prBranchName commitMessage commiter comment date prTitle prBody prStatus prApprover prReviewer prMergeTime } triage { triageStatus createdBy createdAt } } } recommendation sourceTools ruleId fixes { settingType tooltip description warning confirmation inputs { type name options { name selected metadata info displayName isDisabled } multiSelect maxSelect minSelect displayName } } fixAppliedDeatils { appliedBy appliedDate } cwe fixLink cweList { name description url } dependencyChain publicExploitLink createdAt tickets { provider ticketId createdBy issueId issueName appName appId category assignee reporter link project issueType key } slackNotification { channelName timestamp } messages { messagingVendor recipients { name id type } createdAt } fixIssue { fixType fixTitle fixDescription isFixApplied fixAppliedBy sourceControlType fixDate } requestContent responseContent autoFix { fixType fixTitle fixDescription isFixApplied fixAppliedBy sourceControlType fixDate } lowerSeverityReason severityChange originalToolSeverity scaVulnerabilities { issueId oxSeverity severityNumberFromTool severityFromTool cve cveLink cvsVer cvssVersion epss percentile libName dependencyChain runtimeStatus libVersion chainDepth exploitInTheWild exploitInTheWildLink description dateDiscovered minorVerWithFix majorVerWithFix exploitRequirement exploitCode originalSeverity } dependencyGraphNodes { id name width height vulnerable } dependencyGraphEdges { v w } scaTriggerPkg scaTriggerPkgs { scaTriggerPkg fileName } pkgSemanticVersion severityChangeReason severityChangedReason { changeNumber withoutAutoNumbering evidenceLabel reason shortName changeCategory extraInfo { key value link snippet { snippetLineNumber language text fileName } iconLink callBranch } extraInfoContainer { layerSha layerNum artifactName sha registryName } order } aggSeverityExplanation aggSFsForCalcDisplay { changeNumber withoutAutoNumbering evidenceLabel reason shortName changeCategory extraInfo { key value link snippet { snippetLineNumber language text fileName } iconLink callBranch } extraInfoContainer { layerSha layerNum artifactName sha registryName } order } resolvedIssueDate isPRAvailable cicdFields { issueStatus sourceBranch targetBranch jobId jobTriggeredAt jobTriggeredAtDate jobTriggeredBy jobTriggeredReason jobUrl pullRequestId pullRequestUrl enforcement excludedByAlert cicdEventType workflows { id name } } comment excludedByAlert excludedByPolicy excludedByApp countRule exclusionId languageInfo { name version } isMonoRepoChild monoRepoParent isFixAvailable isFixApplied isGPTFixAvailable oscarData { name description url id } gptInfo { gptResponse user createdAt } prDeatils { sourceControlType issueId appId repo prId prURL prBranchName commitMessage commiter comment date prTitle prBody prStatus prApprover prReviewer prMergeTime } tags { tagId name email displayName tagType createdBy purpose deploymentModel tagCategory } originalSeverity overrideSeverity isFalsePositive falsePositiveComment isCanceledFalsePositive cancelFalsePositiveComment falsePositiveDetails { canceledBy reportedBy commentWhenCanceled aggregationsStatus } issueStatus scanIssueStatus resolvedReason resolvedDetails resolvedReasonDetails { description } disappearedReason disappearedDetails disappearedReasonDetails { description } disappearedDate correlatedIssueId correlatedRegistry scaFixType previousSeverity { severity severityChangedDate } version severityFactorsDiff { shortName change status } exposedByApiItems { apiId codeLocations { link callBranch } } originBranchName exclusionComment exclusionExpiredAt problematicPkg serverlessDeploymentOperation { userIdentity { type principalId arn accountId accessKeyId sessionContext { sessionIssuer { type principalId arn accountId userName } attributes { creationDate mfaAuthenticated } } } deploymentTime sourceIPAddress userAgent connectedFromConsole location linkToCode functionName functionArn internalFunctionName cloudRegion version revisionId codeSha256 entryPoint codeSize memorySize timeout runtime runtimeVersionConfig { runtimeVersionArn } architectures role recipientAccountId description } eventFromExternalTool issueOwners { name email } overrideIssueOwner originalIssueOwners { name email } cveExclusions { label recommended tooltip type id oxRuleId level excludeBy uidOnly isDefault ffKey exclusionScope } } totalDisappearedIssues totalFilteredDisappearedIssues totalResolvedIssues offset topOffset selectedPosition totalActiveIssues cursorValue } }",
 "variables": {
    "getRemovedIssuesInput": {
      "scanID": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
      "limit": 100,
      "offset": 0,
      "sort": {
        "fields": ["Category"],
        "order": ["ASC"]
      },
      "owners": ["example"],
      "tagIds": ["example"],
      "inventoryFilters": ["New"],
      "dateRange": {
        "from": 1749000000000,
        "to": 1749900000000
      },
      "search": [
        {
          "fieldName": "example",
          "value": ["example"]
        }
      ],
      "openItems": ["digest"],
      "conditionalFilters": [
        {
          "condition": "AND",
          "fieldName": "digest",
          "values": ["example"],
          "greaterThan": 13.37,
          "lessThan": 13.37
        }
      ],
      "exportsOptions": {
        "flattenAgg": true,
        "isDemoEnabled": true,
        "name": "SomeName",
        "columns": [
          {
            "key": "Severity",
            "name": "SomeName"
          }
        ],
        "rowsLimit": 42
      },
      "restrictToCategories": [42],
      "topLevelSearch": "example",
      "topOffset": 42,
      "issueId": "30966426-oxPolicy_securityCloudScan_100-example",
      "scrollDirection": "example",
      "cursorValue": "example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetRemovedIssues($getRemovedIssuesInput: DisappearedIssuesInput) { getRemovedIssues(getRemovedIssuesInput: $getRemovedIssuesInput) { disappearedIssues { importantSeverityBreakdown overrideSeverityReason highestOXCVESeverity latestCommit { originalSeverity oxSeverity callBranch linkToExternalProduct stars forks downloads vulBySeverity nameAndVer sourceRepoName sourceRepoLink sourceCreationDate sourceLastModifyDate destinationRepoName destinationRepoLink destinationCreationDate destinationLastModifyDate destinationRepoVisibility reasons _id url additionalToolData events allEvents pushType sha title link mergedBy date fileCount diffInDays reviewers user userLink userAvatar devOperation devOperationDate adminOperation adminOperationDate reviewOperation reviewOperationDate orgRole earliestActivityDate repoPermissions adminLocation email pullRequestsCount diffFromNowToCreatedAtInDays username accessLevel createdAt lastAccess fileName fileUri startLine endLine match snippet commitLink commitBy mergeDate dateCommitPushed pullRequestNumber pullRequestLink codeOwners region eduVideoLink resource service accountName cloudEnv secret secretType secretTypeDescription secretStatus image imageCreatedAt pkgCount dockerVer os binariesCount tag reputation sha256 size pushedAt source sourceLink ruleId realMatch excludedByAlert filePath lockfile accountId snippetLineNumber language daysOpen isFixAvailable aggId pkgName installedVersion fixedVersion triggerPkgName triggerPkgVersion triggerPkgUpgradeVersion dependencyType branch hashAggId repo repoCreator lastCodeDate lastAdminOperation exclusionId numberOfReposDomainAppear layer baseImage imageLink registryName project resourceGroup cloudResourceTags location locationLink parameter test cvss evidence request response dastUrl method parameterType value cluster type cloudType k8sType consoleLink name subscriptionId stringifiedClusters aggStatus falsePositive { isFalsePositive comment reportedBy reportedAt isCanceled cancelComment canceledBy canceledAt commentWhenCanceled } cbomId prDeatils { sourceControlType issueId appId repo prId prURL prBranchName commitMessage commiter comment date prTitle prBody prStatus prApprover prReviewer prMergeTime } triage { triageStatus createdBy createdAt } } additionalTabs { type aggItems { originalSeverity oxSeverity callBranch linkToExternalProduct stars forks downloads vulBySeverity nameAndVer sourceRepoName sourceRepoLink sourceCreationDate sourceLastModifyDate destinationRepoName destinationRepoLink destinationCreationDate destinationLastModifyDate destinationRepoVisibility reasons _id url additionalToolData events allEvents pushType sha title link mergedBy date fileCount diffInDays reviewers user userLink userAvatar devOperation devOperationDate adminOperation adminOperationDate reviewOperation reviewOperationDate orgRole earliestActivityDate repoPermissions adminLocation email pullRequestsCount diffFromNowToCreatedAtInDays username accessLevel createdAt lastAccess fileName fileUri startLine endLine match snippet commitLink commitBy mergeDate dateCommitPushed pullRequestNumber pullRequestLink codeOwners region eduVideoLink resource service accountName cloudEnv secret secretType secretTypeDescription secretStatus image imageCreatedAt pkgCount dockerVer os binariesCount tag reputation sha256 size pushedAt source sourceLink ruleId realMatch excludedByAlert filePath lockfile accountId snippetLineNumber language daysOpen isFixAvailable aggId pkgName installedVersion fixedVersion triggerPkgName triggerPkgVersion triggerPkgUpgradeVersion dependencyType branch hashAggId repo repoCreator lastCodeDate lastAdminOperation exclusionId numberOfReposDomainAppear layer baseImage imageLink registryName project resourceGroup cloudResourceTags location locationLink parameter test cvss evidence request response dastUrl method parameterType value cluster type cloudType k8sType consoleLink name subscriptionId stringifiedClusters aggStatus falsePositive { isFalsePositive comment reportedBy reportedAt isCanceled cancelComment canceledBy canceledAt commentWhenCanceled } cbomId prDeatils { sourceControlType issueId appId repo prId prURL prBranchName commitMessage commiter comment date prTitle prBody prStatus prApprover prReviewer prMergeTime } triage { triageStatus createdBy createdAt } } } issueDetailsHeaders { id label featureFlag } compliance { standard standardLink control category description categoryLink controlLink } sbom { id references { triggerPackage location locationLink dependencyType dependencyLevel commit { commitedAt committerName committerEmail } fileName } language libraryName libraryVersion license appName location dependencyType source appId locationLink appLink pkgName copyWriteInfo copyWriteInfoLink libLink vulnerabilityCounts { appox critical high medium low info } triggerPackage vulnerabilities { issueId oxSeverity severityNumberFromTool severityFromTool cve cveLink cvsVer cvssVersion epss percentile libName dependencyChain runtimeStatus libVersion chainDepth exploitInTheWild exploitInTheWildLink description dateDiscovered minorVerWithFix majorVerWithFix exploitRequirement exploitCode originalSeverity } latestVersion latestVersionDate stars forks openIssues packageManager packageManagerLink maintainers contributors downloads sourceLink notPopular licenseIssue malicious malwareType osVname notMaintained isDeprecated notImported notUpdated dependencyLevel requestId licenseLink artifactInSbomLibs { image imageLink imageCreatedAt sha os osVersion baseImage baseImageVersion tag layer registryName source } sha maintainersList { name email } runtimeStatus usedVersionReleaseDate projectDescription } dependencyGraph { nodes { id name width height vulnerable } allNodes { id name width height vulnerable } edges { v w } allEdges { v w } } groupId name mainTitle secondTitle scanId sla { daysPastSLA status } issueUpdatedAt scanDate description impact exposure severity owners ownerEmails occurrences score { value comments } orgConScore connector learnMore extraInfo { key val value snippet { detectionType fileName snippetLineNumber language text } link callBranch iconLink tags } resource { id type } appName app { id name businessPriority riskScore secPosture type typeComments applicationFlows { artifacts { type name hashType system subType hash size date location { runBy foundBy foundIn link } linkName k8sType cluster region } cloudDeployments { type subType name hash hashType link location { runBy foundBy foundIn link } k8sType imageName date cluster region } cicdInfo { type system latestDate lastMonthJobCount location { runBy foundBy foundIn link } } orchestrators { type name hashType system hash size date location { runBy foundBy foundIn link } } kubernetes { type name hashType system hash subType size date location { runBy foundBy foundIn link } } repository { type system date location { runBy foundBy foundIn link } } } fakeApp originBranchName repoId organization repoName owners { name email roles } credentialsId lastCodeChange createdAt publicVisibility branch } policy { id name detailedDescription } issueId category { name categoryId subCategoryName subCategoryComment } aggregations { type columns { columns { header key tooltip href type } comment } items { originalSeverity oxSeverity callBranch linkToExternalProduct stars forks downloads vulBySeverity nameAndVer sourceRepoName sourceRepoLink sourceCreationDate sourceLastModifyDate destinationRepoName destinationRepoLink destinationCreationDate destinationLastModifyDate destinationRepoVisibility reasons _id url additionalToolData events allEvents pushType sha title link mergedBy date fileCount diffInDays reviewers user userLink userAvatar devOperation devOperationDate adminOperation adminOperationDate reviewOperation reviewOperationDate orgRole earliestActivityDate repoPermissions adminLocation email pullRequestsCount diffFromNowToCreatedAtInDays username accessLevel createdAt lastAccess fileName fileUri startLine endLine match snippet commitLink commitBy mergeDate dateCommitPushed pullRequestNumber pullRequestLink codeOwners region eduVideoLink resource service accountName cloudEnv secret secretType secretTypeDescription secretStatus image imageCreatedAt pkgCount dockerVer os binariesCount tag reputation sha256 size pushedAt source sourceLink ruleId realMatch excludedByAlert filePath lockfile accountId snippetLineNumber language daysOpen isFixAvailable aggId pkgName installedVersion fixedVersion triggerPkgName triggerPkgVersion triggerPkgUpgradeVersion dependencyType branch hashAggId repo repoCreator lastCodeDate lastAdminOperation exclusionId numberOfReposDomainAppear layer baseImage imageLink registryName project resourceGroup cloudResourceTags location locationLink parameter test cvss evidence request response dastUrl method parameterType value cluster type cloudType k8sType consoleLink name subscriptionId stringifiedClusters aggStatus falsePositive { isFalsePositive comment reportedBy reportedAt isCanceled cancelComment canceledBy canceledAt commentWhenCanceled } cbomId prDeatils { sourceControlType issueId appId repo prId prURL prBranchName commitMessage commiter comment date prTitle prBody prStatus prApprover prReviewer prMergeTime } triage { triageStatus createdBy createdAt } } } recommendation sourceTools ruleId fixes { settingType tooltip description warning confirmation inputs { type name options { name selected metadata info displayName isDisabled } multiSelect maxSelect minSelect displayName } } fixAppliedDeatils { appliedBy appliedDate } cwe fixLink cweList { name description url } dependencyChain publicExploitLink createdAt tickets { provider ticketId createdBy issueId issueName appName appId category assignee reporter link project issueType key } slackNotification { channelName timestamp } messages { messagingVendor recipients { name id type } createdAt } fixIssue { fixType fixTitle fixDescription isFixApplied fixAppliedBy sourceControlType fixDate } requestContent responseContent autoFix { fixType fixTitle fixDescription isFixApplied fixAppliedBy sourceControlType fixDate } lowerSeverityReason severityChange originalToolSeverity scaVulnerabilities { issueId oxSeverity severityNumberFromTool severityFromTool cve cveLink cvsVer cvssVersion epss percentile libName dependencyChain runtimeStatus libVersion chainDepth exploitInTheWild exploitInTheWildLink description dateDiscovered minorVerWithFix majorVerWithFix exploitRequirement exploitCode originalSeverity } dependencyGraphNodes { id name width height vulnerable } dependencyGraphEdges { v w } scaTriggerPkg scaTriggerPkgs { scaTriggerPkg fileName } pkgSemanticVersion severityChangeReason severityChangedReason { changeNumber withoutAutoNumbering evidenceLabel reason shortName changeCategory extraInfo { key value link snippet { snippetLineNumber language text fileName } iconLink callBranch } extraInfoContainer { layerSha layerNum artifactName sha registryName } order } aggSeverityExplanation aggSFsForCalcDisplay { changeNumber withoutAutoNumbering evidenceLabel reason shortName changeCategory extraInfo { key value link snippet { snippetLineNumber language text fileName } iconLink callBranch } extraInfoContainer { layerSha layerNum artifactName sha registryName } order } resolvedIssueDate isPRAvailable cicdFields { issueStatus sourceBranch targetBranch jobId jobTriggeredAt jobTriggeredAtDate jobTriggeredBy jobTriggeredReason jobUrl pullRequestId pullRequestUrl enforcement excludedByAlert cicdEventType workflows { id name } } comment excludedByAlert excludedByPolicy excludedByApp countRule exclusionId languageInfo { name version } isMonoRepoChild monoRepoParent isFixAvailable isFixApplied isGPTFixAvailable oscarData { name description url id } gptInfo { gptResponse user createdAt } prDeatils { sourceControlType issueId appId repo prId prURL prBranchName commitMessage commiter comment date prTitle prBody prStatus prApprover prReviewer prMergeTime } tags { tagId name email displayName tagType createdBy purpose deploymentModel tagCategory } originalSeverity overrideSeverity isFalsePositive falsePositiveComment isCanceledFalsePositive cancelFalsePositiveComment falsePositiveDetails { canceledBy reportedBy commentWhenCanceled aggregationsStatus } issueStatus scanIssueStatus resolvedReason resolvedDetails resolvedReasonDetails { description } disappearedReason disappearedDetails disappearedReasonDetails { description } disappearedDate correlatedIssueId correlatedRegistry scaFixType previousSeverity { severity severityChangedDate } version severityFactorsDiff { shortName change status } exposedByApiItems { apiId codeLocations { link callBranch } } originBranchName exclusionComment exclusionExpiredAt problematicPkg serverlessDeploymentOperation { userIdentity { type principalId arn accountId accessKeyId sessionContext { sessionIssuer { type principalId arn accountId userName } attributes { creationDate mfaAuthenticated } } } deploymentTime sourceIPAddress userAgent connectedFromConsole location linkToCode functionName functionArn internalFunctionName cloudRegion version revisionId codeSha256 entryPoint codeSize memorySize timeout runtime runtimeVersionConfig { runtimeVersionArn } architectures role recipientAccountId description } eventFromExternalTool issueOwners { name email } overrideIssueOwner originalIssueOwners { name email } cveExclusions { label recommended tooltip type id oxRuleId level excludeBy uidOnly isDefault ffKey exclusionScope } } totalDisappearedIssues totalFilteredDisappearedIssues totalResolvedIssues offset topOffset selectedPosition totalActiveIssues cursorValue } }';

fetch("https://api.cloud.ox.security/api/apollo-gateway", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_TOKEN"
  },
  body: JSON.stringify({
    query: query,
    // This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.
    variables: {
      getRemovedIssuesInput: {
        scanID: "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        limit: 100,
        offset: 0,
        sort: {
          fields: ["Category"],
          order: ["ASC"]
        },
        owners: ["example"],
        tagIds: ["example"],
        inventoryFilters: ["New"],
        dateRange: {
          from: 1749000000000,
          to: 1749900000000
        },
        search: [
          {
            fieldName: "example",
            value: ["example"]
          }
        ],
        openItems: ["digest"],
        conditionalFilters: [
          {
            condition: "AND",
            fieldName: "digest",
            values: ["example"],
            greaterThan: 13.37,
            lessThan: 13.37
          }
        ],
        exportsOptions: {
          flattenAgg: true,
          isDemoEnabled: true,
          name: "SomeName",
          columns: [
            {
              key: "Severity",
              name: "SomeName"
            }
          ],
          rowsLimit: 42
        },
        restrictToCategories: [42],
        topLevelSearch: "example",
        topOffset: 42,
        issueId: "30966426-oxPolicy_securityCloudScan_100-example",
        scrollDirection: "example",
        cursorValue: "example"
      }
    }
  })
})
.then(response => response.json())
.then(result => console.log(JSON.stringify(result, null, 2)))
.catch(error => console.error('Error:', error));
```

{% endtab %}

{% tab title="Python" %}

```python
import requests

query = 'query GetRemovedIssues($getRemovedIssuesInput: DisappearedIssuesInput) { getRemovedIssues(getRemovedIssuesInput: $getRemovedIssuesInput) { disappearedIssues { importantSeverityBreakdown overrideSeverityReason highestOXCVESeverity latestCommit { originalSeverity oxSeverity callBranch linkToExternalProduct stars forks downloads vulBySeverity nameAndVer sourceRepoName sourceRepoLink sourceCreationDate sourceLastModifyDate destinationRepoName destinationRepoLink destinationCreationDate destinationLastModifyDate destinationRepoVisibility reasons _id url additionalToolData events allEvents pushType sha title link mergedBy date fileCount diffInDays reviewers user userLink userAvatar devOperation devOperationDate adminOperation adminOperationDate reviewOperation reviewOperationDate orgRole earliestActivityDate repoPermissions adminLocation email pullRequestsCount diffFromNowToCreatedAtInDays username accessLevel createdAt lastAccess fileName fileUri startLine endLine match snippet commitLink commitBy mergeDate dateCommitPushed pullRequestNumber pullRequestLink codeOwners region eduVideoLink resource service accountName cloudEnv secret secretType secretTypeDescription secretStatus image imageCreatedAt pkgCount dockerVer os binariesCount tag reputation sha256 size pushedAt source sourceLink ruleId realMatch excludedByAlert filePath lockfile accountId snippetLineNumber language daysOpen isFixAvailable aggId pkgName installedVersion fixedVersion triggerPkgName triggerPkgVersion triggerPkgUpgradeVersion dependencyType branch hashAggId repo repoCreator lastCodeDate lastAdminOperation exclusionId numberOfReposDomainAppear layer baseImage imageLink registryName project resourceGroup cloudResourceTags location locationLink parameter test cvss evidence request response dastUrl method parameterType value cluster type cloudType k8sType consoleLink name subscriptionId stringifiedClusters aggStatus falsePositive { isFalsePositive comment reportedBy reportedAt isCanceled cancelComment canceledBy canceledAt commentWhenCanceled } cbomId prDeatils { sourceControlType issueId appId repo prId prURL prBranchName commitMessage commiter comment date prTitle prBody prStatus prApprover prReviewer prMergeTime } triage { triageStatus createdBy createdAt } } additionalTabs { type aggItems { originalSeverity oxSeverity callBranch linkToExternalProduct stars forks downloads vulBySeverity nameAndVer sourceRepoName sourceRepoLink sourceCreationDate sourceLastModifyDate destinationRepoName destinationRepoLink destinationCreationDate destinationLastModifyDate destinationRepoVisibility reasons _id url additionalToolData events allEvents pushType sha title link mergedBy date fileCount diffInDays reviewers user userLink userAvatar devOperation devOperationDate adminOperation adminOperationDate reviewOperation reviewOperationDate orgRole earliestActivityDate repoPermissions adminLocation email pullRequestsCount diffFromNowToCreatedAtInDays username accessLevel createdAt lastAccess fileName fileUri startLine endLine match snippet commitLink commitBy mergeDate dateCommitPushed pullRequestNumber pullRequestLink codeOwners region eduVideoLink resource service accountName cloudEnv secret secretType secretTypeDescription secretStatus image imageCreatedAt pkgCount dockerVer os binariesCount tag reputation sha256 size pushedAt source sourceLink ruleId realMatch excludedByAlert filePath lockfile accountId snippetLineNumber language daysOpen isFixAvailable aggId pkgName installedVersion fixedVersion triggerPkgName triggerPkgVersion triggerPkgUpgradeVersion dependencyType branch hashAggId repo repoCreator lastCodeDate lastAdminOperation exclusionId numberOfReposDomainAppear layer baseImage imageLink registryName project resourceGroup cloudResourceTags location locationLink parameter test cvss evidence request response dastUrl method parameterType value cluster type cloudType k8sType consoleLink name subscriptionId stringifiedClusters aggStatus falsePositive { isFalsePositive comment reportedBy reportedAt isCanceled cancelComment canceledBy canceledAt commentWhenCanceled } cbomId prDeatils { sourceControlType issueId appId repo prId prURL prBranchName commitMessage commiter comment date prTitle prBody prStatus prApprover prReviewer prMergeTime } triage { triageStatus createdBy createdAt } } } issueDetailsHeaders { id label featureFlag } compliance { standard standardLink control category description categoryLink controlLink } sbom { id references { triggerPackage location locationLink dependencyType dependencyLevel commit { commitedAt committerName committerEmail } fileName } language libraryName libraryVersion license appName location dependencyType source appId locationLink appLink pkgName copyWriteInfo copyWriteInfoLink libLink vulnerabilityCounts { appox critical high medium low info } triggerPackage vulnerabilities { issueId oxSeverity severityNumberFromTool severityFromTool cve cveLink cvsVer cvssVersion epss percentile libName dependencyChain runtimeStatus libVersion chainDepth exploitInTheWild exploitInTheWildLink description dateDiscovered minorVerWithFix majorVerWithFix exploitRequirement exploitCode originalSeverity } latestVersion latestVersionDate stars forks openIssues packageManager packageManagerLink maintainers contributors downloads sourceLink notPopular licenseIssue malicious malwareType osVname notMaintained isDeprecated notImported notUpdated dependencyLevel requestId licenseLink artifactInSbomLibs { image imageLink imageCreatedAt sha os osVersion baseImage baseImageVersion tag layer registryName source } sha maintainersList { name email } runtimeStatus usedVersionReleaseDate projectDescription } dependencyGraph { nodes { id name width height vulnerable } allNodes { id name width height vulnerable } edges { v w } allEdges { v w } } groupId name mainTitle secondTitle scanId sla { daysPastSLA status } issueUpdatedAt scanDate description impact exposure severity owners ownerEmails occurrences score { value comments } orgConScore connector learnMore extraInfo { key val value snippet { detectionType fileName snippetLineNumber language text } link callBranch iconLink tags } resource { id type } appName app { id name businessPriority riskScore secPosture type typeComments applicationFlows { artifacts { type name hashType system subType hash size date location { runBy foundBy foundIn link } linkName k8sType cluster region } cloudDeployments { type subType name hash hashType link location { runBy foundBy foundIn link } k8sType imageName date cluster region } cicdInfo { type system latestDate lastMonthJobCount location { runBy foundBy foundIn link } } orchestrators { type name hashType system hash size date location { runBy foundBy foundIn link } } kubernetes { type name hashType system hash subType size date location { runBy foundBy foundIn link } } repository { type system date location { runBy foundBy foundIn link } } } fakeApp originBranchName repoId organization repoName owners { name email roles } credentialsId lastCodeChange createdAt publicVisibility branch } policy { id name detailedDescription } issueId category { name categoryId subCategoryName subCategoryComment } aggregations { type columns { columns { header key tooltip href type } comment } items { originalSeverity oxSeverity callBranch linkToExternalProduct stars forks downloads vulBySeverity nameAndVer sourceRepoName sourceRepoLink sourceCreationDate sourceLastModifyDate destinationRepoName destinationRepoLink destinationCreationDate destinationLastModifyDate destinationRepoVisibility reasons _id url additionalToolData events allEvents pushType sha title link mergedBy date fileCount diffInDays reviewers user userLink userAvatar devOperation devOperationDate adminOperation adminOperationDate reviewOperation reviewOperationDate orgRole earliestActivityDate repoPermissions adminLocation email pullRequestsCount diffFromNowToCreatedAtInDays username accessLevel createdAt lastAccess fileName fileUri startLine endLine match snippet commitLink commitBy mergeDate dateCommitPushed pullRequestNumber pullRequestLink codeOwners region eduVideoLink resource service accountName cloudEnv secret secretType secretTypeDescription secretStatus image imageCreatedAt pkgCount dockerVer os binariesCount tag reputation sha256 size pushedAt source sourceLink ruleId realMatch excludedByAlert filePath lockfile accountId snippetLineNumber language daysOpen isFixAvailable aggId pkgName installedVersion fixedVersion triggerPkgName triggerPkgVersion triggerPkgUpgradeVersion dependencyType branch hashAggId repo repoCreator lastCodeDate lastAdminOperation exclusionId numberOfReposDomainAppear layer baseImage imageLink registryName project resourceGroup cloudResourceTags location locationLink parameter test cvss evidence request response dastUrl method parameterType value cluster type cloudType k8sType consoleLink name subscriptionId stringifiedClusters aggStatus falsePositive { isFalsePositive comment reportedBy reportedAt isCanceled cancelComment canceledBy canceledAt commentWhenCanceled } cbomId prDeatils { sourceControlType issueId appId repo prId prURL prBranchName commitMessage commiter comment date prTitle prBody prStatus prApprover prReviewer prMergeTime } triage { triageStatus createdBy createdAt } } } recommendation sourceTools ruleId fixes { settingType tooltip description warning confirmation inputs { type name options { name selected metadata info displayName isDisabled } multiSelect maxSelect minSelect displayName } } fixAppliedDeatils { appliedBy appliedDate } cwe fixLink cweList { name description url } dependencyChain publicExploitLink createdAt tickets { provider ticketId createdBy issueId issueName appName appId category assignee reporter link project issueType key } slackNotification { channelName timestamp } messages { messagingVendor recipients { name id type } createdAt } fixIssue { fixType fixTitle fixDescription isFixApplied fixAppliedBy sourceControlType fixDate } requestContent responseContent autoFix { fixType fixTitle fixDescription isFixApplied fixAppliedBy sourceControlType fixDate } lowerSeverityReason severityChange originalToolSeverity scaVulnerabilities { issueId oxSeverity severityNumberFromTool severityFromTool cve cveLink cvsVer cvssVersion epss percentile libName dependencyChain runtimeStatus libVersion chainDepth exploitInTheWild exploitInTheWildLink description dateDiscovered minorVerWithFix majorVerWithFix exploitRequirement exploitCode originalSeverity } dependencyGraphNodes { id name width height vulnerable } dependencyGraphEdges { v w } scaTriggerPkg scaTriggerPkgs { scaTriggerPkg fileName } pkgSemanticVersion severityChangeReason severityChangedReason { changeNumber withoutAutoNumbering evidenceLabel reason shortName changeCategory extraInfo { key value link snippet { snippetLineNumber language text fileName } iconLink callBranch } extraInfoContainer { layerSha layerNum artifactName sha registryName } order } aggSeverityExplanation aggSFsForCalcDisplay { changeNumber withoutAutoNumbering evidenceLabel reason shortName changeCategory extraInfo { key value link snippet { snippetLineNumber language text fileName } iconLink callBranch } extraInfoContainer { layerSha layerNum artifactName sha registryName } order } resolvedIssueDate isPRAvailable cicdFields { issueStatus sourceBranch targetBranch jobId jobTriggeredAt jobTriggeredAtDate jobTriggeredBy jobTriggeredReason jobUrl pullRequestId pullRequestUrl enforcement excludedByAlert cicdEventType workflows { id name } } comment excludedByAlert excludedByPolicy excludedByApp countRule exclusionId languageInfo { name version } isMonoRepoChild monoRepoParent isFixAvailable isFixApplied isGPTFixAvailable oscarData { name description url id } gptInfo { gptResponse user createdAt } prDeatils { sourceControlType issueId appId repo prId prURL prBranchName commitMessage commiter comment date prTitle prBody prStatus prApprover prReviewer prMergeTime } tags { tagId name email displayName tagType createdBy purpose deploymentModel tagCategory } originalSeverity overrideSeverity isFalsePositive falsePositiveComment isCanceledFalsePositive cancelFalsePositiveComment falsePositiveDetails { canceledBy reportedBy commentWhenCanceled aggregationsStatus } issueStatus scanIssueStatus resolvedReason resolvedDetails resolvedReasonDetails { description } disappearedReason disappearedDetails disappearedReasonDetails { description } disappearedDate correlatedIssueId correlatedRegistry scaFixType previousSeverity { severity severityChangedDate } version severityFactorsDiff { shortName change status } exposedByApiItems { apiId codeLocations { link callBranch } } originBranchName exclusionComment exclusionExpiredAt problematicPkg serverlessDeploymentOperation { userIdentity { type principalId arn accountId accessKeyId sessionContext { sessionIssuer { type principalId arn accountId userName } attributes { creationDate mfaAuthenticated } } } deploymentTime sourceIPAddress userAgent connectedFromConsole location linkToCode functionName functionArn internalFunctionName cloudRegion version revisionId codeSha256 entryPoint codeSize memorySize timeout runtime runtimeVersionConfig { runtimeVersionArn } architectures role recipientAccountId description } eventFromExternalTool issueOwners { name email } overrideIssueOwner originalIssueOwners { name email } cveExclusions { label recommended tooltip type id oxRuleId level excludeBy uidOnly isDefault ffKey exclusionScope } } totalDisappearedIssues totalFilteredDisappearedIssues totalResolvedIssues offset topOffset selectedPosition totalActiveIssues cursorValue } }'

response = requests.post(
  "https://api.cloud.ox.security/api/apollo-gateway",
  headers={
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_TOKEN"
  },
  json={
    "query": query,
    # This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.
    "variables": {
      "getRemovedIssuesInput": {
        "scanID": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        "limit": 100,
        "offset": 0,
        "sort": {
          "fields": ["Category"],
          "order": ["ASC"]
        },
        "owners": ["example"],
        "tagIds": ["example"],
        "inventoryFilters": ["New"],
        "dateRange": {
          "from": 1749000000000,
          "to": 1749900000000
        },
        "search": [
          {
            "fieldName": "example",
            "value": ["example"]
          }
        ],
        "openItems": ["digest"],
        "conditionalFilters": [
          {
            "condition": "AND",
            "fieldName": "digest",
            "values": ["example"],
            "greaterThan": 13.37,
            "lessThan": 13.37
          }
        ],
        "exportsOptions": {
          "flattenAgg": true,
          "isDemoEnabled": true,
          "name": "SomeName",
          "columns": [
            {
              "key": "Severity",
              "name": "SomeName"
            }
          ],
          "rowsLimit": 42
        },
        "restrictToCategories": [42],
        "topLevelSearch": "example",
        "topOffset": 42,
        "issueId": "30966426-oxPolicy_securityCloudScan_100-example",
        "scrollDirection": "example",
        "cursorValue": "example"
      }
    }
  }
)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

{% endtab %}
{% endtabs %}

### Arguments

You can use the following argument(s) to customize your `getRemovedIssues` query.

| Argument                                                                                                                                                    | Description                                            | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getRemovedIssuesInput [`DisappearedIssuesInput`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/disappeared-issues-input) | Parameters for filtering and paginating removed issues | <p>scanID <code>String</code><br>limit <code>Int!</code><br>offset <code>Int!</code><br>sort <a href="../types/inputs/d-issues-sort"><code>DIssuesSort</code></a><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>inventoryFilters <a href="../types/enums/inventory-types"><code>\[InventoryTypes]</code></a><br>dateRange <a href="../../api--application/types/inputs/date-range"><code>DateRange</code></a><br>search <a href="../../api--application/types/inputs/auto-complete-search"><code>\[AutoCompleteSearch]</code></a><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a><br>conditionalFilters <a href="../../api--application/types/inputs/conditional-filters"><code>\[ConditionalFilters]</code></a><br>exportsOptions <a href="../types/inputs/issues-export-options"><code>IssuesExportOptions</code></a><br>restrictToCategories <code>\[Int]</code><br>topLevelSearch <code>String</code><br>topOffset <code>Int</code><br>issueId <code>String</code><br>scrollDirection <code>String</code><br>cursorValue <code>String</code></p> |

### Fields

Return type: [`DisappearedIssuesResponse`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/disappeared-issues-response)

You can use the following field(s) to specify what information your `getRemovedIssues` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                  | Description                                                                    | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| disappearedIssues [`[Issue]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue) | List of security issues that have disappeared from recent scans                | <p>importantSeverityBreakdown <code>\[String]</code><br><del>isCVERelated <code>Boolean</code></del> ⚠️<br>overrideSeverityReason <code>String</code><br>highestOXCVESeverity <code>String</code><br>latestCommit <a href="../types/objects/agg-item"><code>AggItem</code></a><br>additionalTabs <a href="../types/objects/additional-tab"><code>\[AdditionalTab]</code></a><br>issueDetailsHeaders <a href="../types/objects/issue-details-tabs"><code>\[IssueDetailsTabs]</code></a><br>compliance <a href="../types/objects/compliance-item"><code>\[ComplianceItem]</code></a><br>sbom <a href="../types/objects/sbom-lib"><code>SbomLib</code></a><br>dependencyGraph <a href="../types/objects/sbom-dependency-graph-response"><code>SbomDependencyGraphResponse</code></a><br>groupId <code>String</code><br>name <code>String</code><br>mainTitle <code>String</code><br>secondTitle <code>String</code><br>scanId <code>String</code><br><del>created <code>Float</code></del> ⚠️<br>sla <a href="../types/objects/sla-data"><code>SlaData</code></a><br>issueUpdatedAt <code>Float</code><br>scanDate <code>Float</code><br>description <code>String</code><br>impact <code>String</code><br>exposure <code>String</code><br>severity <code>String</code><br>owners <code>\[String]</code><br>ownerEmails <code>\[String]</code><br>occurrences <code>Int</code><br>score <a href="../types/objects/issue-score"><code>IssueScore</code></a><br>orgConScore <code>Float</code><br>connector <code>String</code><br>learnMore <code>\[String]</code><br>extraInfo <a href="../types/objects/extra-info"><code>\[ExtraInfo]</code></a><br>resource <a href="../types/objects/issue-resource"><code>IssueResource</code></a><br>appName <code>String</code><br>app <a href="../types/objects/i-apps-info"><code>IAppsInfo</code></a><br>policy <a href="../types/objects/i-policy"><code>IPolicy</code></a><br>issueId <code>String</code><br>category <a href="../types/objects/i-category"><code>ICategory</code></a><br>aggregations <a href="../types/objects/i-aggregations"><code>IAggregations</code></a><br>recommendation <code>String</code><br>sourceTools <code>\[String]</code><br>ruleId <code>String</code><br>fixes <a href="../types/objects/policy-fix"><code>PolicyFix</code></a><br>fixAppliedDeatils <a href="../types/objects/fix-applied-deatils"><code>FixAppliedDeatils</code></a><br>cwe <code>\[String]</code><br>fixLink <code>String</code><br>cweList <a href="../types/objects/cwe-list"><code>\[CweList]</code></a><br>dependencyChain <code>\[String]</code><br>publicExploitLink <code>String</code><br>createdAt <code>Float</code><br>tickets <a href="../types/objects/ticket"><code>\[Ticket]</code></a><br>slackNotification <a href="../types/objects/slack-notification"><code>\[SlackNotification]</code></a><br>messages <a href="../types/objects/issue-message"><code>\[IssueMessage]</code></a><br>fixIssue <a href="../types/objects/fix-issue"><code>FixIssue</code></a><br>requestContent <code>String</code><br>responseContent <code>String</code><br>autoFix <a href="../types/objects/fix-issue"><code>FixIssue</code></a><br>lowerSeverityReason <code>\[String]</code><br>severityChange <code>String</code><br>originalToolSeverity <code>String</code><br>scaVulnerabilities <a href="../types/objects/sca-vulnerability"><code>\[SCAVulnerability]</code></a><br>dependencyGraphNodes <a href="../types/objects/dependency-node"><code>\[DependencyNode]</code></a><br>dependencyGraphEdges <a href="../types/objects/dependency-edge"><code>\[DependencyEdge]</code></a><br>scaTriggerPkg <code>String</code><br>scaTriggerPkgs <a href="../types/objects/trigger-package"><code>\[TriggerPackage]</code></a><br>pkgSemanticVersion <code>String</code><br><del>graphExist <code>Boolean</code></del> ⚠️<br>severityChangeReason <code>\[String]</code><br>severityChangedReason <a href="../types/objects/severity-changed-reason"><code>\[SeverityChangedReason]</code></a><br>aggSeverityExplanation <code>String</code><br>aggSFsForCalcDisplay <a href="../types/objects/severity-changed-reason"><code>\[SeverityChangedReason]</code></a><br>resolvedIssueDate <code>Float</code><br>isPRAvailable <code>Boolean</code><br>cicdFields <a href="../types/objects/cicd-fields"><code>CICDFields</code></a><br>comment <code>String</code><br>excludedByAlert <code>Boolean</code><br>excludedByPolicy <code>Boolean</code><br>excludedByApp <code>Boolean</code><br>countRule <a href="../types/enums/count-rule"><code>CountRule</code></a><br>exclusionId <code>String</code><br>languageInfo <a href="../types/objects/language-info"><code>LanguageInfo</code></a><br>isMonoRepoChild <code>Boolean</code><br>monoRepoParent <code>String</code><br>isFixAvailable <code>Boolean</code><br>isFixApplied <code>Boolean</code><br>isGPTFixAvailable <code>Boolean</code><br>oscarData <a href="../types/objects/oscar-item"><code>\[OscarItem]</code></a><br>gptInfo <a href="../types/objects/gpt-info"><code>GPTInfo</code></a><br>prDeatils <a href="../types/objects/pull-request"><code>PullRequest</code></a><br>tags <a href="../../api--application/types/objects/app-tag"><code>\[AppTag]</code></a><br>originalSeverity <code>Int</code><br>overrideSeverity <code>Boolean</code><br>isFalsePositive <code>Boolean</code><br>falsePositiveComment <code>String</code><br>isCanceledFalsePositive <code>Boolean</code><br>cancelFalsePositiveComment <code>String</code><br>falsePositiveDetails <a href="../types/objects/false-positive-details"><code>FalsePositiveDetails</code></a><br>issueStatus <a href="../types/enums/issue-status"><code>IssueStatus</code></a><br>scanIssueStatus <a href="../types/enums/issue-status"><code>IssueStatus</code></a><br>resolvedReason <code>String</code><br>resolvedDetails <code>String</code><br>resolvedReasonDetails <a href="../types/objects/reason-details"><code>ReasonDetails</code></a><br>disappearedReason <code>String</code><br>disappearedDetails <code>String</code><br>disappearedReasonDetails <a href="../types/objects/reason-details"><code>ReasonDetails</code></a><br>disappearedDate <code>Float</code><br>correlatedIssueId <code>String</code><br>correlatedRegistry <code>String</code><br>scaFixType <a href="../types/enums/sca-fix-type"><code>ScaFixType</code></a><br>previousSeverity <a href="../types/objects/prev-severity"><code>PrevSeverity</code></a><br>version <code>String</code><br>severityFactorsDiff <a href="../types/objects/severity-factors-diff"><code>\[SeverityFactorsDiff]</code></a><br>exposedByApiItems <a href="../types/objects/exposed-by-api-item"><code>\[ExposedByApiItem]</code></a><br>originBranchName <code>String</code><br>exclusionComment <code>String</code><br>exclusionExpiredAt <code>Date</code><br>problematicPkg <code>String</code><br>serverlessDeploymentOperation <a href="../types/objects/serverless-deployment-operation"><code>ServerlessDeploymentOperation</code></a><br>eventFromExternalTool <code>Boolean</code><br>issueOwners <a href="../types/objects/i-owner"><code>\[IOwner]</code></a><br>overrideIssueOwner <code>Boolean</code><br>originalIssueOwners <a href="../types/objects/i-owner"><code>\[IOwner]</code></a><br>cveExclusions <a href="../types/objects/recommended-exclusions"><code>\[RecommendedExclusions]</code></a></p> |
| totalDisappearedIssues `Int`                                                                                           | Total count of disappeared issues without any filters applied                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| totalFilteredDisappearedIssues `Int`                                                                                   | Total count of disappeared issues after applying filters                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| totalResolvedIssues `Int`                                                                                              | Total count of issues that have been resolved                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| offset `Int`                                                                                                           | Current pagination offset                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| topOffset `Int`                                                                                                        | Top offset for advanced pagination                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| selectedPosition `Int`                                                                                                 | Selected position of the issue in the list                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| totalActiveIssues `Int`                                                                                                | Total count of currently active issues                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| cursorValue `String`                                                                                                   | Cursor value for pagination. Use this value to fetch the next page of results. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

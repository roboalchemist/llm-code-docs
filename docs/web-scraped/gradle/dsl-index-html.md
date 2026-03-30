# Source: https://docs.gradle.org/dsl/index.html

Title: Gradle DSL Version 9.4.0

URL Source: https://docs.gradle.org/dsl/index.html

Markdown Content:
Gradle DSL Version 9.4.0
===============

[](https://docs.gradle.org/ "Gradle Docs")

DSL Reference

9.4.0

* Community [Community Home](https://gradle.org/) [Community Forums](https://discuss.gradle.org/) [Community Plugins](https://plugins.gradle.org/)  
* [Training](https://gradle.org/training/)
* News [Newsletter](https://newsletter.gradle.org/) [Blog](https://blog.gradle.org/) [Twitter](https://twitter.com/gradle)  
* [Develocity](https://gradle.com/develocity)
* [](https://github.com/gradle/gradle "Gradle on GitHub")

Search

* [User Manual Home](https://docs.gradle.org/userguide/userguide.html)
* [DSL Reference Home](https://docs.gradle.org/dsl/index.html)
* [Release Notes](https://docs.gradle.org/release-notes.html)

  * [Introduction](https://docs.gradle.org/dsl/index.html#N1000C "Introduction")
  * [Some basics](https://docs.gradle.org/dsl/index.html#N10011 "Some basics")
  * [Build script structure](https://docs.gradle.org/dsl/index.html#N10060 "Build script structure")
  * [Core types](https://docs.gradle.org/dsl/index.html#N100C1 "Core types")
  * [Publishing types](https://docs.gradle.org/dsl/index.html#N10224 "Publishing types")
  * [Container types](https://docs.gradle.org/dsl/index.html#N1036B "Container types")
  * [Authentication types](https://docs.gradle.org/dsl/index.html#N103D0 "Authentication types")
  * [Build Cache types](https://docs.gradle.org/dsl/index.html#N1044D "Build Cache types")
  * [Input Normalization types](https://docs.gradle.org/dsl/index.html#N1047B "Input Normalization types")
  * [Help Task types](https://docs.gradle.org/dsl/index.html#N104A5 "Help Task types")
  * [Task types](https://docs.gradle.org/dsl/index.html#N1052B "Task types")
  * [Test types](https://docs.gradle.org/dsl/index.html#N106BB "Test types")
  * [Reporting types](https://docs.gradle.org/dsl/index.html#N10748 "Reporting types")
  * [Eclipse/IDEA model types](https://docs.gradle.org/dsl/index.html#N107AD "Eclipse/IDEA model types")
  * [Eclipse/IDEA task types](https://docs.gradle.org/dsl/index.html#N10836 "Eclipse/IDEA task types")
  * [Xcode task types](https://docs.gradle.org/dsl/index.html#N10893 "Xcode task types")
  * [Visual Studio task types](https://docs.gradle.org/dsl/index.html#N108D2 "Visual Studio task types")
  * [Artifact transform types](https://docs.gradle.org/dsl/index.html#N10905 "Artifact transform types")
  * [Native tool chains model types](https://docs.gradle.org/dsl/index.html#N1092F "Native tool chains model types")
  * [Native software model types](https://docs.gradle.org/dsl/index.html#N1096E "Native software model types")
  * [C++ component model types](https://docs.gradle.org/dsl/index.html#N10ACE "C++ component model types")
  * [Swift component model types](https://docs.gradle.org/dsl/index.html#N10AF8 "Swift component model types")
  * [Native binary task types](https://docs.gradle.org/dsl/index.html#N10B22 "Native binary task types")
  * [Native binary task types](https://docs.gradle.org/dsl/index.html#N10B8B "Native binary task types")

* ### Build script blocks

* [`allprojects { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:allprojects(groovy.lang.Closure))
* [`artifacts { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:artifacts(groovy.lang.Closure))
* [`buildscript { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:buildscript(groovy.lang.Closure))
* [`configurations { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:configurations(groovy.lang.Closure))
* [`dependencies { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:dependencies(groovy.lang.Closure))
* [`repositories { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:repositories(groovy.lang.Closure))
* [`subprojects { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:subprojects(groovy.lang.Closure))
* [`publishing { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:publishing(groovy.lang.Closure))

* ### Core types

* [`Project`](https://docs.gradle.org/dsl/org.gradle.api.Project.html)
* [`Task`](https://docs.gradle.org/dsl/org.gradle.api.Task.html)
* [`Gradle`](https://docs.gradle.org/dsl/org.gradle.api.invocation.Gradle.html)
* [`Settings`](https://docs.gradle.org/dsl/org.gradle.api.initialization.Settings.html)
* [`IncludedBuild`](https://docs.gradle.org/dsl/org.gradle.api.initialization.IncludedBuild.html)
* [`ProjectLayout`](https://docs.gradle.org/dsl/org.gradle.api.file.ProjectLayout.html)
* [`BuildLayout`](https://docs.gradle.org/dsl/org.gradle.api.file.BuildLayout.html)
* [`Script`](https://docs.gradle.org/dsl/org.gradle.api.Script.html)
* [`SourceSet`](https://docs.gradle.org/dsl/org.gradle.api.tasks.SourceSet.html)
* [`SourceSetOutput`](https://docs.gradle.org/dsl/org.gradle.api.tasks.SourceSetOutput.html)
* [`SourceDirectorySet`](https://docs.gradle.org/dsl/org.gradle.api.file.SourceDirectorySet.html)
* [`Configuration`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.Configuration.html)
* [`ConsumableConfiguration`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.ConsumableConfiguration.html)
* [`ResolvableConfiguration`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.ResolvableConfiguration.html)
* [`DependencyScopeConfiguration`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.DependencyScopeConfiguration.html)
* [`ResolutionStrategy`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.ResolutionStrategy.html)
* [`ArtifactResolutionQuery`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.query.ArtifactResolutionQuery.html)
* [`ComponentSelection`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.ComponentSelection.html)
* [`ComponentSelectionRules`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.ComponentSelectionRules.html)
* [`DependencyCollector`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.DependencyCollector.html)
* [`ExtensionAware`](https://docs.gradle.org/dsl/org.gradle.api.plugins.ExtensionAware.html)
* [`ExtraPropertiesExtension`](https://docs.gradle.org/dsl/org.gradle.api.plugins.ExtraPropertiesExtension.html)
* [`PluginDependenciesSpec`](https://docs.gradle.org/dsl/org.gradle.plugin.use.PluginDependenciesSpec.html)
* [`PluginDependencySpec`](https://docs.gradle.org/dsl/org.gradle.plugin.use.PluginDependencySpec.html)
* [`PluginManagementSpec`](https://docs.gradle.org/dsl/org.gradle.plugin.management.PluginManagementSpec.html)
* [`ProviderFactory`](https://docs.gradle.org/dsl/org.gradle.api.provider.ProviderFactory.html)
* [`ResourceHandler`](https://docs.gradle.org/dsl/org.gradle.api.resources.ResourceHandler.html)
* [`TextResourceFactory`](https://docs.gradle.org/dsl/org.gradle.api.resources.TextResourceFactory.html)
* [`InputChanges`](https://docs.gradle.org/dsl/org.gradle.work.InputChanges.html)
* [`Distribution`](https://docs.gradle.org/dsl/org.gradle.api.distribution.Distribution.html)

* ### Publishing types

* [`PublishingExtension`](https://docs.gradle.org/dsl/org.gradle.api.publish.PublishingExtension.html)
* [`IvyPublication`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyPublication.html)
* [`IvyArtifact`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyArtifact.html)
* [`IvyArtifactSet`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyArtifactSet.html)
* [`IvyModuleDescriptorSpec`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyModuleDescriptorSpec.html)
* [`IvyModuleDescriptorAuthor`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyModuleDescriptorAuthor.html)
* [`IvyModuleDescriptorLicense`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyModuleDescriptorLicense.html)
* [`IvyModuleDescriptorDescription`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyModuleDescriptorDescription.html)
* [`MavenPublication`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPublication.html)
* [`MavenArtifact`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenArtifact.html)
* [`MavenArtifactSet`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenArtifactSet.html)
* [`MavenPom`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPom.html)
* [`MavenPomCiManagement`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomCiManagement.html)
* [`MavenPomContributor`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomContributor.html)
* [`MavenPomContributorSpec`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomContributorSpec.html)
* [`MavenPomDeveloper`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomDeveloper.html)
* [`MavenPomDeveloperSpec`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomDeveloperSpec.html)
* [`MavenPomDistributionManagement`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomDistributionManagement.html)
* [`MavenPomIssueManagement`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomIssueManagement.html)
* [`MavenPomLicense`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomLicense.html)
* [`MavenPomLicenseSpec`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomLicenseSpec.html)
* [`MavenPomMailingList`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomMailingList.html)
* [`MavenPomMailingListSpec`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomMailingListSpec.html)
* [`MavenPomOrganization`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomOrganization.html)
* [`MavenPomRelocation`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomRelocation.html)
* [`MavenPomScm`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomScm.html)

* ### Container types

* [`TaskContainer`](https://docs.gradle.org/dsl/org.gradle.api.tasks.TaskContainer.html)
* [`ConfigurationContainer`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.ConfigurationContainer.html)
* [`RepositoryHandler`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.RepositoryHandler.html)
* [`DependencyHandler`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.DependencyHandler.html)
* [`ComponentMetadataHandler`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.ComponentMetadataHandler.html)
* [`ArtifactHandler`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.ArtifactHandler.html)

* ### Build Cache types

* [`BuildCacheConfiguration`](https://docs.gradle.org/dsl/org.gradle.caching.configuration.BuildCacheConfiguration.html)
* [`DirectoryBuildCache`](https://docs.gradle.org/dsl/org.gradle.caching.local.DirectoryBuildCache.html)
* [`HttpBuildCache`](https://docs.gradle.org/dsl/org.gradle.caching.http.HttpBuildCache.html)

* ### Input Normalization types

* [`InputNormalizationHandler`](https://docs.gradle.org/dsl/org.gradle.normalization.InputNormalizationHandler.html)
* [`InputNormalization`](https://docs.gradle.org/dsl/org.gradle.normalization.InputNormalization.html)
* [`RuntimeClasspathNormalization`](https://docs.gradle.org/dsl/org.gradle.normalization.RuntimeClasspathNormalization.html)

* ### Help Task types

* [`TaskReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.TaskReportTask.html)
* [`ProjectReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.ProjectReportTask.html)
* [`DependencyReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.DependencyReportTask.html)
* [`DependencyInsightReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.DependencyInsightReportTask.html)
* [`PropertyReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.PropertyReportTask.html)
* [`ComponentReport`](https://docs.gradle.org/dsl/org.gradle.api.reporting.components.ComponentReport.html)
* [`DependentComponentsReport`](https://docs.gradle.org/dsl/org.gradle.api.reporting.dependents.DependentComponentsReport.html)
* [`ModelReport`](https://docs.gradle.org/dsl/org.gradle.api.reporting.model.ModelReport.html)
* [`OutgoingVariantsReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.OutgoingVariantsReportTask.html)
* [`ResolvableConfigurationsReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.ResolvableConfigurationsReportTask.html)
* [`ArtifactTransformsReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.ArtifactTransformsReportTask.html)

* ### Task types

* [`AntlrTask`](https://docs.gradle.org/dsl/org.gradle.api.plugins.antlr.AntlrTask.html)
* [`BuildEnvironmentReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.BuildEnvironmentReportTask.html)
* [`Checkstyle`](https://docs.gradle.org/dsl/org.gradle.api.plugins.quality.Checkstyle.html)
* [`CodeNarc`](https://docs.gradle.org/dsl/org.gradle.api.plugins.quality.CodeNarc.html)
* [`Copy`](https://docs.gradle.org/dsl/org.gradle.api.tasks.Copy.html)
* [`CreateStartScripts`](https://docs.gradle.org/dsl/org.gradle.jvm.application.tasks.CreateStartScripts.html)
* [`Delete`](https://docs.gradle.org/dsl/org.gradle.api.tasks.Delete.html)
* [`Ear`](https://docs.gradle.org/dsl/org.gradle.plugins.ear.Ear.html)
* [`Exec`](https://docs.gradle.org/dsl/org.gradle.api.tasks.Exec.html)
* [`GenerateIvyDescriptor`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.tasks.GenerateIvyDescriptor.html)
* [`GenerateMavenPom`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.tasks.GenerateMavenPom.html)
* [`GenerateBuildDashboard`](https://docs.gradle.org/dsl/org.gradle.api.reporting.GenerateBuildDashboard.html)
* [`GradleBuild`](https://docs.gradle.org/dsl/org.gradle.api.tasks.GradleBuild.html)
* [`GroovyCompile`](https://docs.gradle.org/dsl/org.gradle.api.tasks.compile.GroovyCompile.html)
* [`Groovydoc`](https://docs.gradle.org/dsl/org.gradle.api.tasks.javadoc.Groovydoc.html)
* [`HtmlDependencyReportTask`](https://docs.gradle.org/dsl/org.gradle.api.reporting.dependencies.HtmlDependencyReportTask.html)
* [`JacocoReport`](https://docs.gradle.org/dsl/org.gradle.testing.jacoco.tasks.JacocoReport.html)
* [`JacocoCoverageVerification`](https://docs.gradle.org/dsl/org.gradle.testing.jacoco.tasks.JacocoCoverageVerification.html)
* [`Jar`](https://docs.gradle.org/dsl/org.gradle.api.tasks.bundling.Jar.html)
* [`JavaCompile`](https://docs.gradle.org/dsl/org.gradle.api.tasks.compile.JavaCompile.html)
* [`Javadoc`](https://docs.gradle.org/dsl/org.gradle.api.tasks.javadoc.Javadoc.html)
* [`JavaExec`](https://docs.gradle.org/dsl/org.gradle.api.tasks.JavaExec.html)
* [`Pmd`](https://docs.gradle.org/dsl/org.gradle.api.plugins.quality.Pmd.html)
* [`ProcessResources`](https://docs.gradle.org/dsl/org.gradle.language.jvm.tasks.ProcessResources.html)
* [`PublishToIvyRepository`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.tasks.PublishToIvyRepository.html)
* [`PublishToMavenRepository`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.tasks.PublishToMavenRepository.html)
* [`ScalaCompile`](https://docs.gradle.org/dsl/org.gradle.api.tasks.scala.ScalaCompile.html)
* [`ScalaDoc`](https://docs.gradle.org/dsl/org.gradle.api.tasks.scala.ScalaDoc.html)
* [`UpdateDaemonJvm`](https://docs.gradle.org/dsl/org.gradle.buildconfiguration.tasks.UpdateDaemonJvm.html)
* [`InitBuild`](https://docs.gradle.org/dsl/org.gradle.buildinit.tasks.InitBuild.html)
* [`Sign`](https://docs.gradle.org/dsl/org.gradle.plugins.signing.Sign.html)
* [`Sync`](https://docs.gradle.org/dsl/org.gradle.api.tasks.Sync.html)
* [`Tar`](https://docs.gradle.org/dsl/org.gradle.api.tasks.bundling.Tar.html)
* [`AbstractTestTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.testing.AbstractTestTask.html)
* [`Test`](https://docs.gradle.org/dsl/org.gradle.api.tasks.testing.Test.html)
* [`TestReport`](https://docs.gradle.org/dsl/org.gradle.api.tasks.testing.TestReport.html)
* [`War`](https://docs.gradle.org/dsl/org.gradle.api.tasks.bundling.War.html)
* [`Wrapper`](https://docs.gradle.org/dsl/org.gradle.api.tasks.wrapper.Wrapper.html)
* [`WriteProperties`](https://docs.gradle.org/dsl/org.gradle.api.tasks.WriteProperties.html)
* [`Zip`](https://docs.gradle.org/dsl/org.gradle.api.tasks.bundling.Zip.html)

* ### Test types

* [`TestingExtension`](https://docs.gradle.org/dsl/org.gradle.testing.base.TestingExtension.html)
* [`TestSuite`](https://docs.gradle.org/dsl/org.gradle.testing.base.TestSuite.html)
* [`JvmTestSuite`](https://docs.gradle.org/dsl/org.gradle.api.plugins.jvm.JvmTestSuite.html)
* [`TestSuiteTarget`](https://docs.gradle.org/dsl/org.gradle.testing.base.TestSuiteTarget.html)
* [`JvmTestSuiteTarget`](https://docs.gradle.org/dsl/org.gradle.api.plugins.jvm.JvmTestSuiteTarget.html)
* [`Test`](https://docs.gradle.org/dsl/org.gradle.api.tasks.testing.Test.html)
* [`Dependencies`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.Dependencies.html)
* [`GradleDependencies`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.GradleDependencies.html)
* [`TestFixturesDependencyModifiers`](https://docs.gradle.org/dsl/org.gradle.api.plugins.jvm.TestFixturesDependencyModifiers.html)
* [`PlatformDependencyModifiers`](https://docs.gradle.org/dsl/org.gradle.api.plugins.jvm.PlatformDependencyModifiers.html)
* [`JvmComponentDependencies`](https://docs.gradle.org/dsl/org.gradle.api.plugins.jvm.JvmComponentDependencies.html)

* ### Reporting types

* [`CustomizableHtmlReport`](https://docs.gradle.org/dsl/org.gradle.api.reporting.CustomizableHtmlReport.html)
* [`SingleFileReport`](https://docs.gradle.org/dsl/org.gradle.api.reporting.SingleFileReport.html)
* [`DirectoryReport`](https://docs.gradle.org/dsl/org.gradle.api.reporting.DirectoryReport.html)
* [`Report`](https://docs.gradle.org/dsl/org.gradle.api.reporting.Report.html)
* [`Reporting`](https://docs.gradle.org/dsl/org.gradle.api.reporting.Reporting.html)
* [`ReportContainer`](https://docs.gradle.org/dsl/org.gradle.api.reporting.ReportContainer.html)
* [`ReportingExtension`](https://docs.gradle.org/dsl/org.gradle.api.reporting.ReportingExtension.html)
* [`AggregateTestReport`](https://docs.gradle.org/dsl/org.gradle.api.tasks.testing.AggregateTestReport.html)
* [`JacocoCoverageReport`](https://docs.gradle.org/dsl/org.gradle.testing.jacoco.plugins.JacocoCoverageReport.html)

* ### Eclipse/IDEA model types

* [`EclipseModel`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseModel.html)
* [`EclipseProject`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseProject.html)
* [`EclipseClasspath`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseClasspath.html)
* [`EclipseJdt`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseJdt.html)
* [`EclipseWtp`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseWtp.html)
* [`EclipseWtpComponent`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseWtpComponent.html)
* [`EclipseWtpFacet`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseWtpFacet.html)
* [`IdeaModel`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.model.IdeaModel.html)
* [`IdeaProject`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.model.IdeaProject.html)
* [`IdeaModule`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.model.IdeaModule.html)
* [`IdeaWorkspace`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.model.IdeaWorkspace.html)
* [`XmlFileContentMerger`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.api.XmlFileContentMerger.html)
* [`FileContentMerger`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.api.FileContentMerger.html)

* ### Eclipse/IDEA task types

* [`GenerateEclipseProject`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.GenerateEclipseProject.html)
* [`GenerateEclipseClasspath`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.GenerateEclipseClasspath.html)
* [`GenerateEclipseJdt`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.GenerateEclipseJdt.html)
* [`GenerateEclipseWtpComponent`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.GenerateEclipseWtpComponent.html)
* [`GenerateEclipseWtpFacet`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.GenerateEclipseWtpFacet.html)
* [`GenerateIdeaModule`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.GenerateIdeaModule.html)
* [`GenerateIdeaProject`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.GenerateIdeaProject.html)
* [`GenerateIdeaWorkspace`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.GenerateIdeaWorkspace.html)

* ### Xcode task types

* [`GenerateSchemeFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.xcode.tasks.GenerateSchemeFileTask.html)
* [`GenerateWorkspaceSettingsFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.xcode.tasks.GenerateWorkspaceSettingsFileTask.html)
* [`GenerateXcodeProjectFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.xcode.tasks.GenerateXcodeProjectFileTask.html)
* [`GenerateXcodeWorkspaceFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.xcode.tasks.GenerateXcodeWorkspaceFileTask.html)

* ### Visual Studio task types

* [`GenerateSolutionFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.visualstudio.tasks.GenerateSolutionFileTask.html)
* [`GenerateProjectFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.visualstudio.tasks.GenerateProjectFileTask.html)
* [`GenerateFiltersFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.visualstudio.tasks.GenerateFiltersFileTask.html)

* ### Artifact transform types

* [`TransformAction`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.transform.TransformAction.html)
* [`TransformOutputs`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.transform.TransformOutputs.html)
* [`TransformSpec`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.transform.TransformSpec.html)

* ### Native tool chain types

* [`Gcc`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.toolchain.Gcc.html)
* [`Clang`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.toolchain.Clang.html)
* [`VisualCpp`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.toolchain.VisualCpp.html)
* [`Swiftc`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.toolchain.Swiftc.html)

* ### C++ component types

* [`CppApplication`](https://docs.gradle.org/dsl/org.gradle.language.cpp.CppApplication.html)
* [`CppLibrary`](https://docs.gradle.org/dsl/org.gradle.language.cpp.CppLibrary.html)
* [`CppTestSuite`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.cpp.CppTestSuite.html)

* ### Swift component types

* [`SwiftApplication`](https://docs.gradle.org/dsl/org.gradle.language.swift.SwiftApplication.html)
* [`SwiftLibrary`](https://docs.gradle.org/dsl/org.gradle.language.swift.SwiftLibrary.html)
* [`SwiftXCTestSuite`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.xctest.SwiftXCTestSuite.html)

* ### Native component task types

* [`CppCompile`](https://docs.gradle.org/dsl/org.gradle.language.cpp.tasks.CppCompile.html)
* [`SwiftCompile`](https://docs.gradle.org/dsl/org.gradle.language.swift.tasks.SwiftCompile.html)
* [`LinkExecutable`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.tasks.LinkExecutable.html)
* [`LinkSharedLibrary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.tasks.LinkSharedLibrary.html)
* [`CreateStaticLibrary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.tasks.CreateStaticLibrary.html)
* [`LinkMachOBundle`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.tasks.LinkMachOBundle.html)
* [`InstallExecutable`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.tasks.InstallExecutable.html)
* [`InstallXCTestBundle`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.xctest.tasks.InstallXCTestBundle.html)
* [`RunTestExecutable`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.tasks.RunTestExecutable.html)
* [`XCTest`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.xctest.tasks.XCTest.html)

[](https://docs.gradle.org/dsl/index.html)Gradle Build Language Reference
=========================================================================

### Version 9.4.0

[](https://docs.gradle.org/dsl/index.html#N1000C)Introduction
-------------------------------------------------------------

This reference guide describes the various types which make up the Gradle build language, or DSL.

[](https://docs.gradle.org/dsl/index.html#N10011)Some basics
------------------------------------------------------------

There are a few basic concepts that you should understand, which will help you write Gradle scripts.

First, Gradle scripts are _configuration scripts_. As the script executes, it configures an object of a particular type. For example, as a build script executes, it configures an object of type [`Project`](https://docs.gradle.org/dsl/org.gradle.api.Project.html). This object is called the _delegate object_ of the script. The following table shows the delegate for each type of Gradle script.

Type of script Delegates to instance of
Build script[`Project`](https://docs.gradle.org/dsl/org.gradle.api.Project.html)
Init script[`Gradle`](https://docs.gradle.org/dsl/org.gradle.api.invocation.Gradle.html)
Settings script[`Settings`](https://docs.gradle.org/dsl/org.gradle.api.initialization.Settings.html)

The properties and methods of the delegate object are available for you to use in the script.

Second, each Gradle script implements the [`Script`](https://docs.gradle.org/dsl/org.gradle.api.Script.html) interface. This interface defines a number of properties and methods which you can use in the script.

[](https://docs.gradle.org/dsl/index.html#N10060)Build script structure
-----------------------------------------------------------------------

A build script is made up of zero or more statements and script blocks. Statements can include method calls, property assignments, and local variable definitions. A script block is a method call which takes a closure as a parameter. The closure is treated as a _configuration closure_ which configures some delegate object as it executes. The top level script blocks are listed below.

Block Description
[`allprojects { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:allprojects(groovy.lang.Closure))Configures this project and each of its sub-projects.
[`artifacts { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:artifacts(groovy.lang.Closure))Configures the published artifacts for this project.
[`buildscript { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:buildscript(groovy.lang.Closure))Configures the build script classpath for this project.
[`configurations { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:configurations(groovy.lang.Closure))Configures the dependency configurations for this project.
[`dependencies { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:dependencies(groovy.lang.Closure))Configures the dependencies for this project.
[`repositories { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:repositories(groovy.lang.Closure))Configures the repositories for this project.
[`subprojects { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:subprojects(groovy.lang.Closure))Configures the sub-projects of this project.
[`publishing { }`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:publishing(groovy.lang.Closure))Configures the [`PublishingExtension`](https://docs.gradle.org/dsl/org.gradle.api.publish.PublishingExtension.html) added by the publishing plugin.

A build script is also a Groovy script, and so can contain those elements allowed in a Groovy script, such as method definitions and class definitions.

[](https://docs.gradle.org/dsl/index.html#N100C1)Core types
-----------------------------------------------------------

Listed below are some of the central types which are used in Gradle scripts:

Type Description
[`Project`](https://docs.gradle.org/dsl/org.gradle.api.Project.html)This interface is the main API you use to interact with Gradle from your build file. From a `Project`, you have programmatic access to all of Gradle's features.
[`Task`](https://docs.gradle.org/dsl/org.gradle.api.Task.html)A `Task` represents a single atomic piece of work for a build, such as compiling classes or generating javadoc.
[`Gradle`](https://docs.gradle.org/dsl/org.gradle.api.invocation.Gradle.html)Represents an invocation of Gradle.
[`Settings`](https://docs.gradle.org/dsl/org.gradle.api.initialization.Settings.html)Declares the configuration required to instantiate and configure the hierarchy of [`Project`](https://docs.gradle.org/dsl/org.gradle.api.Project.html) instances which are to participate in a build.
[`IncludedBuild`](https://docs.gradle.org/dsl/org.gradle.api.initialization.IncludedBuild.html)A build that is included in the composite.
[`ProjectLayout`](https://docs.gradle.org/dsl/org.gradle.api.file.ProjectLayout.html)Provides access to several important locations for a project.
[`BuildLayout`](https://docs.gradle.org/dsl/org.gradle.api.file.BuildLayout.html)Provides access to important locations for a Gradle build.
[`Script`](https://docs.gradle.org/dsl/org.gradle.api.Script.html)This interface is implemented by all Gradle Groovy DSL scripts to add in some Gradle-specific methods. As your compiled script class will implement this interface, you can use the methods and properties declared by this interface directly in your script.
[`SourceSet`](https://docs.gradle.org/dsl/org.gradle.api.tasks.SourceSet.html)A `SourceSet` represents a logical group of Java source and resource files. They are covered in more detail in the [user manual](https://docs.gradle.org/current/userguide/building_java_projects.html#sec:java_source_sets).
[`SourceSetOutput`](https://docs.gradle.org/dsl/org.gradle.api.tasks.SourceSetOutput.html)A collection of all output directories (compiled classes, processed resources, etc.) - notice that [`SourceSetOutput`](https://docs.gradle.org/dsl/org.gradle.api.tasks.SourceSetOutput.html) extends [`FileCollection`](https://docs.gradle.org/javadoc/org/gradle/api/file/FileCollection.html).
[`SourceDirectorySet`](https://docs.gradle.org/dsl/org.gradle.api.file.SourceDirectorySet.html)A `SourceDirectorySet` represents a set of source files composed from a set of source directories, along with associated include and exclude patterns.
[`Configuration`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.Configuration.html)A `Configuration` represents a group of artifacts and their dependencies. Find more information about declaring dependencies to a configuration or about managing configurations in docs for [`ConfigurationContainer`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.ConfigurationContainer.html)
[`ConsumableConfiguration`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.ConsumableConfiguration.html)A [`Configuration`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.Configuration.html) which can be consumed via Publishing and Dependency Management.
[`ResolvableConfiguration`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.ResolvableConfiguration.html)A [`Configuration`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.Configuration.html) which performs dependency resolution to build dependency graphs and resolve artifacts.
[`DependencyScopeConfiguration`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.DependencyScopeConfiguration.html)A [`Configuration`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.Configuration.html) which collects dependencies, dependency constraints, and exclude rules.
[`ResolutionStrategy`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.ResolutionStrategy.html)Defines the strategies around dependency resolution. For example, forcing certain dependency versions, substitutions, conflict resolutions or snapshot timeouts.
[`ArtifactResolutionQuery`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.query.ArtifactResolutionQuery.html)A builder to construct a query that can resolve selected software artifacts of the specified components.
[`ComponentSelection`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.ComponentSelection.html)Represents a tuple of the component selector of a module and a candidate version to be evaluated in a component selection rule.
[`ComponentSelectionRules`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.ComponentSelectionRules.html)Represents a container for component selection rules. Rules can be applied as part of the resolutionStrategy of a configuration and individual components can be explicitly accepted or rejected by rule. Components that are neither accepted or rejected will be subject to the default version matching strategies.
[`DependencyCollector`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.DependencyCollector.html)A `DependencyCollector` is used as part of a dependencies block in the DSL. A collector implements a single dependency scope and exposes the declared dependencies on [`DependencyCollector.getDependencies()`](https://docs.gradle.org/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html#getDependencies--).
[`ExtensionAware`](https://docs.gradle.org/dsl/org.gradle.api.plugins.ExtensionAware.html)Objects that can be extended at runtime with other objects.
[`ExtraPropertiesExtension`](https://docs.gradle.org/dsl/org.gradle.api.plugins.ExtraPropertiesExtension.html)Additional, ad-hoc, properties for Gradle domain objects.
[`PluginDependenciesSpec`](https://docs.gradle.org/dsl/org.gradle.plugin.use.PluginDependenciesSpec.html)The DSL for declaring plugins to use in a script.
[`PluginDependencySpec`](https://docs.gradle.org/dsl/org.gradle.plugin.use.PluginDependencySpec.html)A mutable specification of a dependency on a plugin.
[`PluginManagementSpec`](https://docs.gradle.org/dsl/org.gradle.plugin.management.PluginManagementSpec.html)Configures how plugins are resolved.
[`ProviderFactory`](https://docs.gradle.org/dsl/org.gradle.api.provider.ProviderFactory.html)A factory for creating instances of [`Provider`](https://docs.gradle.org/javadoc/org/gradle/api/provider/Provider.html).
[`ResourceHandler`](https://docs.gradle.org/dsl/org.gradle.api.resources.ResourceHandler.html)Provides access to resource-specific utility methods, for example factory methods that create various resources.
[`TextResourceFactory`](https://docs.gradle.org/dsl/org.gradle.api.resources.TextResourceFactory.html)Creates `TextResource`s backed by sources such as strings, files, and archive entries.
[`InputChanges`](https://docs.gradle.org/dsl/org.gradle.work.InputChanges.html)Provides access to any input files that need to be processed by an incremental work action.
[`Distribution`](https://docs.gradle.org/dsl/org.gradle.api.distribution.Distribution.html)A distribution allows to bundle an application or a library including dependencies, sources...

[](https://docs.gradle.org/dsl/index.html#N10224)Publishing types
-----------------------------------------------------------------

Listed below are the types used to configure publishing:

Type Description
[`PublishingExtension`](https://docs.gradle.org/dsl/org.gradle.api.publish.PublishingExtension.html)The configuration of how to "publish" the different components of a project.
[`IvyPublication`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyPublication.html)An `IvyPublication` is the representation/configuration of how Gradle should publish something in Ivy format, to an Ivy repository. You directly add a named Ivy publication the project's `publishing.publications` container by providing [`IvyPublication`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyPublication.html) as the type.
[`IvyArtifact`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyArtifact.html)An artifact published as part of a [`IvyPublication`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyPublication.html).
[`IvyArtifactSet`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyArtifactSet.html)A Collection of [`IvyArtifact`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyArtifact.html)s to be included in an [`IvyPublication`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyPublication.html). Being a [`DomainObjectSet`](https://docs.gradle.org/javadoc/org/gradle/api/DomainObjectSet.html), an `IvyArtifactSet` provides convenient methods for querying, filtering, and applying actions to the set of [`IvyArtifact`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyArtifact.html)s.
[`IvyModuleDescriptorSpec`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyModuleDescriptorSpec.html)The descriptor of any Ivy publication.
[`IvyModuleDescriptorAuthor`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyModuleDescriptorAuthor.html)An author of an Ivy publication.
[`IvyModuleDescriptorLicense`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyModuleDescriptorLicense.html)A license of an Ivy publication.
[`IvyModuleDescriptorDescription`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.IvyModuleDescriptorDescription.html)The description of an Ivy publication.
[`MavenPublication`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPublication.html)A `MavenPublication` is the representation/configuration of how Gradle should publish something in Maven format. You directly add a named Maven publication the project's `publishing.publications` container by providing [`MavenPublication`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPublication.html) as the type.
[`MavenArtifact`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenArtifact.html)An artifact published as part of a [`MavenPublication`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPublication.html).
[`MavenArtifactSet`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenArtifactSet.html)A Collection of [`MavenArtifact`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenArtifact.html)s to be included in a [`MavenPublication`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPublication.html). Being a [`DomainObjectSet`](https://docs.gradle.org/javadoc/org/gradle/api/DomainObjectSet.html), a `MavenArtifactSet` provides convenient methods for querying, filtering, and applying actions to the set of [`MavenArtifact`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenArtifact.html)s.
[`MavenPom`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPom.html)The POM for a Maven publication.
[`MavenPomCiManagement`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomCiManagement.html)The CI management system of a Maven publication.
[`MavenPomContributor`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomContributor.html)A contributor of a Maven publication.
[`MavenPomContributorSpec`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomContributorSpec.html)Allows to add contributors of a Maven publication.
[`MavenPomDeveloper`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomDeveloper.html)A developer of a Maven publication.
[`MavenPomDeveloperSpec`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomDeveloperSpec.html)Allows to add developers to a Maven publication.
[`MavenPomDistributionManagement`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomDistributionManagement.html)The distribution management configuration of a Maven publication.
[`MavenPomIssueManagement`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomIssueManagement.html)The issue management system of a Maven publication.
[`MavenPomLicense`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomLicense.html)A license of a Maven publication.
[`MavenPomLicenseSpec`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomLicenseSpec.html)Allows to add licenses to a Maven publication.
[`MavenPomMailingList`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomMailingList.html)A mailing list of a Maven publication.
[`MavenPomMailingListSpec`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomMailingListSpec.html)Allows to add mailing lists to a Maven publication.
[`MavenPomOrganization`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomOrganization.html)The organization of a Maven publication.
[`MavenPomRelocation`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomRelocation.html)The relocation information of a Maven publication that has been moved to a new group and/or artifact ID.
[`MavenPomScm`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPomScm.html)The SCM (source control management) of a Maven publication.

[](https://docs.gradle.org/dsl/index.html#N1036B)Container types
----------------------------------------------------------------

Container types that handle various declarative elements (e.g. dependencies, configurations, artifacts, tasks, etc.):

Type Description
[`TaskContainer`](https://docs.gradle.org/dsl/org.gradle.api.tasks.TaskContainer.html)A `TaskContainer` is responsible for managing a set of [`Task`](https://docs.gradle.org/dsl/org.gradle.api.Task.html) instances.
[`ConfigurationContainer`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.ConfigurationContainer.html)A `ConfigurationContainer` is responsible for declaring and managing configurations. See also [`Configuration`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.Configuration.html).
[`RepositoryHandler`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.RepositoryHandler.html)A `RepositoryHandler` manages a set of repositories, allowing repositories to be defined and queried.
[`DependencyHandler`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.DependencyHandler.html)A `DependencyHandler` is used to declare dependencies. Dependencies are grouped into configurations (see [`Configuration`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.Configuration.html)).
[`ComponentMetadataHandler`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.ComponentMetadataHandler.html)Allows the build to provide rules that modify the metadata of software components resolved from external repositories. Component metadata rules are applied in the components section of the dependencies block [`DependencyHandler`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.DependencyHandler.html) of a build script. The rules can be defined in two different ways:
[`ArtifactHandler`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.ArtifactHandler.html)This class is for defining artifacts to be published and adding them to configurations. Creating publish artifacts does not mean to create an archive. What is created is a domain object which represents a file to be published and information on how it should be published (e.g. the name).

[](https://docs.gradle.org/dsl/index.html#N103D0)Authentication types
---------------------------------------------------------------------

Credentials and Authentication types for connecting to repositories:

Type Description
[`AuthenticationSupported`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.repositories.AuthenticationSupported.html)An artifact repository which supports username/password authentication.
[`Credentials`](https://docs.gradle.org/dsl/org.gradle.api.credentials.Credentials.html)Base interface for credentials used for different authentication purposes. (e.g authenticated [`RepositoryHandler`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.RepositoryHandler.html))
[`PasswordCredentials`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.repositories.PasswordCredentials.html)A username/password credentials that can be used to login to password-protected remote repository.
[`AwsCredentials`](https://docs.gradle.org/dsl/org.gradle.api.credentials.AwsCredentials.html)Represents credentials used to authenticate with Amazon Web Services.
[`HttpHeaderCredentials`](https://docs.gradle.org/dsl/org.gradle.api.credentials.HttpHeaderCredentials.html)Credentials that can be used to login to a protected server, e.g. a remote repository by using HTTP header. The properties used for creating credentials from a property are `repoAuthHeaderName` and `repoAuthHeaderValue`, where `repo` is the identity of the repository.
[`AuthenticationContainer`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.repositories.AuthenticationContainer.html)Container for configuring repository authentication schemes of type [`Authentication`](https://docs.gradle.org/dsl/org.gradle.authentication.Authentication.html).
[`Authentication`](https://docs.gradle.org/dsl/org.gradle.authentication.Authentication.html)Base interface for transport authentication schemes.
[`BasicAuthentication`](https://docs.gradle.org/dsl/org.gradle.authentication.http.BasicAuthentication.html)Authentication scheme for basic access authentication over HTTP. When using this scheme, credentials are sent preemptively.
[`HttpHeaderAuthentication`](https://docs.gradle.org/dsl/org.gradle.authentication.http.HttpHeaderAuthentication.html)Authentication scheme for HTTP header authentication over HTTP.
[`DigestAuthentication`](https://docs.gradle.org/dsl/org.gradle.authentication.http.DigestAuthentication.html)Authentication scheme for digest access authentication over HTTP.

[](https://docs.gradle.org/dsl/index.html#N1044D)Build Cache types
------------------------------------------------------------------

Types used to connect to and configure the build cache:

Type Description
[`BuildCacheConfiguration`](https://docs.gradle.org/dsl/org.gradle.caching.configuration.BuildCacheConfiguration.html)Configuration for the [build cache](https://docs.gradle.org/current/userguide/build_cache.html) for an entire Gradle build.
[`DirectoryBuildCache`](https://docs.gradle.org/dsl/org.gradle.caching.local.DirectoryBuildCache.html)Configuration object for the local directory build cache.
[`HttpBuildCache`](https://docs.gradle.org/dsl/org.gradle.caching.http.HttpBuildCache.html)Configuration object for the HTTP build cache. Cache entries are loaded via GET and stored via PUT requests.

[](https://docs.gradle.org/dsl/index.html#N1047B)Input Normalization types
--------------------------------------------------------------------------

Types used to configure input normalization

Type Description
[`InputNormalizationHandler`](https://docs.gradle.org/dsl/org.gradle.normalization.InputNormalizationHandler.html)Used to configure input normalization. Currently, it is only possible to configure runtime classpath normalization.
[`InputNormalization`](https://docs.gradle.org/dsl/org.gradle.normalization.InputNormalization.html)Input normalization configuration. Input normalization is used when Gradle tries to determine if two task inputs are different. Gradle normalizes both inputs and the inputs are considered different if and only if the normalizations are different.
[`RuntimeClasspathNormalization`](https://docs.gradle.org/dsl/org.gradle.normalization.RuntimeClasspathNormalization.html)Configuration of runtime classpath normalization.

[](https://docs.gradle.org/dsl/index.html#N104A5)Help Task types
----------------------------------------------------------------

Below are the task types that are available for every Gradle project. Those task types can also be declared and configured directly in the build script.

Type Description
[`TaskReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.TaskReportTask.html)Displays a list of tasks in the project. An instance of this type is used when you execute the `tasks` task from the command-line.
[`ProjectReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.ProjectReportTask.html)Displays a list of projects in the build. An instance of this type is used when you execute the `projects` task from the command-line.
[`DependencyReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.DependencyReportTask.html)Displays the dependency tree for a project. An instance of this type is used when you execute the `dependencies` task from the command-line.
[`DependencyInsightReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.DependencyInsightReportTask.html)Generates a report that attempts to answer questions like:
[`PropertyReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.PropertyReportTask.html)Displays the properties of a project. An instance of this type is used when you execute the `properties` task from the command-line.
[`ComponentReport`](https://docs.gradle.org/dsl/org.gradle.api.reporting.components.ComponentReport.html)Displays some details about the software components produced by the project.
[`DependentComponentsReport`](https://docs.gradle.org/dsl/org.gradle.api.reporting.dependents.DependentComponentsReport.html)Displays dependent components.
[`ModelReport`](https://docs.gradle.org/dsl/org.gradle.api.reporting.model.ModelReport.html)Displays some details about the configuration model of the project. An instance of this type is used when you execute the `model` task from the command-line.
[`OutgoingVariantsReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.OutgoingVariantsReportTask.html)A task which reports the outgoing variants of a project on the command line. This is useful for listing what a project produces in terms of variants and what artifacts are attached to each variant. Variants, in this context, must be understood as "things produced by a project which can safely be consumed by another project".
[`ResolvableConfigurationsReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.ResolvableConfigurationsReportTask.html)A task which reports the configurations of a project which can be resolved on the command line. This is useful for determining which attributes are associated with the resolvable configurations being used to resolve a project's dependencies. The output can help predict which variant of each dependency will be resolved.
[`ArtifactTransformsReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.ArtifactTransformsReportTask.html)A task which reports information about the Artifact Transforms (implemented by [`TransformAction`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.transform.TransformAction.html)) used by a project. This is useful for investigating ambiguous transformation scenarios. The output can help predict which transforms will need to be modified to remove ambiguity.

[](https://docs.gradle.org/dsl/index.html#N1052B)Task types
-----------------------------------------------------------

Listed below are the various task types which are available for use in your build script:

Type Description
[`AntlrTask`](https://docs.gradle.org/dsl/org.gradle.api.plugins.antlr.AntlrTask.html)Generates parsers from Antlr grammars.
[`BuildEnvironmentReportTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.diagnostics.BuildEnvironmentReportTask.html)Provides information about the build environment for the project that the task is associated with.
[`Checkstyle`](https://docs.gradle.org/dsl/org.gradle.api.plugins.quality.Checkstyle.html)Runs Checkstyle against some source files.
[`CodeNarc`](https://docs.gradle.org/dsl/org.gradle.api.plugins.quality.CodeNarc.html)Runs CodeNarc against some source files.
[`Copy`](https://docs.gradle.org/dsl/org.gradle.api.tasks.Copy.html)Copies files into a destination directory. This task can also rename and filter files as it copies. The task implements [`CopySpec`](https://docs.gradle.org/javadoc/org/gradle/api/file/CopySpec.html) for specifying what to copy.
[`CreateStartScripts`](https://docs.gradle.org/dsl/org.gradle.jvm.application.tasks.CreateStartScripts.html)Creates start scripts for launching JVM applications.
[`Delete`](https://docs.gradle.org/dsl/org.gradle.api.tasks.Delete.html)Deletes files or directories. Example:
[`Ear`](https://docs.gradle.org/dsl/org.gradle.plugins.ear.Ear.html)Assembles an EAR archive.
[`Exec`](https://docs.gradle.org/dsl/org.gradle.api.tasks.Exec.html)Executes a command line process. Example:
[`GenerateIvyDescriptor`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.tasks.GenerateIvyDescriptor.html)Generates an Ivy XML Module Descriptor file.
[`GenerateMavenPom`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.tasks.GenerateMavenPom.html)Generates a Maven module descriptor (POM) file.
[`GenerateBuildDashboard`](https://docs.gradle.org/dsl/org.gradle.api.reporting.GenerateBuildDashboard.html)Generates build dashboard report.
[`GradleBuild`](https://docs.gradle.org/dsl/org.gradle.api.tasks.GradleBuild.html)Executes a Gradle build.
[`GroovyCompile`](https://docs.gradle.org/dsl/org.gradle.api.tasks.compile.GroovyCompile.html)Compiles Groovy source files, and optionally, Java source files.
[`Groovydoc`](https://docs.gradle.org/dsl/org.gradle.api.tasks.javadoc.Groovydoc.html)Generates HTML API documentation for Groovy source, and optionally, Java source.
[`HtmlDependencyReportTask`](https://docs.gradle.org/dsl/org.gradle.api.reporting.dependencies.HtmlDependencyReportTask.html)Generates an HTML dependency report. This report combines the features of the ASCII dependency report and those of the ASCII dependency insight report. For a given project, it generates a tree of the dependencies of every configuration, and each dependency can be clicked to show the insight of this dependency.
[`JacocoReport`](https://docs.gradle.org/dsl/org.gradle.testing.jacoco.tasks.JacocoReport.html)Task to generate HTML, Xml and CSV reports of Jacoco coverage data.
[`JacocoCoverageVerification`](https://docs.gradle.org/dsl/org.gradle.testing.jacoco.tasks.JacocoCoverageVerification.html)Task for verifying code coverage metrics. Fails the task if violations are detected based on specified rules.
[`Jar`](https://docs.gradle.org/dsl/org.gradle.api.tasks.bundling.Jar.html)Assembles a JAR archive.
[`JavaCompile`](https://docs.gradle.org/dsl/org.gradle.api.tasks.compile.JavaCompile.html)Compiles Java source files.
[`Javadoc`](https://docs.gradle.org/dsl/org.gradle.api.tasks.javadoc.Javadoc.html)Generates HTML API documentation for Java classes.
[`JavaExec`](https://docs.gradle.org/dsl/org.gradle.api.tasks.JavaExec.html)Executes a Java application in a child process.
[`Pmd`](https://docs.gradle.org/dsl/org.gradle.api.plugins.quality.Pmd.html)Runs a set of static code analysis rules on Java source code files and generates a report of problems found.
[`ProcessResources`](https://docs.gradle.org/dsl/org.gradle.language.jvm.tasks.ProcessResources.html)Copies resources from their source to their target directory, potentially processing them. Makes sure no stale resources remain in the target directory.
[`PublishToIvyRepository`](https://docs.gradle.org/dsl/org.gradle.api.publish.ivy.tasks.PublishToIvyRepository.html)Publishes an IvyPublication to an IvyArtifactRepository.
[`PublishToMavenRepository`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.tasks.PublishToMavenRepository.html)Publishes a [`MavenPublication`](https://docs.gradle.org/dsl/org.gradle.api.publish.maven.MavenPublication.html) to a [`MavenArtifactRepository`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.repositories.MavenArtifactRepository.html).
[`ScalaCompile`](https://docs.gradle.org/dsl/org.gradle.api.tasks.scala.ScalaCompile.html)Compiles Scala source files, and optionally, Java source files.
[`ScalaDoc`](https://docs.gradle.org/dsl/org.gradle.api.tasks.scala.ScalaDoc.html)Generates HTML API documentation for Scala source files.
[`UpdateDaemonJvm`](https://docs.gradle.org/dsl/org.gradle.buildconfiguration.tasks.UpdateDaemonJvm.html)Generates or updates the Gradle Daemon JVM criteria. This controls the version of the JVM required to run the Gradle Daemon.
[`InitBuild`](https://docs.gradle.org/dsl/org.gradle.buildinit.tasks.InitBuild.html)Generates a Gradle project structure.
[`Sign`](https://docs.gradle.org/dsl/org.gradle.plugins.signing.Sign.html)A task for creating digital signature files for one or more; tasks, files, publishable artifacts or configurations.
[`Sync`](https://docs.gradle.org/dsl/org.gradle.api.tasks.Sync.html)Synchronizes the contents of a destination directory with some source directories and files.
[`Tar`](https://docs.gradle.org/dsl/org.gradle.api.tasks.bundling.Tar.html)Assembles a TAR archive.
[`AbstractTestTask`](https://docs.gradle.org/dsl/org.gradle.api.tasks.testing.AbstractTestTask.html)Abstract class for all test tasks.
[`Test`](https://docs.gradle.org/dsl/org.gradle.api.tasks.testing.Test.html)Executes JUnit (3.8.x, 4.x or 5.x) or TestNG tests. Test are always run in (one or more) separate JVMs.
[`TestReport`](https://docs.gradle.org/dsl/org.gradle.api.tasks.testing.TestReport.html)Generates an HTML test report from the results of one or more [`Test`](https://docs.gradle.org/dsl/org.gradle.api.tasks.testing.Test.html) tasks.
[`War`](https://docs.gradle.org/dsl/org.gradle.api.tasks.bundling.War.html)Assembles a WAR archive.
[`Wrapper`](https://docs.gradle.org/dsl/org.gradle.api.tasks.wrapper.Wrapper.html)Generates scripts (for *nix and windows) which allow you to build your project with Gradle, without having to install Gradle.
[`WriteProperties`](https://docs.gradle.org/dsl/org.gradle.api.tasks.WriteProperties.html)Writes a [`Properties`](https://docs.oracle.com/javase/8/docs/api/java/util/Properties.html) in a way that the results can be expected to be reproducible.
[`Zip`](https://docs.gradle.org/dsl/org.gradle.api.tasks.bundling.Zip.html)Assembles a ZIP archive. The default is to compress the contents of the zip.

[](https://docs.gradle.org/dsl/index.html#N106BB)Test types
-----------------------------------------------------------

Listed below are the tasks and configurable objects related to modeled Test Suites:

Type Description
[`TestingExtension`](https://docs.gradle.org/dsl/org.gradle.testing.base.TestingExtension.html)This DSL element exists to contain a collection of [`TestSuite`](https://docs.gradle.org/dsl/org.gradle.testing.base.TestSuite.html)s.
[`TestSuite`](https://docs.gradle.org/dsl/org.gradle.testing.base.TestSuite.html)Base test suite component. A test suite is a collection of tests.
[`JvmTestSuite`](https://docs.gradle.org/dsl/org.gradle.api.plugins.jvm.JvmTestSuite.html)A test suite is a collection of JVM-based tests.
[`TestSuiteTarget`](https://docs.gradle.org/dsl/org.gradle.testing.base.TestSuiteTarget.html)Base test suite target. A test suite target is a collection of tests that run in a particular context (operating system, Java runtime, etc).
[`JvmTestSuiteTarget`](https://docs.gradle.org/dsl/org.gradle.api.plugins.jvm.JvmTestSuiteTarget.html)Defines the target environment against which a [`JvmTestSuite`](https://docs.gradle.org/dsl/org.gradle.api.plugins.jvm.JvmTestSuite.html) will be run.
[`Test`](https://docs.gradle.org/dsl/org.gradle.api.tasks.testing.Test.html)Executes JUnit (3.8.x, 4.x or 5.x) or TestNG tests. Test are always run in (one or more) separate JVMs.
[`Dependencies`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.Dependencies.html)Universal APIs that are available for all `dependencies` blocks.
[`GradleDependencies`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.dsl.GradleDependencies.html)Dependency APIs available for `dependencies` blocks that can build software that relies on Gradle APIs.
[`TestFixturesDependencyModifiers`](https://docs.gradle.org/dsl/org.gradle.api.plugins.jvm.TestFixturesDependencyModifiers.html)Dependency modifier APIs that can find test fixtures in other modules for `dependencies` blocks.
[`PlatformDependencyModifiers`](https://docs.gradle.org/dsl/org.gradle.api.plugins.jvm.PlatformDependencyModifiers.html)Dependency modifier APIs that can find platform and enforced platforms in other modules for `dependencies` blocks.
[`JvmComponentDependencies`](https://docs.gradle.org/dsl/org.gradle.api.plugins.jvm.JvmComponentDependencies.html)This DSL element is used to add dependencies to a component, for instance a [`TestSuite`](https://docs.gradle.org/dsl/org.gradle.testing.base.TestSuite.html)

[](https://docs.gradle.org/dsl/index.html#N10748)Reporting types
----------------------------------------------------------------

Listed below are some of the types which are used when generating reports:

Type Description
[`CustomizableHtmlReport`](https://docs.gradle.org/dsl/org.gradle.api.reporting.CustomizableHtmlReport.html)A HTML Report whose generation can be customized with a XSLT stylesheet.
[`SingleFileReport`](https://docs.gradle.org/dsl/org.gradle.api.reporting.SingleFileReport.html)A report that is a single file.
[`DirectoryReport`](https://docs.gradle.org/dsl/org.gradle.api.reporting.DirectoryReport.html)A directory based report to be created.
[`Report`](https://docs.gradle.org/dsl/org.gradle.api.reporting.Report.html)A file based report to be created.
[`Reporting`](https://docs.gradle.org/dsl/org.gradle.api.reporting.Reporting.html)An object that provides reporting options.
[`ReportContainer`](https://docs.gradle.org/dsl/org.gradle.api.reporting.ReportContainer.html)A container of [`Report`](https://docs.gradle.org/dsl/org.gradle.api.reporting.Report.html) objects, that represent potential reports.
[`ReportingExtension`](https://docs.gradle.org/dsl/org.gradle.api.reporting.ReportingExtension.html)A project extension named "reporting" that provides basic reporting settings and utilities.
[`AggregateTestReport`](https://docs.gradle.org/dsl/org.gradle.api.tasks.testing.AggregateTestReport.html)A container for the inputs of an aggregated test report.
[`JacocoCoverageReport`](https://docs.gradle.org/dsl/org.gradle.testing.jacoco.plugins.JacocoCoverageReport.html)A container for the inputs of an aggregated JaCoCo code coverage report.

[](https://docs.gradle.org/dsl/index.html#N107AD)Eclipse/IDEA model types
-------------------------------------------------------------------------

Used to configure Eclipse or IDEA plugins

Type Description
[`EclipseModel`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseModel.html)DSL-friendly model of the Eclipse project information. First point of entry for customizing Eclipse project generation.
[`EclipseProject`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseProject.html)Enables fine-tuning project details (.project file) of the Eclipse plugin
[`EclipseClasspath`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseClasspath.html)The build path settings for the generated Eclipse project. Used by the [`GenerateEclipseClasspath`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.GenerateEclipseClasspath.html) task to generate an Eclipse .classpath file.
[`EclipseJdt`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseJdt.html)Enables fine-tuning jdt details of the Eclipse plugin
[`EclipseWtp`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseWtp.html)Enables fine-tuning wtp/wst details of the Eclipse plugin
[`EclipseWtpComponent`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseWtpComponent.html)Enables fine-tuning wtp component details of the Eclipse plugin
[`EclipseWtpFacet`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.model.EclipseWtpFacet.html)Enables fine-tuning wtp facet details of the Eclipse plugin
[`IdeaModel`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.model.IdeaModel.html)DSL-friendly model of the IDEA project information. First point of entry when it comes to customizing the IDEA generation.
[`IdeaProject`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.model.IdeaProject.html)Enables fine-tuning project details (_.ipr file) of the IDEA plugin.
[`IdeaModule`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.model.IdeaModule.html)Enables fine-tuning module details (_.iml file) of the IDEA plugin.
[`IdeaWorkspace`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.model.IdeaWorkspace.html)Enables fine-tuning workspace details (*.iws file) of the IDEA plugin.
[`XmlFileContentMerger`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.api.XmlFileContentMerger.html)Models the generation/parsing/merging capabilities. Adds XML-related hooks.
[`FileContentMerger`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.api.FileContentMerger.html)Models the generation/parsing/merging capabilities.

[](https://docs.gradle.org/dsl/index.html#N10836)Eclipse/IDEA task types
------------------------------------------------------------------------

Tasks contributed by IDE plugins. To configure IDE plugins please use IDE model types.

Type Description
[`GenerateEclipseProject`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.GenerateEclipseProject.html)Generates an Eclipse `.project` file. If you want to fine tune the eclipse configuration
[`GenerateEclipseClasspath`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.GenerateEclipseClasspath.html)Generates an Eclipse `.classpath` file. If you want to fine tune the eclipse configuration
[`GenerateEclipseJdt`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.GenerateEclipseJdt.html)Generates the Eclipse JDT configuration file. If you want to fine tune the eclipse configuration
[`GenerateEclipseWtpComponent`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.GenerateEclipseWtpComponent.html)Generates the org.eclipse.wst.common.component settings file for Eclipse WTP. If you want to fine tune the eclipse configuration
[`GenerateEclipseWtpFacet`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.eclipse.GenerateEclipseWtpFacet.html)Generates the org.eclipse.wst.common.project.facet.core settings file for Eclipse WTP. If you want to fine tune the eclipse configuration
[`GenerateIdeaModule`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.GenerateIdeaModule.html)Generates an IDEA module file. If you want to fine tune the idea configuration
[`GenerateIdeaProject`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.GenerateIdeaProject.html)Generates an IDEA project file for root project _only_. If you want to fine tune the idea configuration
[`GenerateIdeaWorkspace`](https://docs.gradle.org/dsl/org.gradle.plugins.ide.idea.GenerateIdeaWorkspace.html)Generates an IDEA workspace file _only_ for root project. There's little you can configure about workspace generation at the moment.

[](https://docs.gradle.org/dsl/index.html#N10893)Xcode task types
-----------------------------------------------------------------

Tasks contributed by Xcode IDE plugins. To configure IDE plugins please use IDE model types.

Type Description
[`GenerateSchemeFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.xcode.tasks.GenerateSchemeFileTask.html)Task for generating a Xcode scheme file (e.g. `Foo.xcodeproj/xcshareddata/xcschemes/Foo.xcscheme`). An Xcode scheme defines a collection of targets to build, a configuration to use when building, and a collection of tests to execute.
[`GenerateWorkspaceSettingsFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.xcode.tasks.GenerateWorkspaceSettingsFileTask.html)Task for generating a Xcode workspace settings file (e.g. `Foo.xcodeproj/project.xcworkspace/xcshareddata/WorkspaceSettings.xcsettings`).
[`GenerateXcodeProjectFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.xcode.tasks.GenerateXcodeProjectFileTask.html)Task for generating a Xcode project file (e.g. `Foo.xcodeproj/project.pbxproj`). A project contains all the elements used to build your products and maintains the relationships between those elements. It contains one or more targets, which specify how to build products. A project defines default build settings for all the targets in the project (each target can also specify its own build settings, which override the project build settings).
[`GenerateXcodeWorkspaceFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.xcode.tasks.GenerateXcodeWorkspaceFileTask.html)Task for generating a Xcode workspace file (e.g. `Foo.xcworkspace/contents.xcworkspacedata`). A workspace can contain any number of Xcode projects.

[](https://docs.gradle.org/dsl/index.html#N108D2)Visual Studio task types
-------------------------------------------------------------------------

Tasks contributed by Visual Studio IDE plugins. To configure IDE plugins please use IDE model types.

Type Description
[`GenerateSolutionFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.visualstudio.tasks.GenerateSolutionFileTask.html)Task for generating a Visual Studio solution file (e.g. `foo.sln`).
[`GenerateProjectFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.visualstudio.tasks.GenerateProjectFileTask.html)Task for generating a Visual Studio project file (e.g. `foo.vcxproj`).
[`GenerateFiltersFileTask`](https://docs.gradle.org/dsl/org.gradle.ide.visualstudio.tasks.GenerateFiltersFileTask.html)Task for generating a Visual Studio filters file (e.g. `foo.vcxproj.filters`).

[](https://docs.gradle.org/dsl/index.html#N10905)Artifact transform types
-------------------------------------------------------------------------

Used to define artifact transforms.

Type Description
[`TransformAction`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.transform.TransformAction.html)Interface for artifact transform actions.
[`TransformOutputs`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.transform.TransformOutputs.html)The outputs of the artifact transform.
[`TransformSpec`](https://docs.gradle.org/dsl/org.gradle.api.artifacts.transform.TransformSpec.html)Base configuration for artifact transform registrations.

[](https://docs.gradle.org/dsl/index.html#N1092F)Native tool chains model types
-------------------------------------------------------------------------------

Used to configure tool chains for building C++ and Swift components.

Type Description
[`Gcc`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.toolchain.Gcc.html)The [GNU GCC](http://gcc.gnu.org/) tool chain.
[`Clang`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.toolchain.Clang.html)The [Clang](http://clang.llvm.org/) tool chain.
[`VisualCpp`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.toolchain.VisualCpp.html)The Visual C++ tool chain.
[`Swiftc`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.toolchain.Swiftc.html)The [Swift Compiler](https://swift.org/) tool chain.

[](https://docs.gradle.org/dsl/index.html#N1096E)Native software model types
----------------------------------------------------------------------------

Used to configure software components developed with native code.

Type Description
[`PrebuiltLibrary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.PrebuiltLibrary.html)A library component that is not built by gradle.
[`PrebuiltSharedLibraryBinary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.PrebuiltSharedLibraryBinary.html)A shared library that exists at a known location on the filesystem.
[`PrebuiltStaticLibraryBinary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.PrebuiltStaticLibraryBinary.html)A static library that exists at a known location on the filesystem.
[`NativeComponentSpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeComponentSpec.html)Definition of a software component that is to be built by Gradle to run a on JVM platform.
[`NativeExecutableSpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeExecutableSpec.html)Definition of a native executable component that is to be built by Gradle.
[`NativeLibrarySpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeLibrarySpec.html)Definition of a native library component that is to be built by Gradle.
[`NativeTestSuiteSpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.NativeTestSuiteSpec.html)A component representing a suite of tests that will be executed together.
[`CUnitTestSuiteSpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.cunit.CUnitTestSuiteSpec.html)Test suite of CUnit tests.
[`GoogleTestTestSuiteSpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.googletest.GoogleTestTestSuiteSpec.html)Test suite of Google Test tests.
[`NativeBinarySpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeBinarySpec.html)Represents a binary artifact that is the result of building a native component.
[`NativeExecutableBinarySpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeExecutableBinarySpec.html)An binary built by Gradle for a native application.
[`NativeLibraryBinarySpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeLibraryBinarySpec.html)Represents a binary artifact that is the result of building a native library component.
[`SharedLibraryBinarySpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.SharedLibraryBinarySpec.html)A shared library binary built by Gradle for a native library.
[`StaticLibraryBinarySpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.StaticLibraryBinarySpec.html)A static library binary built by Gradle for a native library.
[`NativeTestSuiteBinarySpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.NativeTestSuiteBinarySpec.html)An executable which runs a suite of tests.
[`CUnitTestSuiteBinarySpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.cunit.CUnitTestSuiteBinarySpec.html)An executable which run a CUnit test suite.
[`GoogleTestTestSuiteBinarySpec`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.googletest.GoogleTestTestSuiteBinarySpec.html)An executable which run a Google Test test suite.
[`NativePlatform`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.platform.NativePlatform.html)A target platform for building native binaries. Each target platform is given a name, and may optionally be given a specific [`Architecture`](https://docs.gradle.org/javadoc/org/gradle/nativeplatform/platform/Architecture.html) and/or [`OperatingSystem`](https://docs.gradle.org/javadoc/org/gradle/nativeplatform/platform/OperatingSystem.html) to target.
[`BuildType`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.BuildType.html)Specifies a build-type for a native binary. Common build types are 'debug' and 'release', but others may be defined.
[`Flavor`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.Flavor.html)Defines a custom variant that differentiate a [`NativeBinary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeBinary.html).
[`AssemblerSourceSet`](https://docs.gradle.org/dsl/org.gradle.language.assembler.AssemblerSourceSet.html)A set of assembly language sources.
[`CSourceSet`](https://docs.gradle.org/dsl/org.gradle.language.c.CSourceSet.html)A set of C source files.
[`CppSourceSet`](https://docs.gradle.org/dsl/org.gradle.language.cpp.CppSourceSet.html)A set of C++ source files.
[`ObjectiveCSourceSet`](https://docs.gradle.org/dsl/org.gradle.language.objectivec.ObjectiveCSourceSet.html)A set of Objective-C source files.
[`ObjectiveCppSourceSet`](https://docs.gradle.org/dsl/org.gradle.language.objectivecpp.ObjectiveCppSourceSet.html)A set of Objective-C++ source files.
[`WindowsResourceSet`](https://docs.gradle.org/dsl/org.gradle.language.rc.WindowsResourceSet.html)A set of Windows Resource definition files.
[`VisualStudioProject`](https://docs.gradle.org/dsl/org.gradle.ide.visualstudio.VisualStudioProject.html)A visual studio project, created from one or more native binaries.
[`VisualStudioSolution`](https://docs.gradle.org/dsl/org.gradle.ide.visualstudio.VisualStudioSolution.html)A visual studio solution, representing one or more native binaries in a build.
[`NativeExecutable`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeExecutable.html)An executable native component that is built by Gradle.
[`NativeLibrary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeLibrary.html)A library component that is built by a gradle project.
[`NativeBinary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeBinary.html)Represents a particular binary artifact.
[`NativeExecutableBinary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeExecutableBinary.html)A binary artifact for a [`NativeExecutable`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeExecutable.html), targeted at a particular platform with specific configuration.
[`SharedLibraryBinary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.SharedLibraryBinary.html)A [`NativeLibrary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeLibrary.html) that has been compiled and linked as a shared library.
[`StaticLibraryBinary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.StaticLibraryBinary.html)A [`NativeLibrary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.NativeLibrary.html) that has been compiled and archived into a static library.

[](https://docs.gradle.org/dsl/index.html#N10ACE)C++ component model types
--------------------------------------------------------------------------

Used to configure C++ components.

Type Description
[`CppApplication`](https://docs.gradle.org/dsl/org.gradle.language.cpp.CppApplication.html)Configuration for a C++ application, defining the source files that make up the application plus other settings.
[`CppLibrary`](https://docs.gradle.org/dsl/org.gradle.language.cpp.CppLibrary.html)Configuration for a C++ library, defining the source files and header directories that make up the library plus other settings.
[`CppTestSuite`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.cpp.CppTestSuite.html)A C++ test suite.

[](https://docs.gradle.org/dsl/index.html#N10AF8)Swift component model types
----------------------------------------------------------------------------

Used to configure Swift components.

Type Description
[`SwiftApplication`](https://docs.gradle.org/dsl/org.gradle.language.swift.SwiftApplication.html)Configuration for a Swift application, defining the source files that make up the application plus other settings.
[`SwiftLibrary`](https://docs.gradle.org/dsl/org.gradle.language.swift.SwiftLibrary.html)Configuration for a Swift library, defining the source files that make up the library plus other settings.
[`SwiftXCTestSuite`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.xctest.SwiftXCTestSuite.html)A XCTest suite, implemented in Swift.

[](https://docs.gradle.org/dsl/index.html#N10B22)Native binary task types
-------------------------------------------------------------------------

Tasks used to build native binaries.

Type Description
[`CppCompile`](https://docs.gradle.org/dsl/org.gradle.language.cpp.tasks.CppCompile.html)Compiles C++ source files into object files.
[`SwiftCompile`](https://docs.gradle.org/dsl/org.gradle.language.swift.tasks.SwiftCompile.html)Compiles Swift source files into object files.
[`LinkExecutable`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.tasks.LinkExecutable.html)Links a binary executable from object files and libraries.
[`LinkSharedLibrary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.tasks.LinkSharedLibrary.html)Links a binary shared library from object files and imported libraries.
[`CreateStaticLibrary`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.tasks.CreateStaticLibrary.html)Assembles a static library from object files.
[`LinkMachOBundle`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.tasks.LinkMachOBundle.html)Links a binary bundle from object files and imported libraries.
[`InstallExecutable`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.tasks.InstallExecutable.html)Installs an executable with it's dependent libraries so it can be easily executed.
[`InstallXCTestBundle`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.xctest.tasks.InstallXCTestBundle.html)Creates a XCTest bundle with a run script so it can be easily executed.
[`RunTestExecutable`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.tasks.RunTestExecutable.html)Runs a compiled and installed test executable.
[`XCTest`](https://docs.gradle.org/dsl/org.gradle.nativeplatform.test.xctest.tasks.XCTest.html)Executes XCTest tests. Test are always run in a single execution.

[](https://docs.gradle.org/dsl/index.html#N10B8B)Native binary task types
-------------------------------------------------------------------------

Tasks used to build native binaries.

Type Description
[`CCompile`](https://docs.gradle.org/dsl/org.gradle.language.c.tasks.CCompile.html)Compiles C source files into object files.
[`Assemble`](https://docs.gradle.org/dsl/org.gradle.language.assembler.tasks.Assemble.html)Translates Assembly language source files into object files.
[`ObjectiveCCompile`](https://docs.gradle.org/dsl/org.gradle.language.objectivec.tasks.ObjectiveCCompile.html)Compiles Objective-C source files into object files.
[`ObjectiveCppCompile`](https://docs.gradle.org/dsl/org.gradle.language.objectivecpp.tasks.ObjectiveCppCompile.html)Compiles Objective-C++ source files into object files.
[`WindowsResourceCompile`](https://docs.gradle.org/dsl/org.gradle.language.rc.tasks.WindowsResourceCompile.html)Compiles Windows Resource scripts into .res files.

**Docs**

* [User Manual](https://docs.gradle.org/current/userguide/userguide.html)
* [DSL Reference](https://docs.gradle.org/current/dsl/)
* [Release Notes](https://docs.gradle.org/current/release-notes.html)
* [Javadoc](https://docs.gradle.org/current/javadoc/)

**News**

* [Blog](https://blog.gradle.org/)
* [Newsletter](https://newsletter.gradle.org/)
* [Twitter](https://twitter.com/gradle)

**Products**

* [Build Scan®](https://gradle.com/develocity/product/build-scan)
* [Build Cache](https://gradle.com/build-cache)
* [Develocity Docs](https://gradle.com/enterprise/resources)

**Get Help**

* [Forums](https://discuss.gradle.org/c/help-discuss)
* [GitHub](https://github.com/gradle/)
* [Training](https://gradle.org/training/)
* [Services](https://gradle.org/services/)

##### Stay `UP-TO-DATE` on new features and news

By entering your email, you agree to our [Terms](https://gradle.org/terms/) and [Privacy Policy](https://gradle.org/privacy/).

© [Gradle Inc.](https://gradle.com/)2021 All rights reserved.

[](https://docs.gradle.org/)

[Careers](https://gradle.com/careers) | [Privacy](https://gradle.org/privacy) | [Terms of Service](https://gradle.org/terms) | [Contact](https://gradle.org/contact/)

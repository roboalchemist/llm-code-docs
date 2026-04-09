# Crate rpm 
Source 
## Re-exports§
`pub use ::chrono;`
## Modules§
signature
## Structs§
BuildConfigChangelogEntryUser facing accessor type for a changelog entryChecksummingWriterA wrapper for calculating the sha256 checksum of the contents written to itDependencyDescription of a dependency as present in a RPM header record.DependencyFlagsEvrA full RPM “version” specifier has 3 different components - Epoch, Version, and Release.FileCapsFileDigestFileEntryUser facing accessor type for a file entry with contextual informationFileFlagsFileIteratorFileOptionsFileOptionsBuilderFileOwnershipUser facing accessor type representing ownership of a fileFileVerifyFlagsHeaderNevraA full RPM “NEVRA” consists of 5 different components - Name, Epoch, Version, Release, and Architecture.PackageA complete rpm file.PackageBuilderCreate an RPM file by specifying metadata and files using the builder pattern.PackageFileEntryDescribes a file present in the rpm file.PackageMetadataPackageSegmentOffsetsOffsets into an RPM Package (from the start of the file) demarking locations of each sectionRpmFileScriptletDescription of a scriptlet as present in a RPM header recordScriptletFlagsFlags to configure scriptlet execution,SignatureHeaderBuilderbase signature header builderTimestampTimestamp as a number of seconds that have elapsed since
January 1, 1970 (midnight UTC/GMT), not counting leap seconds
(in ISO 8601: 1970-01-01T00:00:00Z).
## Enums§
CompressionTypeSupported payload compression types.CompressionWithLevelSupported compression types, with an associated compression level. This is used for setting
a custom compression configuration during RPM building.CompressorContentSourceDefine rpm content type source, from file path or raw bytes data.DigestAlgorithmErrorFileModeHashKindIndexSignatureTagIndexTagRpmFormatTimestampError
## Constants§
DIR_FILE_TYPEHEADER_I18NTABLEHEADER_IMAGEHEADER_IMMUTABLEHEADER_MAGICheader magic recognition (not the lead!)HEADER_REGIONSHEADER_SIGBASEHEADER_SIGNATURESHEADER_SIGTOPHEADER_TAGBASEINDEX_ENTRY_SIZESize (in bytes) of each entry in the indexINDEX_HEADER_SIZESize (in bytes) of the index header (the fixed portion of each header)LEAD_SIZESize (in bytes) of the package “lead” sectionREGULAR_FILE_TYPERPM_MAGICrpm magic as part of the lead headerSYMBOLIC_LINK_FILE_TYPE
## Traits§
TagHeader tag.
## Functions§
rpm_evr_compareCompare two strings as RPM EVR valuesvalidate_caps_text
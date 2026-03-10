# Source: https://docs.aws.amazon.com/ebs/latest/APIReference/llms.txt

# EBS direct APIs API Reference

> You can use the Amazon Elastic Block Store (Amazon EBS) direct APIs to create Amazon EBS snapshots, write data directly to your snapshots, read data on your snapshots, and identify the differences or changes between two snapshots. If youâre an independent software vendor (ISV) who offers backup services for Amazon EBS, the EBS direct APIs make it more efficient and cost-effective to track incremental changes on your Amazon EBS volumes through snapshots. This can be done without having to create new volumes from snapshots, and then use Amazon Elastic Compute Cloud (Amazon EC2) instances to compare the differences.

- [Welcome](https://docs.aws.amazon.com/ebs/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/ebs/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/ebs/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/ebs/latest/APIReference/API_Operations.html)

- [CompleteSnapshot](https://docs.aws.amazon.com/ebs/latest/APIReference/API_CompleteSnapshot.html): Seals and completes the snapshot after all of the required blocks of data have been written to it.
- [GetSnapshotBlock](https://docs.aws.amazon.com/ebs/latest/APIReference/API_GetSnapshotBlock.html): Returns the data in a block in an Amazon Elastic Block Store snapshot.
- [ListChangedBlocks](https://docs.aws.amazon.com/ebs/latest/APIReference/API_ListChangedBlocks.html): Returns information about the blocks that are different between two Amazon EBS snapshots of the same volume or between two snapshot copies of the same source snapshot.
- [ListSnapshotBlocks](https://docs.aws.amazon.com/ebs/latest/APIReference/API_ListSnapshotBlocks.html): Returns information about the blocks in an Amazon Elastic Block Store snapshot.
- [PutSnapshotBlock](https://docs.aws.amazon.com/ebs/latest/APIReference/API_PutSnapshotBlock.html): Writes a block of data to a snapshot.
- [StartSnapshot](https://docs.aws.amazon.com/ebs/latest/APIReference/API_StartSnapshot.html): Creates a new Amazon EBS snapshot.


## [Data Types](https://docs.aws.amazon.com/ebs/latest/APIReference/API_Types.html)

- [Block](https://docs.aws.amazon.com/ebs/latest/APIReference/API_Block.html): A block of data in an Amazon Elastic Block Store snapshot.
- [ChangedBlock](https://docs.aws.amazon.com/ebs/latest/APIReference/API_ChangedBlock.html): A block of data in an Amazon Elastic Block Store snapshot that is different from another snapshot of the same volume/snapshot lineage.
- [Tag](https://docs.aws.amazon.com/ebs/latest/APIReference/API_Tag.html): Describes a tag.

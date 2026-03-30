# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-rehydration.md

# Rehydration

You can restore tiered files using rehydration. Except for HDFS, rehydration uses the stub file created from tiering to restore the contents of the file. The stub file contains recall information that Data Optimizer uses to rehydrate the file from the target to its original data source. You can selectively recall any file from its storage location and perform rehydration if a stub file exists in the file system.

**Note:**

* When a file is tiered, the last access time of the file does not change.
* You cannot rehydrate a purged or deleted file.

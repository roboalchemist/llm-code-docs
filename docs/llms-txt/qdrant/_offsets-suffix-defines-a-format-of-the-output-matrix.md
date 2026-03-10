# `_offsets` suffix defines a format of the output matrix.
result = client.search_matrix_offsets(
  collection_name="midlib",
  sample=1000, # Select a subset of the data, as the whole dataset might be too large
  limit=20, # For performance reasons, limit the number of closest neighbors to consider
)
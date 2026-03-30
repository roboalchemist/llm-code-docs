# Define the schema for the new dataframe
schema = StructType([\
    StructField("sentence1", StringType()),\
    StructField("sentence2", StringType()),\
    StructField("dense_vector", ArrayType(FloatType())),\
    StructField("sparse_vector_indices", ArrayType(IntegerType())),\
    StructField("sparse_vector_values", ArrayType(FloatType()))\
])
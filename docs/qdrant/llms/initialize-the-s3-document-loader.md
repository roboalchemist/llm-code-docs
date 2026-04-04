# Initialize the S3 document loader
loader = S3DirectoryLoader(
   "product-dataset",  # S3 bucket name
   "p_1", #S3 Folder name containing the data for the first product
   aws_access_key_id=aws_access_key_id,  # AWS Access Key
   aws_secret_access_key=aws_secret_access_key  # AWS Secret Access Key
)
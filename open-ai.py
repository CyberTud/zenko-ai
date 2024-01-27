import openai
import csv
import pinecone
from tqdm.auto import tqdm  # this is our progress bar
from datasets import load_dataset

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual OpenAI API key

# Check if the API key is authenticated
openai.Engine.list()

# Specify the OpenAI model for text embedding
MODEL = "text-embedding-ada-002"

# Create an OpenAI embedding for a sample query
query = "ala bala portocala"
res = openai.Embedding.create(input=[query], engine=MODEL)
embeds = [record['embedding'] for record in res['data']]

# Specify the path to your CSV file
csv_file_path = "pdf1.csv"

# Create a list to store the data from the CSV file
arr = []

# Open the CSV file
with open(csv_file_path, newline='') as csvfile:
    # Create a CSV reader
    csv_reader = csv.reader(csvfile)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        if len(row) > 1:
            arr.append(str(row[0]))

# Initialize the connection to Pinecone
pinecone.init(
    api_key="c3d9c311-18ff-476c-ba73-6c5065502e86",  # Replace with your actual Pinecone API key
    environment="gcp-starter"  # Replace with your Pinecone environment
)

# Check if 'openai' index already exists (only create index if not)
index_name = "openai"
if index_name not in pinecone.list_indexes():
    # Create the Pinecone index with the appropriate dimension
    pinecone.create_index(index_name, dimension=len(embeds[0]))

# Connect to the Pinecone index
index = pinecone.Index(index_name)

# Process and upsert your data from the 'arr' list
batch_size = 32  # Process data in batches of 32
for i in tqdm(range(0, len(arr), batch_size)):
    i_end = min(i + batch_size, len(arr))  # Determine the end position of the batch
    lines_batch = arr[i:i_end]  # Get a batch of lines
    ids_batch = [str(n) for n in range(i, i_end)]  # Create IDs for the batch
    res = openai.Embedding.create(input=lines_batch, engine=MODEL)  # Create embeddings
    embeds = [record['embedding'] for record in res['data']]  # Extract embeddings
    meta = [{'text': line} for line in lines_batch]  # Prepare metadata
    to_upsert = zip(ids_batch, embeds, meta)  # Upsert batch
    index.upsert(vectors=list(to_upsert))  # Upsert to Pinecone

# Perform a query
query = "What is the history of FDV?"
xq = openai.Embedding.create(input=query, engine=MODEL)['data'][0]['embedding']
res = index.query([xq], top_k=5, include_metadata=True)

for match in res['matches']:
    print(f"{match['score']:.2f}: {match['metadata']['text']}")

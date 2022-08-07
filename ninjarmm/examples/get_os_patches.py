import ninjarmm.app as ninjarmmpy
import os
import json

# Create our client
# Assuming we are storing our keys in environment variables we can access
client = ninjarmmpy.Client(
    AccessKeyID=os.environ.get('NRMM_KEY_ID'),
    SecretAccessKey=os.environ.get('NRMM_SECRET'),
    Europe=False
)
# Get a list of os patches for all devices as Python dictionaries
os_patches = client.get_os_patches()
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
os_patches = json.dumps(os_patches)
# Now we can write the results to a JSON file.
with open('os_patches.json', 'w', newline='') as f:
    print(os_patches, file=f)

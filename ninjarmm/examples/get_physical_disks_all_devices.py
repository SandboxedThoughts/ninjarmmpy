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
# Get a list of disks for all devices as Python dictionaries
disks = client.get_disks()
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
disks = json.dumps(disks)
# Now we can write the results to a JSON file.
with open('disks.json', 'w', newline='') as f:
    print(disks, file=f)

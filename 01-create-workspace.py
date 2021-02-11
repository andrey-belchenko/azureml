# tutorial/01-create-workspace.py
from azureml.core import Workspace

ws = Workspace.create(name='mlt_workspace1', # provide a name for your workspace
                      subscription_id='fd897505-c809-45f3-b74d-50aa6250ab89', # provide your subscription ID
                      resource_group='mlt_resourcegroup', # provide a resource group name
                      create_resource_group=True,
                      location='westeurope') # For example: 'westeurope' or 'eastus2' or 'westus2' or 'southeastasia'.

# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.azureml')
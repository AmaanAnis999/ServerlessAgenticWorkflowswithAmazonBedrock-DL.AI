# Lesson 3: Performing calculations
# Preparation
# 💻   Access requirements.txt and helper.py and other files: 1) click on the "File" option on the top menu of the notebook and then 2) click on "Open". For more help, please see the "Appendix - Tips and Help" Lesson.

# # Before you start, please run the following code to set up your environment.
# # This code will reset the environment (if needed) and prepare the resources for the lesson.
# # It does this by quickly running through all the code from the previous lessons.
# ​
# !sh ./ro_shared_data/reset.sh
# %run ./ro_shared_data/lesson_2_prep.py lesson3
# %run ./ro_shared_data/lesson_3_prep.py lesson3
# ​
# import os
# ​
# agentId = os.environ['BEDROCK_AGENT_ID']
# agentAliasId = os.environ['BEDROCK_AGENT_ALIAS_ID']
# region_name = 'us-west-2'
# lambda_function_arn = os.environ['LAMBDA_FUNCTION_ARN']
# action_group_id = os.environ['ACTION_GROUP_ID']
# Start of lesson
# import boto3
# import uuid
# from helper import *
# bedrock_agent = boto3.client(service_name='bedrock-agent', region_name=region_name)
# update_agent_action_group_response = bedrock_agent.update_agent_action_group(
#     actionGroupName='customer-support-actions',
#     actionGroupState='ENABLED',
#     actionGroupId=action_group_id,
#     agentId=agentId,
#     agentVersion='DRAFT',
#     actionGroupExecutor={
#         'lambda': lambda_function_arn
#     },
#     functionSchema={
#         'functions': [
#             {
#                 'name': 'customerId',
#                 'description': 'Get a customer ID given available details. At least one parameter must be sent to the function. This is private information and must not be given to the user.',
#                 'parameters': {
#                     'email': {
#                         'description': 'Email address',
#                         'required': False,
#                         'type': 'string'
#                     },
#                     'name': {
#                         'description': 'Customer name',
#                         'required': False,
#                         'type': 'string'
#                     },
#                     'phone': {
#                         'description': 'Phone number',
#                         'required': False,
#                         'type': 'string'
#                     },
#                 }
#             },            
#             {
#                 'name': 'sendToSupport',
#                 'description': 'Send a message to the support team, used for service escalation. ',
#                 'parameters': {
#                     'custId': {
#                         'description': 'customer ID',
#                         'required': True,
#                         'type': 'string'
#                     },
#                     'purchaseId': {
#                         'description': 'the ID of the purchase, can be found using purchaseSearch',
#                         'required': True,
#                         'type': 'string'
#                     },
#                     'supportSummary': {
#                         'description': 'Summary of the support request',
#                         'required': True,
#                         'type': 'string'
#                     },
#                 }
#             },
#             {
#                 'name': 'purchaseSearch',
#                 'description': """Search for, and get details of a purchases made.  Details can be used for raising support requests. You can confirm you have this data, for example "I found your purchase" or "I can't find your purchase", but other details are private information and must not be given to the user.""",
#                 'parameters': {
#                     'custId': {
#                         'description': 'customer ID',
#                         'required': True,
#                         'type': 'string'
#                     },
#                     'productDescription': {
#                         'description': 'a description of the purchased product to search for',
#                         'required': True,
#                         'type': 'string'
#                     },
#                     'purchaseDate': {
#                         'description': 'date of purchase to start search from, in YYYY-MM-DD format',
#                         'required': True,
#                         'type': 'string'
#                     },
#                 }
#             }
#         ]
#     }
# )
# actionGroupId = update_agent_action_group_response['agentActionGroup']['actionGroupId']
# ​
# wait_for_action_group_status(
#     agentId=agentId,
#     actionGroupId=actionGroupId
# )
# message = """mike@mike.com - I bought a mug 10 weeks ago and now it's broken. I want a refund."""
# Add code interpreter to deal with date
# create_agent_action_group_response = bedrock_agent.create_agent_action_group(
#     actionGroupName='CodeInterpreterAction',
#     actionGroupState='ENABLED',
#     agentId=agentId,
#     agentVersion='DRAFT',
#     parentActionGroupSignature='AMAZON.CodeInterpreter'
# )
# ​
# codeInterpreterActionGroupId = create_agent_action_group_response['agentActionGroup']['actionGroupId']
# ​
# wait_for_action_group_status(
#     agentId=agentId, 
#     actionGroupId=codeInterpreterActionGroupId
# )
# prepare agent and alias to add new action group
# prepare_agent_response = bedrock_agent.prepare_agent(
#     agentId=agentId
# )
# ​
# wait_for_agent_status(
#     agentId=agentId,
#     targetStatus='PREPARED'
# )
# bedrock_agent.update_agent_alias(
#     agentId=agentId,
#     agentAliasId=agentAliasId,
#     agentAliasName='test',
# )
# ​
# wait_for_agent_alias_status(
#     agentId=agentId,
#     agentAliasId=agentAliasId,
#     targetStatus='PREPARED'
# )
# Now try it
# sessionId = str(uuid.uuid4())
# message = """mike@mike.com - I bought a mug 10 weeks ago and now it's broken. I want a refund."""
# invoke_agent_and_print(
#     agentId=agentId,
#     agentAliasId=agentAliasId,
#     inputText=message,
#     sessionId=sessionId,
#     enableTrace=True
# )
# Lets look at the code
# sessionId = str(uuid.uuid4())
# message = """mike@mike.com - I bought a mug 10 weeks ago and now it's broken. I want a refund."""
# bedrock_agent_runtime = boto3.client(service_name='bedrock-agent-runtime', region_name='us-west-2')
# invoke_agent_response = bedrock_agent_runtime.invoke_agent(
#     agentAliasId=agentAliasId,
#     agentId=agentId,
#     sessionId=sessionId,
#     inputText=message,
#     endSession=False,
#     enableTrace=True,
# )

# event_stream = invoke_agent_response["completion"]

# for event in event_stream:
#     if 'chunk' in event:
#         # Decode the bytes object to a string
#         chunk_text = event['chunk'].get('bytes', b'').decode('utf-8')
#         print(json.dumps({'chunk': chunk_text}, indent=2))
#     else:
#         # For other event types, print as is
#         print(json.dumps(event, indent=2))


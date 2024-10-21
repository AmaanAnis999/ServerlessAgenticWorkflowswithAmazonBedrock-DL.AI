# Lesson 2: Connecting with a CRM
# Preparation
# 💻   Access requirements.txt and helper.py and other files: 1) click on the "File" option on the top menu of the notebook and then 2) click on "Open". For more help, please see the "Appendix - Tips and Help" Lesson.

# # Before you start, please run the following code to set up your environment.
# # This code will reset the environment (if needed) and prepare the resources for the lesson.
# # It does this by quickly running through all the code from the previous lessons.
# ​
# !sh ./ro_shared_data/reset.sh
# %run ./ro_shared_data/lesson_2_prep.py lesson2
# ​
# import os
# ​
# agentId = os.environ['BEDROCK_AGENT_ID']
# agentAliasId = os.environ['BEDROCK_AGENT_ALIAS_ID']
# region_name = 'us-west-2'
# lambda_function_arn = os.environ['LAMBDA_FUNCTION_ARN']
# Start of lesson
# import boto3
# import uuid
# from helper import *
# sessionId = str(uuid.uuid4())
# message = "My name is Mike, my mug is broken and I want a refund."
# invoke_agent_and_print(
#     agentId=agentId, 
#     agentAliasId=agentAliasId, 
#     inputText=message, 
#     sessionId=sessionId
# )
# 💻   The file that is examined in the video is at ./ro_shared_data/functions/lambda_stage_1.py

# bedrock_agent = boto3.client(service_name = 'bedrock-agent', region_name = region_name)
# create_agent_action_group_response = bedrock_agent.create_agent_action_group(
#     actionGroupName='customer-support-actions',
#     agentId=agentId,
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
#                     'supportSummary': {
#                         'description': 'Summary of the support request',
#                         'required': True,
#                         'type': 'string'
#                     }
#                 }
#             }
#         ]
#     },
#     agentVersion='DRAFT',
# )
# create_agent_action_group_response
# actionGroupId = create_agent_action_group_response['agentActionGroup']['actionGroupId']
# ​
# wait_for_action_group_status(
#     agentId=agentId, 
#     actionGroupId=actionGroupId,
#     targetStatus='ENABLED'
# )
# bedrock_agent.prepare_agent(
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
#     agentAliasName='MyAgentAlias',
# )
# ​
# wait_for_agent_alias_status(
#     agentId=agentId,
#     agentAliasId=agentAliasId,
#     targetStatus='PREPARED'
# )
# Now use the agent with functions
# sessionId = str(uuid.uuid4())
# message = "My name is Mike (mike@mike.com), my mug is broken and I want a refund."
# invoke_agent_and_print(
#     agentId=agentId,
#     agentAliasId=agentAliasId,
#     inputText=message,
#     sessionId=sessionId,
#     enableTrace=False
# )
# invoke_agent_and_print(
#     agentId=agentId,
#     agentAliasId=agentAliasId,
#     inputText=message,
#     sessionId=sessionId,
#     enableTrace=True
# )
# ​

# Lesson 5: Read the FAQ Manual
# Preparation
# 💻   Access requirements.txt and helper.py and other files: 1) click on the "File" option on the top menu of the notebook and then 2) click on "Open". For more help, please see the "Appendix - Tips and Help" Lesson.

# # Before you start, please run the following code to set up your environment.
# # This code will reset the environment (if needed) and prepare the resources for the lesson.
# # It does this by quickly running through all the code from the previous lessons.
# ​
# !sh ./ro_shared_data/reset.sh
# %run ./ro_shared_data/lesson_2_prep.py lesson5
# %run ./ro_shared_data/lesson_3_prep.py lesson5
# %run ./ro_shared_data/lesson_4_prep.py lesson5
# %run ./ro_shared_data/lesson_5_prep.py lesson5
# ​
# import os   
# ​
# agentId = os.environ['BEDROCK_AGENT_ID']
# agentAliasId = os.environ['BEDROCK_AGENT_ALIAS_ID']
# region_name = 'us-west-2'
# knowledgeBaseId = os.environ['KNOWLEDGEBASEID']
# Lesson starts here
# import boto3
# import uuid, json
# from helper import *
# bedrock_agent = boto3.client(service_name='bedrock-agent', region_name='us-west-2')
# describe_agent_response = bedrock_agent.get_agent(
#     agentId=agentId
# )
# print(json.dumps(describe_agent_response, indent=4, default=str))
# print(describe_agent_response['agent']['instruction'])
# Look at the knowledge base
# get_knowledge_base_response = bedrock_agent.get_knowledge_base(
#     knowledgeBaseId=knowledgeBaseId
# )
# print(json.dumps(get_knowledge_base_response, indent=4, default=str))
# Connect the knowledge base
# associate_agent_knowledge_base_response = bedrock_agent.associate_agent_knowledge_base(
#     agentId=agentId,
#     knowledgeBaseId=knowledgeBaseId,
#     agentVersion='DRAFT',
#     description='my-kb'
# )
# associate_agent_knowledge_base_response
# Prepare agent and alias
# bedrock_agent.prepare_agent(
#     agentId=agentId
# )
# ​
# wait_for_agent_status(
#     agentId=agentId,
#     targetStatus='PREPARED'
# )
# ​
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
# Try it out
# sessionId = str(uuid.uuid4())
# message=""""mike@mike.com - I bought a mug 10 weeks ago and now it's broken. I want a refund."""
# invoke_agent_and_print(
#     agentId=agentId,
#     agentAliasId=agentAliasId,
#     inputText=message,  
#     sessionId=sessionId,
#     enableTrace=False
# )
# message=""""It's just a minor crack.  What can I do?"""
# invoke_agent_and_print(
#     agentId=agentId,
#     agentAliasId=agentAliasId,
#     inputText=message,  
#     sessionId=sessionId,
#     enableTrace=True
# )
# Another Question, new session
# sessionId = str(uuid.uuid4())
# message=""""My mug is chipped, what can I do?"""
# invoke_agent_and_print(
#     agentId=agentId,
#     agentAliasId=agentAliasId,
#     inputText=message,  
#     sessionId=sessionId,
#     enableTrace=True
# )
# message=""""mike@mike.com - I am not happy.  I bought this mug yesterday. I want a refund."""
# invoke_agent_and_print(
#     agentId=agentId,
#     agentAliasId=agentAliasId,
#     inputText=message,  
#     sessionId=sessionId,
#     enableTrace=True
# )
# ​
# sessionId = str(uuid.uuid4())
# message=""""Try your own message"""
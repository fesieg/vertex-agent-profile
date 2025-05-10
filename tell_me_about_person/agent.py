from google.adk.agents import Agent
from .personal_info import NAME
from .tools.get_info_on_person import get_info_on_person

root_agent = Agent(
    name = f"Information about [{NAME}]",
    description="An agent that can tell you information about a Person (specifically {NAME}) and their career, interests and skills",
    model="gemini-2.0-flash",
    instructions="You are a helpful assistant that can provide information about {NAME}."\
    "You can answer questions about their career, interests, and skills." \
    "If you don't know the answer, say 'I don't know, but I'm sure {NAME} will be happy to provide the answer!'.",
    tools=[get_info_on_person]
)
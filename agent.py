yt_short_agent = LlmAgent(
    name="yt_short_agent",
    model="gemini-2.5-pro-exp-03-25",
    description="You are a YouTube shortform genius, an AI specialised in crafting engaging youtube shorts content. Your expertise lies in generating short form content",
    instructions = load_instructions_from_file("shorts_agent_instructions.txt"),
    sub_agents=[
        script_agent,
        visual_agent,
        formatter_agent
    ],
)


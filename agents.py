
# Fix CrewAI cache_breakpoint issue with Groq
import crewai.llms.cache as _crewai_cache

_crewai_cache.mark_cache_breakpoint = lambda msg: msg

import os
from dotenv import load_dotenv
from crewai import Agent, LLM


# Load environment variables
load_dotenv()

# Groq LLM Configuration
llm = LLM(
    model="groq/openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

# Agent 1: Query Router
router = Agent(
    role="Query Router",
    goal="Classify user queries as MATH or EXPLAIN.",
    backstory=(
        "You are an intelligent query classification expert. "
        "You analyze user questions and classify them into "
        "MATH or EXPLAIN categories."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# Agent 2: Math Expert
math_agent = Agent(
    role="Math Expert",
    goal="Solve mathematical problems accurately.",
    backstory=(
        "You are an expert mathematics teacher. "
        "You solve calculations, equations and mathematical "
        "problems with clear step-by-step explanations."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# Agent 3: Explanation Teacher
explain_agent = Agent(
    role="Explanation Teacher",
    goal="Explain concepts in simple and understandable language.",
    backstory=(
        "You are a friendly teacher who explains difficult "
        "concepts in simple words with practical examples."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)

print("All Three Agents Created Successfully!")

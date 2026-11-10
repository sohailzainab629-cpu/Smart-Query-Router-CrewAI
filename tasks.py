
from crewai import Task


# Task 1: Query Classification
def create_router_task(query, agent):

    return Task(
        description=f"""
        Analyze the following user query:

        {query}

        Classify it into exactly one category:

        MATH:
        For calculations, equations and mathematical problems.

        EXPLAIN:
        For definitions, concepts and general explanations.

        Return ONLY one word: MATH or EXPLAIN.
        """,
        expected_output="Exactly one word: MATH or EXPLAIN.",
        agent=agent
    )


# Task 2: Mathematical Problem Solving
def create_math_task(query, agent):

    return Task(
        description=f"""
        Solve the following mathematical problem:

        {query}

        Provide:
        1. Step-by-step solution.
        2. Correct calculation.
        3. Final answer.
        """,
        expected_output="An accurate mathematical solution with steps.",
        agent=agent
    )


# Task 3: Concept Explanation
def create_explain_task(query, agent):

    return Task(
        description=f"""
        Explain the following question:

        {query}

        Explain in simple beginner-friendly language.
        Include examples wherever helpful.
        """,
        expected_output="A simple and clear explanation with examples.",
        agent=agent
    )

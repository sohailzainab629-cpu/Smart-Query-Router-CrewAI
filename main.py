
from crewai import Crew, Process

from agents import router, math_agent, explain_agent

from tasks import (
    create_router_task,
    create_math_task,
    create_explain_task
)


def smart_query_router(query):

    print("\n" + "=" * 50)
    print("       SMART QUERY ROUTER")
    print("=" * 50)

    # STEP 1: Router Agent
    print("\n[1] Router Agent is analyzing your query...")

    router_task = create_router_task(query, router)

    router_crew = Crew(
        agents=[router],
        tasks=[router_task],
        process=Process.sequential,
        verbose=True
    )

    router_result = router_crew.kickoff()

    category_text = str(router_result).strip().upper()

    # STEP 2: Detect Category
    if category_text.startswith("MATH"):

        print("\n[2] Category: MATH")
        print("Routing to Math Expert Agent...")

        task = create_math_task(query, math_agent)

        selected_agent = math_agent

    elif category_text.startswith("EXPLAIN"):

        print("\n[2] Category: EXPLAIN")
        print("Routing to Explanation Teacher Agent...")

        task = create_explain_task(query, explain_agent)

        selected_agent = explain_agent

    else:

        print("\nUnable to classify the query.")
        print("Router Output:", router_result)
        return

    # STEP 3: Execute Selected Agent
    specialist_crew = Crew(
        agents=[selected_agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    final_result = specialist_crew.kickoff()

    # STEP 4: Display Final Answer
    print("\n" + "=" * 50)
    print("             FINAL ANSWER")
    print("=" * 50)

    print(final_result)


if __name__ == "__main__":

    print("\nWelcome to Smart Query Router!")

    query = input("\nEnter your query: ")

    if query.strip():

        smart_query_router(query)

    else:

        print("Please enter a valid query.")

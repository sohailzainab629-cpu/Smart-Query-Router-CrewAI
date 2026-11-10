# Smart Query Router Using CrewAI & Groq

## Project Overview

Smart Query Router is a multi-agent AI application built using CrewAI and Groq LLM. It automatically analyzes user queries, identifies their category, and sends them to the appropriate AI agent.

The system uses three specialized AI agents to classify queries, solve mathematical problems, and explain concepts in simple language.

## Features

- Automatic query classification
- Multi-agent architecture using CrewAI
- Groq LLM integration
- Mathematical problem solving
- Beginner-friendly concept explanations
- Step-by-step mathematical solutions
- Interactive command-line interface

## AI Agents

### 1. Query Router Agent
- Analyzes the user's query.
- Classifies it into MATH or EXPLAIN.
- Routes the query to the appropriate specialist agent.

### 2. Math Expert Agent
- Solves mathematical calculations.
- Handles equations and mathematical problems.
- Provides step-by-step solutions.

### 3. Explanation Teacher Agent
- Explains concepts in simple language.
- Provides beginner-friendly explanations.
- Includes practical examples where helpful.

## Project Workflow

1. User enters a query.
2. Query Router Agent analyzes the query.
3. The query is classified as MATH or EXPLAIN.
4. MATH queries are sent to the Math Expert Agent.
5. EXPLAIN queries are sent to the Explanation Teacher Agent.
6. The selected agent generates the final answer.

## Technologies Used

- Python
- CrewAI
- Groq LLM
- LiteLLM
- Python-dotenv

## Project Structure

```text
Smart-Query-Router-CrewAI/
│
├── agents.py
├── tasks.py
├── main.py
├── check_api.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Query-Router-CrewAI.git
```

### 2. Open the Project Folder

```bash
cd Smart-Query-Router-CrewAI
```

### 3. Create Virtual Environment

```bash
py -3.12 -m venv .venv
```

### 4. Activate Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Never upload your `.env` file or share your API key publicly.

## Run the Project

First, verify the API key:

```bash
python check_api.py
```

Then execute:

```bash
python main.py
```

Enter your query when prompted.

## Sample Queries

**Math Query:**

```text
What is 25 multiplied by 8?
```

Expected routing:

```text
Query Router → MATH → Math Expert Agent
```

**Explanation Query:**

```text
Explain Artificial Intelligence in simple words.
```

Expected routing:

```text
Query Router → EXPLAIN → Explanation Teacher Agent
```

## Project Testing

The following tests were performed successfully:

| Test Query | Category | Selected Agent | Result |
|---|---|---|---|
| What is 25 multiplied by 8? | MATH | Math Expert | PASS |
| Explain Artificial Intelligence in simple words. | EXPLAIN | Explanation Teacher | PASS |

## Learning Outcomes

Through this project, I learned:

- How to create multiple AI agents using CrewAI.
- How to define agent roles, goals, and backstories.
- How to create tasks for specialized agents.
- How to integrate Groq LLM with CrewAI.
- How to build a query classification and routing workflow.
- How multiple AI agents can work together to solve different problems.

## Author

**Zainab Sohail**

AI / Machine Learning Learner
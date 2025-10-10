## 1. Setup Instructions

### Step 1: Clone this repo
```bash
git clone https://github.com/<your-org>/taller-langchain.git
cd taller-langchain
```

### Step 2: Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate # For Widnows
source .venv/bin/activate # For MacOS
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create your `.env` file
Copy the example file:
```bash
cp .env.example .env
```

Then edit `.env` and add your keys:
```env
OPENAI_API_KEY=your_openai_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_PROJECT=langchain-workshop
```

>  You can get your **LangSmith API key** from [https://smith.langchain.com](https://smith.langchain.com)

---

## 2. Running the Agent

Run the interactive agent to test your setup:
```bash
python agent.py
```

You will be able to:
```
Send a simple prompt to validate the agent function or type 'exit' to quit.
```
## 1. Setup Instructions

### Step 1: Clone this repo
```bash
git clone https://github.com/<your-org>/taller-langchain.git
cd taller-langchain
```

### Step 2: Create a virtual environment (recommended)
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

---

## 3. Running an Evaluation

Run a dataset of prompts to automatically log results in **LangSmith**:
```bash
python eval.py
```

By default, it will use:
```
datasets/sample_dataset.json
```

When prompted, you can also specify another dataset path:

---

## 4. Viewing Results in LangSmith

If your environment variables are configured correctly (`LANGSMITH_TRACING=true`),  
each interaction — both manual (`agent.py`) and automated (`eval.py`) — will appear automatically in [LangSmith](https://smith.langchain.com/).

To view your results:
1. Go to [https://smith.langchain.com](https://smith.langchain.com)
2. Log in (or sign up if needed)
3. Select your project (default: `taller-langchain`)
4. Go to the **Tracing Projects** tab and explore:
   - Inputs and outputs
   - Chains used  
   - Model used  
   - Latency and token usage  
   - Prompt and response details
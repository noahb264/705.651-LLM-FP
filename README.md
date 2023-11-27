# 705.651-LLM-FP

# Setup (for Mac)

```
python3 -m venv venv
source ./venv/bin/activate
pip install -r ./requirements.txt
```

# Running

```
python evaluation.py --level 1 --mover random
```

# Demo

In the demo folder, run Demo.ipynb for demo. 

You can update the following variable to pick the system prompt and user prompt:

`prompt = ['demo_system_1.txt', 'demo_user_1.txt']`

## TODO

- Review the potential bug in action: jump to the right
- Adjust the system and user prompts for better collaboration
- Simplify the LLM JSON output
# 705.651-LLM-FP

## Setup

```
python3 -m venv venv
source ./venv/bin/activate
pip install -r ./requirements.txt
```

## Running


#### Random
```
python evaluation.py --level level_1 --mover random
```

#### Text-based LLM Agent
```
python evaluation.py --level level_1 --mover text
```

#### Vision-based LLM Agent
```
python evaluation.py --level level_1 --mover vision
```

## Demo

Our first integrated pipeline based on text model. Setup for exploration and individual game level experiment. 

You can create more system prompt and user prompt, by updating the following variable:

`prompt = ['demo_system_1.txt', 'demo_user_1.txt']`

### TODO

- Review the potential bug in action: jump to the right => Reference tfidf_string_similarity function in pico_park.ipynb
- Optimize the system and user prompts for better collaboration
- Simplify the LLM JSON output
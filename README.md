# Mathdle

Mathdle allows you to **train your math skills** everyday and improve on **high level questions**. Visit Mathdle everyday to try to answer the daily question !  

**The question is too difficult ?** Don't worry, Mathdle will help you by giving some clues and guiding you to make you find the result by yourself !


## Technos used

- Mistral API
    - Prefixes
    - Python integration
- HTML, CSS, Tailwind (Front End part)
- [Hugging Face](https://huggingface.co/datasets/HuggingFaceH4/MATH-500) for questions dataset
- Flask (Python Web App Framework)
- KaTeX (to render TeX code)

## Run the project

-# To run the project, you need to have the api keys in the `.env` file.

### 1. Clone the project
You can use git clone, or just download the zip.

### 2. Once in the directory, create a virtual environment
```
python -m venv .venv
```

### 3. Activate the virtual environment
```
source .venv/bin/activate
```

### 4. Install the dependencies
```
pip install -r requirements.txt
```

### 5. Run the project
```
python mathdle.py
```

:warning: To work on the frontend, you need to install Tailwind separately! :warning:
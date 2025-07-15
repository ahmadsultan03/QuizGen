import os
import json

from openai import OpenAI
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:
    system_prompt = """You are an expert in Artificial Intelligence and Machine Learning education.
    Your task is to generate a multiple-choice quiz question on AI/ML based on the specified difficulty level.

    For easy questions: Focus on basic ML/AI concepts such as supervised vs unsupervised learning, types of ML algorithms, basic terminology.
    For medium questions: Cover intermediate topics like overfitting, bias-variance tradeoff, types of neural networks, feature engineering, common algorithms (e.g., Decision Trees, SVM).
    For hard questions: Include advanced topics such as backpropagation, gradient descent variants, regularization, attention mechanisms, or recent advancements like transformers.

    Return the challenge in the following JSON structure:
    {
        "title": "The question title",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "correct_answer_id": 0, // Index of the correct answer (0-3)
        "explanation": "Detailed explanation of why the correct answer is right"
    }

    Make sure the options are plausible but with only one clearly correct answer. 
    Randomize the position of the correct answer among the four options — it should not always be first.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Generate a {difficulty} difficulty AI/ML quiz question."}
            ],
            response_format={"type": "json_object"},
            temperature=0.6
        )

        content = response.choices[0].message.content
        challenge_data = json.loads(content)

        required_fields = ["title", "options", "correct_answer_id", "explanation"]
        for field in required_fields:
            if field not in challenge_data:
                raise ValueError(f"Missing required field: {field}")

        return challenge_data

    except Exception as e:
        print(e)
        return {
            "title": "Which method is commonly used to prevent overfitting in machine learning?",
            "options": [
                "Increasing the size of the dataset",
                "Reducing the number of features",
                "Using regularization techniques",
                "Choosing a simpler model"
            ],
            "correct_answer_id": 2,
            "explanation": "Regularization techniques like L1 and L2 help to prevent overfitting by penalizing large weights in the model."
        }

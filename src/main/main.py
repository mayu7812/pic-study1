# main.py

import os
from dotenv import load_dotenv
import openai

# .env ファイルから環境変数を読み込む
load_dotenv()

# APIキーを環境変数から取得
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key is missing. Set the OPENAI_API_KEY environment variable.")

# APIキーを設定
openai.api_key = api_key


import json

try:
    # ここから先のコードで API を使用する
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは気のいい私の友達です。私はあなたに何かお手伝いできますか？"},
            {"role": "user", "content": "こんにちは"}
        ],
    )

    answer = response["choices"][0]["message"]["content"]

    print(json.dumps(answer, ensure_ascii=False))

except Exception as e:
    print("Error:", e)


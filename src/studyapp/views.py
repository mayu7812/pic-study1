# views.py

from django.shortcuts import render
from django.http import JsonResponse
import openai
import asyncio
import asgiref

# 非同期ビューの例
async def some_async_view(request):
    try:
        loop = asyncio.get_event_loop()

        # GPT-3 APIを非同期で使用して簡単なテキスト生成
        response = await loop.run_in_executor(None, lambda: openai.Completion.create(
            engine="text-davinci-003",
            prompt="What is the meaning of life?",
            max_tokens=50
        ))

        # 生成されたテキストを取得
        generated_text = response.choices[0].text.strip()

        return JsonResponse({'generated_text': generated_text})

    except Exception as e:
        return JsonResponse({'error': str(e)})

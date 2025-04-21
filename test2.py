import os
import sys
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

prompt = sys.argv[1] if len(sys.argv) > 1 else "Can you explain the basics of machine learning?"

client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)

response = client.complete(
    messages=[UserMessage(prompt)],
    model="Phi-3.5-mini-instruct",
    temperature=0.8,
    max_tokens=2048,
    top_p=0.1
)

# ✅ 關鍵修正：加入固定前綴，讓主程式可辨識
print("[MODEL OUTPUT]", response.choices[0].message.content)

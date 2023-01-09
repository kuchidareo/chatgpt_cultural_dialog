from revChatGPT.ChatGPT import Chatbot
import os
import sys
from datetime import datetime
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 保存先の有無チェック
if not os.path.isdir('./Log'):
    os.makedirs('./Log', exist_ok=True)

# ファイルハンドラの設定
file_handler = logging.FileHandler(f"./Log/log{datetime.now():%Y%m%d%H%M%S}.log")
# file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(
    logging.Formatter("%(asctime)s@ %(name)s [%(levelname)s] %(funcName)s: %(message)s")
)
logger.addHandler(file_handler)

# ストリームハンドラの設定
stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

prompt = """Misunderstanding nonverbal cues: In a high-context culture, nonverbal cues such as body language and facial expressions may convey a great deal of meaning. A person from a low-context culture who is not attuned to these cues may misunderstand what is being communicated, leading to confusion or misunderstandings.

Generate an example conversation between a person from a high-context culture (H) and a person from a low-context culture (L) to illustrate this statement
"""

with open("config.json") as f:
    chatbot = Chatbot(
            json.loads(f.read()),
            conversation_id=None,
            parent_id=None
        )
with open(f"Log/nonverbal_cues_dialog.txt", mode="w") as f:
    for i in range(50):
        response = chatbot.ask(prompt, conversation_id=None, parent_id=None)
        response["prompt"] = prompt
        logger.info(response)
        f.write(response["message"])
        chatbot.refresh_session()

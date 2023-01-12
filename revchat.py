from revChatGPT.ChatGPT import Chatbot
import prompt_inputs
import os
import sys
from datetime import datetime
import time
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

path_prompt_dict = prompt_inputs.savepath_prompts

with open("config.json") as f:
    config = json.loads(f.read())
    chatbot = Chatbot(
            {"session_token": config["session_token9243"], "proxy": config["proxy"], "driver_exec_path": "/usr/bin/chromedriver", "browser_exec_path": "/usr/bin/google-chrome"},
            conversation_id=None,
            parent_id=None
        )

for path, prompt in path_prompt_dict.items():
    if path != "too_blunt_dialog.txt":
        continue

    with open(f"Log/{path}", mode="a") as f:
        for i in range(5):
            while(1):
                try:
                    response = chatbot.ask(prompt, conversation_id=None, parent_id=None)
                except Exception as e:
                    logger.error(e)
                    time.sleep(120)
                else:
                    break
            response["prompt"] = prompt
            logger.info(response)
            f.write(" ".join(response["message"].split()))
            f.write("\n")
            chatbot.refresh_session()

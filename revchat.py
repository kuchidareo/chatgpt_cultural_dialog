from revChatGPT.ChatGPT import Chatbot
import os
import sys
from datetime import datetime
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

token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..0r0I95LPLHSs2lVP.ehtcgEDyKWIvwvw1NOQ9siFK7Yc3t20Hbo0IaHJCK0QELsdyRiU3ZC1IiLpZblXwUbLMT70ObEsGdHJzWNIkkS8mO0oOYsDZ-R92q4i2Sr8eF_wUY3c4crPcM2Ju_6Iqo_k8unESLKDJnPVr0YmuE3krA_in4K0jAlKPUe2QPldovy6jFTs-GAvyK2QzkFV2YWEsdkgKRJ-QELrEALdJCjN7PYnHBiXAMCh96ww1E9F2NZWk3N9I8lGcj5EBE_NnA6cFmmM5dQo4p_PTwAcWzPqJsouzGP8TUF-2VC8n0ZUwwryiMoyoW2Ipx28PIZUnEsXRunaskDY65d1D1emDodBL2kRSQnC6Ub_3Pf-jAy-Gwia_mZVQ227D9EmLrur0OIhA8QLb7rSQbY1L66wfNF4ILimJwJrgTjL5XnPlFS5PGIakmm4bl5al35MiWCHIG8qGuUjpphuBv1jsqkQACYTpY7ZYAcVj07PGQV976LJ3PYWUEZRs8arerx_-7RN-vaMtH2TggcHfb2z1i-6N5qf6O3gGtBVVTaBL9a6dSkCPQZZTIb6TtntFn7NliUllxjhPcH7ubwS18YXegbihDEStjQ8VceAOBW49LA3S7iQ6lDcYB4R9LNPpgTIzp9SI59yEw9vOz3w9SZHGVms7HQn5b5p8xbXdlwhl9vKaLMi2I__V4RiTVbuYRP15U10KsCslc5QjBKu3nILfj0SgJqbi86ZV3LQiVwJnaRbi-Ru5xYfyFvh0aWSkm7W3HzJ26M41CLeaXLUTZZ6jLYlSSwgKhxYfCjqR4EgkcUM4AsHnyMUqxt2jonsDaTxEOuChSQEIl_V51PyTU-dc3KgbCWKQmWWrLnyjIkPRQcQtBGFTiVtqtC8__1vm4_OduDrsnFshEbcaxFOG8hMybSUWak7HdwT8D4j76PxlYuGFB-0duwAlRN8zJ-keeO4FLOLKzrKqIZqfawUXW_1wXdjpE_8oM1q-xzgEXprjqF1z9RIM3-gaba44ZupoVhwVn-hLZXHrVxq_PK0gUKl_d9LK-oNIjyGen6mZhV9RrbA2WnDclbZZM4-7_QkBm8BmuXAxiyBTTSILLSUttFhtK1AQavPML4Yt4p2JYPe4Z2G4RnIvRb01NYfyKvsnYn4WyYjI2ubFJsS-SVcjbZWJY3xLK-2jHxdkxwlXtZfS2U1Vj1d2M-z-6LbP9g6AeZzA81rR1lZ3ryUBEhObIeeuDIRjjaNjqX59unXt4Xkn3mSlkiCmS4C-uT34m0f7JNY37UloSUrFEU3ocdZrC6LFhmdQQjAR9tsHg-CkN0HLgYgGm00It0WVaSePL9PdGaWbJfEPYC57SJ2YkM6jBQtlFbc-z1MNKSxprCU13uuqUvMVqeQ26cvxIO6B1C40200ZJuXvCAJi2TDAQ74x5B2I8L_iIbojvmFgWNsnfBZsj5eE-FaLraVLAtXj5sE8bsW54D_Q0L_Yx7ipWaxBrJxASyCQkFfNplOTGgHcd8dbXV7izB9oNXekpp3Oww5qJ1J2ighbCc9omkHUtYxvh-SZVyxKD_eP7vhEXnLtDaBdvBU7vy7imYFb6-nYjhnOh0bUv3MHBHVvJGR40q4C-DAJ3aFyIUx7CjeDWtbXgu5-F_Je0zSrl5h_Kr_mQO93T_lplLl-kOUEfaxheZM4i76Hol78hJ4uMwvdwVmxspu60GzaQAJLjnNsATXwofzN_7I5OSxsF4rfeIPmfvReZjVW5hAwCjvnAu6OUgLZPWMfzOMAD0dAw9jOT6XtUSp7eJzIFiPd0YpaHYcA-0Xo-rqJZ4bQatynE-Bdgtbo7MsWrSNAfNR2sMZ7hdhULNXk8Mzur9TSn20JKqDhRjO3L7-r7iSaEBjFj9fMcslJXx2TLdpLYTW2CWWckEV3JK898w5pO_1zbVcwd2Bh0cdxyH2-n5n2tGI0SB8cOz0GKDVG__70cke_Gv2cqS7mnxQOr6PvxmySiz-ahSsezEtcYVPbZPjUjFWCS0UlL-Vn8STnciD2TWNFHl-ArKkZBfzy5LasWNfqqb3Gdd7ectHUpjUukzsZUwvpepikEcr8YGG47_Xe2aBUSSZj8QOYdamK4IbAZVKvKpjw4uUEojhxKKlYIBGRIA1bsi8cfBHQrpdzNxeEXRzPjWX5Srf4gzvMj2rFQKQcjGau_GvcALi36JNs00jDIMlPXbI2UPX7jt0jRTJ7X2RgrUNl61kl9C_dqhdO4MaRuuc1BGtbw-DE5MpZ-y2PYHngaQDwEO5w8TGZxKqC4Ir-4Z6Qk64YYYJr_YyBF7rgn-0_5w3yUAadX97La8YauBABsp0PzSwzGN_w0Lzon7GzXNmTQP8Q46Px6IjnY5f8hvb34b1s.eV__q6r5vhGgtFPqTOUhMw"
  
prompt = """Misunderstanding nonverbal cues: In a high-context culture, nonverbal cues such as body language and facial expressions may convey a great deal of meaning. A person from a low-context culture who is not attuned to these cues may misunderstand what is being communicated, leading to confusion or misunderstandings.

Generate an example conversation to illustrate this statement.
"""

chatbot = Chatbot(
            {"session_token": token, "proxy": "http://localhost:8080"},
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

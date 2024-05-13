from django.conf import settings
from linebot import LineBotApi

from linebot.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def MyAccount(event):
    flex_message = FlexSendMessage(
        alt_text='Flex_message',
        contents={
          "type": "bubble",
          "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "我的帳本",
                "color": "#FFFFFF",
                "weight": "bold",
                "size": "xl"
              },
              {
                "type": "text",
                "text": "請選擇要進行的操作",
                "color": "#FFFFFF",
                "weight": "regular"
              }
            ]
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "uri": "https://liff.line.me/2004983305-2LqXBLZr",
                  "label": "記帳"
                }
              },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "查詢帳本",
                  "uri": "http://linecorp.com/"
                }
              }
            ]
          },
          "styles": {
            "header": {
              "backgroundColor": "#00B900"
            }
          }
        }
    )
    line_bot_api.reply_message(event.reply_token, flex_message)
import html
from googletrans import Translator
from slackbot.bot import default_reply, respond_to, listen_to

translator = Translator()

def translate(message):
    msg_in = html.unescape(message.body["text"])

    if msg_in != "":
        try:
            if  translator.detect(msg_in).lang == "en":
                text = translator.translate(msg_in, dest = "ja").text
            else:
                text = translator.translate(msg_in, dest = "en").text
        except:
            text = "エラー"
        
        msg_out = "```{}```".format(text)

        if message.thread_ts == message.body["event_ts"]:
            message.send(msg_out)
        else:
            message.reply(msg_out)


@default_reply
def my_default_handler(message):
    translate(message)

@respond_to(".*")
def all_replies(message):
    translate(message)

@listen_to(".*")
def all_messages(message):
    translate(message)

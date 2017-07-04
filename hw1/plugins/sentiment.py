# -*- coding: utf-8 -*-
from rtmbot.core import Plugin
from google.cloud import language

language_client = language.Client()

class SentimentPlugin(Plugin):
    def process_message(self, data):
        if data['channel'].startswith("D"):
            text = data['text']
            document = language_client.document_from_text(text)
            sentiment = document.analyze_sentiment().sentiment
            
            if sentiment.score >= 0.25:
                output = "긍정적입니다."
            elif sentiment.score <= -0.25:
                output = "부정적입니다."
            else:
                output = "감정을 파악할 수 없습니다."
            output += " (점수: {}, 강도: {})".format(sentiment.score,
                                                     sentiment.magnitude)
            self.outputs.append([data['channel'], output])


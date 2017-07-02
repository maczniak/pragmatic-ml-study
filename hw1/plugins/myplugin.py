from rtmbot.core import Plugin

class MyPlugin(Plugin):
    def catch_all(self, data):
        print(data)


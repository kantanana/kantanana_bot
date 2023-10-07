from telegram.ext.filters import MessageFilter

class FilterGreetings(MessageFilter):
    def filter(self, message):
        return ('hi' in message.text.lower()) or ('hello' in message.text.lower()) or ('bye' in message.text.lower())

filter_greetings = FilterGreetings()
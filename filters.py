from telegram.ext.filters import MessageFilter

class FilterGreetings(MessageFilter):
    def filter(self, message):
        return ('hi' in message.text.lower()) or ('hello' in message.text.lower()) or ('bye' in message.text.lower())

    def detect(self, message):
        print(message)
        return 'hi' if 'hi' in message.lower() else 'hello' if 'hello' in message.lower() else 'bye'

    def name_presence(self, message, user):
        if 'kantana' in message.lower():
            return "["+user.first_name+"](tg://user?id="+str(user.id)+")"
        else:
            return ""
        







filter_greetings = FilterGreetings()
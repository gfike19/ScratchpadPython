class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, text):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + text + "'"


class BoredChatbot(Chatbot):

    def response(self, text):
        string = ""
        if (len(text) > 20):
            string = "zzz... Oh excuse me, I dozed off reading your essay."
        else:
            string = "It is very interesting that you say: '" + text + "'"
        return string

from mycroft import MycroftSkill, intent_file_handler


class MycroftRoxyTurtlesimTurtleForward(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('forward.turtle.turtlesim.roxy.mycroft.intent')
    def handle_forward_turtle_turtlesim_roxy_mycroft(self, message):
        self.speak_dialog('forward.turtle.turtlesim.roxy.mycroft')


def create_skill():
    return MycroftRoxyTurtlesimTurtleForward()


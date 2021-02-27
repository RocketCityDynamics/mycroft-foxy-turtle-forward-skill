from mycroft import MycroftSkill, intent_file_handler
import subprocess

class MycroftRoxyTurtlesimTurtleForward(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('forward.turtle.turtlesim.roxy.mycroft.intent')
    def handle_forward_turtle_turtlesim_roxy_mycroft(self, message):
        self.speak_dialog('forward.turtle.turtlesim.roxy.mycroft')
        subprocess.call(["ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist '{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}'"],shell=True)


def create_skill():
    return MycroftRoxyTurtlesimTurtleForward()


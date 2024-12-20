import rospy
import actionlib
from pack3cm.msg import MoveRobotAction, MoveRobotFeedback, MoveRobotResult

class MoveRobotServer:
    def __init__(self):
        self.server = actionlib.SimpleActionServer('move_robot', MoveRobotAction, self.execute, False)
        self.server.start()

    def execute(self, goal):
        feedback = MoveRobotFeedback()
        result = MoveRobotResult()

        # Example task: Decrementing distance_remaining
        for i in range(10):
            feedback.distance_remaining = 10 - i
            self.server.publish_feedback(feedback)
            rospy.sleep(1)

        result.success = True
        result.message = "Goal completed successfully."
        self.server.set_succeeded(result)

if __name__ == '__main__':
    rospy.init_node('move_robot_server')
    server = MoveRobotServer()
    rospy.spin()

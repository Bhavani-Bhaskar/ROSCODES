import rospy
import actionlib
from pack3cm.msg import MoveRobotAction, MoveRobotGoal

def feedback_callback(feedback):
    rospy.loginfo(f"Distance remaining: {feedback.distance_remaining}")

if __name__ == '__main__':
    rospy.init_node('move_robot_client')
    client = actionlib.SimpleActionClient('move_robot', MoveRobotAction)
    client.wait_for_server()

    goal = MoveRobotGoal()
    goal.x = 1.0
    goal.y = 2.0
    goal.z = 3.0

    client.send_goal(goal, feedback_cb=feedback_callback)
    client.wait_for_result()

    rospy.loginfo(client.get_result())

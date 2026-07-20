#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator

class WaypointLoop(Node):

    def __init__(self):
        super().__init__('waypoint_loop')
        self.navigator = BasicNavigator()

    def run(self):

        waypoints = []

        p1 = PoseStamped()
        p1.header.frame_id = "map"
        p1.pose.position.x = 0.0
        p1.pose.position.y = 0.0
        p1.pose.orientation.w = 1.0
        waypoints.append(p1)

        p2 = PoseStamped()
        p2.header.frame_id = "map"
        p2.pose.position.x = 1.0
        p2.pose.position.y = 0.0
        p2.pose.orientation.w = 1.0
        waypoints.append(p2)

        while rclpy.ok():

            self.get_logger().info("Starting waypoint loop...")

            self.navigator.followWaypoints(waypoints)

            while not self.navigator.isTaskComplete():
                rclpy.spin_once(self, timeout_sec=0.1)

            self.get_logger().info("Loop completed... Restarting in 2 seconds")

            self.create_rate(0.5).sleep()


def main(args=None):
    rclpy.init(args=args)

    node = WaypointLoop()

    node.run()

    rclpy.shutdown()


if __name__ == "__main__":
    main()

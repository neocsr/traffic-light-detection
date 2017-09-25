import cv2
import rospy
from time import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

out_dir = './simulator_traffic_light/'

bridge = CvBridge()


def image_callback(msg):
    image_name = 'sim-%d.png' % (int(time() * 1e6))
    print('Writing image %s' % image_name)
    try:
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        cv2.imwrite(out_dir + image_name, cv2_img)


def main():
    rospy.init_node('image_listener')

    image_topic = "/image_color"

    rospy.Subscriber(image_topic, Image, image_callback)

    rospy.spin()


if __name__ == '__main__':
    main()

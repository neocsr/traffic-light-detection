import cv2
import rosbag
from cv_bridge import CvBridge, CvBridgeError


bag_name = './traffic_light_bag_files/loop_with_traffic_light.bag'
out_dir = './loop_with_traffic_light/'

bridge = CvBridge()

with rosbag.Bag(bag_name, 'r') as bag:
    for topic, msg, ts in bag.read_messages():
        if topic == '/image_raw':
            img_out_name = '%s%d-%09d' % (out_dir, ts.secs, ts.nsecs) + '.png'
            image = bridge.imgmsg_to_cv2(msg, 'bgr8')
            out = cv2.imwrite(img_out_name, image)
            if not out:
                print('Error writing %s' % img_out_name)

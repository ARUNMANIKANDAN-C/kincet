import freenect
import numpy as np
import cv2

def get_depth():
    # Get depth frame
    depth, _ = freenect.sync_get_depth()
    depth = np.array(depth, dtype=np.uint16)
    return depth

def get_rgb():
    # Get RGB frame
    rgb, _ = freenect.sync_get_video()
    rgb = np.array(rgb, dtype=np.uint8)
    return rgb

while True:
    depth_frame = get_depth()
    rgb_frame = get_rgb()

    # Display the RGB frame
    cv2.imshow('RGB', rgb_frame)

    # Display the depth frame (scaled for visualization)
    depth_frame_scaled = cv2.normalize(depth_frame, None, 0, 255, cv2.NORM_MINMAX)
    depth_frame_scaled = np.uint8(depth_frame_scaled)
    cv2.imshow('Depth', depth_frame_scaled)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

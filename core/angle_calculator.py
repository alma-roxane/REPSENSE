import numpy as np


JOINT_PAIRS = {
    'bicep_curl_left':  (5, 7, 9),
    'bicep_curl_right': (6, 8, 10),
    'squat_left':       (11, 13, 15),
    'squat_right':      (12, 14, 16),
    'pushup_left':      (5, 7, 9),
    'pushup_right':     (6, 8, 10),
}


def calculate_angle(A, B, C):
    vec_BA = A - B
    vec_BC = C - B
    angle1 = np.arctan2(vec_BA[1], vec_BA[0])
    angle2 = np.arctan2(vec_BC[1], vec_BC[0])
    angle = angle2 - angle1
    angle = np.degrees(angle)
    angle = np.abs(angle)
    if angle > 180:
        angle = 360 - angle
    return angle


def get_joint_angle(keypoints, idx_a, idx_b, idx_c):
    if keypoints[idx_a][2] < 0.3:
        return None
    if keypoints[idx_b][2] < 0.3:
        return None
    if keypoints[idx_c][2] < 0.3:
        return None
    point_a = keypoints[idx_a][:2]
    point_b = keypoints[idx_b][:2]
    point_c = keypoints[idx_c][:2]
    return calculate_angle(point_a, point_b, point_c)

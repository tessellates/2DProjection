import numpy as np

def project_point_onto_plane(point, plane_normal, plane_point):
    # Compute the distance between the point and the plane
    d = np.dot(plane_normal, (point - plane_point)) / np.linalg.norm(plane_normal)
    # Project the point onto the plane
    projected_point = point - d * plane_normal
    return projected_point

def intersection(point_line, direction_line, point_plane, normal_plane):
    t = np.dot((point_plane - point_line), normal_plane) / np.dot(direction_line, normal_plane)
    intersection = point_line + t * direction_line
    return intersection

line_point = np.array([1, 9, 1])
line_direction = np.array([1, 1, 3])
plane_normal = np.array([3.0, 2.0, 1])
plane_point = np.array([5,8,9])
_intersection = intersection(line_point, line_direction, plane_point, plane_normal)
print(_intersection)

n = np.cross(d_ab, d_cd)
if np.linalg.norm(n) > 0:
    w = A - C
    s = np.dot(n, np.cross(d_cd, w)) / np.dot(n, d_ab)
    intersection = A + s * d_ab
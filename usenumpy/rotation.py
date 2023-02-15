import numpy as np

def rotate_cube(cube_vertices, angle_x, angle_y, angle_z):
    # Create the rotation matrices around the X, Y, and Z axes
    rotation_matrix_x = np.array([[1, 0, 0],
                                  [0, np.cos(angle_x), -np.sin(angle_x)],
                                  [0, np.sin(angle_x), np.cos(angle_x)]])
    rotation_matrix_y = np.array([[np.cos(angle_y), 0, np.sin(angle_y)],
                                  [0, 1, 0],
                                  [-np.sin(angle_y), 0, np.cos(angle_y)]])
    rotation_matrix_z = np.array([[np.cos(angle_z), -np.sin(angle_z), 0],
                                  [np.sin(angle_z), np.cos(angle_z), 0],
                                  [0, 0, 1]])
    # Combine the rotation matrices into a single rotation matrix
    rotation_matrix = np.dot(rotation_matrix_z, np.dot(rotation_matrix_y, rotation_matrix_x))
    # Rotate each vertex of the cube
    rotated_vertices = np.dot(cube_vertices, rotation_matrix.T)
    return rotated_vertices

# Example usage:
cube_vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                          [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
angle_x = np.pi / 4
angle_y = np.pi / 3
angle_z = np.pi / 6
rotated_vertices = rotate_cube(cube_vertices, angle_x, angle_y, angle_z)
print(rotated_vertices)



import numpy as np

def rotate_cube(vertices, angle_x, angle_y, angle_z):
    cx, cy, cz = vertices.mean(axis=0)
    # Translation to origin
    T = np.array([[1, 0, 0, -cx], [0, 1, 0, -cy], [0, 0, 1, -cz], [0, 0, 0, 1]])
    # Rotation along x-axis
    Rx = np.array([[1, 0, 0, 0], [0, np.cos(angle_x), -np.sin(angle_x), 0], [0, np.sin(angle_x), np.cos(angle_x), 0], [0, 0, 0, 1]])
    # Rotation along y-axis
    Ry = np.array([[np.cos(angle_y), 0, np.sin(angle_y), 0], [0, 1, 0, 0], [-np.sin(angle_y), 0, np.cos(angle_y), 0], [0, 0, 0, 1]])
    # Rotation along z-axis
    Rz = np.array([[np.cos(angle_z), -np.sin(angle_z), 0, 0], [np.sin(angle_z), np.cos(angle_z), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    # Translation back to original position
    Tinv = np.array([[1, 0, 0, cx], [0, 1, 0, cy], [0, 0, 1, cz], [0, 0, 0, 1]])
    # Final transformation matrix
    transform = Tinv @ Rz @ Ry @ Rx @ T
    # Apply transformation to each vertex
    rotated_vertices = np.dot(vertices, transform[:3, :3].T) + transform[:3, 3]
    return rotated_vertices

# Example usage:
vertices = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1], [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]])
rotated_vertices = rotate_cube(vertices, np.pi / 4, np.pi / 4, np.pi / 4)
print(rotated_vertices)

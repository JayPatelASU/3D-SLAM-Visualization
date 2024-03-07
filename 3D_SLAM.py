import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Setting up the figure for our visualization
visualization_figure = plt.figure(figsize=(10, 7))
exploration_space = visualization_figure.add_subplot(111, projection='3d')
visualization_figure.patch.set_color('black')  # Figure background color
exploration_space.set_facecolor('slategray')  # Plotting area background color

# Defining the exploration boundaries
boundary_limit = 30
exploration_space.set_xlim([-boundary_limit, boundary_limit])
exploration_space.set_ylim([-boundary_limit, boundary_limit])
exploration_space.set_zlim([-boundary_limit, boundary_limit])

# Adjusting axes labels and ticks for better visibility
[ax_label.set_color('white') for ax_label in exploration_space.get_xticklabels() + exploration_space.get_yticklabels() + exploration_space.get_zticklabels()]

# Initial setup for the explorer's path and static landmarks
explorer_path = np.array([[0, 0, 0]])  # Start at the origin
fixed_landmarks = np.random.uniform(-boundary_limit, boundary_limit, (20, 3))  # Landmark positions

# Initial rendering of the explorer's path and landmarks with improved aesthetics
path_line, = exploration_space.plot(explorer_path[:, 0], explorer_path[:, 1], explorer_path[:, 2], color='deepskyblue', label='Explorer Path', linewidth=2.5)
landmark_points = exploration_space.scatter(fixed_landmarks[:, 0], fixed_landmarks[:, 1], fixed_landmarks[:, 2], color='magenta', marker='^', s=70, alpha=0.75, label='Landmarks')
exploration_space.legend()

# Function to animate the explorer's movements and path expansion
def animate_explorer(frame):
    global explorer_path
    movement_vector = explorer_path[-1] + np.random.uniform(-1, 1, 3)  # New movement direction
    explorer_path = np.vstack([explorer_path, movement_vector])  # Append the new movement to the path

    # Update the path's visual representation
    path_line.set_data(explorer_path[:, 0], explorer_path[:, 1])
    path_line.set_3d_properties(explorer_path[:, 2])

    # Dynamically adjust the plot's boundaries to keep the path within view
    if np.any(np.abs(movement_vector) > boundary_limit - 5):
        expanded_boundary = np.max(np.abs(explorer_path)) + 10
        exploration_space.set_xlim([-expanded_boundary, expanded_boundary])
        exploration_space.set_ylim([-expanded_boundary, expanded_boundary])
        exploration_space.set_zlim([-expanded_boundary, expanded_boundary])

    return path_line,

# Execute the animation with the updated path color for better visibility
explorer_animation = FuncAnimation(visualization_figure, animate_explorer, frames=100, interval=100, blit=False)

plt.show()

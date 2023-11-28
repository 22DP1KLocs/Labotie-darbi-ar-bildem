#   (__2 figura__)

# import matplotlib.pyplot as plt
# import numpy as np

# def draw_figure():
#     # Define rectangle vertices
#     rectangle_vertices = np.array([[-5, -1], [2, -1], [2, 3], [-5, 3], [-5, -1]])

#     # Plot rectangle
#     plt.plot(rectangle_vertices[:, 0], rectangle_vertices[:, 1], color='blue', linestyle='-', linewidth=2, label='Figure')

#     # Set plot limits
#     plt.xlim(-7, 4)
#     plt.ylim(-3, 5)

#     # Draw coordinate plane
#     plt.axhline(0, color='black', linewidth=0.5)
#     plt.axvline(0, color='black', linewidth=0.5)

#     # Add labels and legend
#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
#     plt.title('Figure Visualization')

#     # Get user input
#     x = float(input("Ievadi x: "))
#     y = float(input("Ievadi y: "))

#     # Plot the input point
#     plt.plot(x, y, 'ro', label='Input Point')

#     # Check the point based on the check_cordinates function
#     if (y >= -1 and y <= 3 and (x == -5 or x == 2)) or (x >= -5 and x <= 2 and (y == -1 or y == 3)):
#         plt.plot(x, y, 'go', label='On Figure Boundary')
#     elif x > -5 and x < 2 and y > -1 and y < 3:
#         plt.plot(x, y, 'yo', label='Inside Figure')
#     else:
#         plt.plot(x, y, 'ro', label='Outside Figure')

#     # Add legend
#     plt.legend()

#     # Show the plot
#     plt.grid(True)
#     plt.show()

# # Call the draw_figure function
# draw_figure()


# fuigura 3 _------------------_

# import matplotlib.pyplot as plt
# import numpy as np

# def funkcija(x, y):

#     if x == -1 and y >= 0 and y <= 4.5 or y == 0 and x >= -1 and x <= 2 or round(y, 4) == round(-1.5 * x + 3, 2):
#         return 2  # Uz robežas
#     elif x > -1 and x < 2 and y > 0 and y < 4.5 and round(y, 2) < round(-1.5 * x + 3, 2):
#         return 3  # Iekšā figūrā
#     else:
#         return 1  # Ārpus figūrai

# def draw_figure():
#     # Define triangle vertices
#     triangle_vertices = np.array([[-1, 0], [2, 0], [0.5, 4.5], [-1, 0]])

#     # Plot triangle
#     plt.plot(triangle_vertices[:, 0], triangle_vertices[:, 1], color='blue', linestyle='-', linewidth=2, label='Figure')

#     # Set plot limits
#     plt.xlim(-2, 3)
#     plt.ylim(-2, 5)

#     # Draw coordinate plane
#     plt.axhline(0, color='black', linewidth=0.5)
#     plt.axvline(0, color='black', linewidth=0.5)

#     # Add labels and legend
#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
#     plt.title('Figure Visualization')

#     # Get user input
#     x = float(input("Ievadi x: "))
#     y = float(input("Ievadi y: "))

#     # Plot the input point
#     plt.plot(x, y, 'ro', label='Input Point')

#     # Check the point based on the funkcija function
#     result = funkcija(x, y)
#     if result == 2:
#         plt.plot(x, y, 'go', label='On the Border')
#     elif result == 3:
#         plt.plot(x, y, 'yo', label='Inside Figure')
#     else:
#         plt.plot(x, y, 'ro', label='Outside Figure')

#     # Add legend
#     plt.legend()

#     # Show the plot
#     plt.grid(True)
#     plt.show()

# # Call the draw_figure function
# draw_figure()

# figura 4

# import matplotlib.pyplot as plt
# import numpy as np

# def draw_figure():
#     # Define circle parameters
#     l, k = 0, 0
#     radius = 1

#     # Create circle
#     circle = plt.Circle((l, k), radius, color='blue', fill=False, label='Figure')

#     # Set plot limits
#     plt.xlim(-2, 2)
#     plt.ylim(-2, 2)

#     # Draw coordinate plane
#     plt.axhline(0, color='black', linewidth=0.5)
#     plt.axvline(0, color='black', linewidth=0.5)

#     # Add labels and legend
#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
#     plt.title('Figure Visualization')

#     # Get user input
#     x = float(input("Ievadi x: "))
#     y = float(input("Ievadi y: "))

#     # Plot the input point
#     plt.plot(x, y, 'ro', label='Input Point')

#     # Check the point based on the check_cordinates function
#     distance = np.sqrt((x - l)**2 + (y - k)**2)
#     if distance == radius:
#         plt.plot(x, y, 'go', label='On the Border')
#     elif distance < radius:
#         plt.plot(x, y, 'yo', label='Inside Figure')
#     else:
#         plt.plot(x, y, 'ro', label='Outside Figure')

#     # Add circle to plot
#     plt.gca().add_patch(circle)

#     # Add legend
#     plt.legend()

#     # Show the plot
#     plt.grid(True)
#     plt.show()

# # Call the draw_figure function
# draw_figure()

# 5 figura


import matplotlib.pyplot as plt
import numpy as np

def draw_figure():
    # Define trapezoid vertices
    trapezoid_vertices = np.array([[-4, 4], [8.3, 4], [4, 8], [-2.9, 8], [-4, 4]])

    # Plot trapezoid
    plt.plot(trapezoid_vertices[:, 0], trapezoid_vertices[:, 1], color='blue', linestyle='-', linewidth=2, label='Figure')

    # Set plot limits
    plt.xlim(-5, 9)
    plt.ylim(3, 9)

    # Draw coordinate plane
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Add labels and legend
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Figure Visualization')

    # Get user input
    x = float(input("Ievadi x: "))
    y = float(input("Ievadi y: "))

    # Plot the input point
    plt.plot(x, y, 'ro', label='Input Point')

    # Check the point based on the check_cordinates function
    if (y == 4 and x >= -4 and x < 8.3 or
        y == 8 and x >= -2.9 and x <= 4) or \
            round(y, 4) == round(6/1.1*x + 26.2/1.1, 4) or \
            round(y, 4) == round(-6/4.3*x + 58.4/4.3, 4):
        plt.plot(x, y, 'go', label='On the Border')
    elif -4 < x < 8.3 and 4 < y < 8 and round(y, 4) < round(6/1.1*x + 26.2/1.1, 4) and round(y, 4) < round(-6/4.3*x + 58.4/4.3, 4):
        plt.plot(x, y, 'yo', label='Inside Figure')
    else:
        plt.plot(x, y, 'ro', label='Outside Figure')

    # Add legend
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()

# Call the draw_figure function
draw_figure()

import random
import matplotlib.pyplot as plt
#50 random walkers will take 10000 steps each
for walker in range(50):
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)

    x_positions = [x]
    y_positions = [y]
    #every walker will take 10000 steps in a random direction
    for step in range(50):
        direction = random.choice(['up', 'down', 'left', 'right'])

        if direction == 'right':
            x = x + 1

        elif direction == 'left':
            x = x - 1

        elif direction == 'up':
            y = y + 1

        elif direction == 'down':
            y = y - 1

        x_positions.append(x)
        y_positions.append(y)
    #draw the each random walk
    plt.plot(x_positions, y_positions, alpha=0.6, linewidth=1)

plt.scatter(0, 0, color='green', s=100, label='Start')
plt.title("50 Independent 2D Random Walks")
plt.legend()
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.grid()
plt.axis('equal')
plt.show()

import random
import matplotlib.pyplot as plt
position = 0
#Every time it moves, we'll add its new position to the list using:
positions = [position]
for step in range(50):
    move = random.choice([-1, 1])
    position += move
    positions.append(position)

#draw the random walk
plt.scatter(0, [positions[0]], color='green', label='Start')
plt.scatter(len(positions)-1, [positions[-1]], color='red', label='End')
plt.legend()
plt.xlabel('Step')
plt.ylabel('Position')
plt.title('Random Walk')
plt.grid(True)
plt.show()
import numpy as np
scores = np.array([
    [12, 18, 20, 15],
    [10, 25, 18, 22],
    [30, 12, 15, 20],
    [25, 18, 22, 10]
])
total=np.sum(scores,axis=1)
print("Total score per player",total)
print("Player with the highest total score",np.argmax(total))
avg=np.mean(scores,axis=0)>20
print("Games where average score > 20",avg)
scores[scores<15]=0
print("Replace all scores < 15 with 0",scores)

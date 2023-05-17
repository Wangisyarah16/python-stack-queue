#queue sederhana
from collections import deque

queue = deque([1,2,3,4,5])
print('antrian sekarang:', queue)

queue.append(6)
print('tumpukan masuk:',6)
print('tumpukan sekarang: ',queue)

queue.append(7)
print('tumpukan masuk:',7)
print('tumpukan sekarang: ',queue)

out = queue.popleft()
print('tumpukan masuk:',out)
print('tumpukan sekarang: ',queue)
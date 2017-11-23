import json
import pickle
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))
print(pickle.dumps(d))

with open('CMakeLists.txt','wb') as r:
    pickle.dump(d,r)
with open('CMakeLists.txt','rb') as r:
    print(pickle.load(r))


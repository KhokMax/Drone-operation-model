from cargo import Cargo
from drons import Dron, Base
from datetime import datetime, timedelta
from functions import *
import matplotlib.pyplot as plt
import random




dron = Dron(0)
base = Base()
cargos = [Cargo(i) for i in range(70)]
cargos_1 = cargos.copy()

for cargo in cargos:
    print(cargo.id , cargo.weight)


result = []
all_time = 0
while len(cargos) > 0:
   res, cargos, time = kneckpack_1(dron, cargos, base, 0)
   all_time += time
   result.append(res)

print(timedelta(seconds=all_time))

fig, ax = plt.subplots()
plt.scatter(0, 0, s=100, marker='D')

for col,cargos in enumerate(result):
    x = [cargo.x for cargo in cargos]
    y = [cargo.y for cargo in cargos]

    plt.plot(x, y, color='b', zorder=1)
    plt.scatter(x, y, color='y')
    plt.scatter(x[0], y[0], marker='s', s=45, color='r')
    for i in range(len(cargos)):
        ax.annotate(str(cargos[i].id), (cargos[i].x + 0.4, cargos[i].y), size=10)

plt.show()


dron.charge_dron()
cargos = cargos_1
for cargo in cargos:
    print(cargo.id , cargo.weight)


result = []
all_time = 0
while len(cargos) > 0:
   res, cargos, time = kneckpack(dron, cargos, base, 0)
   all_time += time
   result.append(res)

print(timedelta(seconds=all_time))

fig, ax = plt.subplots()
plt.scatter(0, 0, s=100, marker='D')

for col,cargos in enumerate(result):
    x = [cargo.x for cargo in cargos]
    y = [cargo.y for cargo in cargos]

    plt.plot(x, y, color='b', zorder=1)
    plt.scatter(x, y, color='y')
    plt.scatter(x[0], y[0], marker='s', s=45, color='r')
    for i in range(len(cargos)):
        ax.annotate(str(cargos[i].id), (cargos[i].x + 0.4, cargos[i].y), size=10)

plt.show()

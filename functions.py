from cargo import Cargo
from math import sqrt
from datetime import datetime
from drons import Base
from datetime import timedelta

e = 10**(-10)


def search_distance(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def profit_count(base, cargo, res_last):
    return 1/(search_distance(base, cargo) + 3 * search_distance(cargo, res_last))

def kneckpack(dron, cargos, base, time):

    if dron.charge_percentage <= 20:
        time += (100 - dron.charge_percentage) * 3
        dron.charge_dron()


    res = []
    weight = [cargo.weight for cargo in cargos]
    profit = [cargo.profit for cargo in cargos]


    #print(weight)

    p_w = [(profit[i] / (sum(profit)/len(profit))) + (weight[i] / (sum(weight)/len(weight)))  for i in range(len(cargos))]
    res.append(cargos[p_w.index(max(p_w))])
    weight.pop(p_w.index(max(p_w)))
    profit.pop(p_w.index(max(p_w)))
    cargos.pop(p_w.index(max(p_w)))

    current_weight = res[-1].weight

    while True:

        if len(cargos) == 0:
            break

        profit = [profit_count(base, cargo, res[-1]) for cargo in cargos]
        p_w = [profit[i] * (weight[i]**(1/8)) for i in range(len(cargos))]

        if search_distance(res[-1], base) * 1.5 < search_distance(res[-1], cargos[p_w.index(max(p_w))]):
            break

        # chek allowable weight
        current_weight += cargos[profit.index(max(profit))].weight
        if current_weight >= dron.max_weight:
            break

        # chek allowable energy
        new_res = res.copy()
        new_res.append(cargos[profit.index(max(profit))])
        if energy_count(base, new_res) > dron.charge_percentage:
            break

        res.append(cargos[p_w.index(max(p_w))])
        weight.pop(p_w.index(max(p_w)))
        profit.pop(p_w.index(max(p_w)))
        cargos.pop(p_w.index(max(p_w)))

    # update time
    time += count_time(res, base)

    # update dron`s energy percentage
    dron.update_percentage(energy_count(base, res))

    print('used percentage:', energy_count(base, res))
    print('percentage of charge:', dron.charge_percentage)

    for cargo in res:
        print(cargo.id)

    print('________________')
    return res, cargos, time

#--------------------------------------------------#
#--------------------------------------------------#
def count_time(res, base):
    distance = 0
    for i in range(len(res)):
        if i == 0:
            distance += search_distance(base, res[i]) * 100
        else:
            distance += search_distance(res[i - 1], res[i]) * 100
    distance += search_distance(base, res[-1]) * 100
    print('distance:',distance)
    print('time:',timedelta(seconds=distance / 14))
    return distance / 14

def energy_count(base, res):
    all_weight = sum([cargo.weight for cargo in res])
    energy = 0
    for i in range(len(res)):
        if i == 0:
            distance = search_distance(base, res[i])/10
        else:
            distance = search_distance(res[i-1], res[i])/10

        energy += distance * 1 + distance * (all_weight/1000) * 2.5
        all_weight -= res[i].weight
    energy += (search_distance(base, res[-1])/10) * 1
    return energy


def profit_count_1(object, cargo, weights, distances):
    weight_kof = cargo.weight / (sum(weights) / len(weights))
    distances_kof = search_distance(object, cargo) / (sum(distances) / len(distances))
    return sqrt(weight_kof) + 2 / (distances_kof + e)


def kneckpack_1(dron, cargos, base, time):

    if dron.charge_percentage <= 20:
        time += (100 - dron.charge_percentage) * 3
        dron.charge_dron()

    res = []
    weights = [cargo.weight for cargo in cargos]
    distances = [search_distance(base, cargo) for cargo in cargos]
    profit = [profit_count_1(base, cargo, weights, distances) for cargo in cargos]


    res.append(cargos[profit.index(max(profit))])
    weights.pop(profit.index(max(profit)))
    cargos.pop(profit.index(max(profit)))

    current_weight = res[-1].weight

    while True:
        # chek cargos len is not null
        if len(cargos) == 0:
            break

        distances = [search_distance(res[-1], cargo) for cargo in cargos]
        profit = [profit_count_1(res[-1], cargo, weights, distances) for cargo in cargos]

        # chek allowable weight
        current_weight += cargos[profit.index(max(profit))].weight
        if current_weight >= dron.max_weight:
            break

        # chek allowable energy
        new_res = res.copy()
        new_res.append(cargos[profit.index(max(profit))])
        if energy_count(base, new_res) > dron.charge_percentage:
            break


        res.append(cargos[profit.index(max(profit))])
        weights.pop(profit.index(max(profit)))
        cargos.pop(profit.index(max(profit)))

    # update time
    time += count_time(res, base)

    # update dron`s percentage of charge
    dron.update_percentage(energy_count(base, res))

    print('used percentage:', energy_count(base, res))
    print('percentage of charge:', dron.charge_percentage)

    for cargo in res:
        print(cargo.id)

    print('_____________')
    return res, cargos, time

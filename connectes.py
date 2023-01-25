#!/usr/bin/env python3
"""
fonzoef
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv

from geo.point import Point 


def load_instance(filename: str):
    """
    loads .pts file.
    returns distance limit and points.
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        points = [Point([float(f) for f in l.split(",")]) for l in lines]

    return distance, points

def liste_adjacence(distance: float, points: list[Point]):
    """Renvoit un dictionnaire ayant pour entrée les points et affichant
    la liste de leurs points adjascents
    """
    adj_list = {}
    for point in points:
        adj_list[point] = []
        for autre_point in points:
            if point.distance_to(autre_point) < distance:
                adj_list[point].append(autre_point)
    return adj_list

def liste_composantes(adj_list):
    """
    Renvoit la liste des composantes à partir des listes d'adjacence
    """
    vus = []
    def composante(adj_list, composante_courante):
        res = []
        for elem in adj_list:
            if elem not in vus:
                vus.append(elem)
                res += composante(adj_list, composante_courante + [elem])
        return res
    composantes = []
    for point, adj in adj_list.items():
        composante_courante = [point]
        if point not in vus:
            composantes.append(composante(adj, composante_courante))
    return composantes



def print_components_sizes(distance: float, points: list[Point]):
    """
    affichage des tailles triees de chaque composante
    """
    adj_list = liste_adjacence(distance, points)
    composantes = liste_composantes(adj_list)
    tailles = [len(compo) for compo in composantes]
    tailles.sort()
    print(tailles)

def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()

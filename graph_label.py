class Vertex:
    value = 0


dict = {0: [1, 3, 5], 1: [0, 2], 2: [1], 3: [0, 4],
        4: [3], 5: [0, 6], 6: [5]}


def construct_graph(dict):
    graph = []
    for i in range(len(dict)):
        graph.append([Vertex(), []])

    for i in range(len(graph)):
        inc_indices = dict[i]
        inc_vertices = graph[i][1]
        for j in inc_indices:
            inc_vertices.append(graph[j][0])
    return graph


graph = construct_graph(dict)

import itertools


def find_graceful(graph, ends=True, debug=False):
    end_vectors = []
    symmetric_group = itertools.permutations(list(range(len(graph))))
    for perm in symmetric_group:
        for i in range(len(perm)):
            graph[i][0].value = perm[i]
        edge_differences = {}
        for i in range(len(graph)):
            value = graph[i][0].value
            inc_vertices = graph[i][1]
            for vertex in inc_vertices:
                diff = abs(value - vertex.value)
                if diff not in edge_differences:
                    edge_differences[diff] = 1
                else:
                    edge_differences[diff] += 1
        edges = len(graph) - 1
        if len(edge_differences) == edges:
            leaves = []
            for i in range(len(graph)): 
                if len(graph[i][1]) == 1:
                    leaves.append(graph[i][0].value)
            if leaves not in end_vectors:
                end_vectors.append(leaves)
            if debug:
                string = ""
                for i in range(len(graph)):
                    string += str(i) + " : " + str(graph[i][0].value) + ", "
                print(string)

    return end_vectors

def fact(n):
    temp = 1
    for i in range(2, n+1):
        temp *= i
    return temp


def find_perm_density(end_vectors, graph):
    return float(len(end_vectors)) / float(fact(len(graph)))


def write_end_vecs(end_vectors, f, math=True):
    for vec in end_vectors:
        if not math:
            f.write("1 ")
        for i in range(len(vec)):
            f.write(str(vec[i]))
            if i != len(vec)-1:
                f.write(" ")
            else:
                f.write("\n")


def get_graceful_data(dict, filename, math=False, debug=False):
    graph = construct_graph(dict)
    end_vectors = find_graceful(graph, debug=debug)
    if math:
        f = open(filename + 'math', 'w')
        write_end_vecs(end_vectors, f)
        f.close()
    f = open(filename, 'w')
    f.write(str(len(end_vectors))+' ' + str(1 + len(end_vectors[0])) + '\n')
    write_end_vecs(end_vectors, f, math=False)
    f.close()
    f = open(filename + 'density', 'w')
    f.write("number graceful ends: "+str(len(end_vectors))+"\\\\number permutations: "+str(fact(len(graph)))+\
            "="+str(len(graph))+"!\\\\permutation density: "+str(find_perm_density(end_vectors, graph))+"\\\\")
    f.close()
    f = open(filename+'poly', 'w')
    write_end_vecs(end_vectors, f, math=False)
    f.close()


def run_on_graphs():
    dict = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0]}
    get_graceful_data(dict, '1-1-1')

    dict = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [3]}
    get_graceful_data(dict, '2-1-1')

    dict = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [3, 5], 5: [4]}
    get_graceful_data(dict, '3-1-1')

    dict = {0: [1, 2, 4], 1: [0], 2: [0, 3], 3: [2], 4: [0, 5], 5: [4]}
    get_graceful_data(dict, '2-2-1')

    dict = {0: [1, 2, 3], 1: [0], 2: [0], 3: [
        0, 4], 4: [3, 5], 5: [4, 6], 6: [5]}
    get_graceful_data(dict, '4-1-1')

    dict = {0: [1, 2, 4], 1: [0], 2: [0, 3],
            3: [2], 4: [0, 5], 5: [4, 6], 6: [5]}
    get_graceful_data(dict, '3-2-1')

    dict = {0: [1, 3, 5], 1: [0, 2], 2: [1],
            3: [0, 4], 4: [3], 5: [0, 6], 6: [5]}
    get_graceful_data(dict, '2-2-2')

    dict = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4],
            4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6]}
    get_graceful_data(dict, '5-1-1')

    dict = {0: [1, 2, 4], 1: [0], 2: [0, 3], 3: [
        2], 4: [0, 5], 5: [4, 6], 6: [5, 7], 7: [6]}
    get_graceful_data(dict, '4-2-1')

    dict = {0: [1, 2, 5], 1: [0], 2: [0, 3], 3: [
        2, 4], 4: [3], 5: [0, 6], 6: [5, 7], 7: [6]}
    get_graceful_data(dict, '3-3-1')

    dict = {0: [1, 3, 5], 1: [0, 2], 2: [1], 3: [
        0, 4], 4: [3], 5: [0, 6], 6: [5, 7], 7: [6]}
    get_graceful_data(dict, '3-2-2')

    dict = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [
        3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7]}
    get_graceful_data(dict, '6-1-1')

    dict = {0: [1, 2, 4], 1: [0], 2: [0, 3], 3: [2], 4: [
        0, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7]}
    get_graceful_data(dict, '5-2-1')

    dict = {0: [1, 2, 5], 1: [0], 2: [0, 3], 3: [2, 4],
            4: [3], 5: [0, 6], 6: [5, 7], 7: [6, 8], 8: [7]}
    get_graceful_data(dict, '4-3-1')

    dict = {0: [1, 3, 5], 1: [0, 2], 2: [1], 3: [0, 4],
            4: [3], 5: [0, 6], 6: [5, 7], 7: [6, 8], 8: [7]}
    get_graceful_data(dict, '4-2-2')

    dict = {0: [1, 3, 6], 1: [0, 2], 2: [1], 3: [0, 4],
            4: [3, 5], 5: [4], 6: [0, 7], 7: [6, 8], 8: [7]}
    get_graceful_data(dict, '3-3-2')

run_on_graphs()

files = ['1-1-1', '2-1-1', '3-1-1', '2-2-1', '4-1-1', '3-2-1', '2-2-2', '5-1-1',
         '4-2-1', '3-3-1', '3-2-2', '6-1-1', '5-2-1', '4-3-1', '4-2-2', '3-3-2']

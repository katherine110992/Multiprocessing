import multiprocessing


def create_graph(vertex, nodes):
    return list(range(vertex * nodes))


def start_process():
    print('Starting', multiprocessing.current_process().name)

if __name__ == '__main__':
    vertex_1 = 20
    vertex_2 = 30
    nodes_1 = 10
    nodes_2 = 30

    inputs = list()
    inputs.append([vertex_1, nodes_1])
    inputs.append([vertex_2, nodes_2])

    pool = multiprocessing.Pool(processes=2, initializer=start_process,)
    pool_outputs = pool.starmap(create_graph, inputs)
    pool.close()  # no more tasks
    pool.join()  # wrap up current tasks

    graph_1 = pool_outputs[0]
    graph_2 = pool_outputs[1]
    print(graph_1)
    print(graph_2)

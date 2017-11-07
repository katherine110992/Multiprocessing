from multiprocessing import Process, Queue


def create_graph(number, vertex, nodes, queue):
    queue.put([number, vertex * nodes])
    return

if __name__ == '__main__':
    queue = Queue()

    vertex_1 = 20
    vertex_2 = 30
    nodes_1 = 10
    nodes_2 = 30

    graph_process_1 = Process(target=create_graph, args=(1, vertex_1, nodes_1, queue))
    graph_process_2 = Process(target=create_graph, args=(2, vertex_2, nodes_2, queue))

    graph_process_1.start()
    graph_process_2.start()

    graph_process_1.join()
    graph_process_2.join()

    while not queue.empty():
        print(queue.get())

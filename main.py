from queue import PriorityQueue
import json
import math

# test
# test2

# makes json files into dictionaries
def read_json():
    names = ["Coord", "Cost", "Dist", "G"]
    files = {}
    for name in names:
        f = open("./data/" + name + ".json", "r")
        data = json.loads(f.read())
        # print(data[0])
        files[name] = data
    # print(names)
    return files

# find the direct distance (for hauristic)
def find_dist (node1, node2, files):
    return math.sqrt((files["Coord"][node2][0] - files["Coord"][node1][0])^2 
                + (files["Coord"][node2][1] - files["Coord"][node1][1])^2)

# prints final results
def print_results (goal, parent_reference, dist):
    path = [goal]
    current_child = goal
    while parent_reference[current_child] != "":
        current_child = parent_reference[current_child]
        print(current_child)
        path.append(current_child)
    pathway = ""
    for i in reversed(path):
        pathway += i + " -> "
    print(pathway.strip(' -> '))
    
# only depending on distance for now
def ucs_algo(src, goal, files):
    sortedqueue = PriorityQueue()
    sortedqueue.put((0, src))
    dist_till_now = {src: 0.0}
    parent_reference = {src: ""}

    # prev_node = ""
    # dist = 0
    # visited = []
    while not sortedqueue.empty():

        current_node = sortedqueue.get()[1]
        # visited.append(current_node)
        print(current_node)
        if(current_node == goal):
            print_results(current_node, parent_reference, dist_till_now[current_node])
            return dist_till_now[current_node]
        else:
            for adj_node in files["G"][current_node]:
                print("adj: " + adj_node)
                new_dist = 0.0
                new_dist = (files["Dist"][current_node + "," + adj_node] + dist_till_now[current_node])
                if adj_node not in dist_till_now or new_dist < dist_till_now[adj_node]:
                    dist_till_now[adj_node] = new_dist
                    sortedqueue.put((new_dist, adj_node))
                    parent_reference[adj_node] = current_node
                # print(sortedqueue)
                print(dist_till_now)


def main():
    files = read_json()
    print(files["Coord"]["1"])
    print(ucs_algo("1", "13", files))


if __name__ == "__main__":
    main()
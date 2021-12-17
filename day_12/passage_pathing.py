from pathlib import Path
from path import PathTracker, PathTracker2


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def parse_input(input_string):
    nodes = set()
    edges = dict()
    for line in input_string.split("\n"):
        edge = line.split("-")
        nodes.update(edge)

        for i in [0, 1]:
            edges[edge[i]] = edges.get(edge[i], []) + [edge[1 - i]]

    return nodes, edges


def part_one(input_string=INPUT_STRING, PathClass=PathTracker):
    _, edges = parse_input(input_string)

    active_paths = [PathClass() + "start"]
    finished_paths = []
    stranded_paths = []

    while active_paths:
        path = active_paths.pop(0)
        available_nodes = [
            node for node in edges[path.current_node()] if path.is_available(node)
        ]
        if available_nodes:
            new_paths = [(path + node) for node in available_nodes]
            for new_path in new_paths:
                if new_path.current_node() == "end":
                    finished_paths.append(new_path)
                else:
                    active_paths.append(new_path)
        else:
            stranded_paths.append(path)

    # print("Finished paths:\n", "\n".join(str(path) for path in finished_paths))
    # print("Stranded paths:\n", "\n".join(str(path) for path in stranded_paths))
    print(f"{len(finished_paths)} paths finished, {len(stranded_paths)} stranded")
    return len(finished_paths)


def part_two(input_string=INPUT_STRING):
    part_one(input_string, PathClass=PathTracker2)


if __name__ == "__main__":
    part_one()
    part_two()

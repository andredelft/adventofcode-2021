from pathlib import Path
import re
import numpy as np
from distance import DistanceTable


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def iterate_indices(height, length):
    for i in range(height):
        for j in range(length):
            yield (i, j)


def yield_neighbours(position, height, length):
    i, j = position
    if i > 0:
        yield (i - 1, j)
    if j > 0:
        yield (i, j - 1)
    if i < height - 1:
        yield (i + 1, j)
    if j < length - 1:
        yield (i, j + 1)


def parse_input(input_string):
    array = np.array(
        [
            [int(n) for n in re.findall(r"\d", line)]
            for line in input_string.split("\n")
            if line
        ]
    )
    if not all(len(line) == len(array[0]) for line in array):
        raise ValueError("Not all lines are equal")
    return array


def part_one(input_string=INPUT_STRING):
    array = parse_input(input_string)
    height, length = array.shape

    positions = list(iterate_indices(height, length))

    current_position = (0, 0)
    current_distance = 0

    target_position = (height - 1, length - 1)
    distance_table = DistanceTable(positions=positions)
    distance_table[current_position].shortest_distance = 0

    visited = set()
    unvisited = set(positions)

    # Dijkstra's algorithm: https://medium.com/swlh/pathfinding-algorithms-6c0d4febe8fd
    while unvisited:
        print(len(unvisited), end="\n\n")

        # Visit the unvisited vertex with the smallest known distance from the start vertex
        current_distance_entry = distance_table.get_shortest_distance_entry(
            position_filter=unvisited
        )

        current_position = current_distance_entry.position
        current_distance = current_distance_entry.shortest_distance

        neighbours = list(yield_neighbours(current_position, height, length))

        # For the current position, calculate the distance of each neighbour from the start position
        for neighbour in neighbours:
            dist_to_neighbour = current_distance + array[neighbour]
            if (
                not distance_table[neighbour].shortest_distance
                or distance_table[neighbour].shortest_distance > dist_to_neighbour
            ):
                # Update values if we found a smaller position or none is yet defined
                distance_table[neighbour].shortest_distance = dist_to_neighbour
                distance_table[neighbour].prev_pos = current_position

        visited.add(current_position)
        unvisited.remove(current_position)

    distance_entry = distance_table[target_position]
    print(f"Shortest route to end is {distance_entry.shortest_distance} units long")
    return distance_entry.shortest_distance


def part_two(input_string=INPUT_STRING):
    parsed_input = parse_input(input_string)


if __name__ == "__main__":
    part_one()
    part_two()

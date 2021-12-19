class DistanceEntry:
    def __init__(self, position, shortest_distance=None, prev_pos=None):
        self.position = position
        self.shortest_distance = shortest_distance
        self.prev_pos = prev_pos

    def __lt__(self, other):
        if self.shortest_distance and other.shortest_distance:
            return self.shortest_distance < other.shortest_distance
        else:
            raise ValueError("No comparison is possible between these distance entries")

    def __le__(self, other):
        if self.shortest_distance and other.shortest_distance:
            return self.shortest_distance <= other.shortest_distance
        else:
            raise ValueError("No comparison is possible between these distance entries")

    def __gt__(self, other):
        if self.shortest_distance and other.shortest_distance:
            return self.shortest_distance > other.shortest_distance
        else:
            raise ValueError("No comparison is possible between these distance entries")

    def __ge__(self, other):
        if self.shortest_distance and other.shortest_distance:
            return self.shortest_distance >= other.shortest_distance
        else:
            raise ValueError("No comparison is possible between these distance entries")

    def __eq__(self, other):
        if self.shortest_distance and other.shortest_distance:
            return self.shortest_distance == other.shortest_distance
        else:
            raise ValueError("No comparison is possible between these distance entries")

    def __ne__(self, other):
        if self.shortest_distance and other.shortest_distance:
            return self.shortest_distance != other.shortest_distance
        else:
            raise ValueError("No comparison is possible between these distance entries")


class DistanceTable:
    def __init__(self, positions):
        self._distance_table = {
            position: DistanceEntry(position) for position in positions
        }

    def __getitem__(self, pos):
        return self._distance_table[pos]

    def yield_visited(self, pos):
        distance_entry = self._distance_table[pos]
        while distance_entry.prev_pos != None:
            yield distance_entry.prev_pos
            distance_entry = self._distance_table[distance_entry.prev_pos]

    def get_shortest_distance_entry(self, position_filter=set()):
        distance_entries = [
            distance_entry
            for distance_entry in self._distance_table.values()
            if distance_entry.shortest_distance != None
        ]

        if position_filter:
            distance_entries = [
                distance_entry
                for distance_entry in distance_entries
                if distance_entry.position in position_filter
            ]

        return min(distance_entries)

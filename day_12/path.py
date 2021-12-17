class NodeNotAvailable(Exception):
    pass


class PathTracker(object):
    def __init__(self, visited: set = set(), path: list[str] = []):
        self.visited = visited
        self.path = path

    def __repr__(self):
        return f"<Path: {self}>"

    def __str__(self):
        return ",".join(self.path) if self.path else "[]"

    def __add__(self, node: str):

        if not isinstance(node, str):
            raise TypeError("Only addition with strings is possible")

        visited, path = self.visited.copy(), self.path.copy()
        self.add(node, visited)
        path.append(node)
        return self.__class__(visited, path)

    def add(self, node, visited):
        if self.is_available(node):
            visited = self._add_node_to_visited(visited, node)
        else:
            raise NodeNotAvailable("Node not available")

    def current_node(self):
        return self.path[-1] if self.path else None

    def is_available(self, node: str):
        return node.isupper() or node not in self.visited

    def _add_node_to_visited(self, visited: set, node: str):
        visited.add(node)
        return visited


class PathTracker2(PathTracker):
    def __init__(self, visited: dict[str, int] = dict(), path: list[str] = []):
        self.visited = visited
        self.path = path

    def is_available(self, node: str):
        num_visits = self.visited.get(node, 0)
        if node.isupper():
            return True
        elif node in ["start", "end"]:
            return num_visits == 0
        else:
            return num_visits < 2

    def _add_node_to_visited(self, visited: dict[str, int], node: str):
        print(list(visited.values()))
        visited[node] = visited.get(node, 0) + 1
        return visited

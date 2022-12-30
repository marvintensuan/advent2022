import networkx as nx  # type: ignore


def generate_DiGraph(instructions: list[str]):

    curr_path: list[str] = []
    tree = nx.DiGraph()

    for io in instructions:
        if (pref_cd := "$ cd ") in io:
            arg = io.removeprefix(pref_cd)
            curr_path.pop() if arg == ".." else curr_path.append(arg)
            continue
        if "$ ls" in io:
            continue

        desc, node = io.split(" ")
        lbl = lambda x: f"{'/'.join(curr_path)}/{x}"
        node = lbl(node)
        tree.add_edge("/".join(curr_path), node)

        nx.set_node_attributes(tree, values={node: (desc == "dir")}, name="is_dir")
        nx.set_node_attributes(
            tree, values={node: (int(desc) if desc.isnumeric() else None)}, name="filesize"
        )

    return tree


def get_filesize_of(node_label: str) -> int:
    return sum(
        [
            size
            for n in nx.descendants(tree, node_label)
            if (size := tree.nodes[n]["filesize"]) is not None
        ]
    )


with open("inputs/day07_part1.txt") as f:
    data = f.read().splitlines()

tree = generate_DiGraph(data)


def part1(tree=tree) -> int:
    dir_map = nx.get_node_attributes(tree, "is_dir")
    dir_sizes = [get_filesize_of(key) for key, value in dir_map.items() if value]
    return sum(filter(lambda x: x <= 100_000, dir_sizes))


def part2(tree=tree, total_space=70_000_000, space_required=30_000_000) -> int:
    """Given `total_space` and `space_required`, give the size of the directory which could be deleted to free up space."""

    space_used_current = get_filesize_of("/")
    to_delete = space_required - (total_space - space_used_current)

    assert total_space == space_used_current + (space_required - to_delete), "Algebra."

    dir_map: dict[str, bool] = nx.get_node_attributes(tree, "is_dir")
    dir_sizes = sorted(
        [
            size
            for key, value in dir_map.items()
            if value and (size := get_filesize_of(key)) >= to_delete
        ]
    )

    return min(dir_sizes)


print(f"{part1(tree)=:,}")
print(f"{part2(tree)=:,}")

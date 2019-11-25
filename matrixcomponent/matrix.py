"""Python object models to be manipulated"""
import json
from dataclasses import dataclass
from typing import List, Any, Set


## GraphPath is all for input files

class GraphPath:
    name: str
    links: 'List[GraphPath.LinkEntry]'
    bins: 'List[GraphPath.Bin]'
    bin_set: []
    mapping_id2idx: {}

    def __init__(self, name=''):
        self.name = name
        self.bins = []  # Bin
        self.links = []  # LinkEntry
        self.bin_set = set()
        self.mapping_id2idx = dict()

    class Bin:
        next_bin: int

        def __init__(self):
            self.bin_id = 0
            self.coverage = 0
            self.inversion_rate = 0
            self.mean_pos = 0
            self.sequence = ''
            self.next_bin = 0

        def set(self, bin_id, coverage, inversion_rate, mean_pos, sequence=''):
            self.bin_id = bin_id
            self.coverage = coverage
            self.inversion_rate = inversion_rate
            self.mean_pos = mean_pos
            self.sequence = sequence
            self.next_bin = 0

    class LinkEntry:
        def __init__(self, upstream, downstream):
            self.upstream = upstream
            self.downstream = downstream
            # TODO: self.insert_size will require a topology search to find this

    def __contains__(self, item):  # used by " x in Path "
        return item in self.bin_set

    def finalize_bins(self):
        self.bin_set = {x.bin_id for x in self.bins}  # build and cache a set



## For Output to RDF  ###########
@dataclass
class LinkColumn:
    upstream: int
    downstream: int
    participants: Set[str]  # path names


class Component:
    """Block of co-linear variation within a Graph Matrix"""
    first_bin: int
    last_bin: int
    # active_members: int
    arrivals: List[LinkColumn]
    departures: List[LinkColumn]

    def __init__(self, first_bin: int, last_bin: int):
        self.first_bin = first_bin
        self.last_bin = last_bin
        # bin_id and seq are global to column and could be reduced to save memory,
        # careful construction can reuse Bin.sequence memory pointer
        self.arrivals = []  # reverse ordered Links
        self.departures = []  # ordered Links


@dataclass
class PangenomeSchematic:
    components: List[Component]
    path_names: List[str]
    break_points: List[dict]

    def json_dump(self):
        def dumper(obj):
            if isinstance(obj, set):
                return list(obj)
            try:
                return obj.__dict__
            except:
                return obj

        return json.dumps(self, default=dumper, indent=4)


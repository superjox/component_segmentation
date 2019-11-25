import json
import logging
from matrixcomponent.matrix import GraphPath

LOGGER = logging.getLogger(__name__)

def parse(file):
        data = []
        with open(file) as f:
            for line in f:
                data.append(json.loads(line))

        paths = []
        max_bin = 1
        for path in data:
            if "path_name" in path:
                LOGGER.info("reading " + path['path_name'])

                p = GraphPath(path['path_name'])

                prev_bin = p.Bin()
                for b in path['bins']:
                    bin = p.Bin()
                    bin.set(b[0], b[1], b[2], b[3])
                    if b[0] > max_bin:
                        max_bin = b[0]
                    p.bins.append(bin)
                    prev_bin.next_bin = b[0]
                    prev_bin = bin
                prev_bin.next_bin = max_bin
                p.bins.append(prev_bin)  # last bin in a GraphPath needs to indicate stop, max_bin?

                p.finalize_bins()
                
                for l in path['links']:
                    p.links.append(p.LinkEntry(l[0], l[1]))

                paths.append(p)

        return paths


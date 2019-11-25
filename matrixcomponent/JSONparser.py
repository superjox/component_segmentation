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

                # dummy first bin in p.bins:
                prev_bin = p.Bin()
                prev_bin.set(0, 0, 0, 0)
                p.bins.append(prev_bin)

                p.mapping_id2idx[0] = 0
                idx = 1
                for b in path['bins']:
                    # store bin values in 'bin'
                    bin = p.Bin()
                    bin.set(b[0], b[1], b[2], b[3])
                    if b[0] > max_bin:
                        max_bin = b[0]
                    p.bins.append(bin)

                    # set next_bin of the previous bin (prev_bin) to this bin:
                    prev_bin.next_bin = b[0]
                    prev_bin = bin

                    # populate mapping betw binID and index in bin_set:
                    p.mapping_id2idx[b[0]] = idx
                    idx += 1
                # last bin points to itself:
                #p.mapping_id2idx[prev_bin.bin_id] = idx-1
                prev_bin.next_bin = prev_bin.bin_id
                #p.bins.append(prev_bin)

                p.finalize_bins()
                
                for l in path['links']:
                    p.links.append(p.LinkEntry(l[0], l[1]))

                paths.append(p)

        return paths


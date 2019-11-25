import json
import logging
import matrixcomponent.matrix as matrix

LOGGER = logging.getLogger(__name__)

def parse(file):
        data = []
        with open(file) as f:
            for line in f:
                data.append(json.loads(line))

        paths = []
        for path in data:
            if "path_name" in path:
                LOGGER.info("reading " + path['path_name'])

                p = matrix.Path(path['path_name'])

                prev_bin = p.Bin()
                idx = 0
                for b in path['bins']:
                    bin = p.Bin()
                    bin.set(b[0], b[1], b[2], b[3])
                    p.bins.append(bin)
                    prev_bin.next_bin = b[0]
                    prev_bin = bin
                    p.mapping_id2idx[b[0]] = idx
                    idx += 1
                prev_bin.next_bin = 0
                p.finalize_bins()
                
                for l in path['links']:
                    p.links.append(p.LinkEntry(l[0], l[1]))

                paths.append(p)

        return(paths)


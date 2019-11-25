from matrixcomponent.matrix import GraphPath


def test_construction():
    p = GraphPath()
    p.bins = [GraphPath.Bin(1, .9, 0, 0.11), GraphPath.Bin(2, .8, 0, 0.15), ]
    p.links = [GraphPath.LinkEntry(1, 2)]


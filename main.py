from src import PathGen

pathgen = PathGen.PathGenerator(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])
path = [pathgen.seq]
while (path):
    path = pathgen.permute(limit=10)
    print path

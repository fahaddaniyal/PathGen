from itertools import product, izip


class PathGenerator():
    def __init__(self, sequence):
        self.seq = sequence
        self.gen = None
        self.seq_len = len(self.seq)

    def permute(self, limit=10):
        if self.gen is None:
            self.gen = product([0, 1], repeat=self.seq_len)
        sub_paths = []
        count = 0
        for idx, loc_map in enumerate(self.gen):
            if sum(loc_map) in (0, self.seq_len):
                continue
            sub_paths.append([tp_name for bin, tp_name in izip(loc_map, self.seq) if bin == 1])
            count+=1
            if count >= limit:
                return sub_paths
        return sub_paths








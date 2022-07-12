import hashlib
from Minhash import *
from itertools import combinations

#LSH class to compute Locality-sensitive Hashing similar pairs
#candidate_pairs are a list containing pairs hashed to the same bucket
#pairs are list containing similar pairs (according to LSH, Jacc(signature1,signature2) > threshold)
class LSH:
    def __init__(self, minhashes, b, r, threshold = 0.8):
        self.candidate_pairs = set()
        self.pairs = set()

        #loop the bands
        for i in range(0, b*r, r):
            #key = hash of the band 
            #value = list of doc_id
            buckets = dict()
            
            #building the buckets
            #for each Minhash object we take the fraction corresponding
            #to the current band, we hash it and we update the buckets
            for minhash in minhashes:
                signature = minhash.signature
                band = str(signature[i: i+r])
                h = int(hashlib.sha1(band.encode("utf8")).hexdigest()[-16:], 16)
                
                buckets[h] = buckets.get(h, [])
                #returns buckets[bucket] if bucket in buckets, otherwise []
                buckets[h].append(minhash.id)

            
                
            #getting the candidate pairs
            #for each bucket we compute all possibile pairs
            for h, bucket in buckets.items():
                self.candidate_pairs = self.candidate_pairs.union(combinations(bucket, 2))

        #LSH computation
        #for each candidate pair we check if their similarity is above the desired threshold (false positives are removed)
        for id_1, id_2 in self.candidate_pairs:
            if (minhashes[id_1-1].Jaccard(minhashes[id_2-1]) >= threshold):
                self.pairs.add((id_1, id_2))

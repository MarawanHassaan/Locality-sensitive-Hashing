from __future__ import division
from hashlib import sha1


#Shingles class to compute set of hashed shingles
#Shingles is a set of hashed shingles

class Shingles:
    def __init__(self, doc, doc_id, k):
        self.id = doc_id
        self.k = min(len(doc), k)
        self.shingles = set()
        
        for i in range(len(doc)-self.k+1):
            shingle = doc[i:i+self.k]
            
            #Hashing starts with encoding the shingle, apply SHA1, take the digest in hexadecimal, take last 16 characters and convert to int
            digest = int(sha1(shingle.encode("utf8")).hexdigest()[-16:], 16)
            self.shingles.add(digest)


    def Jaccard(self, doc_shingle):
        intersection = len(self.shingles.intersection(doc_shingle.shingles))
        union = len(self.shingles.union(doc_shingle.shingles))
        return float(intersection) / union

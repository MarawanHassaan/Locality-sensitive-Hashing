from __future__ import division
import hashlib
import Shingles
from HashGenerator import HashGenerator


#MinHash class to compute the minhash signature
#id of shingle object is the id of the document

class Minhash:
    def __init__(self, doc_shingle, size, generator = HashGenerator()):
        self.id = doc_shingle.id
        self.signature = []
        
        for i in range(size):
            hash_i = generator.HashFamily(i)
            
            #Minimum Initialize
            minimum = hash_i(next(iter(doc_shingle.shingles)))

            for shingle in doc_shingle.shingles:
                minimum = min(hash_i(shingle), minimum)

            self.signature.append(minimum)

    #Computation of the Jaccard similarity
    def Jaccard(self, minhash):
        ret = 0.0
    
        sig1 = self.signature
        sig2 = minhash.signature

        if len(sig1) != len(sig2):
            return ret

        for hash1, hash2 in zip(sig1, sig2):
            if hash1 == hash2:
                ret += 1

        return ret / len(sig1)



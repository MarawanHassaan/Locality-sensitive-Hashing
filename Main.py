import Shingles
import Minhash
import LSH
import time

def run_LSH(shingles, k, b, r):
    #list of Minhash objects each contaning the signature
    minhashes = []
    
    print("\nComputing minhashes...", end="")
    
    t0 = time.time()
    for doc_shingle in shingles:
        minhashes.append(Minhash.Minhash(doc_shingle, r*b))
    t1 = time.time()
    
    print("done!")
    print("Minhashes computed - Elapsed Time: ", t1-t0)

    print("\nComputing LSH pairs...", end="")
    t0 = time.time()
    LSH_pairs = LSH.LSH(minhashes, b, r, 0.8).pairs
    t1 = time.time()
    
    print("done!")
    print("LSH pairs computed - Elapsed Time: ", t1-t0)
    
    return LSH_pairs

def bruteforce_pairs(shingles):
    pairs = set()
    n_docs = len(shingles)

    print("\nComputing brute-force pairs...", end="")
    
    t0 = time.time()
    for i in range(n_docs):
        for j in range(i+1, n_docs):
            sim = shingles[i].Jaccard(shingles[j])
            if (sim >= 0.8):
                pairs.add((shingles[i].id, shingles[j].id))
    t1 = time.time()

    print("done!")
    print("Brute-force pairs computed - Elapsed Time: ", t1-t0)
    return pairs
    



docs_file = "apartments.tsv"
k = 10
b = 9
r = 12

#list of Shingles objects each containing the set of shingles
shingles = []
doc_id = 1

########################################### Creating Shingles ##########################################################

print("Reading documents and computing shingles...", end="")
t0 = time.time()
with open(docs_file, encoding="utf8") as f:
    for line in f:
        doc = line.split("\t")[1].strip()
        shingles.append(Shingles.Shingles(doc, doc_id, k))
        doc_id += 1

t1 = time.time()
print("done!")
print("Shingles computed - Elapsed Time: ", t1-t0)


################################################## LSH #################################################################
LSH_pairs = run_LSH(shingles, k, b, r)

print("LSH - Found duplicates: ", len(LSH_pairs))


############################################### Brute Force ############################################################
brute_force_pairs = bruteforce_pairs(shingles)

print("Brute-force - Found duplicates: ", len(brute_force_pairs))

################################################## Analysis ############################################################
print("\nIntersection size: ", len(LSH_pairs.intersection(brute_force_pairs)))

FN = brute_force_pairs - LSH_pairs
FP = LSH_pairs - brute_force_pairs
print("\nFP and FN analysis:")
print("FNR = |brute_force_pairs - LSH_pairs| = ", len(FN))
print("FPR = |LSH_pairs - brute_force_pairs| = ", len(FP))



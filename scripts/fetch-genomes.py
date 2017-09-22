#!/usr/bin/python

import urllib2
import os
import sys
import time

if len(sys.argv) != 3:
    print("USAGE: fetch_genome.py <genome_id_list> <out_dir>")
    sys.exit(1)

url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=gb&retmode=text"

#os.mkdir(sys.argv[2])
if not os.path.exists(sys.argv[2]):
    os.mkdir(sys.argv[2])

for id in open(sys.argv[1]):
    id = id.strip()
    if id == "":
        continue

    sys.stdout.write("Fetching %s..." % id)
    sys.stdout.flush()
    gbk_out_file = os.path.join(sys.argv[2], id + ".gbk")
    if os.path.exists(gbk_out_file):
        print("already fetched)")
    try:
        open(gbk_out_file, "w").write(urllib2.urlopen(url_template % id).read())
        continue
    except:
        print(id + " not found")
        os.system('echo '+ id + '>> genomes_not_found.txt')
    print("Done")
    time.sleep(1.0/3)


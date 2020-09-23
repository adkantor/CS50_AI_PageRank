from pagerank import crawl

corp_dirs = ['corpus0','corpus1','corpus2']
for corp_dir in corp_dirs:
    corpus = crawl(corp_dir)
    print(corp_dir)
    print(corpus)
    print('\n')
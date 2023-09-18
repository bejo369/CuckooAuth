from cuckoopy import CuckooFilter
cf = CuckooFilter(capacity=1, bucket_size=1, fingerprint_size=1)
cf.insert("iooh ;i;.kj lkjnmi hnhpoj")
print (cf.contains("aaaaaaaaaa"))




def bucket_lists() :
    s3_bukcets=["demo_bucket_1","demo_bucket_2","demo_bucket_3","demo_bucket_4"] # This is list which are mutable
    numbers=[2,1,10,0,3]
    random=[2,3,4,"demo_bucket","karim" ]

    numbers.sort()
    s3_bukcets.append("demo_bucket_5")
    s3_bukcets.remove("demo_bucket_1")

    print(s3_bukcets[2])
    print(len(s3_bukcets))
    print(s3_bukcets[0:3])
    print(numbers)
    print(s3_bukcets[0] + "--" + s3_bukcets[2])
    print(random)


def bucket_tuples() :
    s3_buckets=("demo_bucket_1","demo_bucket_2","demo_bucket_3","demo_bucket_4") # This is tuple which are immutable
    cordinates=(5,4)
    x,y = cordinates

    new_tuple= s3_buckets + cordinates
    is_present= "demo_bucket_1" in s3_buckets

    print(s3_buckets[2])
    print(len(s3_buckets))
    print("X is :" , x , "and" , "Y is :" , y)
    print(new_tuple)
    print(is_present)


bucket_lists()
bucket_tuples()
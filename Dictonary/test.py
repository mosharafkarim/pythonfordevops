ec2_instances_info = [
    {
        "name" : "1st ec2 instance",
        "type" : "t2.micro"
    },
    {
        "name" : "2nd ec2 instance",
        "type" : "t2.small"
    },
    {
        "name" : "3rd ec2 instance",
        "type" : "t2.medium"
    },
    {
        "name" : "4th ec2 instance",
        "type" : "t2.large"
    }
]

print(ec2_instances_info[2]["name"])
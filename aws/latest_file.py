import os
import os.path
from os.path import splitext
import sys
import boto3

s3 = boto3.client('s3')

def main(course,term):
    objs = s3.list_objects_v2(Bucket=course+term)['Contents']
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][0]
    print(last_added)

if __name__ == '__main__':
    course = "climate102"
    term   = "w20"
    main(course,term)

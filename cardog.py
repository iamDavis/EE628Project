import os
import shutil

train_filenames = os.listdir('/Users/dengzeyu/Documents/628 final/train)
train_cat = filter(lambda x:x[:3] == 'cat', train_filenames)
train_dog = filter(lambda x:x[:3] == 'dog', train_filenames)

def rmrf_mkdir(dirname):
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
    os.mkdir(dirname)


rmrf_mkdir('train2')
os.mkdir('train2/cat')
os.mkdir('taain2/dog')

rmrf_mkdir('test2')
os.symlink('../test/', 'test2/test')

for filename in train_cat:
    os.symlink('/Users/dengzeyu/Documents/628 final/train'+filename, 'train2/cat/filename')

for filename in train_dog:
    os.symlink('/Users/dengzeyu/Documents/628 final/train'+filename, 'train2/dog/filename')

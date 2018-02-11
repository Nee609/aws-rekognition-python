
# coding: utf-8

# In[2]:

import boto3


# In[3]:

s3 = boto3.resource('s3')


# In[5]:

buckets = s3.buckets.all()


# In[6]:

for bucket in buckets:
    print(bucket.name)


# In[10]:

imageName = 'Lighthouse.jpg'
client = boto3.client('rekognition')
response = client.detect_labels(Image={'S3Object':{'Bucket':'nmtestspark','Name':imageName}},MinConfidence=75)


# In[11]:

response


# In[13]:

videoName = 'testVideo.MP4'
arnName = 'arn:aws:sns:us-east-1:414502989863:VideoAnalysis'
roleArn = 'arn:aws:iam::414502989863:role/TestSNSRole'
response2 = client.start_label_detection(Video={'S3Object':{'Bucket':'nmtestspark','Name':videoName}},NotificationChannel={'SNSTopicArn':arnName,'RoleArn':roleArn},MinConfidence=75)


# In[14]:

response2


# In[15]:

response3 = client.get_label_detection(JobId = '38587fb20ddc1eac2abbedd4bad96111d068a2fe584e92c4f1792e51b7f51677')


# In[17]:

for i in range(len(response3['Labels'])):
    print(response3['Labels'][i]['Label']['Name'] + '*****' + str(response3['Labels'][i]['Label']['Confidence']))


# In[ ]:




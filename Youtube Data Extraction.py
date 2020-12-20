#!/usr/bin/env python
# coding: utf-8

# 
# # Youtube Data Extraction
# 
# ### Task
# 
# Write a script that extracts YouTube data to analyze the #endsars# trend that rocked the entire world. The script should be able to perform the following:
# 
# Filter out channels and playlists.
# * Get only videos published this year.
# * Include videos that are between 4 to 20 mins long.
# * Generic such that the search query can be changed.
# 
# ### Output
# 
# Store the output into a csv with the filename having the following format: current_timestamp_youtube_data.
# 
# The following video attributes should be a part of the dataset:
# 
# * the time video was published
# * the video id
# * the title of the video
# * description
# * the URL of the video thumbnail
# * number of views
# * number of likes
# * number of dislikes
# * number of comments
# 
# Create an additional the column that builds the video URL using the video id.

# ## Import Libraries

# In[1]:


from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd
import pprint 
import matplotlib.pyplot as pl
import time
import datetime
import keys as k


# ## Set API Parameters

# In[2]:


key = k.credentials['DEVELOPER_KEY']


# In[3]:


YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


# ## Search and Video Request

# In[4]:


def youtube_search(q, max_results=50,order="relevance",nextPage_token = None, location=None, location_radius=None):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=key)

    search_response = youtube.search().list(
    q=q,
    type="video",
    order = order,
    part="id,snippet", # Part signifies the different types of data you want 
    maxResults=max_results,
    pageToken = nextPage_token, 
    location=location,
    locationRadius=location_radius,
    videoDuration = 'medium',
    publishedAfter = '2020-01-01T00:00:00Z').execute()
    
    nextPage_token = search_response.get("NextPageToken")



#   the attributes that we want to be able to view in the dataset
    title = []
    channelId = []
    channelTitle = []
    categoryId = []
    videoId = []
    viewCount = []
    likeCount = []
    dislikeCount = []
    commentCount = []
    favoriteCount = []
    category = []
    tags = []
    videos = []
    thumbnail_url = []
    publishTime = []
    description = []
    
    for search_result in search_response.get("items", []):
        #pprint.pprint(search_result)
  
  
        if search_result["id"]["kind"] == "youtube#video":

            title.append(search_result['snippet']['title']) 

            videoId.append(search_result['id']['videoId'])

            response = youtube.videos().list(
                part='statistics, snippet',
                id=search_result['id']['videoId']).execute()

            channelId.append(response['items'][0]['snippet']['channelId'])
            channelTitle.append(response['items'][0]['snippet']['channelTitle'])
            categoryId.append(response['items'][0]['snippet']['categoryId'])
            favoriteCount.append(response['items'][0]['statistics']['favoriteCount'])
            viewCount.append(response['items'][0]['statistics']['viewCount'])
            thumbnail_url.append(response['items'][0]['snippet']['thumbnails']['default']['url'])
            publishTime.append(response['items'][0]['snippet']['publishedAt'])
            description.append(response['items'][0]['snippet']['description'])

 
        if 'commentCount' in response['items'][0]['statistics'].keys():
            commentCount.append(response['items'][0]['statistics']['commentCount'])
        else:
            commentCount.append([])
        if 'likeCount' in response['items'][0]['statistics'].keys():
            likeCount.append(response['items'][0]['statistics']['likeCount'])
        else:
            likeCount.append([])
        if 'dislikeCount' in response['items'][0]['statistics'].keys():
            dislikeCount.append(response['items'][0]['statistics']['dislikeCount'])
        else:
            dislikeCount.append([])
	  
        if 'tags' in response['items'][0]['snippet'].keys():
            tags.append(response['items'][0]['snippet']['tags'])
        else:
            tags.append([])
#     pprint.pprint(response)
    youtube_dict = {'tags':tags,'channelId': channelId,'channelTitle': channelTitle,'categoryId':categoryId,'title':title,'videoId':videoId,'viewCount':viewCount,'likeCount':likeCount,'dislikeCount':dislikeCount,'commentCount':commentCount,'favoriteCount':favoriteCount, 'publishTime':publishTime, 'thumbnail_url': thumbnail_url, 'description': description}

    return youtube_dict


# In[5]:


endsars = youtube_search('endsars')


# In[6]:


endsars = pd.DataFrame(endsars)


# In[7]:


endsars.head()


# ## Store data to csv file with current timestamp

# In[11]:


import time
import os

def save_to_csv(endsars):
    path = os.getcwd() + '\data\\'
    current_timestamp = time.strftime("%y%m%d_%H%M%S")

    if not os.path.exists(path):
        os.mkdir(path)

    file_name = current_timestamp+"_youtube_data.csv"
    
    full_path = os.path.join(path, file_name)
    
    endsars.to_csv(full_path, index=False)
    
    return full_path


# In[12]:


path = save_to_csv(endsars)
print("File created successfully. File save to: {0}".format(path))


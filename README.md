# YouTube-Data-Extraction

## Extracting Video Data Using Youtube API V3

This task lays out the basics of how to work with the Youtube V3 API in python. Using the Google API Client library for python,data can be extracted from Youtube. The second part of the task requires that the data extracted is stored in a csv file.

## Task

Write a script that extracts YouTube data to analyze the #endsars# trend that rocked the entire world.
The script should be able to perform the following:

* Filter out channels and playlists.
* Get only videos published this year.
* Include videos that are between 4 to 20 mins long.
* Generic such that the search query can be changed.

### Output

Store the output into a csv with the filename having the following format: current_timestamp_youtube_data.

The following video attributes should be a part of the dataset:

* the time video was published
* the video id
* the title of the video
* description
* the URL of the video thumbnail
* number of views
* number of likes
* number of dislikes
* number of comments

Create an additional the column that builds the video URL using the video id.

## Pre-requisites

* Google Account
* Youtube V3 API Key  

## Setting Up

The project was developed using:

* Python
* Anaconda (conda)
* Google API Client
* Pandas

Follow the steps below to setup the project.
### Create and activate environment

Create and activate a conda environment using the command:
```
conda create -n "env-name" python=3.6
```
Activate the environment using the command:
```
conda activate env-name
```

### Install packages

Install project packages using the command:
```
pip install -r requirements.txt
```


## Resources

#### Documentations

* [Youtube V3 API - Getting Started](https://developers.google.com/youtube/v3/getting-started)
* [YouTube API source](https://developers.google.com/youtube/v3/getting-started)

## Tutorial Articles

* [How To Create A Youtube API Key(2020)](https://m.youtube.com/watch?v=VqML5F8hcRQ)
* [YouTube Data In Python](https://medium.com/greyatom/youtube-data-in-python-6147160c5833)

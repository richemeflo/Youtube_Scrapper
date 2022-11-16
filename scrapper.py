import json
import random
import os
import re
import sys
from dataclasses import dataclass
from typing import List
import pytest

import requests
from bs4 import BeautifulSoup


class JsonError(Exception):
    def __init__(self):
        self.message = "JSON error"
    def __str__(self):
        return self.message

class ArgError(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return self.message


@dataclass
class Video:
    id: str
    title: str
    creator: str
    likes: int
    description: str
    links: List[str]
    first_comments: List[str]

    def __init__(self, id, title, creator, likes, description, links, first_comments) -> None:
        self.id = id
        self.title = title
        self.creator = creator
        self.likes = likes
        self.description = description
        self.links = links
        self.first_comments = first_comments

    def __str__(self) -> str:
        msg = []
        msg.append(self.id)
        msg.append(self.title)
        msg.append(self.creator)
        msg.append(self.likes)
        msg.append(self.description)
        msg.append(self.links)
        msg.append(self.first_comments)
        msg = list(filter(lambda x: x is not None, msg))
        msg = list(map(str, msg))
        return ";".join(msg)

    def as_list(self):
        return str(self).split(";")


    ##GETTER AND SETTER
    def _get_id(self):
        return self.id
    def _set_id(self,id):
        self.id = id

    def _get_title(self):
        return self.title
    def _set_title(self,title):
        self.title = title

    def _get_creator(self):
        return self.creator
    def _set_creator(self,creator):
        self.creator = creator

    def _get_likes(self):
        return self.likes
    def _set_likes(self,likes):
        self.likes = likes

    def _get_description(self):
        return self.description
    def _set_description(self,description):
        self.description = description

    def _get_links(self):
        return self.links
    def _set_links(self,links):
        self.links = links

    def _get_first_comments(self):
        return self.first_comments
    def _set_first_comments(self,first_comments):
        self.first_comments = first_comments
    




def load_json(filename):
    if filename[-5:]==".json":
        f= open(filename,"r")
        jsonContent = f.read()
        data = json.loads(jsonContent)
        return data
    else:
        raise JsonError

def transformDescription(brut):
    description=""
    links=[]
    for i in range(len(brut)):
        description=description+brut[i]['text']
        if (brut[i]['text'][:4]=="http"):
             links.append(brut[i]['text'])
    return [description,links]

def scrap(id,nb_comment):
    url = "https://www.youtube.com/watch?v="+id
    page_requested = requests.get(url)
    soup = BeautifulSoup(page_requested.content,"lxml")
    scripts=soup.find('body').find_all('script')
    string_data = scripts[22].text.replace('var ytInitialData = ', '').replace(';','')
    json_data = json.loads(string_data)

    for i in range(len(json_data['engagementPanels'])):
        if 'structuredDescriptionContentRenderer' in json_data['engagementPanels'][i]['engagementPanelSectionListRenderer']['content']:
            break
    base=json_data['engagementPanels'][i]['engagementPanelSectionListRenderer']['content']
    for j in range(len(base['structuredDescriptionContentRenderer']['items'])):
        if 'videoDescriptionHeaderRenderer' in base["structuredDescriptionContentRenderer"]["items"][j]:
            break
    item = base["structuredDescriptionContentRenderer"]["items"][j]['videoDescriptionHeaderRenderer']
    title = item['title']['runs'][0]['text']
    creator=item['channel']['simpleText']
    likes=item['factoid'][0]['factoidRenderer']['value']['simpleText'].replace("\u00a0k","000")

    for k in range(len(base['structuredDescriptionContentRenderer']['items'])):
        if 'expandableVideoDescriptionBodyRenderer' in base["structuredDescriptionContentRenderer"]["items"][k]:
            break
    desc_base=base["structuredDescriptionContentRenderer"]["items"][k]['expandableVideoDescriptionBodyRenderer']['descriptionBodyText']
    description_brut=desc_base['runs']
    description,links = transformDescription(description_brut)
    first_comments=[]
    ##first_comments.append(json_data['contents']['twoColumnWatchNextResults']['results']['results']['contents'][4]['itemSectionRenderer']['contents'][0]['commentsEntryPointHeaderRenderer']['contentRenderer']['commentsEntryPointTeaserRenderer']['teaserContent']['simpleText'])
    v = Video(id, title, creator, int(likes), description, links, first_comments)
    return v

    
    
    
    

def main():
    nb_comment=1
    args=sys.argv[1:]
    int_cpt=len(args)
    if int_cpt == 0:
        input_file = "input.json"
        output_file = "output.json"
    elif int_cpt == 1:
        input_file = args[0]
    elif int_cpt == 2 :
        input_file = args[0]
        output_file = args[1]
    elif int_cpt == 4 :
        if (args[0]!="--input" and args[0]!="--output" and args[2]!="--input" and args[2]!="--output"):
            raise ArgError("Arguments error flag allowed : --input and --output")
        if args[0] == "--input":
            input_file = args[1]
        else:
            output_file = args[1]
        if args[2] == "--input":
            input_file = args[1]
        else:
            output_file = args[1]   
    else:
        raise ArgError("Arguments error, please run the command python3 scrapper.py --input input_file.json --output output_file.json")
    return [input_file,output_file,nb_comment]




try:
    input_file,output_file,nb_comment=main()
    input_data = load_json(input_file)
    for j in range(len(input_data['videos_id'])):
        try:
            v=scrap(input_data['videos_id'][j],1)
            if j==0:
                with open(output_file, 'w') as fw:
                    json.dump(v.__dict__,fw)
            else:
                with open(output_file, 'a') as fa:
                    fa.write(',')
                    json.dump(v.__dict__,fa)
            del v
        except Exception:
            break
except ArgError as a:
    print(a)
except JsonError as j:
    print(j)
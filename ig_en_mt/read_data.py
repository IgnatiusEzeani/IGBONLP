# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:24:59 2020

@author: ignatius ezeani
"""

import os

datapath = os.getcwd() #or appropriate data path

class ParallelData:
    def __init__(self, datapath):
        self.datapath = datapath
        self.devset=[]
        self.test=[]

    def readData(self, datafile):
        with open(datafile, 'r', encoding='utf8') as f: 
            return [sent.strip() for sent in f.readlines()]
    
    def getData(self, _dir, _prefix):
        ig,en = {},{}
        curr_path = os.path.join(datapath, _dir)
        for i in range(1,6):
            ig[f't{i}'] = self.readData(os.path.join(
                    curr_path,f'{_prefix}_t{i}.ig'))
            en[f't{i}'] = self.readData(os.path.join(
                    curr_path,f'{_prefix}_t{i}.en'))
        return ig, en

    def get_evalsets(self):
        ig_sents, en_sents = [], []        
        ig, en = self.getData('ig_en','bbcigbo')
        for k, lines in ig.items(): ig_sents += lines
        for k, lines in en.items(): en_sents += lines

        en, ig = self.getData('en_ig','naijanewpaper')
        for k, lines in ig.items(): ig_sents += lines
        for k, lines in en.items(): en_sents += lines
        
        self.devset = ig_sents[:10000], en_sents[:10000]
        self.testset = ig_sents[10000:], en_sents[10000:]

par_data = ParallelData(datapath)
par_data.get_evalsets()

print('---Igbo sentences:')
print("\n".join(par_data.devset[0][:5]))
print('\n---English sentences:')
print("\n".join(par_data.devset[1][:5]))
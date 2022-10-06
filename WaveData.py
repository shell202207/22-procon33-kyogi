# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:37:16 2022

@author: ore
"""

import glob
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import csv
import wave
import argparse
import librosa
from pydub import AudioSegment


"""
print(file_name)
print("Channel: ", ch)
print("Sample width: ", width)
print("Frame Rate: ", fr)
print("Frame num: ", fn)
print("Params: ", wr.getparams())
print("Total time: ", 1.0 * fn / fr)
"""

# 設定パラメータ
class_n = 88   # クラス数
x = []        # 画像データ用
y = []        # ラベルデータ用

def wav_read():
    outfile ="./Quisdata/" + str("7680_") + str(class_n) +  ".csv"
    
    def glob_read(path,label):
        list=glob.glob('C:\\Users\ore\Documents\KerasMake\JKspeech/*.wav')
        data=random.choice(list)
        file_name=os.path.split(data)[1]#ファイル名
        
        wr = wave.open(data, 'r')       #ファイルデータの取得
        ch = wr.getnchannels()          #チャンネルの取得
        width = wr.getsampwidth()       #サンプルサイズ
        fr = wr.getframerate()          #サンプリングレート
        fn = wr.getnframes()            #オーディオスケール
        # waveの実データを取得し、数値化
        wav_data = wr.readframes(wr.getnframes())
        wr.close()
        X = np.frombuffer(wav_data, dtype=np.int16)
        num=0
        for f in list:
            if num >= len(list): break
            num += 1
            x.append(X)
            y.append(label)
        
        
    for i in range(class_n):
         glob_read("./wav/" + str(i), i)  # 各画像のフォルダーを読む
         print("file: " + str(i))
         
    ### ファイルへ保存 ###
    with open(outfile, 'w') as f:
 
       writer = csv.writer(f)
       writer.writerow(x)
       writer.writerows(y)

    f.close()
    print("npzファイルを保存しました :" + outfile, len(x))

if __name__ == '__main__':
    wav_read()
    

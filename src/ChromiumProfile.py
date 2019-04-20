#/usr/bin/python3
#coding: utf8
import json
import os.path
# ブラウザのプロファイル情報を取得する。
# file: ~/.config/chromium/Local State
#   python -m json.tool "Local State" > LocalState.json
#     .profile.info_cache
#     .profile.info_cache.name
#     .profile.last_used
class ChromiumProfile:
    def __init__(self):
        self.__FilePath = '~/.config/chromium/Local State'
        self.__JSON = json.load(open(os.path.expanduser(os.path.expandvars('~/.config/chromium/Local State'))))
    @property
    def LocalStatePath(self): return self.__FilePath;
    @LocalStatePath.setter
    def LocalStatePath(self, value):
        if os.path.exists(value):
            self.__FilePath = value
            __Open()
    def __Open(self):
        if os.path.exists(self.__FilePath): self.__JSON = open(os.path.expanduser(os.path.expandvars(self.__FilePath))) 
    def __NewLine(self, array):
        str=''
        for v in array: str+=v+'\n'
        return str.rstrip('\n')
    @property
    def __Dirnames(self):
        return sorted(self.__JSON['profile']['info_cache'].keys())
    @property
    def Dirnames(self):
        return self.__NewLine(self.__Dirnames)
    @property
    def Usernames(self):
        names = []
        for key in self.__Dirnames:
            names.append(self.__JSON['profile']['info_cache'][key]['name'])
        return self.__NewLine(names)
    @property
    def Tsv(self):
        tsv = ''
        for key in self.__Dirnames:
            tsv += key + '\t' + self.__JSON['profile']['info_cache'][key]['name'] + '\n'
        return tsv.rstrip("\n")
    def GetDirname(self, username):
        for key in self.__Dirnames:
            if username == self.__JSON['profile']['info_cache'][key]['name']: return key;
    def GetUsername(self, profileDirname): return self.__JSON['profile']['info_cache'][profileDirname]['name']
    @property
    def LastUsed(self): return self.__JSON['profile']['last_used']

# 使い方
#c = ChromiumProfile()
#print(c.Dirnames)
#print(c.Usernames)
#print(c.Tsv)
#print(c.GetDirname("view"))
#print(c.GetUsername("Profile 4"))
#print(c.LastUsed)

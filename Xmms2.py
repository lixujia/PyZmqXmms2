#!/usr/bin/python3

import os
import pexpect
import subprocess

class Xmms2:
    def __init__(self,*args,**kargs):
        pass

    def cmdExec(self,cmd):
        cmd_lst = ['xmms2',]
        cmd_lst.extend([a for a in cmd.split(' ') if '' != a])
        return subprocess.check_call(cmd_lst)

    def readFeedback(self,cmd):
        cmd_lst = ['xmms2',]
        cmd_lst.extend([a for a in cmd.split(' ') if '' != a])
        print(cmd_lst)
        return str(subprocess.check_output(cmd_lst),encoding = "utf-8")
    
    def playlistExist(self,listname):
        fb = self.readFeedback("playlist list")

        print(fb)
        for l in fb.split("\n"):
            if listname.strip() == l.strip("*").strip():
                return True

        return False
    
    def createPlaylist(self,playlist):
        if not isinstance(playlist,dict):
            raise Exception

        if "name" not in playlist or "songs" not in playlist:
            raise Exception
        
        if self.playlistExist(playlist["name"]):
            self.cmdExec("playlist clear {}".format(playlist["name"]))
        else:
            self.cmdExec("playlist create {}".format(playlist["name"]))

        self.cmdExec("playlist switch {}".format(playlist["name"]))
        for song in playlist["songs"]:
            self.cmdExec("add {}".format(song))

    def deletePlaylist(self,plname):
        if not self.playlistExist(plname):
            return True

        return self.cmdExec("playlist delete {}".format(plname))
        
if __name__ == "__main__":
    xmms2 = Xmms2()

    pl = {"name": "Python List"}

    path = "/home/john/Codes/CoolSite/static/upload/Music"

    pl["songs"] = [os.path.join(path,s) for s in os.listdir(path)]
    xmms2.createPlaylist(pl)

    

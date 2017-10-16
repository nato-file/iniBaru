# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token="ElG5iVMoAKewclurqnc7.hga8Bw6ZO8X1BAw2hYPJrW.rrqFERTkcoFzv03rJlWbfp/dJ0x3KGGh4YgpM1z9CCM=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="ElcRa7hygyEjEFCdXlm3.J8JKyyOhfn7JInH7YP8s8W.5OnATD76xRL8kwZ1t76bu3bjqWcAB/GhOBMgf29TKSY=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="El6I3qYAzYvyIMPMV8P0.wyYA8bGs58lOwdcrXNrIma.ky/hDW9On9BPFqHsbxavxndR6GkJHeV0Ibq89K4fdQw=")
kk.loginResult()

ar = LINETCR.LINE()
ar.login(token="ElUSGFUMaZTMbRmbv8dc.GeBvu6aiiktEKuWvEKqxNa.+crtKcUvTuk3x7VlS3Ew9OXhGH3p0OL3N8gCRKgHOxo=")
ar.loginResult()

#pi = LINETCR.LINE()
#pi.login(qr=True)
#pi.loginResult()


print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""Gunakan dengan bijak keyword dibawah ini!

!Keberuntungan & ketamvanan/kecantikan Anda Berlaku!


<※ Keyword  Ar-Har ※>

+[Id︎]
+[Mid]
+[Mid 「@」] By Tag
+[Me︎]
+[TL︎:「Text」]
+[Mc 「mid」]
+[K on/off]
+[Summon]
+[PING]
+[About Creator]
+[ngasyi ah]
+[cancel]
+[Arbot]
+[ArBot siapa?]
+[Welcome]
+[Hallo]
+[Ginfo]
+[Gurl]
+[Ini apa?]
+[Say 「text」]
+[Saran keyword]

[~!] Only Creator Bot [!~]

※[Tagall1]
※[Curl]
※[Ourl]
※[url]
※[url:「Group ID」]
※[Invite：「mid」]
※[Usir：「mid」]
※[jointicket]
※[Cancel]
※[Gn 「group name」]
※[Nk 「name」]
※[Usir Catatan]
※[Kill 「@」]
※[Catat 「@」] By Tag
※[Uncatat 「@」] By Tag
※[Catat] Share Contact
※[Uncatat] Share Contact
※[List Catatan]
※[Cek Catatan]
※[Cv ︎invite:「mid」]
※[Cv ︎rename:「name」]
※[Cv ︎gift]
※[Respo︎n]
※[Bot cancel]
※[Title:]



*ada beberapa key yang tidak bisa digunakan, itu dibuat untuk kepuasan tersendiri 😂✌️*


*jika ada sesuatu yang error segera hubungi sang Creator Ar-bot 📲 Ok😂👌*



Di Add ya line si creator
Kasihan, kesepian dia
Ok 😉
Creator : http://line.me/ti/p/~a.r.- """
KAC=[cl,ki,kk,ar]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = ar.getProfile().mid
#Dmid = pi.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
profile = cl.getProfile()
admin=["u308205dd6abcc4bec5da585db20ab076","u1c603c6d6eb3a3cc756da5b61f2a6347","u8fc8e4618a0714dee388d87bca9f12f3","u598c9af01812e7c2e8583091c6746230","u8046d553a00820a4de914c157a44179c"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me 😄\nJangan lupa add si Creator juga ya\nhttp://line.me/ti/p/~a.r.-",
    "lang":"JP",
    "comment":"Thanks for add me 😊",
    "commentOn":True,
    "commentBlack":{},
    "wblack":True,
    "dblack":True,
    "clock":False,
    "cName":"Ar-Har",
    "winvite":True,
    "blacklist":{},
    "wblacklist":True,
    "dblacklist":True,
    "protectionOn":True,
    "ProtectQr":True,
    "ProtectGuest":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    print nm
    for mm in nama:
      akh = akh + 3
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 4
      akh = akh + 1
      bb += "@x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = bb
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       cl.sendMessage(msg)
    except Exception as error:
        print error

def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''

    # Here's the metadata for the upload. All of these are optional, including
    # this config dict itself.
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

    return image

def sendImage(self, to_, path):
    M = Message(to=to_, text=None, contentType = 1)
    M.contentMetadata = None
    M.contentPreview = None
    M2 = self._client.sendMessage(0,M)
    M_id = M2.id
    files = {
       'file': open(path, 'rb'),
    }
    params = {
       'name': 'media',
       'oid': M_id,
       'size': len(open(path, 'rb').read()),
       'type': 'image',
       'ver': '1.0',
    }
    data = {
       'params': json.dumps(params)
    }
    r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
    if r.status_code != 201:
       raise Exception('Upload image failure.')
    return True

def sendImage2(self, to_, path):
    M = Message(to=to_,contentType = 1)
    M.contentMetadata = None
    M.contentPreview = None
    M_id = self._client.sendMessage(M).id
    files = {
       'file': open(path, 'rb'),
    }
    params = {
       'name': 'media',
       'oid': M_id,
       'size': len(open(path, 'rb').read()),
       'type': 'image',
       'ver': '1.0',
    }
    data = {
       'params': json.dumps(params)
    }
    r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
    if r.status_code != 201:
       raise Exception('Upload image failure.')
    return True

def sendImageWithURL(self, to_, url):
    path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
    r = requests.get(url, stream=True)
    if r.status_code == 200:
       with open(path, 'w') as f:
          shutil.copyfileobj(r.raw, f)
    else:
       raise Exception('Download image failure.')
    try:
       self.sendImage(to_, path)
    except:
       try:
        self.sendImage(to_, path)
       except Exception as e:
          raise e


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_ACCEPT_GROUP_INVITATION(op):
    #print op
    try:
        cl.sendText(op.param1, cl.getContact(op.param2).displayName + "Selamat Datang😊\n " + group.name + "Salam Kenal Bro!")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ACCEPT_GROUP_INVITATION\n\n")
        return

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        cl.sendText(op.param1, cl.getContact(op.param3).displayName + " Jangan Main Kick!\n(/*´･ω･*\)")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_KICKOUT_FROM_GROUP\n\n")
        return

def NOTIFIED_LEAVE_GROUP(op):
    try:
        cl.sendText(op.param1, cl.getContact(op.param2).displayName + " Good Bye\n(*´･ω･*)")
        ki.sendText(msg,to,"Semoga Tenang Bagi yang Meninggalkan Grup 🏳️")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_LEAVE_GROUP\n\n")
        return

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = ar.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ar.updateGroup(X)
                        Ti = ar.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ar.updateGroup(X)
                        Ti = ar.reissueGroupTicket(op.param1)

#                if op.param3 in Bmid:
#                   if op.param2 in Cmid:
#                       X = pi.getGroup(op.param1)
#                       X.preventJoinByTicket = False
#                       pi.updateGroup(X)
#                       Ti = pi.reissueGroupTicket(op.param1)
#                       ar.acceptGroupInvitationByTicket(op.param1,Ti)
#                       X.preventJoinByTicket = True
#                       pi.updateGroup(X)
#                       Ti = pi.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                            ki.rejectGroupInvitation(op.param1)
                            kk.rejectGroupInvitation(op.param1)
                            ar.rejectGroupInvitation(op.param1)
                            pi.rejectGroupInvitation(op.param1)

                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            ar.acceptGroupInvitation(op.param1)
                            pi.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        ar.acceptGroupInvitation(op.param1)
                        pi.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
                        ki.rejectGroupInvitation(op.param1)
                        kk.rejectGroupInvitation(op.param1)
                        ar.rejectGroupInvitation(op.param1)
                        pi.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 15:
            if op.param2 in Bots:
                group = random.choice(KAC).getGroup(op.param1)
                cb = Message()
                cb.to = op.param1
                cb.text = + random.choice(KAC).getContact(op.param2).displayName + " [LeaveGroup]\n\n" + random.choice(KAC).getContact(op.param2).displayName + " Selamat Tinggal Kawan\n(*´･ω･*)"
                random.choice(KAC).sendMessage(cb)

        if op.type == 17:
                group = random.choice(KAC).getGroup(op.param1)
                cb = Message()
                cb.to = op.param1
                cb.text = random.choice(KAC).getContact(op.param2).displayName + " [NewMemb]\n\nSelamat Datang " + random.choice(KAC).getContact(op.param2).displayName + " di [" + group.name + "]\nJangan nakal disini! ok!" + "\n\nOwner => " + group.creator.displayName 
                random.choice(KAC).sendMessage(cb)

        if op.type == 17:
                if op.param3 in wait["blacklist"]:
                    try:
                        cl.kickoutFromGroup(op.param1, op.param3)
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1, op.param3)

        if op.type == 19:
                if op.param3 in Bots:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 19:
                if op.param3 in admin:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                else:
                    pass

        if op.type == 19:
                if op.param2 not in admin and Bots:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[admin])
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    ar.acceptGroupInvitationByTicket(op.param1,Ti)
                    pi.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        ar.kickoutFromGroup(op.param1,[op.param2])
                        pi.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    ar.acceptGroupInvitationByTicket(op.param1,Ti)
                    pi.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
#----------Open Qr Kick Start----------
        if op.type == 11:
            if wait["ProtectQr"] == True:
                if op.param2 not in admin:
                  if op.param2 not in Bots:
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).updateGroup(G)
#--------------------------------------
#----------Invite User Kick Start----------
        if op.type == 13:
            if wait["ProtectGuest"] == True:
                if op.param2 not in admin and Bots:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#------------------------------------------
        if op.type == 32:
                if op.param2 not in admin and Bots:
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#------------------------------------------
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                            ki.rejectGroupInvitation(op.param1)
                            kk.rejectGroupInvitation(op.param1)
                            ar.rejectGroupInvitation(op.param1)
                            pi.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            ar.acceptGroupInvitation(op.param1)
                            pi.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        ar.acceptGroupInvitation(op.param1)
                        pi.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
                        ki.rejectGroupInvitation(op.param1)
                        kk.rejectGroupInvitation(op.param1)
                        ar.rejectGroupInvitation(op.param1)
                        pi.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                print "ArBot Meninggalkan Grup."
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                print "ArBot Meninggalkan Grup."
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.toType == 2:
                if msg.contentType == 0:
                  if msg.text in["Tag","tag"]:
                      if msg.from_ in admin:
                         group = cl.getGroup(msg.to)
                         nama = [contact.mid for contact in group.members]
                         nm1, nm2, nm3, jml = [], [], [], len(nama)
                         if jml <= 100:
                            mention(msg.to, nama)
                         if jml > 100 and jml < 200:
                            for i in range(0, 99):
                                nm1 += [nama[i]]
                            mention(msg.to, nm1)
                            for j in range(100, len(nama)-1):
                                nm2 += [nama[j]]
                            mention(msg.to, nm2)
                         if jml > 200  and jml < 300:
                            for i in range(0, 99):
                                nm1 += [nama[i]]
                            mention(msg.to, nm1)
                            for j in range(100, 199):
                                nm2 += [nama[j]]
                            mention(msg.to, nm2, jml)
                            for k in range(200, len(nama)-1):
                                nm3 += [nama[k]]
                            mention(msg.to, nm3, jml)
                         if jml > 300:
                            print "Terlalu Banyak Men 300+"
                         cnt = Message()
                         cnt.text = "Mentioned:"+str(jml)
                         cnt.to = msg.to
                         cl.sendMessage(cnt)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
                ki.like(url[25:58], url[66:], likeType=1001)
                kk.like(url[25:58], url[66:], likeType=1001)
                ar.like(url[25:58], url[66:], likeType=1001)
                pi.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False
                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada siapapun di List Catatan")

               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ki.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False
                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","Key","menu","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"Maaf, anda bukan admin.")
            elif ("Cv1 gn " in msg.text):
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv2 gn " in msg.text):
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    cl.sendText(msg.to,"Maaf, anda bukan admin.")
            elif "Usir " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Usir ","")
                    cl.kickoutFromGroup(msg.to,[midd])
                else:
                    cl.sendText(msg.to,"Sorry, lu bukan admin")
            elif "Cv1 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Cv1 kick ","")
                    ki.kickoutFromGroup(msg.to,[midd])
            elif "Cv2 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Cv2 kick ","")
                    ki.kickoutFromGroup(msg.to,[midd])
            elif "Cv3 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Cv3 kick ","")
                    kk.kickoutFromGroup(msg.to,[midd])
            elif "Undang " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Undang ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
            elif "Cv1 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Cv1 invite ","")
                    ki.findAndAddContactsByMid(midd)
                    ki.inviteIntoGroup(msg.to,[midd])
            elif "Cv2 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Cv2 invite ","")
                    ki.findAndAddContactsByMid(midd)
                    ki.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["Me2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif msg.text in ["Me3"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki.sendMessage(msg)
            elif msg.text in ["Me4"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                ki.sendMessage(msg)
            elif msg.text in ["Me5"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ada yang error, pak!")
                        ki.sendText(msg.to,"Harap segera hubungi Si Creator!")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tagall1"]:
                if msg.from_ in admin:
       		      group = cl.getGroup(msg.to)
		      mem = [contact.mid for contact in group.members]
		      for mm in mem:
               	          xname = cl.getContact(mm).displayName
	                  xlen = str(len(xname)+1)
                          msg.text = "@"+xname+" "
		          msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
		          try:
                              cl.sendMessage(msg)
		          except Exception as error:
                     	      print error
            elif msg.text in ["Cv cancel","Bot cancel"]:
                if msg.toType == 2:
                    G = ki.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No one is inviting")
                        else:
                            ki.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ada yang error, pak!")
                        ki.sendText(msg.to,"Harap segera hubungi Si Creator!")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                        ki.sendText(msg.to,"Link Grup Sudah Terbuka")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka.")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Maaf, anda bukan admin.")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 ourl","Cv1 link on"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done")
                    else:
                        ki.sendText(msg.to,"Sudah terbuka.")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                        ki.sendText(msg.to,"Link Grup Sudah Tertutup")
                    else:
                        cl.sendText(msg.to,"Sudah tertutup.")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sorry, lu bukan admin ArBot.")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 curl","Cv1 link off"]:
                if msg.from_ in admin:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done")
                    else:
                        ki.sendText(msg.to,"Sudah tertutup.")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"Info Grup Ini:")
                        ki.sendText(msg.to,"[Nama Grup]\n" + str(ginfo.name) + "\n[Id Grup]\n" + msg.to + "\n[Pembuat Grup]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nMembers:" + str(len(ginfo.members)) + "Anggota\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[Nama Grup]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[Pembuat grup]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ada yang error, pak!")
                        ki.sendText(msg.to,"Harap segera hubungi Si Creator!")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)

            elif msg.text in ["Lgroup"]:
                if msg.from_ in admin:
                  gid = cl.getGroupIdsJoined()
                  h = ""
                  for i in gid:
                      h += "[~] [%s]:\n" % (cl.getGroup(i).name)
                  cl.sendText(msg.to,"======[List Group]======\n"+ h +"Total Group : "+str(len(gid)))

            elif msg.text in ["GIA"]:
                if msg.from_ in admin:
                  gids = cl.getGroupIdsJoined()
                  h = ""
                  for i in gids:
                      gn = cl.getGroup(i).name
                      h += "[+] [%s]\n" % (gn)
                  cl.sendText(msg.to,"======[List Group]======\n"+ h +"Total group: "+str(len(gids)))

            elif msg.text in ["Daftar grup"]:
                if msg.from_ in admin:
                  gid = cl.getGroupIdsJoined()
                  h = ""
                  for i in gid:
                      h += "[*] [%s]\n" % (cl.getGroup(i).name)
                  cl.sendText(msg.to,"======[List Group]======\n"+ h +"Total Group :" +str(len(gid)))

            elif msg.text in ["/ListIDGroup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = "===[List Group]==="
                    if msg.text in ["List group"]:
                       for i in gid:
                           h += "[%s]\n -+GroupID :" +  "%s\n -+TotalMembers :" + "%s\n -+MembersPending :" +  "%s\n -+Creator : %s\n" % (cl.getGroup(i).name,i,str(cl.getGroup(i).members),cl.getGroup(i).invite,cl.getGroup(i).creator.displayName)
                       cl.sendText(msg.to,h + "|[Total Group]| : " + str(len(gid)))

            elif msg.text in ["List group","Glist"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[⭐] %s  \n" % (cl.getGroup(i).name + " | Members : " + str(len (cl.getGroup(i).members)))
                    cl.sendText(msg.to, "☆「Group List」☆\n"+ h +"Total Group : " +str(len(gid)))

        #-------------Fungsi Creator Start-----------------#
            elif msg.text in ["Bot Creator"]:
                if msg.toType == 2:
                      msg.contentType = 13
                      Creatorbot = "u308205dd6abcc4bec5da585db20ab076"
                      try:
                          msg.contentMetadata = {'mid': Creatorbot}
                      except:
                          Creatorbot = "Error"
                      cl.sendText(msg.to, "My Creator : Ari.")
                      cl.sendMessage(msg)

#-----------------------------------------

            elif "Copy @" in msg.text:
                if msg.from_ in admin:
                     print "[COPY] Ok"
                     _name = msg.text.replace("Copy @","")
                     _nametarget = _name.rstrip('  ')
                     gs = cl.getGroup(msg.to)
                     targets = []
                     for g in gs.member:
                         if _nametarget == g.displayName:
                             targets.append(g.mid)
                     if targets == []:
                         cl.sendMessage(msg.to, "Not Found...")
                     else:
                         for target in targets:
                             try:
                                cl.CloneContactProfile(target)
                                cl.sendMessage(msg.to, "Succes Copy profile")
                             except Exception as e:
                                 print error

            elif "Steal: " in msg.text:
                if msg.from_ in admin:
                    salsa = msg.text.replace("Steal: ","")
                    Manis = cl.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Foto Profilenya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        cl.sendText(msg.to,"Gambar Covernya")
                        cl.sendImageWithURL(msg.to,cover)

#-----------------------------------------

	    elif wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 kk.sendText(msg.to,"Banned contact!, \n➡Unban: " + invite)
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Invited: \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         try:
                                             ki.findAndAddContactsByMid(invite)
                                             ki.inviteIntoGroup(op.param1,[invite])
                                             wait["winvite"] = False
                                             ki.sendText(msg.to,"Failed Invite: \n➡" + _name)
                                             break
                                         except:
                                            try:
                                                 kk.findAndAddContactsByMid(invite)
                                                 kk.inviteIntoGroup(op.param1,[invite])
                                                 wait["winvite"] = False
                                                 kk.sendText(msg.to,"Done. \n➡" + _name)
                                                 break
                                            except:
                                                 cl.sendText(msg.to,"Negative, Error detected")
                                                 wait["winvite"] = False
                                                 break

            elif msg.text in ["Cinvite"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact 😉")

#-----------------------------------------

            elif "Spamg " in msg.text:
               if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spamg "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                 #@rid1bdbx
                if txt[1] == "on":
                    if jmlh <= 1000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")

            elif "Spamn " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spamn ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                 #Keke cantik <3
                if txt[1] == "on":
                    if jmlh <= 999:
                       for x in range(jmlh):
                           ki.sendText(msg.to, teks)
                    else:
                       ki.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 999:
                        ki.sendText(msg.to, tulisan)
                    else:
                        ki.sendText(msg.to, "Kelebihan batas :v")

#-----------------------------------------

            elif msg.text in ["bot out"]:
                if msg.from_ in admin:
                   gid = cl.getGroupIdsJoined()
                   gid = ki.getGroupIdsJoined()
                   gid = kk.getGroupIdsJoined()
                   gid = ar.getGroupIdsJoined()
                   gid = pi.getGroupIdSpjudulgan
                   for i in gid:
                       ki.leaveGroup(i)
                       kk.leaveGroup(i)
                   if wait["lang"] == "JP":
                       cl.sendText(msg.to,"Good bye my friends :)")
                   else:
                       cl.sendText(msg.to,"He declined all invitations")

        #-------------Fungsi Creator Finish-----------------#

            elif msg.text in ["Gcreator:inv"]:
                if msg.from_ in admin:
                   ginfo = cl.getGroup(msg.to)
                   gCreator = ginfo.creator.mid
                   try:
                      cl.findAndAddContactsByMid(gCreator)
                      cl.inviteIntoGroup(msg.to,[gCreator])
                      print "success inv gCreator"
                   except:
                      pass

            elif "GroupCreator" == msg.text:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"old user")

            elif msg.text in["@tag"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, jml = [], [], [], len(nama)
                if jml <= 100:
                   mention(msg.to, nama)
                if jml > 100 and jml < 200:
                   for i in range(0, 99):
                       nm1 += [nama[i]]
                   mention(msg.to, nm1)
                   for j in range(100, len(nama)-1):
                       nm2 += [nama[j]]
                   mention(msg.to, nm2)
                if jml > 200  and jml < 300:
                   for i in range(0, 99):
                       nm1 += [nama[i]]
                   mention(msg.to, nm1)
                   for j in range(100, 199):
                       nm2 += [nama[j]]
                   mention(msg.to, nm2, jml)
                   for k in range(200, len(nama)-1):
                       nm3 += [nama[k]]
                   mention(msg.to, nm3, jml)
                if jml > 300:
                    print "Terlalu Banyak Men 300+"
                cnt = Message()
                cnt.text = "Done:"+str(jml)
                cont.to = msg.to
                cl.sendMessage(cnt)
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
            elif msg.text in ["Mid all","Mid All"]:
                 cl.sendText(msg.to,"[ArHar, ArQyu, ArKan ID\n\nArHar ID\n" + mid + "\n\nArQyu ID\n" + Amid + "\n\nArKan ID\n" + Bmid)
                 print "[Command]Mid executed"
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
            elif "Mid @" == msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.displayName + "\n" + g.mid)
                    else:
                        pass
            elif "Me @" == msg.text:
                msg.contentType = 13
                _name = msg.text.replace("Me @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                        pass
            elif "Cv1 mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentTpython2ype = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                if msg.from_ in admin:
                   string = msg.text.replace("Cn ","")
                   if len(string.decode('utf-8')) <= 20:
                       profile = cl.getProfile()
                       profile.displayName = string
                       cl.updateProfile(profile)
                       cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv1 rename "]:
                if msg.toType == 2:
                   string = msg.text.replace("Cv1 rename ","")
                   if len(string.decode('utf-8')) <= 20:
                       profile_B = ki.getProfile()
                       profile_B.displayName = string
                       ki.updateProfile(profile_B)
                       ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(mmid)

            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Sett"]:
                if msg.from_ in admin:
                     md = "Admin Setting:\n"
                     if wait["contact"] == True: md+=" Contact : on\n"
                     else: md+=" Contact : off\n"
                     if wait["autoJoin"] == True: md+=" Auto join : on\n"
                     else: md +=" Auto join : off\n"
                     if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                     else: md+= " Group cancel : off\n"
                     if wait["ProtectQr"] == True: md+=" Protect Qr : on\n"
                     else: md+=" Protect Qr : off\n"
                     if wait["ProtectGuest"] == True: md+=" Protect Guest : on\n"
                     else: md+=" Protect Guest : off\n"
                     if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
                     else: md+=" Auto leave : off\n"
                     if wait["timeline"] == True: md+=" Share : on\n"
                     else:md+=" Share : off\n"
                     if wait["autoAdd"] == True: md+=" Auto add : on\n"
                     else:md+=" Auto add : off\n"
                     if wait["commentOn"] == True: md+=" Comment : on\n"
                     else:md+=" Comment : off\n"
                     if wait["atjointicket"] == True: md+=" Auto Join Group by Ticket : on\n"
                     else:md+=" Auto Join Group by Ticket : off\n"
                     cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                gid = msg.text.replace("album removeâ†’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["ProtectQr on"]:
                if msg.from_ in admin:
                   if wait["ProtectQR"] == True:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectQr on")
                       else:
                           cl.sendText(msg.to,"done")
                   else:
                       wait["ProtectQR"] = True
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectQr on")
                       else:
                           cl.sendText(msg.to,"done")
            elif msg.text in ["ProtectQr off"]:
                if msg.from_ in admin:
                   if wait["ProtectQR"] == False:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect QR Off")
                       else:
                           cl.sendText(msg.to,"done")
                   else:
                       wait["ProtectQR"] = False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect QR Off")
                       else:
                           cl.sendText(msg.to,"done")
            elif msg.text in ["ProtectGuest on"]:
                if msg.from_ in admin:
                   if wait["ProtectGuest"] == True:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect Guest On")
                       else:
                           cl.sendText(msg.to,"done")
                   else:
                       wait["ProtectGuest"] == True
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect Guest On")
                       else:
                           cl.sendText(msg.to,"done")
            elif msg.text in ["ProtectGuest off"]:
                if msg.from_ in admin:
                   if wait["ProtectGuest"] == False:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect Guest Off")
                       else:
                           cl.sendText(msg.to,"done")
                   else:
                       wait["ProtectGuest"] == False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect Guest Off")
                       else:
                           cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if msg.from_ in admin:
                   if wait["autoAdd"] == True:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"already on")
                       else:
                           cl.sendText(msg.to,"done")
                   else:
                       wait["autoAdd"] = True
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"done")
                       else:
                           cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if msg.from_ in admin:
                   if wait["autoAdd"] == False:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"already off")
                       else:
                           cl.sendText(msg.to,"done")
                   else:
                       wait["autoAdd"] = False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"done")
                       else:
                           cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                if msg.from_ in admin:
                   wait["message"] = msg.text.replace("Message change: ","")
                   cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                if msg.from_ in admin:
                   wait["message"] = msg.text.replace("Message add: ","")
                   if wait["lang"] == "JP":
                       cl.sendText(msg.to,"message changed")
                   else:
                       cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if msg.from_ in admin:
                   if wait["lang"] == "JP":
                       cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                   else:
                       cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                if msg.from_ in admin:
                   c = msg.text.replace("Comment:","")
                   if c in [""," ","\n",None]:
                       cl.sendText(msg.to,"message changed")
                   else:
                       wait["comment"] = c
                       cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                if msg.from_ in admin:
                   c = msg.text.replace("Add comment:","")
                   if c in [""," ","\n",None]:
                       cl.sendText(msg.to,"String that can not be changed")
                   else:
                       wait["comment"] = c
                       cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if msg.from_ in admin:
                   if wait["commentOn"] == True:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"done")
                       else:
                           cl.sendText(msg.to,"already on")
                   else:
                       wait["commentOn"] = True
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"done")
                       else:
                           cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if msg.from_ in admin:
                   if wait["commentOn"] == False:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"done")
                       else:
                           cl.sendText(msg.to,"already off")
                   else:
                       wait["commentOn"] = False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"done")
                       else:
                           cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"Perbarui grup...%")
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"Perbarui grup...%")
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
                if msg.from_ in admin:
                   if wait["clock"] == True:
                       cl.sendText(msg.to,"already on")
                   else:
                       wait["clock"] = True
                       now2 = datetime.now()
                       nowT = datetime.strftime(now2,"(%H:%M)")
                       profile = cl.getProfile()
                       profile.displayName = wait["cName"] + nowT
                       cl.updateProfile(profile)
                       cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
                if msg.from_ in admin:
                   if wait["clock"] == False:
                       cl.sendText(msg.to,"already off")
                   else:
                       wait["clock"] = False
                       cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
                if msg.from_ in admin:
                   n = msg.text.replace("Change clock ","")
                   if len(n.decode("utf-8")) > 13:
                       cl.sendText(msg.to,"changed")
                   else:
                       wait["cName"] = n
                       cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if msg.from_ in admin:
                   if wait["clock"] == True:
                       now2 = datetime.now()
                       nowT = datetime.strftime(now2,"(%H:%M)")
                       profile = cl.getProfile()
                       profile.displayName = wait["cName"] + nowT
                       cl.updateProfile(profile)
                       cl.sendText(msg.to,"Jam Update")
                   else:
                       cl.sendText(msg.to,"Please turn on the name clock")

            elif msg.text == "$set":
                if msg.toType == 2:
                    cl.sendText(msg.to, "Check sider")
                    ki.sendText(msg.to, "Check sider")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2

            elif msg.text == "$read":
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")

            elif msg.text == "Cctv":
                if msg.toType == 2:
                      cl.sendText(msg.to, "Cek CCTV")
                      try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                      except:
                          pass
                      now2 = datetime.now()
                      wait2['readPoint'][msg.to] = msg.id
                      wait2['readMember'][msg.to] = ""
                      wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                      wait2['ROM'][msg.to] = {}
                      print wait2
            elif msg.text == "Ciduk":
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                    cl.sendText(msg.to, "||===== Di Read Oleh =====||%s\n||======= SVF BOT ======||\n\n||Pelaku CCTV 👇👇👇||\n%sOrang Ini Gak Normal Plak\n\nBuang Aja Ke Laut\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                else:
                    cl.sendText(msg.to, "CCTV Sudah Di Ketik Koplak\nTinggal Ketik Ciduk Aja\nDASAR PIKUN ♪")

#-----------------------------------------------
            elif "Bcc: " in msg.text:
                if msg.from_ in admin:
                     broadcasttxt = msg.text.replace("Bcc: ", "")
                     orang = cl.getAllContactIds()
                     for manusia in orang:
                          ki.sendText(manusia, (broadcasttxt))

            elif "Bcgc: " in msg.text:
                if msg.from_ in admin:
                     broadcasttxt = msg.text.replace("Bcgc: ", "")
                     orang = cl.getGroupIdsJoined()
                     for manusia in orang:
                          kk.sendText(manusia, (broadcasttxt))

            elif "Bcgroup " in msg.text:
                if msg.from_ in admin:
                    bctxt = msg.text.replace("Bcgroup ", "")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                         cl.sendText(manusia, (bctxt))

            elif "Bccontact " in msg.text:
                if msg.from_ in admin:
                    bctxt = msg.text.replace("Bccontact ", "")
                    t = cl.getAllContactIds()
                    for manusia in t:
                         cl.sendText(manusia, (bctxt))

#-----------------------------------------------

            elif msg.text in ["All join","All Join"]:
                if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ar.acceptGroupInvitationByTicket(msg.to,Ticket)
                        pi.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text in ["Cv1 join"]:
                if msg.from_ in admin:
                     X = cl.getGroup(msg.to)
                     X.preventJoinByTicket = False
                     cl.updateGroup(X)
                     invsend = 0
                     Ti = cl.reissueGroupTicket(msg.to)
                     cl.acceptGroupInvitationByTicket(msg.to,Ti)
                     G = ki.getGroup(msg.to)
                     G.preventJoinByTicket = True
                     ki.updateGroup(G)
                     Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["Cv2 join"]:
                if msg.from_ in admin:
                     X = cl.getGroup(msg.to)
                     X.preventJoinByTicket = False
                     cl.updateGroup(X)
                     invsend = 0
                     Ti = cl.reissueGroupTicket(msg.to)
                     ki.acceptGroupInvitationByTicket(msg.to,Ti)
                     kk.acceptGroupInvitationByTicket(msg.to,Ti)
                     G = cl.getGroup(msg.to)
                     G.preventJoinByTicket = True
                     cl.updateGroup(G)
                     Ticket = ki.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Cv3 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


#-----------------------------------------------

            elif msg.text in ["Bye bot","Bye 69"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                        ki.leaveGroup(msg.to)
                        ar.leaveGroup(msg.to)
                        pi.leaveGroup(msg.to)
                        cl.sendText(msg.to,"Good Bye Kawan-Kawan " + str(ginfo.name) + "\nTerima Kasih Untuk Group nya " + ginfo.creator.displayName + "\n\n~Salam ArHar~")
                        cl.leaveGroup(msg.to)
                    except:
                        pass
                else:
                    kk.sendText(msg.to,"Command denied.")
                    kk.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Bye 2"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"Good Bye Kawan-Kawan " + str(ginfo.name) + "\nTerima Kasih Untuk Group nya " + ginfo.creator.displayName + "\n\n~Salam ArQyu~")
                        ki.leaveGroup(msg.to)
                    except:
                        pass
                else:
                    random.choice(KAC).sendText(msg.to,"Command denied.")
                    random.choice(KAC).sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Bye 1"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"Good Bye Kawan-Kawan " + str(ginfo.name) + "\nTerima Kasih Untuk Group nya " + ginfo.creator.displayName + "\n\n~Salam ArHar~")
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye 3"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.sendText(msg.to,"Good Bye Kawan-Kawan " + str(ginfo.name) + "\nTerima Kasih Untuk Group nya " + ginfo.creator.displayName + "\n\n~Salam ArKan~")
                        kk.leaveGroup(msg.to)
                    except:
                        pass
                else:
                    random.choice(KAC).sendText(msg.to,"Command denied.")
                    random.choice(KAC).sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Cv1 @bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg,to)
                    except:
                        pass
                else:
                    kc.sendText(msg.to,"Command denied.")
                    kc.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"

#-----------------------------------------------
            elif msg.text in["@tag"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, jml = [], [], [], len(nama)
                if jml <= 100:
                   mention(msg.to, nama)
                if jml > 100 and jml < 200:
                   for i in range(0, 99):
                       nm1 += [nama[i]]
                   mention(msg.to, nm1)
                   for j in range(100, len(nama)-1):
                       nm2 += [nama[j]]
                   mention(msg.to, nm2)
                if jml > 200  and jml < 300:
                   for i in range(0, 99):
                       nm1 += [nama[i]]
                   mention(msg.to, nm1)
                   for j in range(100, 199):
                       nm2 += [nama[j]]
                   mention(msg.to, nm2, jml)
                   for k in range(200, len(nama)-1):
                       nm3 += [nama[k]]
                   mention(msg.to, nm3, jml)
                if jml > 300:
                    print "Terlalu Banyak Men 300+"
                cnt = Message()
                cnt.text = "Done:"+str(jml)
                cont.to = msg.to
                cl.sendMessage(cnt)
#-----------------------------------------------
            elif msg.text in ["Summon"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    ki.sendMessage(msg)
                except Exception as error:
                    print error

            elif msg.text in ["tag all"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                aa = ""
                bb = ""
                strt = int(0)
                akh = int(0)
                nm = nama
                print nm
                for mm in nm:
                  akh = akh + 3
                  aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
                  strt = strt + 4
                  akh = akh + 1
                  bb += "\xe2\x98\xbb @x \n"
                aa = (aa[:int(len(aa)-1)])
                msg = Message()
                msg.to = op.param1
                msg.from_ = profile.mid
                msg.text = bb
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
                print msg
                try:
                   cl.sendMessage(msg)
                except Exception as error:
                    print error

            elif msg.text in ["Ar Tagall", "Ar tagall"]:
                group = cl.getGroup(msg.to)
                msg_appended = ""
                strt = int(0)
                mem = [contact.mid for contact in group.members]
                for mm in mem:
                    xname = cl.getContact(mm).displayName
                    xlen = str(len(xname)+1)
                    msg.contentType = 0
                    msg.text ="=>"+"@"+xname+"]\n"
                    msg.contentMetadata={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
                    msg_appended += "->" +msg+ "\n"
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error

            else:
                if cl.getGroup(msg.to).preventJoinByTicket == False:
                    cl.reissueGroupTicket(msg.to)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                else:
                    if msg.from_ in admin and Bots:
                        pass
                    else:
                        print "No Action"

#-----------------------------------------------
            if msg.text in ["Kill"]:
                if msg.from_ in admin:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Ratakan" in msg.text:
                if msg.from_ in admin and Bots:
                    print "ok"
                    _name = msg.text.replace("Ratakan","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    cl.sendText(msg.to,"Siap!")
                    ki.sendText(msg.to,"Memnyiapkan Proses Perataan.")
                    ki.sendText(msg.to,"Memulai Perataan.")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                           if not target in admin and Bots:
                            try:
                                klist=[cl,ki]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Grup sudah rata Bang Ar.")
                                ki.sendText(msg.to,"Siap melaksanakan perintah selanjutnya!")
            elif "Dj " in msg.text:
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           random.choice(KAC).kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif "Kickout " in msg.text:
                 if msg.from_ in admin:
                      nk0 = msg.text.replace("Kickout ","")
                      nk1 = nk0.lstrip()
                      nk2 = nk1.replace("@","")
                      nk3 = nk2.rstrip()
                      _name = nk3
                      gs = cl.getGroup(msg.to)
                      targets = []
                      for s in gs.members:
                          if _name in s.displayName:
                             targets.append(s.mid)
                      if targets == []:
                          sendMessage(msg.to,"user does not exist")
                          pass
                      else:
                          for target in targets:
                               try:
                                   klist=[cl,ki]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                               except:
                                   ki.sendText(msg.to,"Succes Bang Ar")
                                   ki.sendText(msg.to,"👌")

            elif ("Bye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass

            elif ("Tandai " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass

            elif msg.text in ["Ar list"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    xname = ""
                    for mi_d in wait["blacklist"]:
                        xname = cl.getContact(mi_d).displayName + "\n"
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+"\n" " "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mi_d)+'}]}','EMTVER':'4'}
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error

            elif "Blacklist @" in msg.text:
                if msg.from_ in admin:
                   print "[Blacklist]ok"
                   _name = msg.text.replace("Blacklist @","")
                   _kicktarget = _name.rstrip(' ')
                   gs = ki.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _kicktarget == g.displayName:
                           targets.append(g.mid)
                           if targets == []:
                               cl.sendText(msg.to,"Not found")
                           else:
                               for target in targets:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       k3.sendText(msg.to,"Succes Bang Ar")
                                   except:
                                       ki.sendText(msg.to,"Gagal Bang :'(")
            elif "Catat @" in msg.text:
                if msg.from_ in admin:
                    print "[Catat]ok"
                    _name = msg.text.replace("Catat @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes Tercatat Bang Ar")
                            except:
                                ki.sendText(msg.to,"Gagal tercatat Bang Ar :(")
                                ki.sendText(msg.to,"Sorry...")
            elif "Uncatat @" in msg.text:
                if msg.from_ in admin:
                    print "[Uncatat]ok"
                    _name = msg.text.replace("Uncatat @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Selamat!")
                                ki.sendText(msg.to,"Success dilepaskan dari catatan.")
                            except:
                                ki.sendText(msg.to,"Succes Bro!")

            elif msg.text in ["Fuck","fuck","Kontol","kontol"]:
                if op.param2 not in admin:
                    print receiver
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

#-----------------------------------------------
            elif msg.text in ["On Bot","On bot"]:
                cl.sendText(msg.to,"On Bos  􀨁􀄻double thumbs up􏿿")
            elif msg.text in ["Test","test"]:
                cl.sendText(msg.to,"Lulus")
            elif msg.text in ["Tes","tes"]:
                cl.sendText(msg.to,"Tis")
            elif msg.text in ["Tis","tis"]:
                cl.sendText(msg.to,"Dih doyan biji\nCiri khas Pedo nih")
#-----------------------------------------------
            elif msg.text in ["wc","Wc","wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Guys Di " + str(ginfo.name))
                cl.sendText(msg.to,"Owner " + str(ginfo.name) + " :\n=>" + ginfo.creator.displayName )

#-----------------------------------------------
            elif "Say " in msg.text:
                if msg.toType == 2:
                	bctxt = msg.text.replace("Say ","")
	        	cl.sendText(msg.to,(bctxt))
			ki.sendText(msg.to,(bctxt))
#            elif "Sms: " in msg.text:
#               if msg.from_ in admin:
#                   cond = msg.text.split(" ")
#                   target = int(cond[1])
#                   text = msg.text.replace("Mengirim Kepada: " + str(target) + "\nIsi Pesan: ","")
#                   try:
#                       cl.findAndAddContactsByMid(target)
#                       cl.sendText(msg.to, target + "Ada Pesan Untukmu: \n"" + text + "\n\n~Pesan Berakhir~")
#                       cl.sendText(msg.to,"Berhasil mengirim pesan")
#                   except:
#                       cl.sendText(msg.to,"Gagal mengirim pesan, mungkin midnya salah")

#-----------------------------------------------

            elif msg.text in ["ArHar say hi"]:
                cl.sendText(msg.to,"Hi  􀜁􀅔Har Har􏿿")
#-----------------------------------------------

            elif msg.text in ["ArHar say hinata pekok"]:
                ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["ArHar say didik pekok"]:
                ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["ArHar say bobo ah","Bobo dulu ah"]:
                ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
            elif msg.text in ["ArHar say chomel pekok"]:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang di Localhost@Tersakiti Family Room")
                ki.sendText(msg.to,"Jangan nakal ok!")
            elif msg.text in ["AKU","Aku","aku","Aku?","aku?"]:
                ki.sendText(msg.to,"Iya sayang")
                ki.sendText(msg.to,"Kamu doank")
                ki.sendText(msg.to,"Muacchh..♡♡♡")
            elif msg.text in ["Ban","ban","BAN","Banned"]:
                cl.sendText(msg.to,"Mau nge Ban?")
                ki.sendText(msg.to,"Bikin bot sendiri!")
                ki.sendText(msg.to,"Dasar Ndeso!")
            elif msg.text in ["Saran Keyword"]:
                cl.sendText(msg.to,"Mau kirim saran keyword?")
                ki.sendText(msg.to,"Kirim langsung aja ke Bang Ar(Si Creator) \nDengan mengisi format dibawah👇")
                ki.sendText(msg.to,"Saran keyword:\n\nQ:...[diisi]\nA:...[diisi]\nA:...[boleh diisi jika jawaban A ada lanjutannya]\nJumlah jawaban A:...[diisi]\n\n\nKirim langsung ke Bang Ar, tunggu beberapa hari dan saranmu akan masuk ke list keyword\n\n\nIsilah saranmu dengan sekreatif mungkin, tetapi yang wajar.")
            elif msg.text in ["Unicodes"]:
                cl.sendText(msg.to,"Harap berhati-hati")
                ki.sendText(msg.to,"4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.")
            elif msg.text in ["hust","hus","Hust","Hus","Husst","husst","husss"]:
                ki.sendText(msg.to,"Meong 🐈")
            elif msg.text in ["ah","Ah","Argh","argh","akh","Akh","aah","Aah"]:
                cl.sendText(msg.to,"Ih")
                ki.sendText(msg.to,"Uh")
                cl.sendText(msg.to,"Eh")
                ki.sendText(msg.to,"Oh")
            elif msg.text in ["Hai","hai","haii","Haii"]:
                ki.sendText(msg.to,"Hai juga sayang 😘")
#-----------------------------------------------
            elif msg.text in ["Siapa Aku?","Siapa aku?","siapa aku?","Siapa aku","Siapa Aku"]:
                answ = ['Ente Manusie','You are the lazy human','Kamu adalah seorang anak dari 2 orang tua','Elo manusia oon','Aku? Jadi duta micin lain? Ahahaha','Orang','Manusia','Setan','Juragan Micin']
                psn = random.choice(answ)
                cl.sendText(msg.to,psn)

            elif msg.text in ["Quote","quote","quotes","Quotes"]:
                quote = ['Barangsiapa yang suka meninggalkan barang di tempat umum maka ia akan kehilangan barangnya tersebut\n\nQuote By Ari.','Kunci KESUKSESAN itu cuma satu, yakni lu harus BERHASIL.\n\nQuote By Ari.','Sebaik-baik orang memberi lebih baik ditabung\n\nQuote By Ari.','Lebih baik tangan diatas dari pada tangan di dalam celana\n\nQuote By Ari.']
                psn = random.choice(quote)
                cl.sendText(msg.to,psn)

            elif msg.text in ["Apakah Saya Ganteng?","Apakah saya ganteng?","apakah saya ganteng?"]:
                aw1 = ["Ya, anda ganteng"]
                aw2 = ["Ya, kamu ganteng"]
                aw3 = ["Tidak, anda jelek"]
                aw4 = ["Tidak, kamu jelek"]
                aw5 = ["Tidak, kamu buluk"]
                nan0 = [aw1,aw2,aw3,aw4,aw5]
                psn = random.choice(nan0)
                cl.sendText(msg.to,psn)


#-----------------------------------------------
            elif msg.text in ["Eh","eh","EH"]:
                ki.sendText(msg.to,"Apa eh???")
            elif msg.text in ["Sayang","sayang","ayang","Ayang"]:
                ki.sendText(msg.to,"Iya sayang")
            elif msg.text in ["Spam"]:
                ki.sendText(msg.to,"Yang spam mah kick aja")
            elif msg.text in ["p"]:
                cl.sendText(msg.to,"ler")
            elif msg.text in ["P"]:
                cl.sendText(msg.to,"Ler...")
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
            elif msg.text in ["...","..",".","Hh","hhh","hh","hhhhh"]:
                ki.sendText(msg.to,"Galau? Minum baygon aja :v")
            elif msg.text in [":v"]:
                ki.sendText(msg.to,"Ketawa bang?")
            elif msg.text in ["Laper","laper","Laver","laver"]:
                ki.sendText(msg.to,"Makan bang")
            elif msg.text in ["Hallo","hallo","Halo","halo","Alo","alo","Aloo","aloo"]:
                ki.sendText(msg.to,"Ya, ada yang bisa ArQyu bantu?")
            elif msg.text in ["Error","error","Eror","eror","Errno"]:
                ki.sendText(msg.to,"Ada yang error?")
                ki.sendText(msg.to,"Hubungi si Creator Ar-Har aja\nhttp://line.me/ti/p/~a.r.-")
            elif msg.text in ["Hmm","hmm","Hm","hm"]:
                ki.sendText(msg.to,"Ada Apa sayang?")
            elif msg.text in ["Ini apa?","Itu apa?","ini apa?","itu apa?"]:
                cl.sendText(msg.to,"Ini ArHar.👦")
                ki.sendText(msg.to,"Ini Ibu ArHar.👩")
                kk.sendText(msg.to,"Ini Bapak ArHar.👨")
            elif msg.text in ["Ar Har siapa?","ArHar siapa?","ar har siapa?","arhar siapa?","Itu siapa?","itu siapa?","Itu saha"]:
                cl.sendText(msg.to,"I'm ArHar :v\nCreator => Ari\nhttp://line.me/ti/p/~-a.r.i")
            elif msg.text in ["ngasyi ah?","ngasyi ah","Ngasyi ah","Ngasyi ah?"]:
                ki.sendText(msg.to,"Bang, kalo ngomong jangan disingkat-singkat")
                ki.sendText(msg.to,"Pakai Bahasa Indonesia yang wajar aja bang, lebih mudah dimengerti orang lain")
            elif msg.text in ["sepi ya","Sepi ya"]:
                ki.sendText(msg.to,"Karena gk rame sayang")
            elif msg.text in ["Woi","woi"]:
                cl.sendText(msg.to,"Apaan woi???")
            elif msg.text in ["sepi","Sepi"]:
                ki.sendText(msg.to,"Karena gk rame")
            elif msg.text in ["Anjing","anjing","njing","Anjeng","anjeng","njeng","Njir","njir","Njeng"]:
                ki.sendText(msg.to,"Kalem Euy")
                ki.sendText(msg.to,"Kalem, jangan ngegas :v")
            elif msg.text in ["About Creator","About creator","about creator"]:
                ki.sendText(msg.to,"About Creator:\nCreator ArHar itu si Bang Ar\nhttp://line.me/ti/p/~a.r.- \n\n Fakta tentang creator:\n-Masih Single\n-Wajah tamvan\n-Tubuh atletik + tinggi\n-Hobby baca buku bekas(bukan bekas dijilat)\n-Suka ngelawak tapi Garing\n-Sangat anti kekerasan")
            elif msg.text in ["/join","/Join"]:
                ki.sendText(msg.to,"Ini bukan bot WW")
                ki.sendText(msg.to,"ini bot ArQyu")

#-----------------------------------------------

            elif msg.text in ["ArHar","arhar"]:
                ki.sendText(msg.to,"Hadir✋􀜁􀅔Har Har�")
#-----------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Loading...")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))

#------------------------------------------------------------------
            elif msg.text in ["Catat"]:
                if msg.from_ in admin:
                     wait["wblacklist"] = True
                     cl.sendText(msg.to,"send contact")
                     ki.sendText(msg.to,"send contact")
            elif msg.text in ["Uncatat"]:
                if msg.from_ in admin:
                     wait["dblacklist"] = True
                     cl.sendText(msg.to,"send contact")
                     ki.sendText(msg.to,"send contact")
            elif msg.text in ["List Catatan"]:
                if msg.toType == 2:
                  if wait["blacklist"] == {}:
                      cl.sendText(msg.to,"nothing")
                      ki.sendText(msg.to,"Tak ada siapapun bos.")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
            elif msg.text in ["Ar Banlist","Ar banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"No user is Blacklisted")
                else:
                    cl.sendText(msg.to,"Blacklisted user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Banlist executed"
            elif msg.text in ["Cek Catatan"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kick catatan"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        ki.sendText(msg.to,"Tak ada siapapun bos.")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist harus di usir!")
                    ki.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    cl.sendText(msg.to,"Betul")
                    cl.sendText(msg.to,"Betul")
                    cl.sendText(msg.to,"Betul")
            elif msg.text in ["Bersihkan"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "Acak:" in msg.text:
                if msg.from_ in admin:
                    strnum = msg.text.replace("Acak:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "Ar img" in msg.text:
                path = "a.png"
                try:
                    cl.sendImage(msg.to, path)
                except:
                    cl.sendText(msg.to, "Failed to upload image")
            else:
                if cl.getGroup(msg.to).preventJoinByTicket == False:
                    cl.reissueGroupTicket(msg.to)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                else:
                    if msg.from_ in admin:
                        pass
                    else:
                        print "No Action"

            if msg.text in ["Ar Like", "Ar like"]:
                if msg.from_ in admin:
                    print "[Command]Like executed"
                    cl.sendText(msg.to,"Trying to Like post from admin")
                    try:
                        likePost()
                    except:
                        pass

            elif "albumchat" in msg.text:
                try:
                    albumtags = msg.text.replace("albumchat","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakechat" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakechat","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                       cl.sendText(msg.to,str(e))
                    except:
                        pass
                else:
                    kc.sendText(msg.to,"Command denied.")
                    kc.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n👉" + Name
                        wait2['ROM'][op.param1][op.param2] = "👉" + Name
                else:
                    cl.sendText
            except:
                  pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def autolike():
     for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in admin:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ArHar\nCreator 👇.\n\nhttp://line.me/ti/p/~a.r.-")
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ArQyu\nCreator 👇.\n\nhttp://line.me/ti/p/~a.r.-")
                    print "Like"
                except:
                    pass
            else:
                print "Already Liked"
     time.sleep(100)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

# -*- coding: utf-8 -*-
from ..Net.LineConnect import LineConnect
from .LineCallback import LineCallback


class LineClient(LineConnect):

    def __init__(self):
        LineConnect.__init__(self)

    def _loginresult(self):
        if self.onLogin == True:
            print "authToken : " + self.authToken + "\n"

            print "certificate : " + self.certificate + "\n"

            """:type profile: Profile"""
            profile = self._client.getProfile()

            print "name : " + profile.displayName
        else:
            print "must login!\n"


    """User"""
    def getProfile(self):
        return self._client.getProfile()

    def getSettings(self):
        return self._client.getSettings()

    def getSessions(self):
        return self._client.getSessions()

    def getUserTicket(self):
        return self._client.getUserTicket()

    def updateProfile(self, profileObject):
        return self._client.updateProfile(0, profileObject)

    def updateSettings(self, settingObject):
        return self._client.updateSettings(0, settingObject)


    """Operation"""
    def fetchOperation(self, revision, count):
        return self._client.fetchOperations(revision, count)

    def getLastOpRevision(self):
        return self._client.getLastOpRevision()


    """Message"""
    def sendEvent(self, messageObject):
        return self._client.sendEvent(0, messageObject)

    def sendMessage(self, messageObject):
        return self._client.sendMessage(0,messageObject)

    """Contact"""

    def blockContact(self, mid):
        return self._client.blockContact(0, mid)

    def unblockContact(self, mid):
        return self._client.unblockContact(0, mid)

    def findAndAddContactsByMid(self, mid):
        return self._client.findAndAddContactsByMid(0, mid)

    def findAndAddContactsByUserid(self, userid):
        return self._client.findAndAddContactsByUserid(0, userid)

    def findContactsByUserid(self, userid):
        return self._client.findContactByUserid(userid)

    def findContactByTicket(self, ticketId):
        return self._client.findContactByUserTicket(ticketId)

    def getAllContactIds(self):
        return self._client.getAllContactIds()

    def getBlockedContactIds(self):
        return self._client.getBlockedContactIds()

    def getContact(self, mid):
        return self._client.getContact(mid)

    def getContacts(self, midlist):
        return self._client.getContacts(midlist)

    def getFavoriteMids(self):
        return self._client.getFavoriteMids()

    def getHiddenContactMids(self):
        return self._client.getHiddenContactMids()


    """Group"""

    def acceptGroupInvitation(self, groupId):
        return self._client.acceptGroupInvitation(0, groupId)

    def acceptGroupInvitationByTicket(self, groupId, ticketId):
        return self._client.acceptGroupInvitationByTicket(0, groupId, ticketId)

    def cancelGroupInvitation(self, groupId, contactIds):
        return self._client.cancelGroupInvitation(0, groupId, contactIds)

    def createGroup(self, name, midlist):
        return self._client.createGroup(0, name, midlist)

    def getGroup(self, groupId):
        return self._client.getGroup(groupId)

    def getGroups(self, groupIds):
        return self._client.getGroups(groupIds)

    def getGroupIdsInvited(self):
        return self._client.getGroupIdsInvited()

    def getGroupIdsJoined(self):
        return self._client.getGroupIdsJoined()

    def inviteIntoGroup(self, groupId, midlist):
        return self._client.inviteIntoGroup(0, groupId, midlist)

    def kickoutFromGroup(self, groupId, midlist):
        return self._client.kickoutFromGroup(0, groupId, midlist)

    def leaveGroup(self, groupId):
        return self._client.leaveGroup(0, groupId)

    def rejectGroupInvitation(self, groupId):
        return self._client.rejectGroupInvitation(0, groupId)

    def reissueGroupTicket(self, groupId):
        return self._client.reissueGroupTicket(groupId)

    def updateGroup(self, groupObject):
        return self._client.updateGroup(0, groupObject)

    """Room"""

    def createRoom(self, midlist):
        return self._client.createRoom(0, midlist)

    def getRoom(self, roomId):
        return self._client.getRoom(roomId)

    def inviteIntoRoom(self, roomId, midlist):
        return self._client.inviteIntoRoom(0, roomId, midlist)

    def leaveRoom(self, roomId):
        return self._client.leaveRoom(0, roomId)


    """unknown function"""

    def noop(self):
        return self._client.noop()
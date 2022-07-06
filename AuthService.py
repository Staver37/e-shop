#HW3 
## -try to fonish this class
from .Client import Client
from .Model import Model
class AuthService(Model):
#
    def signUp():
        signUP_Auth = Client.create()
        return signUP_Auth
#        
     

    def signIn():
        pass

    def signOut():
        pass

    def deleteAcount(id):
        del_A = Client.delete(id)
        return del_A

    def updateAcount(self):
        update_A = Client.save(self)
        return update_A


#########################
    def viewProfile(C_id):
        client_V = Client.all(C_id)
        return client_V


    def changePassword():
        pass
#########################   
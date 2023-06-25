from pyVoIP.VoIP import VoIPPhone, InvalidStateError, VoIPCall
from pyVoIP.VoIP import VoIPPhone, InvalidStateError, CallState


class Call(VoIPCall):

    def ringing(self, invite_request):
        try:
            self.answer()
            self.hangup()
        except InvalidStateError:
            pass

if __name__ == "__main__":
    server_ip = '31' # 
    server_port = ''
    server_login = '<SIP Server Username>'
    server_pswd = 'mHhhhhhhhh'
    myIP = '1mmmmmmmmmmmmmmmmm'  # 
    bind_ip = '0.0.0.0'  # 'ddddddddddd'
    bind_port = 5060
    sipPort = 5060
    phone = 'mmmmmmmmmmmm'
    phone = VoIPPhone(server_ip, sipPort, server_login, server_pswd, myIP)
    
    phone.start()
    print(phone.get_status())
    phone.call(phone)
    input('Press enter to disable the phone')
    phone.stop()

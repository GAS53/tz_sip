from pyVoIP.VoIP import VoIPPhone, InvalidStateError, VoIPCall
from pyVoIP.VoIP import VoIPPhone, InvalidStateError, CallState
import time
import wave




def answer(call):
    try:
        f = wave.open('1_source.wav', 'rb')
        frames = f.getnframes()
        data = f.readframes(frames)
        f.close()

        call.answer()
        call.write_audio(data)  # This writes the audio data to the transmit buffer, this must be bytes.

        stop = time.time() + (frames / 8000)  # frames/8000 is the length of the audio in seconds. 8000 is the hertz of PCMU.

        while time.time() <= stop and call.state == CallState.ANSWERED:
            time.sleep(0.1)
        call.hangup()
    except InvalidStateError:
        pass
    except:
        call.hangup()



if __name__ == "__main__":
    server_ip = 'fffffff' # 'sip.novofon.com'
    server_port = 'fffffffffffff'
    server_login = 'ffff' # <SIP Server Username>
    server_pswd = 'mffffffffff'
    myIP = 'ffffffff'  # '178.57.116.145'
    sipPort = 5060
    # rtpPortLow = 8080
    # rtpPortHigh = 8088
    phone = VoIPPhone(server_ip, sipPort, server_login, server_pswd, myIP, callCallback=answer)
    input('Press enter to disable the phone')
    phone.stop()

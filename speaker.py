import sys, gtts

def info():
	print ("Usage: python toolName.py yourText filename")

def speaker():
	tts = gtts.gTTS(text = sys.argv[1], lang = "ru")

	tts.save(sys.argv[2])
    
    print ("Operation done!")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        info()
    else:
        speaker()
import time
import pyaudio
import numpy as np
from matplotlib import pyplot as plt


CHUNKSIZE = 44100 # fixed chunk size

# initialize portaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=CHUNKSIZE)

# do this as long as you want fresh samples
#plt.axis([0, 44100, -10000, 10000])
plt.ion()
plt.show()

while True:
	plt.clf()
	data = stream.read(CHUNKSIZE)
	numpydata = np.fromstring(data, dtype=np.int16)
	# plot data
	plt.plot(numpydata)
	plt.draw()
	time.sleep(0.001)
	
# close stream
stream.stop_stream()
stream.close()
p.terminate()

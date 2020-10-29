from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_nonsilent
import os

class AudioSegmenting:

    def AudioSegmenting(self, fileName):

        self.fileName = fileName

        DirectPath = os.path.dirname(fileName)
        os.mkdir(DirectPath + "/Chunks/")

        sound = AudioSegment.from_file(fileName, format="wav")
        soundNoiseThresh = sound.dBFS - 16

        chunks = split_on_silence(sound, min_silence_len=1000, silence_thresh=soundNoiseThresh)

        target_length = 25*1000

        output_chunks = [chunks[0]]

        for chunk in chunks[1:]:
            if len(output_chunks[-1]) < target_length:
                output_chunks[-1] += chunk
            else:
                output_chunks.append(chunk)

        for i, chunk in enumerate(output_chunks):
            chunk.export(DirectPath + "/Chunks/chunk{0:04}.wav".format(i), format="Wav")








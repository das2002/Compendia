import moviepy.editor as mp
from scenedetect import SceneManager, open_video, ContentDetector
from pytube import YouTube

class Processor:

    video_filename = str()
    audio_filename = str()
    image_timestamps = []
    images = []
    snippets = []
    audio_snippets= []
    snippets_to_text = []

    def splitAV(self, filename, threshold=27.0):
        """This function extracts the audio and video files from the video in the filepath
        

        """
        SAVE_PATH = "C:/Users/pratd/OneDrive/Documents/UC Berkeley/Junior Year/LectureSynth/"
        print(filename)
        videoclip = mp.VideoFileClip(filename)
        print(videoclip.duration)
        audioclip = videoclip.audio
        print(audioclip.duration)
        audioclip.write_audiofile(filename = SAVE_PATH + "_audio.mp3")
        video = open_video(filename)
        scene_manager = SceneManager()
        scene_manager.add_detector(
            ContentDetector(threshold=threshold)
        )
        scene_manager.detect_scenes(video)
        snippets = scene_manager.get_scene_list()
        final_snippets = list()

        for x in snippets:
            if x[1].get_seconds() - x[0].get_seconds() > 2:
                final_snippets.append(x)
        print(final_snippets)

        audio_segments = list()
        
        for i in range(len(final_snippets)-1):
            audio_segments.append([final_snippets[i][0], final_snippets[i+1][0]])
        
        audio_snippets = [audioclip.cutout(i[1].get_seconds() - i[0].get_seconds()) for i in audio_segments]
        
        
        return None

    def findChangeTimestamps(self, video):
        """For an uploaded video, find the timestamps of when the video changes.
        
        When a change is detected, put the image associated with that change in the images list
        """

        return None



    def createAudioSnippets(self, audio):
        """ using the image_timestamps, store the audio snippets in the snippets list"""

        return None
        
    def snippetsToText(self):
        """go through the audio snippets and """

def main():
    processor = Processor()
    '''
    
    url = "https://www.youtube.com/watch?v=xDPUHRjsgA4&list=PLgNUCz66KaWRSVzIeT_qB2yBgHocLmRWI&index=8"
    SAVE_PATH = "C:/Users/pratd/OneDrive/Documents/UC Berkeley/Junior Year/LectureSynth"
    try:
        yt = YouTube(url)
    except:
        print("Connection Error")

    mp4files = yt.streams.filter(file_extension='mp4')
    d_video = yt.streams.get_by_itag(22) #yt.streams.get(mp4files[1].extension, mp4files[1].resolution)
    try:
        d_video.download(output_path = SAVE_PATH, filename= "lecture.mp4")
    except:
        print("Some Error!")
    print("Download Complete!")

    '''


    processor.splitAV("lecture.mp4")

if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
import os
import fnmatch
import subprocess
import argparse

# SOX_EXE = 'c:\Program Files (x86)\sox-14-4-2\sox.exe'
SOX_EXE = os.path.join('sox', 'sox.exe')
SOXI_EXE = os.path.join('sox', 'soxi.exe')

MUSIC_DIRS= []

# Display options on the output graph
renderer_settings = {'show_title': True,
                     'output_to_separate_dir': True,
                     'output_relative_dir_name': 'Spectrogram'}
print('renderer settings=', renderer_settings)

def MatchesExtensions(name,extensions=["*.flac", "*.mp3", "*.wav"]):
    for pattern in extensions:
        if fnmatch.fnmatch(name, pattern):
            return True
    return False

parser = argparse.ArgumentParser(description='Convert .flac into spectrogram PNG')
parser.add_argument('-i', '--input',
                      nargs='+',
                      dest='input_dirs',
                      required=True)
parser.add_argument('-t', '--title',
                    action='store_true',
                    default=True,
                    dest='title')
                   
opts = parser.parse_args()
print(opts.input_dirs)
# wait = input("PRESS ENTER TO CONTINUE.")

for dir in opts.input_dirs:
    print('Processing: ', dir)
     
    for root, dirs, files in os.walk(dir):
        for name in files:
            if MatchesExtensions(name):
                fpath = os.path.join(root, name)
                # print('Creating spectrogram for: ', name)
                 
                # spectrogram titleformatting
                title = name # use filename as title
                 
                """−x num Change the (maximum) width (X-axis) of the spectrogram from its default value of 800
                pixels to a given number between 100 and 200000. See also −X and −d."""
                x_size = 800
                 
                """−Y num
                Sets the target total height of the spectrogram(s). The default value is 550 pixels. Using
                this option (and by default), SoX will choose a height for individual spectrogram channels
                that is one more than a power of two, so the actual total height may fall short of the
                given number. However, there is also a minimum height per channel so if there are many
                channels, the number may be exceeded. See −y for alternative way of setting spectrogram
                height."""
                y_size = 600
                 
                """
                Default filepath = same dir as the source audio file.
                """
                output_fpath = fpath + ".png"
 
                if renderer_settings['output_to_separate_dir'] == True:
                    output_dir = os.path.join(root, renderer_settings['output_relative_dir_name'])
#                     print('output_dir=', output_dir)
                     
                    if not os.path.exists(output_dir):
                        os.mkdir(output_dir)
                         
                    output_fpath = os.path.join(output_dir, name + ".png")
                 
                # default command
                cmd = [SOX_EXE, fpath, '-n', 'spectrogram', '-h', '-o', output_fpath]
                
                # add footer text at bottom left, (file name - Created with Sox - http://castellaine.net)
                footer = "%s - Created with Sox - http://castellaine.net" % (title) 
                cmd.append('-c')
                cmd.append(footer)
                 
                if opts.title == True:
                    # get song metadata from header
                    metadata = ['-t', '-r', '-c', '-d', '-b', '-p', '-e']
#                     −t Show detected file-type.
#                     −r Show sample-rate.
#                     −c Show number of channels.
#                     −s Show number of samples (0 if unavailable).
#                     −d Show duration in hours, minutes and seconds (0 if unavailable). Equivalent to number of samples
#                     divided by the sample-rate.
#                     −D Show duration in seconds (0 if unavailable).
#                     −b Show number of bits per sample (0 if not applicable).
#                     −B Show the bitrate averaged over the whole file (0 if unavailable).
#                     −p Show estimated sample precision in bits.
#                     −e Show the name of the audio encoding.
#                     −a Show file comments (annotations) if available.

                    result = []
                    for _ in metadata:
                        cmd_soxi = [SOXI_EXE, _, fpath]
                        output = subprocess.check_output(cmd_soxi, shell=True)
                        result.append(output.decode('utf-8').rstrip())
                    
                    # title format: type, 44100 Hz, 16 bits, 2 channels
                    header = "%s, %s Hz, %s bits, %s channels, %s" % (result[6], result[1], result[4], result[2], result[3])
                    cmd.append('-t')
                    cmd.append(header)
     
                print('Analyzing ', name)
                subprocess.call(cmd, shell=True)
         


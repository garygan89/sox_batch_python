# sox_batch_python
Batch convert music files recursively to render spectrogram using Sox. It will scan for music file recursively from a directory and generate spectrogram PNGs using Sox backend. By default those are saved into `Spectrogram` folder relative to each folder where the music resides. 

# Limitations
Currently only support processing 'flac, mp3 and wav' since those are the default decoder that sox support. Might support more file format using ffmpeg in the future for those unsupported music format.

Usage
```
python sox_batch.py <INPUT_DIR>
```

Example:
```
python sox_batch.py "C:\Music\My Album"
```

# Integration with TotalCommander Toolbar Button
1. Create a new toolbar menu
2. Paste the following into each field:
`Command`: python "sox_batch.py"
`Parameters`: -i "%P
3. Save it

Next time you could just select a file in the file pane and click the button to start generating the Spectrogram.

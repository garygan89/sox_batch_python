# sox_batch_python
Batch process music files to render spectrogram using Sox. It will generate the spectrogram PNGs using Sox backend into `Spectrogram` folder under each folder where the music resides. 

# Limitations
Currently only support processing 'flac, mp3 and wav' since those are the default decoder that sox support. 

Usage
```
python sox_batch.py <INPUT_DIR>
```

Example:
```
python sox_batch.py "C:\Music\Music"
```

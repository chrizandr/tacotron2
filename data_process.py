import numpy as np
import os


def process_data(filename, prefix):
    f = open(filename, "r")
    fnames = []
    texts = []
    for line in f:
        data = line.split('"')
        fname = data[0].strip('(').strip() + ".wav"
        fname = os.path.join(prefix, fname)
        text = data[1].strip()
        fnames.append(fname)
        texts.append(text)
    f.close()

    return fnames, texts


def shuffle_into_files(train_file, val_file, data):
    fnames, texts = data
    data_size = len(fnames)
    joint = [fnames[i] + '|' + texts[i] for i in range(data_size)]

    shuffle = np.random.permutation(data_size)
    shuff_data = [joint[x] for x in shuffle]

    train = shuff_data
    val_split = len(train) - 100
    val = train[val_split::]
    train = train[0:val_split]

    f = open(train_file, "w")
    f.write("\n".join(train))
    f.close()

    f = open(val_file, "w")
    f.write("\n".join(val))
    f.close()


if __name__ == "__main__":
    text_path = "/home/chris/tel_f_tts/txt.done.data"
    prefix = "/ssd_scratch/cvit/chris/Telugu/wavs/"
    train_file = "filelists/ljs_audio_text_train_filelist.txt"
    val_file = "filelists/ljs_audio_text_val_filelist.txt"

    data = process_data(text_path, prefix)
    shuffle_into_files(train_file, val_file, data)

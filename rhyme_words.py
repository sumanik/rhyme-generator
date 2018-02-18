import nltk
import math
import argparse

def check_rhyme(pron,syl,match_len):
    return pron[-match_len:]==syl[-match_len:]

def match_words(w1,w2):
    return w1 in w2 or w2 in w1


def get_rhyming_words(inp, percent=0.8):
    entries = nltk.corpus.cmudict.entries()
    inp_syllables = [(wrd,syl) for wrd,syl in entries if wrd==inp]
    matches = {}
    for wrd,syl in inp_syllables:
        match_len = max(int(math.floor(percent*len(syl))),1)
        matches.update(dict([(word, abs(len(syl)-len(pron))) for word,pron in entries if check_rhyme(pron,syl,match_len) and not match_words(word,wrd)]))
    rhymes = sorted(matches, key=lambda x:matches[x])
    return rhymes

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=str, help="input word")
    parser.add_argument('-p', type=float, help="fraction overlap (0.0 to 1.0)", default=0.8)

    args = parser.parse_args()

    wrd = args.w
    percent = args.p

    print get_rhyming_words(wrd, percent)

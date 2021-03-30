#!/usr/bin/env python3

import json
import sys

THRESHOLD = 1

class Srtize:
    def __init__(self, threshold):
        self.threshold = threshold
        self.entries = list()

    def append_element(self, elem):
        self.entries.append({'elems': list()})
        self.extend_element(elem)
    
    def extend_element(self, elem):
        self.entries[-1]['elems'].append(elem)

    def load(self, filename, skip_punctuation = True):
        with open(filename, 'r') as f:
            data = json.load(f)
            last_timecode = -9999
            for elem in data['results']['items']:
                if skip_punctuation and elem['type'] == 'punctuation':
                    continue
                if float(elem['start_time']) < (last_timecode + self.threshold):
                    # continued
                    self.extend_element(elem)
                else:
                    self.append_element(elem)
                last_timecode = float(elem['end_time'])

    def sec_to_timecode(self, sec):
        part_sec = int(sec)
        part_subsec = int(sec * 1000) % 1000
        out_sec = part_sec % 60
        out_min = int(part_sec / 60) % 60
        out_hour = int(part_sec / 3600)
        return '{:02}:{:02}:{:02},{:03}'.format(out_hour, out_min, out_sec, part_subsec)

    def compose_subtitle(self, idx, timecode_start, timecode_end, subtitle):
        return "{}\n{} --> {}\n{}\n\n".format(idx, self.sec_to_timecode(timecode_start), self.sec_to_timecode(timecode_end), subtitle)

    def dump(self):
        idx = 1
        for entry in self.entries:
            timecode_start = float(entry['elems'][0]['start_time'])
            timecode_end = float(entry['elems'][-1]['end_time'])
            subtitle = ''.join([el['alternatives'][0]['content'] for el in entry['elems']])
            print(self.compose_subtitle(idx, timecode_start, timecode_end, subtitle))
            idx += 1

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: srtize.py asrOutput.json [1.5]')
        sys.exit(1)
    f = Srtize(float(sys.argv[2]) if 3 <= len(sys.argv) else THRESHOLD)
    f.load(sys.argv[1])
    f.dump()

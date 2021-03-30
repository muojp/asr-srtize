# asr-srtize

asr-srtize converts asrOutput.json (produced by Amazon Transcribe) into SRT subtitle files.
Mostly intended to be used for CJK languages.

## Usage

### Prerequisites

 - Python 3

### Clone code

```
$ git clone https://github.com/muojp/asr-srtize.git
```

### Run asr-srtize

```
$ cd asr-srtize

$ cat sample/asrOutput.json
{"jobName":"testjob","accountId":"123","results":{"transcripts":[{"transcript":
"皆さん 初め まして こん にち は"}],"items":[{"start_time":"6.54","end_time":"6
.95","alternatives":[{"confidence":"0.9796","content":"皆さん"}],"type":"pronun
ciation"},{"start_time":"6.95","end_time":"7.23","alternatives":[{"confidence":
"0.8","content":"初め"}],"type":"pronunciation"},{"start_time":"7.23","end_time
":"7.54","alternatives":[{"confidence":"0.7312","content":"まして"}],"type":"pr
onunciation"},{"start_time":"8.59","end_time":"8.84","alternatives":[{"confiden
ce":"0.7312","content":"こん"}],"type":"pronunciation"},{"start_time":"8.91","e
nd_time":"9.23","alternatives":[{"confidence":"0.7312","content":"にち"}],"type
":"pronunciation"},{"start_time":"9.33","end_time":"9.54","alternatives":[{"con
fidence":"0.7312","content":"は"}],"type":"pronunciation"}]},"status":"COMPLETE
D"}

$ ./asr-srtize.py sample/asrOutput.json
1
00:00:06,540 --> 00:00:07,540
皆さん初めまして


2
00:00:08,590 --> 00:00:09,540
こんにちは
```

## Parameters

- asr-srtize.py SOURCE_FILE [THRESHOLD]
- SOURCE_FILE (required): filepath to process
- THRESHOLD (optional): threshold used to break SRT entries (seconds; default = 1 sec)

example:

```
$ ./asr-srtize.py sample/asrOutput.json 0.03
1
00:00:06,540 --> 00:00:07,540
皆さん初めまして


2
00:00:08,590 --> 00:00:08,840
こん


3
00:00:08,910 --> 00:00:09,230
にち


4
00:00:09,330 --> 00:00:09,540
は
```

## Notes

Punctuation marks are internally ignored because they are mostly useless for non-European languages (on current Amazon Transcribe).

## License

MIT

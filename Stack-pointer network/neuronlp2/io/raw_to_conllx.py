import sys
import json

def to_conllx_format(line):
    pass

if __name__ == "__main__":
    json_file = sys.argv[1]
    print(("json_file: {}".format(json_file)))
    corpus_dict = json.load(json_file)

    print(corpus_dict)




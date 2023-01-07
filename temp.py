import os
import glob


names = [x[8:-5] for x in glob.glob('layouts/*.json')]
names = sorted(names, key=lambda x: x.lower())

import json
print(json.dumps(names, indent=4))
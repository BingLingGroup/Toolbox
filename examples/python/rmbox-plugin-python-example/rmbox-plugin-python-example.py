import json
import sys
from typing import Any

argv: str = sys.argv

meta = {
    'id': 'Ruminoid.Toolbox.Plugins.Examples.RmboxPluginPythonExample',
    'class_name': 'RmboxPluginPythonExample',
    'name': 'Python 插件示例',
    'description': 'Python 编写的 Ruminoid Toolbox 插件示例。',
    'config_sections': [
        'Ruminoid.Toolbox.Plugins.Common.ConfigSections.IOConfigSection',
    ],
}

if len(argv) == 1:
    print(json.dumps(meta))
    exit(0)

config_sections: Any

with open(argv[1], 'r', encoding='utf-8') as config_section_file:
    config_sections = json.load(config_section_file)

io_section: Any = config_sections['Ruminoid.Toolbox.Plugins.Common.ConfigSections.IOConfigSection']

commands = [
    {
        'target': 'ffmpeg',
        'args': f'-i {io_section["video"]} {io_section["output"]}',
    },
]

print(json.dumps(commands))

""" Manages data from a YAML file. """

import yaml
import pathlib


class YamlManager:
    file_path = None

    def __init__(self, file_path):
        self.file_path = pathlib.Path(file_path)

    def get(self):
        return yaml.load(
            self.file_path.read_text(),
            Loader=yaml.Loader
        )

    def set(self, data, part=False):
        new_data = data
        if part:
            new_data = {
                **self.get(),
                **data
            }

        with self.file_path.open('w') as f:
            f.write(yaml.dump(new_data,
                              Dumper=yaml.Dumper,
                              allow_unicode=True))

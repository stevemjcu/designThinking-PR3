import yaml

class Config(yaml.YAMLObject):
    yaml_tag = u'!Config'

    def __init__(self, **entries):
        self.emulate: bool
        self.instances: list[Config.Instance]
        self.__dict__.update(entries)

    class Instance(yaml.YAMLObject):
        yaml_tag = u'!Instance'

        def __init__(self, **entries):
            self.name: str
            self.file: str
            self.pin: int
            self.channel: int
            self.__dict__.update(entries)

with open('config.yaml', 'r') as f:
    config: Config = yaml.load(f, yaml.Loader)
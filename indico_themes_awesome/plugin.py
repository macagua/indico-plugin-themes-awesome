import os

from indico.core import signals
from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint


class AwesomeThemesPlugin(IndicoPlugin):
    """Awesome Themes

    Provides event themes for Awesome.
    """

    def init(self):
        super().init()
        self.connect(signals.plugin.get_event_themes_files, self._get_themes_yaml)

    def get_blueprints(self):
        return IndicoPluginBlueprint(self.name, __name__)

    def _get_themes_yaml(self, sender, **kwargs):
        return os.path.join(self.root_path, 'themes-awesome.yaml')


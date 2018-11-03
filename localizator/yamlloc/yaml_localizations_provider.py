import os
import yaml

from typing import Dict

from localizator.localization import Localization
from localizator.localizations_provider import LocalizationsProvider
from localizator.dict_localization import DictLocalization


class YamlLocalizationsProvider(LocalizationsProvider):
    def __init__(self, localizations_root='localizations', encoding='utf-8'):
        self._loaded_localizations = dict()
        self.encoding = encoding
        self.localizations_root = localizations_root

    def get_localization(self, language: str) -> Localization:
        if language not in self._loaded_localizations:
            self.__load_localization(language)

        return self._loaded_localizations[language]

    def __load_localization(self, language: str) -> None:
        path = os.path.join(self.localizations_root, language + '.yaml')

        with open(path, encoding=self.encoding) as localization_file:
            loaded_dict = yaml.load(localization_file)

        self._loaded_localizations[language] = DictLocalization(loaded_dict, language)

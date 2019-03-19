import chardet
import os


class TextFiles:

    @staticmethod
    def _is_text_file(file_name):
        return file_name.endswith('.txt')

    @staticmethod
    def _get_content_from_unicode_file(file_path):
        """
        Opens a file normally in python. The default is unicode, and how the majority of our files is encoded.
        :param file_path: contains the path where we want to load the file.
        :return: decoded content of the file
        """
        with open(file_path, 'r') as fp:
            return fp.read()

    @staticmethod
    def _get_content_from_non_unicode_file(file_path):
        """
        Tries to detect the encoding of the file, and decode it accordingly.
        :param file_path: string containing the path where we want to load the file.
        :return: decoded content of the file
        """
        with open(file_path, 'rb') as fp:
            raw_data = fp.read()
            detected_encoding = chardet.detect(raw_data)['encoding']
            return raw_data.decode(detected_encoding)

    @staticmethod
    def _get_category_names(file_root):
        return file_root.split("/")[1:]

    @staticmethod
    def _create_file_content_json(file_raw_content, categories):
        file_content_json = dict()
        file_content_json['raw_content'] = file_raw_content
        for category_number, category in enumerate(categories):
            file_content_json[f"category_{category_number + 1}"] = category
        return file_content_json

    def get_content_from_file(self, file_path):
        try:
            return self._get_content_from_unicode_file(file_path)
        except UnicodeDecodeError:
            return self._get_content_from_non_unicode_file(file_path)

    def read_folder(self, root_folder, ignored_files=None):
        """
        Function to read all files in a particular folder, navigating down the file tree.
        :param root_folder: folder where we'll be reading the files from
        :param ignored_files: list of strings, containing ignored files.
        :return:
        """
        if ignored_files is None:
            ignored_files = list()

        contents = list()
        for root, folder, file_names in os.walk(root_folder):
            for file_name in file_names:
                if self._is_text_file(file_name) and file_name not in ignored_files:
                    file_path = os.path.join(root, file_name)
                    file_raw_content = self.get_content_from_file(file_path)
                    contents.append(file_raw_content)

        return contents

    def read_folder_with_categories(self, root_folder, ignored_files=None):
        """
        Function to read all files in a particular folder, navigating down the file tree, appending a category
        for each subfolder.
        :param root_folder: folder where we'll be reading the files from
        :param ignored_files: list of strings, containing ignored files.
        :return: list with jsons, like the following.
        {
            "raw_content": raw contents of the file
            "category_1": name of the first level category
        }
        It can contain more categories, that will be named category_2, category_3, etc.
        """
        if ignored_files is None:
            ignored_files = list()

        contents = list()
        for root, folder, file_names in os.walk(root_folder):
            for file_name in file_names:
                if self._is_text_file(file_name) and file_name not in ignored_files:
                    file_path = os.path.join(root, file_name)
                    file_raw_content = self.get_content_from_file(file_path)
                    categories = self._get_category_names(root)
                    file_content_json = self._create_file_content_json(file_raw_content, categories)
                    contents.append(file_content_json)

        return contents

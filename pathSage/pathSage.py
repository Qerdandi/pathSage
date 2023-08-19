# V4.17.08.23

import os
from pathlib import Path

class pathSage():
    def as_path(self, path):
        """This function allows to normalize the path put as parameter and return it as a string to be readable by all functions that need a path. It checks if the parameter is a string or a Path. It also checks if the path exists else if generate a ValueError: PEBCAK.

        Args:
            path (string | Path): the path that needs to be normalized.

        Returns:
            string: the input path normalized.
        """
        
        if not self.exists(path): return self.error_e()
        return Path(path).as_posix() + '/'
    
    def as_file(self, path):
        """This function allows to normalize the file path put as parameter and return it as a string to be readable by all functions that need a path. It checks if the parameter is a string or a Path. It also checks if the file exists else if generate a ValueError: PEBCAK.

        Args:
            file path (string | Path): the file path that needs to be normalized.

        Returns:
            string: the input file path normalized.
        """

        if not self.exists(path): return self.error_e()
        return Path(path).as_posix()
    
    def as_new_path(self, path):
        """This function allows to normalize the path put as parameter and return it as a string to be readable by all functions that need a path. It checks if the parameter is a string or a Path. As it's a new path, it doesn't yet exist, so the function doesn't check the path's existence.

        Args:
            path (string | Path): the path that needs to be normalized.

        Returns:
            string: the input path normalized.
        """

        if not self.valid(path): return self.error_f()
        return Path(path).as_posix() + '/'
    
    def as_new_file(self, path):
        """This function allows to normalize the file path put as parameter and return it as a string to be readable by all functions that need a path. It checks if the parameter is a string or a Path. As it's a new file path, it doesn't yet exist, so the function doesn't check the file path's existence.

        Args:
            file path (string | Path): the file path that needs to be normalized.

        Returns:
            string: the input file path normalized.
        """

        if not self.valid(path): return self.error_f()
        return Path(path).as_posix()
    
    def as_extension(self, extension: str):
        """This function normalizes the extension set as a parameter, adding a dot at the beginning if it hasn't already been done.

        Args:
            extension (str): the file extension.

        Returns:
            string: the file extension normalized.
        """

        return (
            f".{extension}"
            if not extension.startswith('.')
            else extension
        )
    
    def as_cmd(self, path):
        """This function converts the path set as parameter to be understood by Windows cmd or shell. It checks if the parameter is a string or a Path. It also checks if the path exists else if generate a ValueError: PEBCAK.

        Args:
            path (string | Path): the path that needs to be converted.

        Returns:
            string: the input path converted.
        """

        return os.path.realpath(self.as_path(path))
    
    def join(self, root, elements: list):
        """This function allows to use joinpath from pathlib with Path but also with string parameters.

        Args:
            root (string | Path): the path to a specific directory.
            elements (list): the list of sub directories and/or file of the root path.

        Returns:
            Path: the concatenate path. You can use 'as_path()' or 'as_new_path()' to normalize it as string.
        """

        if not self.valid(root): return self.error_f()

        path = Path(root)
        for element in elements:
            path = path.joinpath(element)
        return path
    
    def stem(self, path):
        """This function allows to get file name from file path (without extension).

        Args:
            path (string | Path): the file path containing the file name to extract.

        Returns:
            string: the file name without extension.
        """

        if not self.valid(path): return self.error_f()
        return Path(path).stem

    def name(self, path):
        """This function allows to get file name from file path (without extension).

        Args:
            path (string | Path): the file path containing the file name to extract.

        Returns:
            string: the file name with extension.
        """

        if not self.valid(path): return self.error_f()
        return Path(path).name
    
    def suffix(self, path):
        """This function allows to get file extension from file path.

        Args:
            path (string | Path): the file path containing the extension to extract.

        Returns:
            string: the file extension.
        """

        if not self.valid(path): return self.error_f()
        return Path(path).suffix
    
    def parent_path(self, path, parent_nb: int):
        """This function allows to get the n-th parent path from the path defined as parameter.

        Args:
            path (string | Path): the child path as start point.
            parent_nb (int): the n-th parent needed.

        Returns:
            string: the n-th parent path normalized.
        """
        
        parent_path = Path(path)
        for _ in range(parent_nb):
            parent_path = parent_path.parent
        return self.as_path(parent_path)
    
    def exists(self, path):
        """This function checks whether the path or file defined as a parameter have a correct type (Path or string) and exists.

        Args:
            path (string | Path): the path or file to check.

        Returns:
            boolean: true if path or file exists else false.
        """

        if self.valid(path):
            return Path(path).exists()
        else:
            return False
        
    def valid(self, path):
        """This function checks whether the path or file defined as a parameter have a correct type (Path or string).

        Args:
            path (string | Path): the path or file to check.

        Returns:
            boolean: true if path or file type is correct else false.
        """

        return isinstance(path, Path) or isinstance(path, str)
    
    def has_extension(self, path, extension):
        """This function compares a file path with an extension defined as parameters.

        Args:
            path (string | Path): the file path to check.
            extension (string): the reference extension.

        Returns:
            boolean: true if the file has the same extension as the reference extension else false.
        """

        if not self.exists(path): return self.error_e()
        return Path(path).suffix in extension
    
    def file_start(self, path, pattern):
        """This function checks if the file name, containing in a path, starts with a defined pattern.

        Args:
            path (string | Path): the path containing the file name.
            pattern (string): the pattern to compare with the file name.

        Returns:
            boolean: true if the file name starts with the pattern else false.
        """

        return self.stem(path).startswith(pattern)
    
    def file_end(self, path, pattern):
        """This function checks if the file name, containing in a path, ends with a defined pattern.

        Args:
            path (string | Path): the path containing the file name.
            pattern (string): the pattern to compare with the file name.

        Returns:
            boolean: true if the file name ends with the pattern else false.
        """

        return self.self.stem(path).endswith(pattern)
    
    def similar_file(self, path, start='', end=''):
        """This function allows to get an existing file path similar to the file path defined as parameter by editing the start and the end of the file name.

        Args:
            path (string | Path): the file path.
            start (str, optional): the pattern at the beginning of the peer file name. Defaults to ''.
            end (str, optional): the pattern at the end of the peer file name. Defaults to ''.

        Returns:
            string: the peer file path normalized of the input file path.
        """

        file = start + self.name(path) + end
        return self.as_file(self.join(Path(path).parent, [file]))

    def get_files_path(self, path, pattern=None, extension=None):
        """This function allows to get all file paths from the path defined as parameter. It can also filter results by using pattern or extension extraction.

        Args:
            path (string | Path): the path that contains files to extract.
            pattern (string, optional): the pattern contained in file names to extract. Defaults to None.
            extension (string, optional): the extension of files to extract. Defaults to None.

        Returns:
            list: the list of file paths normalized.
        """

        if pattern is not None and extension is not None:
            return [self.as_file(file) for file in Path(path).iterdir() if pattern in file.stem and self.has_extension(file, extension)]
        elif pattern is not None:
            return [self.as_file(file) for file in Path(path).iterdir() if pattern in file.stem]
        elif extension is not None:
            return [self.as_file(file) for file in Path(path).iterdir() if self.has_extension(file, extension)]
        else:
            return [self.as_file(file) for file in Path(path).iterdir()]
    
    def get_files_stem(self, path, pattern=None, extension=None):
        """This function allows to get all file names (without extension) from the path defined as parameter. It can also filter results by using pattern or extension extraction.

        Args:
            path (string | Path): the path that contains files to extract.
            pattern (string, optional): the pattern contained in file names to extract. Defaults to None.
            extension (string, optional): the extension of files to extract. Defaults to None.

        Returns:
            list: the list of file names (without extension).
        """

        if pattern is not None and extension is not None:
            return [file.stem for file in Path(path).iterdir() if pattern in file.stem and self.has_extension(file, extension)]
        elif pattern is not None:
            return [file.stem for file in Path(path).iterdir() if pattern in file.stem]
        elif extension is not None:
            return [file.stem for file in Path(path).iterdir() if self.has_extension(file, extension)]
        else:
            return [file.stem for file in Path(path).iterdir()]
        
    def get_files_name(self, path, pattern=None, extension=None):
        """This function allows to get all file names (with extension) from the path defined as parameter. It can also filter results by using pattern or extension extraction.

        Args:
            path (string | Path): the path that contains files to extract.
            pattern (string, optional): the pattern contained in file names to extract. Defaults to None.
            extension (string, optional): the extension of files to extract. Defaults to None.

        Returns:
            list: the list of file names (with extension).
        """

        if pattern is not None and extension is not None:
            return [file.name for file in Path(path).iterdir() if pattern in file.stem and self.has_extension(path, extension)]
        elif pattern is not None:
            return [file.name for file in Path(path).iterdir() if pattern in file.stem]
        elif extension is not None:
            return [file.name for file in Path(path).iterdir() if self.has_extension(path, extension)]
        else:
            return [file.name for file in Path(path).iterdir()]
        
    def delete(self, file_path):
        """This function allows to delete a file. It also checks if the parameter is a string or a Path and if the file exists else if generate a ValueError: PEBCAK.

        Args:
            file_path (string | Path): the file path to delete.
        """

        os.remove(self.as_file(file_path))

    def rename(self, current_path, new_path):
        """This function allows to rename a directory or file name.

        Args:
            current_path (string | Path): the file or directory path that need to be renamed.
            new_path (string | Path): the new file or directory path.

        """

        if not self.exists(current_path): return self.error_e()
        if not self.valid(new_path): return self.error_f()

        Path(current_path).rename(new_path)
    
    def error_f(self):
        raise ValueError("PEBCAK : Problem Exists Between Chair And Keyboard. Wrong parameter type.")
    
    def error_e(self):
        raise ValueError("PEBCAK : Problem Exists Between Chair And Keyboard. The path or file defined in the parameter does not exist (or its type is incorrect).")
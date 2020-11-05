'''
Description:  
Version: 1.0
Author: Penn
Date: 2020-10-30 10:13:38
LastEditors: Penn
LastEditTime: 2020-11-05 15:34:24
'''
import logging
import time
from logging import Handler, FileHandler, StreamHandler
from pathlib import Path


class PathFileHandler(FileHandler):
    def __init__(self, path, filename, mode='a', encoding=None, delay=False):
        if not Path(path).exists():
            Path.mkdir(path)
        self.baseFilename = Path.joinpath(path, filename)
        self.mode = mode
        self.encoding = encoding
        self.delay = delay
        if delay:
            Handler.__init__(self)
            self.stream = None
        else:
            StreamHandler.__init__(self, self._open())


class Loggers(object):
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARNING,
        'error': logging.ERROR, 'critical': logging.CRITICAL
    }

    def __init__(self, filename='{time}.log'.format(time=int(time.time())), level='info', log_dir='log',
                 fmt='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        self.directory = Path.joinpath(Path(__file__).parent.parent, log_dir)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        file_handler = PathFileHandler(path=self.directory, filename=filename, mode='a')
        file_handler.setFormatter(format_str)
        if level == "debug":
            stream_handler = logging.StreamHandler()  # 往屏幕上输出
            stream_handler.setFormatter(format_str)
            self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

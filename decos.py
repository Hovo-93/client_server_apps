import sys
import logging
import logs.config_client_log
import logs.config_server_log
import traceback
import inspect

# 'sys.argv[0] = /PycharmProjects/Client-Server/decos.py',Если не найдено client, возвращает -1.

if sys.argv[0].find('client') == - 1:
    # если не client то server
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func_log):
    """Decorator func"""

    def log_func(*args, **kwargs):
        ret = func_log(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func_log.__name__} с параметрами {args}, {kwargs}. '
                     f' Вызов из модуля {func_log.__module__}. Вызов из '
                     f' функции {traceback.format_stack()[0].strip().split()[-1]}.'
                     f'Вызов из функции {inspect.stack()[1][3]}'

                     )
        return ret

    return log_func()

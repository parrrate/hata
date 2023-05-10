__all__ = ()

from os import mkdir as create_directory
from os.path import join as join_paths

from ..... import __package__ as PACKAGE_NAME

from .helpers import create_directory_recursive
from .naming import get_bot_constant_name, get_bot_module_name, get_bot_variable_name, get_project_module_name


def create_manage_py_file(directory_path, project_name):
    """
    Creates a `/manage.py` file.
    
    Parameters
    ----------
    directory_path : `str`
        The file's directory's path.
    project_name : `str`
        The project's name.
    """
    with open(join_paths(directory_path, 'manage.py'), 'w') as file:
        file.write(
            f'from {project_name}.cli import main\n'
            f'\n'
            f'if __name__ == \'__main__\':\n'
            f'    main()\n'
        )


def build_dot_env_file_content(bot_names):
    """
    Builds the content of `/.env` file.
    
    Parameters
    ----------
    bot_names : `list` of `str`
        The bots' names.
    
    Returns
    -------
    content : `str`
    """
    content_parts = []
    
    for bot_name in bot_names:
        bot_constant_name = get_bot_constant_name(bot_name)
        content_parts.append(bot_constant_name)
        content_parts.append('=\n')
    
    return ''.join(content_parts)
    

def create_dot_env_file(directory_path, bot_names):
    """
    Creates a `/.env` file.
    
    Parameters
    ----------
    directory_path : `str`
        The file's directory's path.
    bot_names : `list` of `str`
        The bots' names.
    """
    with open(join_paths(directory_path, 'manage.py'), 'w') as file:
        file.write(build_dot_env_file_content(bot_names))


def create_gitignore_file(directory_path):
    """
    Creates a `{project_name}/.gitignore` file.
    
    Parameters
    ----------
    directory_path : `str`
        The file's directory's path.
    """
    with open(join_paths(directory_path, '.gitignore'), 'w') as file:
        file.write(
            f'# Generic\n'
            f'*.env\n'
            f'*.venv\n'
            f'\n'
            f'# Python\n'
            f'*.pyc\n'
            f'__pycache__/\n'
            f'\n'
            f'# Editor\n'
            f'.idea\n'
            f'\n'
            f'# Data files\n'
            f'*.pickle\n'
            f'*.sqlite3\n'
            f'\n'
            f'# Hata\n'
            f'.profiles\n'
        )


def create_project_init_file(directory_path):
    """
    Creates a `{project_name}/__init__.py` file.
    
    Parameters
    ----------
    directory_path : `str`
        The file's directory's path.
    """
    with open(join_paths(directory_path, '__init__.py'), 'w') as file:
        file.write(
            f'__all__ = ()\n'
        )


def create_cli_file(directory_path):
    """
    Creates a `{project_name}/cli.py` file.
    
    Parameters
    ----------
    directory_path : `str`
        The file's directory's path.
    """
    with open(join_paths(directory_path, 'cli.py'), 'w') as file:
        file.write(
            f'__all__ = (\'main\',)\n'
            f'\n'
            f'def main():\n'
            f'    try:\n'
            f'        from hata.main import execute_command_from_system_parameters\n'
            f'    except ImportError as err:\n'
            f'        raise ImportError(\n'
            f'            \'Couldn\\\'t import {PACKAGE_NAME}. \'\n'
            f'            \'Are you sure it\'s installed and available on your PYTHONPATH environment variable? \'\n'
            f'            \'Did you forget to activate a virtual environment?\'\n'
            f'        ) from err\n'
            f'\n'
            f'    from hata.ext.plugin_auto_reloader import start_auto_reloader, warn_auto_reloader_availability\n'
            f'    from hata.ext.plugin_loader import load_all_plugin, frame_filter, register_plugin\n'
            f'    from scarletio import get_event_loop, write_exception_sync'
            f'\n'
            f'    from bots import *\n'
            f'\n'
            f'    register_plugin(\'plugins\')\n'
            f'\n'
            f'    try:\n'
            f'        load_all_plugin()\n'
            f'    except BaseException as err:\n'
            f'        write_exception_sync(err, filter = frame_filter)\n'
            f'        get_event_loop().stop()\n'
            f'        raise SystemExit from None\n'
            f'\n'
            f'    warn_auto_reloader_availability()\n'
            f'    start_auto_reloader()\n'
            f'\n'
            f'    execute_command_from_system_parameters()\n'
        )


def create_main_file(directory_path):
    """
    Creates a `{project_name}/__main__.py` file.
    
    Parameters
    ----------
    directory_path : `str`
        The file's directory's path.
    """
    with open(join_paths(directory_path, '__main__.py'), 'w') as file:
        file.write(
            f'__all__ = ()\n'
            f'\n'
            f'from .cli import main\n'
        )


def build_bots_init_file_content(bot_names):
    """
    Builds the content of `/{project_name}/bots/__init__.py` file.
    
    Parameters
    ----------
    bot_names : `list` of `str`
        The bots' names.
    
    Returns
    -------
    content : `str`
    """
    content_parts = []
    
    bot_module_names = [get_bot_module_name(bot_name) for bot_name in bot_names]
    
    for bot_module_name in bot_module_names:
        content_parts.append('from .')
        content_parts.append(bot_module_name)
        content_parts.append(' import *\n')
    
    content_parts.append('\n\n__all__ = (\n')
    
    for bot_module_name in bot_module_names:
        content_parts.append('    *')
        content_parts.append(bot_module_name)
        content_parts.append('.__all__,\n')
    
    content_parts.append(')\n')
    
    return ''.join(content_parts)


def create_bots_init_file(directory_path, bot_names):
    """
    Creates a `{project_name}/bots/__init__.py` file.
    
    Parameters
    ----------
    directory_path : `str`
        The file's directory's path.
    bot_names : `list` of `str`
        The bots' names.
    """
    with open(join_paths(directory_path, '.__init__.py'), 'w') as file:
        file.write(build_bots_init_file_content(bot_names))


def create_bot_file(directory_path, bot_name):
    """
    Creates a `/{project_name}/bots/{bot_name}.py` file.
    
    Parameters
    ----------
    directory_path : `str`
        The file's directory's path.
    bot_name : `str`
        The bot's name.
    """
    bot_variable_name = get_bot_variable_name(bot_name)
    bot_constant_name = get_bot_constant_name(bot_name)
    with open(join_paths(directory_path, bot_name + '.py')) as file:
        file.write(
            f'__all__ = (\'{bot_variable_name}\',)\n'
            f'\n'
            f'from hata import Client\n'
            f'from hata.env import get_str_env\n'
            f'\n'
            f'\n'
            f'{bot_variable_name} = Client(\n'
            f'    get_str_env(\'{bot_constant_name}_TOKEN\', raise_if_missing_or_empty = True)\n'
            f')\n'
        )


def create_plugins_init_file(directory_path):
    """
    Creates a `/{project_name}/plugins/__init__.py` file.
    
    Parameters
    ----------
    directory_path : `str`
        The file's directory's path.
    """
    with open(join_paths(directory_path, '__init__.py')) as file:
        file.write(
            f'from hata.ext.plugin_loader import mark_as_plugin_root_directory\n'
            f'\n'
            f'mark_as_plugin_root_directory()\n'
        )


def create_project_structure(root_directory_path, bot_names):
    """
    Creates a project.
    
    Structure:
    ```
    {root}
    ├─ .env
    ├─ .gitignore
    ├─ manage.py
    └─ {project}
        ├─ __init__.py
        ├─ __main__.py
        ├─ cli.py
        ├─ bots
        │   ├─ __init__.py
        │   ├─ {bots[n]}.py
        │   └─ ...
        └─ plugins
            └─ __init__.py
    ```
    
    Parameters
    ----------
    root_directory_path : `str`
        The project's root directory's path.
    bot_names : `list` of `str`
        The bots' names.
    """
    project_module_name = get_project_module_name(root_directory_path)
    
    # root
    create_directory_recursive(root_directory_path)
    
    create_dot_env_file(root_directory_path, bot_names)
    create_gitignore_file(root_directory_path)
    create_manage_py_file(root_directory_path, project_module_name)
    
    # root / project
    project_directory_path = join_paths(root_directory_path, project_module_name)
    create_directory(project_directory_path)
    
    create_cli_file(project_directory_path)
    create_main_file(project_directory_path)
    
    # root / project / bots
    bots_directory_path = join_paths(project_directory_path, 'bots')
    create_directory(bots_directory_path)
    
    create_bots_init_file(bots_directory_path, bot_names)
    for bot_name in bot_names:
        create_bot_file(bots_directory_path, bot_name)
    
    # root / project / plugins
    plugins_directory_path = join_paths(project_directory_path, 'plugins')
    create_directory(plugins_directory_path)
    
    create_plugins_init_file(plugins_directory_path)

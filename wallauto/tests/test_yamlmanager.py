import pathlib
import uuid
from wallauto.yamlmanager import YamlManger


def yamlManager_setup():
    file_path = pathlib.Path.cwd() / 'data' / 'test_file.yml'
    print(file_path)
    return YamlManger(file_path)

def test_yaml_get_data():
    DB = yamlManager_setup()
    data = DB.get()
    assert data['name'] == 'Rick Sanchez'

def test_yaml_set_data():
    id = uuid.uuid4().hex
    DB = yamlManager_setup()
    data = DB.get()
    data['random_id'] = id
    DB.set(data)
    assert DB.get()['random_id'] == id

def test_yaml_set_part_data():
    id = uuid.uuid4().hex
    DB = yamlManager_setup()
    DB.set({'random_id': id}, part=True)
    data = DB.get()
    assert data['random_id'] == id and data['name'] == 'Rick Sanchez'

def test_yaml_new_element():
    id = uuid.uuid4().hex
    DB = yamlManager_setup()
    new_data = {}
    new_data[id] = id
    DB.set(new_data, part=True)
    data = DB.get()
    assert data[id] == id \
        and data['name'] == 'Rick Sanchez'

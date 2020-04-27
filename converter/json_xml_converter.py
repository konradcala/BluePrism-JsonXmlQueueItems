import logging
from lxml import etree


class JsonXmlConverter:
    logger = logging.getLogger(__name__)

    def convert_to_queue_item_xml(self, json) -> str:
        root = etree.Element('collection')
        row = etree.SubElement(root, 'row')
        for el in json:
            self.__add_child(row, el, json[el])
        self.logger.info(f"Converted xml [%s]", etree.tostring(root, encoding='unicode'))
        return etree.tostring(root, encoding='unicode')

    def __add_child(self, parent, key, json):
        json_type = type(json)
        if json_type in set([str, int, float, bool]):
            field = etree.SubElement(parent, 'field')
            field.set('value', str(json))
            field.set('type', self.__get_bp_type__(json))
            field.set('name', key)
        elif json_type == list:
            field = etree.SubElement(parent, 'field')
            field.set('name', key)
            field.set('type', 'collection')
            for item in json:
                row = etree.SubElement(field, 'row')
                self.__add_child(row, 'JSON:Array', item)
        elif json_type == dict:
            field = etree.SubElement(parent, 'field')
            field.set('name', key)
            field.set('type', 'collection')
            row = etree.SubElement(field, 'row')
            for el in json:
                self.__add_child(row, el, json[el])
        elif json is None:
            field = etree.SubElement(parent, 'field')
            field.set('value', '')
            field.set('type', 'text')
            field.set('name', key)
        else:
            raise Exception(f"Not supported type {json_type}")

    def __add_list_children(self, field, collection):
        for item in collection:
            row = etree.SubElement(field, 'row')
            self.__add_child(row, item)

    def __get_bp_type__(self, el):
        el_type = type(el)
        if el_type == str:
            return 'text'
        if el_type == bool:
            return 'flag'
        elif el_type == int or el_type == float:
            return 'number'
        elif el_type == list:
            return 'collection'
        elif el_type == bool:
            return 'flag'
        else:
            raise Exception(f"Not supported type {el_type}")

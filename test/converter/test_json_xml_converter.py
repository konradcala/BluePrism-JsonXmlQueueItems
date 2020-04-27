import json
import logging
from doctest import Example
from unittest import TestCase

from lxml.doctestcompare import LXMLOutputChecker

from converter.json_xml_converter import JsonXmlConverter


class TestJsonXmlConverter(TestCase):
    logging.basicConfig(level=logging.DEBUG)
    jsonXmlConverter = JsonXmlConverter()

    def assertXmlEqual(self, got, want):
        checker = LXMLOutputChecker()
        if not checker.check_output(want, got, 0):
            message = checker.output_difference(Example("", want), got, 0)
            raise AssertionError(message)

    def test_simple_scenario(self):
        # given
        with open('test/resources/converter/simple.json') as res_file:
            cards_json = res_file.read()
        json_object = json.loads(cards_json)

        with open('test/resources/converter/simple.xml') as res_file:
            xml = res_file.read()

        # when
        result = self.jsonXmlConverter.convert_to_queue_item_xml(json_object)

        # then
        self.assertXmlEqual(result, xml)

    def test_nested_scenario(self):
        # given
        with open('test/resources/converter/nested.json') as res_file:
            cards_json = res_file.read()
        json_object = json.loads(cards_json)

        with open('test/resources/converter/nested.xml') as res_file:
            xml = res_file.read()

        # when
        result = self.jsonXmlConverter.convert_to_queue_item_xml(json_object)

        # then
        self.assertXmlEqual(result, xml)

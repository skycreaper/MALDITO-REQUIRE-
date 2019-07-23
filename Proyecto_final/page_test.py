from __future__ import unicode_literals
import os
from os.path import dirname, join
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export

this_folder = dirname(__file__)
class SimpleType(object):
    """
    We are registering user SimpleType class to support
    simple types (integer, string) in our entity models
    Thus, user doesn't need to provide integer and string
    types in the model but can reference them in attribute types nevertheless.
    """
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name

    def __str__(self):
        return self.name

def get_entity_mm(debug = False):
    type_builtins = {
            'integer': SimpleType(None, 'integer'),
            'string': SimpleType(None, 'string'),
            'bool': SimpleType(None, 'bool'),
            'float': SimpleType(None, 'float')
    }
    entity_mm = metamodel_from_file(join(this_folder, 'entity.tx'),
                                    classes=[SimpleType],
                                    builtins=type_builtins,
                                    debug=debug)
    return entity_mm
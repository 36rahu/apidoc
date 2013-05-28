from apidoc.object.source import Parameter as ObjectParameter

from apidoc.factory.source.element import Element as ElementFactory

from apidoc.lib.util.decorator import add_property
from apidoc.lib.util.cast import to_bool


class Parameter(ElementFactory):
    """ Parameter Factory
    """

    def create_from_name_and_dictionary(self, name, datas):
        """Return a populated object Parameter from dictionary datas
        """
        parameter = ObjectParameter()
        self.set_common_datas(parameter, name, datas)

        if "optional" in datas:
            parameter.optional = to_bool(datas["optional"])
        if "type" in datas:
            parameter.type = str(datas["type"])

        return parameter
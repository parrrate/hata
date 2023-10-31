import vampytest

from ....channel.channel.fields import validate_id
from ....channel.channel_metadata.fields import validate_status

from ...conversion_helpers.converters import (
    get_converter_description, get_converter_id, put_converter_description, put_converter_id
)

from ..channel import CHANNEL_CONVERSIONS, ID_CONVERSION, STATUS_CONVERSION


def test__CHANNEL_CONVERSIONS():
    """
    Tests whether `CHANNEL_CONVERSIONS` contains conversion for every expected key.
    """
    vampytest.assert_eq(
        {*CHANNEL_CONVERSIONS.get_converters.keys()},
        {'status', 'channel_id'}
    )


# ---- status ----

def test__STATUS_CONVERSION__generic():
    """
    Tests whether ``STATUS_CONVERSION`` works as intended.
    """
    vampytest.assert_is(STATUS_CONVERSION.get_converter, get_converter_description)
    vampytest.assert_is(STATUS_CONVERSION.put_converter, put_converter_description)
    vampytest.assert_is(STATUS_CONVERSION.validator, validate_status)


# ---- id ----

def test__ID_CONVERSION__generic():
    """
    Tests whether ``ID_CONVERSION`` works as intended.
    """
    vampytest.assert_is(ID_CONVERSION.get_converter, get_converter_id)
    vampytest.assert_is(ID_CONVERSION.put_converter, put_converter_id)
    vampytest.assert_is(ID_CONVERSION.validator, validate_id)

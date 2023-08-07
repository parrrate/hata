import vampytest

from ....component import ComponentType

from ..fields import put_type_into


def _iter_options():
    yield ComponentType.row, False, {'type': ComponentType.row.value}
    yield ComponentType.row, True, {'type': ComponentType.row.value}


@vampytest._(vampytest.call_from(_iter_options()).returning_last())
def test__put_type_into(input_value, defaults):
    """
    Tests whether ``put_type_into`` is working as intended.
    
    Parameters
    ----------
    input_value : ``ComponentType``
        Input value.
    defaults : `bool`
        Whether fields with their default values should be included as well.
    
    Returns
    -------
    data : `dict<str, object>`
    """
    return put_type_into(input_value, {}, defaults)

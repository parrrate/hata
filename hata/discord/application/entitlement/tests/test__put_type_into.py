import vampytest

from ..fields import put_type_into
from ..preinstanced import EntitlementType


def _iter_options():
    yield EntitlementType.purchase, False, {'type': EntitlementType.purchase.value}
    yield EntitlementType.purchase, True, {'type': EntitlementType.purchase.value}


@vampytest._(vampytest.call_from(_iter_options()).returning_last())
def test__put_type_into(input_value, defaults):
    """
    Tests whether ``put_type_into`` is working as intended.
    
    Parameters
    ----------
    input_value : ``EntitlementType``
        Input value.
    defaults : `bool`
        Whether fields with their default values should be included as well.
    
    Returns
    -------
    data : `dict<str, object>`
    """
    return put_type_into(input_value, {}, defaults)
